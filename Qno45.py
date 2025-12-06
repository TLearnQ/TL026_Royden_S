import logging
def checkLog(lines):
    c,ers,ap = 0,0,[]
    for line in lines:
        c += 1
        try:
            if "ERROR" in line or "WARNING" in line:
                ap.append(line)
            if "FAIL" in line:
                raise Exception("Check for errors")
        except:
            ers += 1
    print(f"Processed={count}, Audited={len(audit)}, Failed={errors}")
logging.basicConfig(level=DEBUG)
def filecheck(file):
    if ".json" not in file:
        logging.WARNING("file is not in json format")
    try:
        with open(file,"r") as f:
            d = json.load(f)
    except Exception:
        print("Error")

input_lines = [
    "INFO: File opened successfully",
    "ERROR: Improper File",
    "WARNING: File format warning",
    "INFO: Operation FAIL"
]
checkLog(input_lines)




