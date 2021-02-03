from ursina import *




app = Ursina()



cube = Entity(model = 'Quad', scale = (1.5,1), position = (0,3), texture = 'lado_b.png')
circle = Entity(model = 'Quad', scale = (1.5,1),position = (0,-3), texture = 'lado_c.png')

def update():
    cube.x -= held_keys['a'] * .1
    cube.x += held_keys['d'] * .1
    cube.y -= held_keys['s'] * .1
    cube.y += held_keys['w'] * .1
    circle.x -= held_keys['j'] * .1
    circle.x += held_keys['l'] * .1
    circle.y -= held_keys['k'] * .1
    circle.y += held_keys['i'] * .1



app.run()














