import re

# Příkladový řetězec
retezec = "Mg + HCl = MgCl2 + H2"

# Použití regulárního výrazu pro split
vysledek = re.split(r'(?=[A-Z])', retezec)

# Odstranění prázdných prvků (pokud řetězec začíná velkým písmenem)
vysledek = [slovo for slovo in vysledek if slovo]

print(vysledek)