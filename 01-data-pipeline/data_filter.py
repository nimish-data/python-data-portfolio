import json
import os


def extract_filter(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("FILE NOT FOUND")

    prlist = []
    for i in data:
        if i.get("status", "").strip() == "active":
            prdict = {
                "name": i.get("user", "unknown"),
                "role": i.get("role", "General"),
                "hours": i.get("hours_logged", 0),
            }
            prlist.append(prdict)

    thours = sum(i["hours"] for i in prlist)

    with open("ouput.txt", "w") as file:
        file.write("=== ACTIVE USERS PRODUCTION REPORT ===\n")
        file.write(f"Total Active Users Found: {len(prlist)}\n")
        file.write(f"Combined Work Hours: {thours} hours\n")
        file.write("-------------------------------------\n")
        file.write("\n")
        for i in prlist:
            file.write(f" {i['name']} [{i['role']}] - Logged: {i['hours']} hours\n")


extract_filter("raw_data.json")
