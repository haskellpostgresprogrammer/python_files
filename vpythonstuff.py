import visual as v

# ground = box()
# ground.color = color.green
# ground.length = 20
# ground.width = 10
# ground.height = 0.1
# ground.x = 0
# ground.y = -5
# ground.z = -5

# import pyosd

# p = pyosd.osd()
# p.set_timeout(2)
# a = 0
# words = ["hello","mother","fucker"]
# import time
# for x in words:
#     p.set_align(a)
#     p.display(x)
#     time.sleep(1)
#     a = a + 1
#     ground.rotate(angle=0.5)
# p.set_align(1)
# p.display("quit")
# #scene.exit
# while 1:
#     if scene.kb.keys:
#         s = scene.kb.getkey()
#         p.display(s)

# def ballbounce():
#     floor = box (pos=(0,0,0), length=4, height=0.5, width=4, color=color.blue)
#     ball = sphere (pos=(0,4,0), radius=1, color=color.red)
#     ball.velocity = vector(0,-1,0)
#     dt = 0.01

#     while 1:
#         rate (100)
#         ball.pos = ball.pos + ball.velocity*dt
#         if ball.y < ball.radius:
#             ball.velocity.y = abs(ball.velocity.y)
#         else:
#             ball.velocity.y = ball.velocity.y - 9.8*dt

# import pyosd
# p = pyosd.osd()
# p.set_align(2)

ground = v.box()
ground.color = v.color.green
ground.length = 20
ground.width = 10
ground.height = 1
ground.x = 0
ground.y = -5
ground.z = -5
c = 1
s = 1
ground.length = 1
while 1:
    v.rate(30)
#     ground.rotate(angle=0.1,axis=(0,1,0))
    if c == 20:
        s = -1
    elif c == 1:
        s = 1
    if s == 1:
        c = c+1
    elif s == -1:
        c = c-1
    ground.length = c

        
