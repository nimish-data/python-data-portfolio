import csv
import os


def filter_sort(filename):
    try:
        with open(filename, "r") as file:
            data = list(csv.DictReader(file))

    except FileNotFoundError:
        print("File Not Found")
        return

    flist = []
    for i in data:
        mth = int(i.get("math", 0) or 0)
        sci = int(i.get("science", 0) or 0)
        eng = int(i.get("english", 0) or 0)
        avg = round((mth + sci + eng) / 3, 2)
        if avg >= 75:
            i["average"] = avg
            flist.append(i)

    flist.sort(key=lambda x: x["average"], reverse=True)

    with open("high_achievers.csv", "w") as file:
        fname = ["name", "math", "science", "english", "average"]
        writer = csv.DictWriter(file, fieldnames=fname)
        writer.writeheader()
        writer.writerows(flist)


filter_sort("raw_csv.csv")
