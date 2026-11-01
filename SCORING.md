# Resemblance scoring

This copy includes +/- resizing and local CLIP image/text scoring.
The original coverage scorer remains in the source for preservation, but is no longer called.

## Setup and play

Use Python 3.9 or later (3.11 recommended). In this folder run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-scoring.txt
.venv/bin/python mosaic_master.py
```

The first Finish downloads openai/clip-vit-base-patch32 from Hugging Face
(several hundred MB). Internet is required for setup; model inference runs
locally, with no API key, API fees, or uploaded compositions. Subsequent runs
reuse the cached model. Setup/evaluation can exceed the original 2.5 seconds.
The game stays responsive and waits up to five minutes. If scoring fails,
your composition returns for retry and no score or served count is recorded.
The terminal gives the underlying error. A background job may continue after
a timeout; wait for it or restart the game before retrying.

## What the score means

The full rendered canvas is padded, not cropped, and compared with three
text descriptions of the actual customer request. The model's cosine
similarity is mapped from 0.18–0.35 to 0–100 and gated by its advantage over
blank-canvas/abstract-tile descriptions (0–0.08). These are starting heuristic
thresholds, not calibrated accuracy percentages. Coverage, number of tiles,
and color variety earn no independent points. Recognition can be imperfect,
especially for tiny abstract mosaics or precise spatial relationships.
Tune thresholds using real player examples before treating scores as fair
competitive rankings. This is text/image matching, not a comparison with a
reference picture, because customers currently provide text only.

## Manual check

For the same request, compare a recognizable composition with a random
arrangement of the same tiles. Try a clearly mismatched subject, a sparse
recognizable subject, and a crowded but meaningless canvas. Verify the
recognizable version usually scores higher. Verify +/- and R still work.

Model/API documentation: https://huggingface.co/docs/transformers/model_doc/clip
