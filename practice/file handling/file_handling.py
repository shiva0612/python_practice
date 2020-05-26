with open("try.mp4","rb") as f:
    a = f.read()

with open("copied.mp4","wb") as r:
    r.write(a)
