# Завдання: 
# Створіть словник, що містить інформацію про країни та їх столиці. 
# Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).

countries = {
    "Ukraine": "Kyiv",
    "Portugal": "Lisbon",
    "Spain": "Madrid",
    "China": "Pekin"
}

print(f"Ukraine: {countries.get("Ukraine", None)}")
print(f"Spain: {countries.get("Spain", None)}")
print(f"Brazil: {countries.get("Brazil", None)}")
print(f"USA: {countries.get("USA", None)}")