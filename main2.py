from pyscript import document

Non_metals = {
    "H": ("H", "Hydrogen", 1, 1.008),
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "P": ("P", "Phosphorus", 15, 30.974),
    "S": ("S", "Sulfur", 16, 32.06),
    "SE": ("Se", "Selenium", 34, 78.971),
    "F": ("F", "Fluorine", 9, 18.998),
    "CL": ("Cl", "Chlorine", 17, 35.45),
    "BR": ("Br", "Bromine", 35, 79.904),
    "I": ("I", "Iodine", 53, 126.904),
    "NE": ("Ne", "Neon", 10, 20.180),
    "AR": ("Ar", "Argon", 18, 39.948),
    "HE": ("He", "Helium", 2, 4.003),
    "KR": ("Kr", "Krypton", 36, 83.798),
    "XE": ("Xe", "Xenon", 54, 131.293),
    "RN": ("Rn", "Radon", 86, 222),
}

def search_element(e):

    element_input = document.getElementById("nonmetal1").value.strip().upper()
    result = Non_metals.get(element_input, ("Element not found", "-", "-", "-"))
    
    document.getElementById("code").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("order").innerText = result[2]
    document.getElementById("count").innerText = result[3]