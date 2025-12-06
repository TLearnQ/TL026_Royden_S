def analysis(data):
    avgt = sum(data)/len(data)
    if avgt > 75:
        return "PEAK"
    elif avgt > 55:
        return "HEALTHY"
    elif avgt > 40:
        return "LOW MARGIN"
    else:
        return "LOSS"
transc = {
    "DAY 1":[45,65,65],
    "DAY 2":[65,78,21],
    "DAY 3":[75,96,34],
    "DAY 4":[89,54,32],
    "DAY 5":[23,35,7],
    "DAY 6":[77,77,77],
    "DAY 7":[23,98,78]
}
for day,trx in transc.items():
    print(f"Transactions of {day} ended up at {analysis(trx)}")