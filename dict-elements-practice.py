# Amaliyot
# 1.
python_dict = {
    "integer": "butun son",
    "float": "o`nlik son",
    "string": "matn",
    "boolean": "mantiqiy qiymat",
    "list": "ro`yxat",
    "tuple": "o`zgarmas ro`yxat"
}
for key, value in sorted(python_dict.items()):
    print(f"{key.title()}: {value}")
# 2.
davlatlar = {
    "o`bekiston": "toshkent",
    'rossiya': "moskva",
    "aqsh": "vashington",
    "italiya": "rim",
    "fransiya": "parij",
    "ispaniya": "madrid",
    "germaniya": "berlin",
    "braziliya": "brazilia",
    "hindiston": "dehli",
    "xitoy": "pekin"
}
print("Davlatlar:")
for davlat in sorted(davlatlar.items()):
    print(davlat[0].title())
print("\nPoytaxtlar:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
# 3.
# 1-usul
kalit = input("Davlat nomini kiriting:").strip().lower()
if kalit in davlatlar:
    print(f"{kalit()}ning poytaxti {davlatlar[kalit].title()}")
else:
    print("Bizda bu davlat haqidagi ma'lumot yo'q")
# 2-usul
if davlatlar.get(kalit) == None:
    print("Bizda bu davlat haqidagi ma'lumot yo'q")
else:
    print(f"{kalit.title()}ning poytaxti {davlatlar[kalit].title()}")