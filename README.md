# By phase 1 author
# Mosaic-Game
game project for 15-114
I want to build a multiplayer art game. This should be a python file. The concept is a single or multiplayer  player art game in a pixel style where the objective is to recreate client image requests out of simple mosaics. The first screen should be a pixelated landscape scene with the title of the game “mosaic master” and an option for single or multiplayer. If a single player is chosen. The next screen should be  the first person view with a desk, a box of assorted tiles of shapes and colors, and a line of customer npcs in front. The npc walks up to the table and a speech bubble with their image request pops up. A button for accept and a button for skip appear as well. If the active player accepts the request by pressing accept, the worldview shifts so the screen is entirely filled by the table with a canvas, tile pile, shape options, image request, and finish button ( reference Desktop-1.png) 

The user should be able to toggle between shapes by pressing any of the shape buttons at the bottom of the screen which should change the tiles in the pile to only be of variations of that shape and lots of different colors. For example, if i chose a circle i should see lots of different colors and sizes of circle tiles in the pile. The user should be able to drag any of the tiles from the pile onto the canvas to create an arrangement. The tiles should only overlap if double clicked, otherwise they should not overlap. When a user is finished with their composition they hit submit which changes the worldview back to starting but the table displays their finished piece. An API call runs a similarity check between the image request and the composition and the easier the composition is to identify as the image query the higher percentage score out of 100 the user receives. This should take 2-3 seconds. After this, the npc walks away and the next one comes to the front of the line and poses a new randomly generated image request. The images should be of simple objects or scenes. Such as “black dog”, “sunflower”, “sunset on beach” etc. 

If multiplayer is chosen, an option to either join server or create server will appear as buttons. If the create server is selected, the user will see a code popup and a waiting for friend text line to appear. The other user on their own computer will select the join server and then be prompted to enter a code. They will enter the code on the first person’s computer and be connected to the server. Instead of clients, multiplayer will just consist of the mosaic creations type and a random image prompt. There will be a customizable time limit of 30 seconds, 1 minute, 2 minutes, 5 minutes, or 10 minutes. Both players create the mosaic and hit finish before the timer runs out. The worldview will shift to display both mosaics side by side and the players vote on which turned out best. The users can play multiple rounds once voting is over by clicking the next round button or exit by clicking return home button. 

claude's updates below:
## Running the game (single player)

1. Open Terminal and go to this folder:
   `cd ~/Documents/GitHub/Mosaic-Game`
2. One-time setup:
   `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
3. Play:
   `.venv/bin/python mosaic_master.py`

### Controls
- **Drag** a tile from the pile onto the canvas. Tiles slide to the nearest open spot instead of overlapping.
- **Double-click** a tile on the canvas to let it overlap others (it glows). Double-click again to turn that off.
- **R** rotates the tile under your mouse (Shift+R rotates the other way).
- **Drag a tile off the canvas** to remove it.
- Shape buttons along the bottom switch what's in the pile.
- **Finish** hands your piece to the customer, who scores it 0-100%.

### Status
- Scoring is a **placeholder**: `placeholder_score()` in `mosaic_master.py` rewards canvas coverage, color variety and tile count. It doesn't check whether the picture matches the request yet; the plan is to replace it with an image-similarity API call that returns `(score, comment)`.
- Multiplayer is not built yet.
--------
tweaks to make:
1. no way to scale tiles, this could be useful.
2. no way to duplicate tiles
3. need to integrate a low/no cost way to do scoring so it actually depends on how close the user's composition is and not just how full the canvas is.

# Updated from phase 2
## Primary Changes
During phase 2, I updated the mosaic game based on the ideas in the original README from phase 1. The two changes are: 1. Added tile resizing function. 2. Improved scoring using free AI model (CLIP) which compares the picture with descriptions of the requested subject
 
## New controls: 
- **Drag** a tile from the pile onto the canvas. Tiles slide to the nearest open spot instead of overlapping.
- **Double-click** a tile on the canvas to let it overlap others (it glows). Double-click again to turn that off.
- **R** rotates the tile under your mouse (Shift+R rotates the other way).
- **Drag a tile off the canvas** to remove it.
- Shape buttons along the bottom switch what's in the pile.
- **Finish** hands your piece to the customer, who scores it 0-100%.
- **New:** **Resize** hover over a tile and press + or - to enlarge or shrink.

## Play the game (single player) (by chatgpt): 
1. Download updated GitHub repository: Code → Download ZIP, then unzip it.
2. Open that extracted folder in VS Code.
3. Choose Terminal → New Terminal, then run the below code one at a time, wait for installation to finish:
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-scoring.txt
.venv/bin/python mosaic_master.py
## Acceptance Criteria 
- Python game with pixel-art graphics: Met — original game foundation preserved with minor updates on functionality.
- Landscape title and mode choices: Met — multiplayer choice remains a placeholder.
- Shop, desk, tiles, and customer queue: Met — original scene retained.
- Request bubble, Accept, and Skip: Met — original interactions retained.
- Workspace with canvas, pile, request, shapes, and Finish: Met — original workspace retained.
- Multiple tile shapes, colors, and sizes: Met — original selection retained.
- Drag-and-drop composition: Met — original controls retained.
- Double-click to allow overlap: Met — original placement rules retained.
- Display finished composition: Met — original shop display retained.
- Resemblance scoring through an API: Met — local CLIP scoring added
- Scoring within 2–3 seconds: Partially met — model loading and evaluation may take longer depending on the complexity of description and drawing.
- Low/no-cost resemblance scoring: Partially met — no API fees; quality still needs testing
- New customers and random requests: Met — original progression retained.
- Multiplayer rooms, codes, and connections: Not met — outside this update’s scope.
- Multiplayer: Not met — multiplayer remains unfinished.
## Code map
mosaic_master.py: game screens, tiles, customers, controls, and judging flow.
Game.resize_tile(): resizing using existing placement rules.
mosaic_scoring.py: local model loading, image/text comparison, and scores.
requirements-scoring.txt: dependencies, including the original requirements.
SCORING.md: detailed scoring setup and limitations.
index.html: original browser launcher, currently incompatible.
prompt_log.md: development prompts and AI tool use.

