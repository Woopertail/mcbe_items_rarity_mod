import os
import sys
import colorama
from colorama import Fore, Style
from javalike_rarity_table import rarity_table


colorama.init()

rarity_colors = {
    0: "",  # no rarity
    1: "§7",  # common - light gray
    2: "§a",  # uncommon - green
    3: "§3",  # rare - dark aqua
    4: "§d",  # unique - light purple
    5: "§e",  # legendary - yellow
    6: "§6§l",  # relic - orange bold
}

f_credits = "## Items Rarity © 2022 by Woopertail is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/"

files = input("Enter filename: ") + ".lang"

files = os.listdir("langs\\old") if files == "all.lang" else [files]

for file in files:
    if not os.path.exists(f"langs\\old\\{file}"):
        print(f"Файл {file} не найден.")
        sys.exit()

    with open(f"langs\\old\\{file}", "r", encoding="utf-8") as f:
        old_file = f.read()

    with open(f"langs\\new\\{file}", "w", encoding="utf-8") as f:
        f.write(f"{f_credits}\n\n\n\n")
        for line in old_file.split("\n"):
            item_id = line.split("=")[0]
            if item_id not in rarity_table or rarity_table[item_id] == 0:
                print(f"{Fore.RED}{line}{Style.RESET_ALL}")
                continue

            if not rarity_table[item_id] in rarity_colors:
                color = rarity_table[item_id]
            else:
                color = rarity_colors[rarity_table[item_id]]

            new_line = line.replace("=", f"={color}")\
                .replace("#", "")\
                .strip()\
                + "§r"
            f.write(f"{new_line}\n")
            print(f"{Fore.GREEN}{new_line}{Style.RESET_ALL}")
        f.write(f"\n\n\n{f_credits}")

    print(f"\n\n\n\n\n\n{Fore.GREEN}Done.{Style.RESET_ALL}")
