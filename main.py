import os
import sys
import colorama
from colorama import Fore, Style
from rarity_table import rarity_table


colorama.init()


rarity_colors = {
    0: "",  # no rarity
    1: "§7",  # common
    2: "§a",  # uncommon
    3: "§3",  # rare
    4: "§d",  # unique
    5: "§e",  # legendary
    6: "§6§l",  # relic
}

file_name = input("Enter filename: ") + ".lang"

if file_name == "all.lang":
    file_name = os.listdir("langs\\old")
else:
    file_name = [file_name]

for file in file_name:
    if not os.path.exists(f"langs\\old\\{file}"):
        print("Файл не найден.")
        sys.exit()

    with open(f"langs\\old\\{file}", "r", encoding="utf-8") as f:
        old_file = f.read()

    with open(f"langs\\new\\{file}", "w", encoding="utf-8") as f:
        for line in old_file.split("\n"):
            if not line.split("=")[0] in rarity_table:
                print(f"{Fore.RED}{line}{Style.RESET_ALL}")
                continue

            if not rarity_table[line.split("=")[0]] in rarity_colors:
                color = rarity_table[line.split("=")[0]]
            else:
                color = rarity_colors[rarity_table[line.split('=')[0]]]

            new_line = line.replace("=", f"={color}")
            f.write(f"{new_line}\n")
            print(f"{Fore.GREEN}{new_line}{Style.RESET_ALL}")

    print(f"\n\n\n\n\n\n{Fore.GREEN}Done.{Style.RESET_ALL}")