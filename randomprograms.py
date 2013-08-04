import random

def funcs(num):
    f = [
        "plus",
        "minus",
        "multiply",
        "divide",
        "dup",
        "drop",
        "swap",
        ]
    return [random.choice(f) for x in range(num)]    

def ints(num,lower,upper):
    return [str(random.randint(lower,upper)) for x in range(num)]

def floats(num,lower,upper):
    return [str(random.uniform(lower,upper)) for x in range(num)]

def floatszeroone(num):
    return [str(random.random()) for x in range(num)]

# could also add bunch of other floats from distributions
# such as exps guassians gammas, see random module

def consts(num):
    c = [
        "3"
        ]
    return [random.choice(c) for x in range(num)]


def randomprogram(total,f,c,iin,il,iu,fn,fu,fl,fzn):    
    return " ".join(random.sample(
        funcs(f)+consts(c)+ints(iin,il,iu),
#         +floats(fn,fu,fl)
#         +floatszeroone(fzn),
        total))

def getrandomprogram():
    return randomprogram(1000,200,1,2000,0,10000,20,100,1000,20)

import stacklanguage

def runprogram(program):
    e = stacklanguage.Interpreter()
    e.process_line(program)
    return e.stack.data

def runrandomprogram():
    return runprogram(getrandomprogram())
