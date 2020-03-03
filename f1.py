import pyglet
import pymunk 
from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1280,720,'Pymunk Tester',resizable=False)
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0,-1000
body = pymunk.Body(1)