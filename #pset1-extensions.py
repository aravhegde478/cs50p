#pset1-extensions
name = input ("What is the name of the file? ").strip().lower()
if name.endswith(".jpeg"):
    print ("image/jpeg")
elif name.endswith(".gif"):
    print ("image/gif")
elif name.endswith(".zip"):
    print ("image/zip")
elif name.endswith(".jpg"):
    print ("image/jpg")
elif name.endswith(".pdf"):
    print ("image/pdf")
elif name.endswith(".png"):
    print ("image/png")
elif name.endswith(".txt"):
    print ("text/plain")
else:
    print ("application/octet-stream")