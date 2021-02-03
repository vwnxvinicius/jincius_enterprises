from ursina import *




app = Ursina()


cube = Entity(model = 'Quad', scale = (1.5,1), position = (0,3),collider = 'box', texture = 'lado_b.png')

bg = Entity(model = 'Quad', texture = 'bg.jpeg', scale = (15,8))
circle = Entity(model = 'Quad', scale = (1.5,1),position = (0,-3),collider = 'box', texture = 'lado_c.png')

ammo = Entity(model = 'Circle', scale = (0.1,0.1),collider = 'box', color = color.yellow)

def update():
    cube.x -= held_keys['a'] * .1
    cube.x += held_keys['d'] * .1
    circle.x -= held_keys['j'] * .1
    circle.x += held_keys['l'] * .1
    ammo.y += .1



app.run()














