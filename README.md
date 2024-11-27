# Dokumentace k Python projektu

Tento projekt je určen pro výpočet stechiometrických koeficientů chemických rovnic na základě vstupních dat. Projekt se skládá ze tří souborů: `app.py`, `calcStoichCoeff.py` a `main.py`.

---

## Obsah
1. [Hlavní soubory projektu](#hlavní-soubory-projektu)
2. [Struktura souborů](#struktura-souborů)
3. [Jak spustit projekt](#jak-spustit-projekt)

---

## Hlavní soubory projektu

### 1. `app.py`
Tento modul obsahuje základní funkce potřebné pro práci s chemickými rovnicemi:
- **`getSideOfEquation`**: Rozdělí rovnici na levou a pravou stranu a vrátí seznam molekul.
- **`formatSideOfEquation`**: Naformátuje molekuly do seznamu prvků a jejich počtu.
- **`getElementsOfEquation`**: Získá všechny unikátní chemické prvky v rovnici.
- **`createMatrixOfChemEquation`**: Vytvoří matici rovnice reprezentující výskyt prvků na levé a pravé straně.
- **`gauss`**: Provádí Gaussovu eliminaci k vytvoření horní trojúhelníkové matice.
- **`backSubst`**: Provádí zpětné dosazování k výpočtu stechiometrických koeficientů.

### 2. `calcStoichCoeff.py`
Tento modul definuje funkci **`calcStoichCoeff`**, která:
- Načítá vstupní chemické rovnice ze zadaného textového souboru.
- Používá funkce z `app.py` pro zpracování rovnic a výpočet stechiometrických koeficientů.
- Ukládá výsledky do výstupního textového souboru.

### 3. `main.py`
Hlavní spustitelný soubor projektu:
- Definuje vstupní a výstupní soubor (např. `input/file.txt` a `output/file.txt`).
- Volá funkci `calcStoichCoeff` z modulu `calcStoichCoeff.py`.

---

## Struktura souborů
app.py # Obsahuje základní funkce pro práci s chemickými rovnicemi.
calcStoichCoeff.py # Obsahuje funkci pro zpracování souborů s chemickými rovnicemi.
main.py # Hlavní soubor spouštějící program.
input/ # Složka s textovým souborem obsahujícím vstupní chemické rovnice. 
output/ # Složka pro uložení výsledků.

---

## Jak spustit projekt

### 1. Vytvoření vstupního souboru
Do souboru `input/file.txt` vložte chemické rovnice v následujícím formátu: Na + Cl2 = NaCl

### 2. Spuštění programu
Příkaz pro spuštění:
```bash
python main.py

### 3. Výstup
Výsledky budou uloženy do souboru output/file.txt ve formátu: 2Na + Cl2 = 2NaCl

---

## Requirements

- Python 3.7 or higher
- Required libraries: `re`

---

## Contributing

Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

## Author

Jan Beneš

## License

This project is licensed under the MIT License.
