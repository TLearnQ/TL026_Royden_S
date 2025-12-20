import requests, json

url = "https://httpbin.org/get"

res = requests.get(url)

print("Status code: ", res.status_code)
print("Response:")
print(res.json())

with open("./userData.json", "w") as f:
    json.dump(res.json(), f, indent=4)

payload = {
    "a": 1,
    "b": 2,
    "c": 3
}    

res2 = requests.post("https://httpbin.org/post", data=payload)
print("Status code: ", res2.status_code)

with open(r".\userData.json","r") as f:
    data = json.load(f)
print(data)

c = 0
for key, value in payload.items():
    c+= 1
print("Total items echoed: ", c)    