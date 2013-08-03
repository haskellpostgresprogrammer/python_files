import gtk

yesbutton = gtk.Button("yes")
def yesclick(yesbutton):
    print "yes"
yesbutton.connect("clicked",yesclick)

nobutton = gtk.Button("no")
def noclick(nobutton):
    print "no"
nobutton.connect("clicked",noclick)

nextbutton = gtk.Button("next")
def nextclick(nextbutton):
    print "next"
yesbutton.connect("clicked",nextclick)

image = gtk.Image()
imagefilename = "/home/umar/dog.jpg"
image.set_from_file(imagefilename)

mainbox = gtk.VBox()
yesnobox = gtk.HBox()

yesnobox.pack_start(yesbutton)
yesnobox.pack_start(nobutton)

mainbox.pack_start(image)
mainbox.pack_start(yesnobox)
mainbox.pack_start(nextbutton)

w = gtk.Window()
w.add(mainbox)

w.show_all()
gtk.main()
