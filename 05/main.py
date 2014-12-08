import pickle
import urllib.request

response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
banner = pickle.load(response)
response.close()
for line in banner:
    for char in line:
        print(char[0]*char[1],end="")
    print("\n")
