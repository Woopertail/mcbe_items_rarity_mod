import colorama
from colorama import Fore, Style
from block_list import block_list
from rarity_table import rarity_table


colorama.init()


with open("langs\\old\\ru_RU.lang", "r", encoding="utf-8") as f:
    input_data = f.read()

output_data = "rarity_table = {\n"

for line in input_data.split("\n"):
    if not (line.startswith("tile.") or line.startswith("item.") or line.startswith("itemGroup.") or
            line.startswith("potion.") or line.startswith("enchantment.level.") or line.startswith("tipped_arrow.effect.")):
        print(f"{Fore.RED}{line}{Style.RESET_ALL}")
        continue

    block = False
    for blocked in block_list:
        if line.startswith(blocked):
            block = True
            print(f"{Fore.MAGENTA}{line}{Style.RESET_ALL}")
            break
    if block:
        continue

    short_name = line.split("=")[0]
    value = 0 if short_name not in rarity_table else rarity_table[short_name]
    if not isinstance(value, int):
        value = f"\"{value}\""
    name = line.split("=")[1].replace("#", "").strip()
    parent_text = "" if not line.startswith("itemGroup.") else " (подкатегория)"
    new_line = f"   \"{short_name}\":{' '*(44-len(short_name))}{value},{' '*5}# {name}{parent_text}\n"
    output_data += new_line
    print(f"{Fore.GREEN}{line}{Style.RESET_ALL}")

output_data += "}"

with open("rarity_table_2.py", "w", encoding="utf-8") as f:
    f.write(output_data)

print(f"\n\n\n\n\n\n\n{Fore.GREEN}Done.{Style.RESET_ALL}")
