## Useful commands
#### Create a new virtual environment: 
`python -m venv .venv`\
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`\
`.venv\Scripts\activate`\
In VS Code Command pane, Select Python Interpretor > .\.`venv\Scripts\python.exe`

#### Install py5
`pip install py5`\
`winget install EclipseAdoptium.Temurin.21.JDK` \
` java -version` --> must be > 17.0 \
`pip install pillow` ---> to save GIFs

#### Commit to git
create repository on github page if it is first commit\
`git init` ---> only for the first time\
`git add .`\
`git status`\
`git commit -m "MESSAGE GOES HERE"`\
`git remote set-url origin https://github.com/<REPOSITORY_PATH>`\
`git push -u origin main`\
`git pull origin main --allow-unrelated-histories`\
`git push -u origin main`

## Projects
### Flow art Perlin Noise
#### Dependencies:
py5, pillow, numpy

#### Instructions ot run
Run `python flow_art\flow_art_perlin_noise.py`\
Press **`s`** at any time to save a PNG snapshot.\
Press **`g`** at any time to save a GIF file.

#### Visual Output

| Animated Flow | Static Frame |
| :---: | :---: |
| ![Animated Flow](flow_art/outputs/flow_art_perlin_noise_20261111_145025.gif) | ![Static Frame](flow_art/outputs/flow_art_perlin_noise20261111_144411_0048.png) |



#### Credits & Inspiration
* **Algorithm:** Ken Perlin (Perlin Noise, 1983)
* **Conceptual Inspiration:** Daniel Shiffman (*The Nature of Code*) & Tyler Hobbs (*Flow Fields*)
* **Boilerplate Assistance:** Initial starter template generated via AI assistant, refactored and tuned by @swagatip.
Use code with caution.
