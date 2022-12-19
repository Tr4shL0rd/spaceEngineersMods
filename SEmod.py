#!/usr/bin/env python3
import csv
import argparse
from rich import print as rprint
parser = argparse.ArgumentParser(prog="SEmod",epilog="Made By @Tr4shL0rd")
parser.add_argument("-n","--new-mod"   , help="add new mod to the list", dest="new_mod"  , action="store"     , type=str )
parser.add_argument("-r", "--read-mods", help="read mods"              , dest="read_mods", action="store_true", type=bool) 
parser.add_argument("-D", "--DEBUG"    , help="DEBUG MODE"             , dest="DEBUG"    , action="store_true", type=bool)
args = parser.parse_args()
def check_err(mod_list) -> bool:
    """
        returns True if nothing is wrong
    """
    if len(mod_list) < 2:
        print("TR4_ERR_001: did you forget to add a link or a name?")
        return False
    elif len(mod_list) > 2:
        print("TR4_ERR_002: Too many values in list")
        return False
    elif "/?id=" not in mod_list[1] or not mod_list[1].split("/?=")[0].isdigit():
        print("TR4_ERR_003: Steam workshop id is not valid!")
        return False

    return True
def link_fixer(mod):
    """
        checks if "https://" is at the start of the link
    """
    if not mod[1].startswith("https://"):
        mod[1] = f"https://{mod[1]}" 
        return mod
def new_mod(new_mod, mod_file="mods.csv"):        
    """
        add new mod to mod_file
    """
    header = ["name", "url"]
    data = [
                ["Modular Encounter Systems","https://steamcommunity.com/sharedfiles/filedetails/?id=1521905890"],
                ["Independent Contractors","https://steamcommunity.com/sharedfiles/filedetails/?id=445996030"],
                ["Imber Corporation","https://steamcommunity.com/sharedfiles/filedetails/?id=973526550"],
                ["Parallax Concepts","https://steamcommunity.com/sharedfiles/filedetails/?id=1135484957"],
            ]
    
    mod = link_fixer(new_mod.strip().split(","))
    if not check_err(mod):
        rprint(f"[red][underline]ERROR ADDING NEW MOD: [/red]{mod}[/underline]")
        exit()
    
    print(f"adding {mod[0]}" if not args.DEBUG else f"adding {mod}")
    data.append(mod)
    if not args.DEBUG:
        with open(mod_file, "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
def read_mods(mod_file="mods.csv"):
    """
        reads all mods from mod_file
    """
    with open(mod_file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        name = []
        link = []
        for row in reader:
            name.append(row[0])
            link.append(row[1])
            print(row[0].title())
if __name__ == "__main__":
    if args.new_mod:
        new_mod(args.new_mod)
    elif args.read_mods:
        read_mods()