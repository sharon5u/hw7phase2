"""Local image/text resemblance scoring. No coverage or tile-count rewards."""
import math
import threading

_MODEL = None
_PROCESSOR = None
_LOCK = threading.Lock()
MODEL_ID = "openai/clip-vit-base-patch32"


def similarity_score(target, unrelated):
    """Heuristic game scale, not a probability; tune against player examples."""
    if not math.isfinite(target) or not math.isfinite(unrelated):
        raise ValueError("Invalid model output")
    # Require both absolute similarity and evidence beyond an abstract tile image.
    absolute = max(0.0, min(1.0, (target - 0.18) / 0.17))
    recognizable = max(0.0, min(1.0, (target - unrelated) / 0.08))
    return int(round(100 * absolute * recognizable))


def judge_mosaic(rgb, size, request):
    """Evaluate an RGB snapshot against the actual customer request locally."""
    global _MODEL, _PROCESSOR
    if not request or not request.strip():
        raise ValueError("Missing customer request")
    if not _LOCK.acquire(blocking=False):
        raise RuntimeError("Model is still working on an earlier request; retry shortly")
    try:
        import torch
        from PIL import Image, ImageOps
        from transformers import CLIPModel, CLIPProcessor

        if _MODEL is None:
            processor = CLIPProcessor.from_pretrained(MODEL_ID)
            model = CLIPModel.from_pretrained(MODEL_ID, use_safetensors=True)
            model.eval()
            _PROCESSOR, _MODEL = processor, model
        image = Image.frombytes("RGB", size, rgb)
        # Square padding preserves the entire wide canvas through CLIP's crop.
        image = ImageOps.pad(image, (224, 224), method=Image.Resampling.NEAREST,
                             color=(244, 236, 216))
        texts = [
            "a simple mosaic picture of " + request,
            "a pixel art picture of " + request,
            "a simple drawing of " + request,
            "an abstract arrangement of unrelated colored geometric tiles",
            "a blank plain cream colored canvas",
        ]
        inputs = _PROCESSOR(text=texts, images=image, return_tensors="pt", padding=True)
        with torch.inference_mode():
            result = _MODEL(**inputs)
            similarities = (result.logits_per_image[0] / _MODEL.logit_scale.exp()).tolist()
        target = sum(similarities[:3]) / 3
        score = similarity_score(target, max(similarities[3:]))
        if score >= 80:
            comment = "I can clearly recognize my request!"
        elif score >= 60:
            comment = "I can see it! Refine the main features."
        elif score >= 40:
            comment = "Some resemblance. Make the subject clearer."
        else:
            comment = "I can't recognize my request yet."
        return score, comment
    finally:
        _LOCK.release()
