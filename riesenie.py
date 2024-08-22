from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

# Načítaj existujúci Excel súbor
wb = load_workbook('statistika.xlsx')

# Odkaz na pôvodný hárok
sheet = wb['V.A']  # Názov prvého hárku, kt. chceme kopírovať V.A

# Pre každý nový hárok vytvor kópiu pôvodného
for i in range(1, 4): # Napr. 3 kópie
    new_sheet = wb.copy_worksheet(sheet)
    new_sheet.title = f'Kopia{i}'

    # Zabezpeč ochranu nového hárku
    new_sheet.protection.sheet = True
    new_sheet.protection.enable()
# Ulož nový súbor
wb.save('statistika.xlsx')
