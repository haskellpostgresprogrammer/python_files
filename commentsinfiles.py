import umarutils as u

def comments():
    files = [x for x in os.listdir("/home/umar/pythonfiles/")
             if x.endswith(".py") == True]
    data = []
    for thefile in files:
        filedata = [thefile]
        lines = u.readfilenn("/home/umar/pythonfiles/"+thefile)
        for line in lines:
            if line.startswith("#") == True:
                filedata.append(line)
        data.append(filedata)
    return data
