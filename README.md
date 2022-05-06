# Space-Exploration
A Sandbox Game powered by Python and Ursina Engine


# History
It all started back when I was 11 and I wanted to make a space game where you can explore and build as free as it could be. 2 years later, I started making the game with the Ursina Engine, when Panda3d Engine version Failed. I hope you like it. You can support my work by giving ideas and fixing bugs. The game will be free, but you need to check out the license.

# Build and Run
First of all you will need to have python installed as pypi on your machine www.python.org/download .

Next install panda3d, ursina, perlin_noise and pickle with pypi:

`pip install [package]`
or
`pip3 install [package]`


In **ursina/lights.py** I changed `DirectionalLight` to `Ursina_DirectionalLight` because of a conflict problem between panda3d.core and ursina.

Then `run` main.py!!!
