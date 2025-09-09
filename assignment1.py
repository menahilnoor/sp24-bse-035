
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
    "Menahil Noor": "12/12/2004"
}

print("Welcome to the birthday dictionary.:")
for name in birthdays:
    print(name)


person = input("Who's birthday do you want to look up? ")

print(birthdays.get(person, "Sorry, not found."))




sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

new_dict = {}

for k in keys:
    new_dict[k] = sample_dict[k]

print(new_dict)
