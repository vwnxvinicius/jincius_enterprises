from ursina import *




app = Ursina()


cube = Entity(model = 'Quad', scale = (1.5,1), position = (0,3),collider = 'box', texture = 'lado_b.png')
circle = Entity(model = 'Quad', scale = (1.5,1),position = (0,-3),collider = 'box', texture = 'lado_c.png')

def update():
    cube.x -= held_keys['a'] * .1
    cube.x += held_keys['d'] * .1
    circle.x -= held_keys['j'] * .1
    circle.x += held_keys['l'] * .1




app.run()














