import requests

url = "https://img12.360buyimg.com/n1/s200x200_jfs/t1/35834/35/18375/64578/636e75c3Eaea42a9e/abb59d643e8f8e5c.jpg"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

response = requests.get(url,headers = headers)
pic = response.content

with open("pic.jpg", "wb") as f:
    f.write(pic)

print("done")