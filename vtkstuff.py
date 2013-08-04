import vtk

def ex():
    # create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    WIDTH=640
    HEIGHT=480
    renWin.SetSize(WIDTH,HEIGHT)
 
    # create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
 
    # create cone
    cone = vtk.vtkConeSource()
    cone.SetResolution(60)
    cone.SetCenter(-2,0,0)
 
    # mapper
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInput(cone.GetOutput())
 
    # actor
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
 
    # assign actor to the renderer
    ren.AddActor(coneActor)

    # enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()

import math
def ex1():
    p0 = (0,0,0)
    p1 = (1,1,1)
 
    distSquared = vtk.vtkMath.Distance2BetweenPoints(p0,p1)
 
    dist = math.sqrt(distSquared)
 
    print "p0 = ", p0
    print "p1 = ", p1
    print "distance squared = ", distSquared
    print "distance = ", dist

def ex2():
    arrowSource = vtk.vtkArrowSource()
    # arrowSource.SetShaftRadius(0.01)
    # arrowSource.SetTipLength(.9)
 
    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(arrowSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
 
    # Visualize
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
 
    renderer.AddActor(actor)
    renderer.SetBackground(.1, .2, .3) # Background color dark blue
 
    renderWindow.Render()
    renderWindowInteractor.Start()
