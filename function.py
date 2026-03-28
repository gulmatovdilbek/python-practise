# Function - ma`lum  vazifani bajaruvchi kod bloki.
# Funksiyalarni yaratish uchun def kalit so`zidan foydalanamiz.
# Pythondagi tayyor funksiyalar - print(), input(), len(), list() va boshqalar.
# print("Hello world!") 
# Funksiyani e`lon qilish(declaration)
# def salom_ber():
    # print("Salom, dunyo!")

# Funksiyani chaqarish(call)
# salom_ber() # Natija: Salom, dunyo!
# salom_ber() # Natija: Salom, dunyo!

# Funksiyada parametrlar, argumentlar
# def salom_ber(ism):
#     print(f"Assalomu alaykum, {ism}!")

# salom_ber("Ali") 
# salom_ber("Vali")

# def yigindi(a, b):
#     print(a + b)
# yigindi(7, 8) # Natija 15 
# yigindi(10, 20) # Natija 30

# def calculate_age(birth_year=1995, name="Olim"):
#     age = 2026 - birth_year
#     print(f"{name}ning yoshi {age} da.")

# calculate_age(2010, "Ismoil")
# calculate_age(2001, "Raximboy")


def solishtirish(a, b):
    if a > b:
        print(f"{a} {b} dan katta.")
    elif a < b:
        print(f"{a} {b} dan kichik.")
    else:
        print(f"{a} va {b} teng.")
        
solishtirish(10, 5)
solishtirish(3, 7)

# 1
def t_yil():
    ism = input("Ismingizni kiriting:")
    yosh = int(input("Yoshingizni kiriting:"))
    t_yil = 2026 - yosh
    print(f"{ism.title()}, siz {t_yil}-yilda tug`ilgansiz.")
# # 2
def son_kvadrati():
    son = int(input("Istalgan son kiriting:"))
    kvadrat = son ** 2
    print(f"{son} ning kvadrati {kvadrat} ga teng.")

# 3
son = int(input("Son kiriting:"))
def tekshirish_son(son):
 if son % 2 == 0:
    print("Juft")
 else:
    print("Toq")

 tekshirish_son(son)

# 5
def daraja_hisobla(son, daraja):
    natija = son ** daraja
    print(f"{son} ning {daraja} - darajasi {natija} ga teng.")
x = int(input("Asos sonni kiriting:"))
y = int(input("Daraja sonni kiriting:"))
daraja_hisobla(x, y)

# 7
def bolinish(son):
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo`linadi.")
bolinish(70)