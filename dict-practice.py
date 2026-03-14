# Amaliyot
# 1
otam = {
    'ism': 'Abdulloh',
    'yosh': 67,
    'tyil': 1959,
    'viloyat': 'Samarqand'
}
tyil = otam['tyil']
viloyat = otam['viloyat']
print(f"Otamning ismi {otam['ism'].title()}, {tyil}-yilda, {viloyat.title()} viloyatida tug'ilgan")

# 2
taomlar = {
    'Raximboy' : "manti",
    'Gulomjon' : "osh",
    'Otabek' : "shashlik",
    'husan':"mastava"
}
taom = taomlar['Raximboy']
print(f"Raximboyning sevimli taomi {taomlar['Raximboy']}")

# 4
python_dictionary = {
    'integer': 'butun son',
    'float': 'o\'nlik son',
    'string': 'matn',
    'list': 'ro\'yxat',
    'tuple': 'o\'zgarmas ro\'yxat',
    'dictionary': 'lug\'at'
}
text = input("Kalit so`zni kiriting:")
print(python_dictionary.get(text))
if python_dictionary.get(text) == None:
    print("Bunday kalit so`z mavjud emas")
else:
    print(python_dictionary.get(text))
