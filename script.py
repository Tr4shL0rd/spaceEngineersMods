import csv
def new_mod():
    header = ["name", "url"]
    data = [
                ["Modular Encounter Systems","https://steamcommunity.com/sharedfiles/filedetails/?id=1521905890"],
                ["Independent Contractors","https://steamcommunity.com/sharedfiles/filedetails/?id=445996030"],
                ["Imber Corporation","https://steamcommunity.com/sharedfiles/filedetails/?id=973526550"],
                ["Parallax Concepts","https://steamcommunity.com/sharedfiles/filedetails/?id=1135484957"],
            ]
    with open("mods.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
def read_mods():
    with open("mods.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        name = []
        link = []
        for row in reader:
            name.append(row[0])
            link.append(row[1])
            print(row[0])

read_mods()