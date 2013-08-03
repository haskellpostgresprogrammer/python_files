import povray as pv

def house(x,y,z):
    return pv.cylinder([x,y,z],[x,y+2,z],10,"Silver")

def housestack(x,y,z,num,seperation):
    return [house(x,y,z) for y in
            range(y,num*seperation,seperation)]

def pillar(x,y,z,height):
    return pv.cylinder([x,y,z],[x,y+height,z],5,"Black")

def building(x,y,z,stories):
    return [
        pillar(x,y,z,stories*4),
        housestack(x-20,y,z,stories,4),
        housestack(x+20,y,z,stories,4),
        housestack(x,y,z-20,stories,4),
        housestack(x,y,z+20,stories,4),        
        ]

def run():
    pv.runpov(standardfile(),"ex3")

def standardfile():
    return [
        pv.incfiles(),
        pv.skysphere(),
        pv.plane("y",0,"Green"),
        pv.camera([50,50,-80],[0,20,100]),
        pv.lightsource([500,500,1000],"White"),
        building(0,0,0,10),
        ]
