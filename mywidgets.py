# pyjamas library
# app pyjamas library

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.ToggleButton import ToggleButton
from pyjamas.ui.HTML import HTML
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Image import Image
import pyjamas.Window as Window
from pyjamas.ui.TextBox import TextBox

def rootadd(x):
    RootPanel().add(x)

def rootclear():
    RootPanel().clear()    

def button(x,y):
    z = Button(x,y)
    return z

def togglebutton(x,y,z):
    a = ToggleButton(x,y)
    return a

def label(x):
    y = Label(x)
    return y

def labelbutton(x,y):
    z = Label(x)
    z.addClickListener(y)
    return z

def html(x):
    y = HTML(x)
    return y

def br():
    return html("<br>")

def verticalpanel():
    return VerticalPanel()

def horizontalpanel():
    return HorizontalPanel()

def flatten(table):
    l = []
    for x in table:
        l.extend(x)
    return l

def flextable(data):
    table = FlexTable()
    rows = len(data)
    columns = len(data[0])
    datalist = flatten(data)
    columnlist = flatten([range(columns) for x in range(rows)])
    rowlist = flatten([[x for y in range(columns)]
                       for x in range(rows)])
    tablelist = zip(rowlist,columnlist,datalist)
    for x in tablelist:
        table.setText(x[0],x[1],x[2])
    table.setBorderWidth(2)
    return table

def clearandplace(place,item):
    place.clear()
    place.add(item)

def image(theurl):
    return Image(url=theurl)

def urlwindow(link,title):
    Window.open(link,title)

def textbox():
    return TextBox()
