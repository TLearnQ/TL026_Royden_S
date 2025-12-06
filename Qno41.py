data = []
def restS(entry):
    split = entry.split(" ")
    mea = split[0]
    path = split[1]
    if len(entry) < 2:
        return "Incomplete entry!"
    elif mea == "GET" and path == "/users":
        return data
    elif mea == "POST" and path == "/users":
        if len(split) < 3:
            return "Data to be added is Missing"
        addD = split[2]
        data.append(addD)
        return f"User {addD} added."
    elif mea == "GET" and path == "/count":
        return "Number of users: ",len(data)
    else:
        return "INVALID ENTRY"

print(restS("GET /users"))
print(restS("POST /users [id:101]"))
print(restS("POST /users [id:104]"))
print(restS("GET /users"))
print(restS("POST /users"))
print(restS("POST /users [id:103]"))
print(restS("GET /users"))
print(restS("GET /count"))
