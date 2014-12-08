import urllib.request

preq = "44582"
for i in range(400):
    body = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+preq).read()
    preq = ""
    for j in (bytes.decode(body)):
        if j.isdigit():
            preq+=j
    print(body)
