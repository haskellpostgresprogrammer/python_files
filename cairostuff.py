import math
import cairo

WIDTH, HEIGHT  = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.rectangle (0,0,1,1)
ctx.set_source (pat)
ctx.fill ()

surface.write_to_png('/home/umar/gradient.png')

# incomplete
