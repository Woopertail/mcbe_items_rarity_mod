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

f_credits = """## This file is created by Woopertail.
## To download or update more add-ons, visit next links:
##
## MCPEDL: mcpedl.com/user/woopertail/
## Discord: discord.gg/hYtZMEfZSE 
##
## You able to:
## Include this file in your add-on.
## Modify this file, include modified file in your add-on.
## Use this file on public servers or realms.
## Do with this file whatever you want, in general.
##
## BUT
## do not remove my credits (this text)
## do not edit my credits (this text)"""

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