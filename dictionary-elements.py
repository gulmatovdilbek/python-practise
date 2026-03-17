# Dictionary elementlari bilan ishlash 
phone = {
    'brand': 'Apple',
    'model': 'iPhone 17 pro max',
    'year': 2025,
    'color': 'black',
    'price': 1500
}
# 1. get metodi - kalit orqali qiymatni olish
print(phone.get('model'))  # iPhone 17 pro max
print(phone.get('price', "Narx topilmadi"))  # 1500
print(phone.get('battery')) # None, chunki 'battery' kaliti mavjud emas
print(phone.get('battery', "Batareya haqida ma'lumot topilmadi"))  # Batareya haqida ma'lumot topilmadi

# 2. items() metodi - lug'at elementlarini (kalit-qiymat juftlarini) olish
print(phone.items())  # dict_items([('brand', 'Apple'), ('model', 'iPhone 17 pro max'), ('year', 2025), ('color', 'black'), ('price', 1500)])
for key, value in phone.items():
    print(f"{key}: {value}")

telefonlar = {
        'ali': 'iPhone 17 pro max',
        'vali': 'Samsung Galaxy S30',
        'olim': 'Xiaomi Mi 12',
        'anvar': 'Google Pixel 7'
    }
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni: {q}")

# 3. keys() metodi - lug'atning barcha kalitlarini olish
print(phone.keys())  # dict_keys(['brand', 'model', 'year', 'color', 'price'])
print(telefonlar.keys())  # dict_keys(['ali', 'vali', 'olim', 'anvar'])

mahsulotlar = {
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'shaftoli': 15000
}
# print(mahsulotlar.keys())
print('Do`kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori
# 1. listda in operatori element mavjudligini tekshiradi
# fruits = ['olma', 'anor', 'uzum', 'shaftoli']
# print('olma' in fruits)  # True
# print('banan' in fruits)  # False

fruit = input("Qaysi meva yoqadi? ")
if fruit in fruits:
    print(f"{fruit.title()} do`konimizda bor.")
else:
    print(f"{fruit.title()} do`konimizda yo`q.")


bozorlik = ['anor', 'uzum', 'non', 'sut']
for mahsulot in mahsulotlar:
    print(mahsulot) # Lug`atning kalitlari bo`ladi

# mahsulotlar - lug`at, bozorlik - ro`yxat, mahsulot - luga`atning kaliti
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so`m")

# print(sorted(mahsulotlar.keys()))  
# print("Do`konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar.keys()):
#     print(mahsulot.title())print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
telefonlar = {
    'ali': 'iPhone 17 pro max',
    'vali': 'Samsung Galaxy S30',
    'olim': 'Xiaomi Mi 12',
    'anvar': 'Google Pixel 7'
}
print('Foydalanuvchilar quyiagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)