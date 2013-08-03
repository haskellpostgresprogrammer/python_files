# from logilab.constraint import *
# variables = ('c01','c02','c03','c04','c05','c06','c07','c08','c09','c10')
# values = [(room,slot)
#           for room in ('room A','room B','room C')
#           for slot in ('day 1 AM','day 1 PM','day 2 AM','day 2 PM')]
# domains = {}
# for v in variables:
#     domains[v]=fd.FiniteDomain(values)


from constraint import *

def ex():
    problem = Problem()
    problem.addVariable("a",[1,2,3])
    problem.addVariable("b",[4,5,6])
#     problem.addConstraint(lambda a,b: a*2 == b,("a","b"))
    problem.addConstraint(excons,("a","b"))
    return problem.getSolutions()

def excons(a,b):
    return a*3 == b
