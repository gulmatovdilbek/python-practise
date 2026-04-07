# Qiymat Qaytaruvchi funksiya
# def add_1(a, b):
#     print(a + b)

# add_1(4, 5)

# def add_2(a, b):
#     return a + b

# print(add_2(3, 4))
# value = add_2(5, 8)
# print(value)

# def toliq_ism_yasa(ism, familiya):
#     """Toliq isim_yasa funksiyasi"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# print(toliq_ism_yasa("Ali", "Valiyev"))

# print("a" * 3) # a harfini 3 marta takrorlaydi  => "aaa"
# print("abc" * 5) # abc matnini 5 marta takrorlaydi => "abcabcabcabcabc"
# print("abc" + 2) # error
# print("abc" / 5)

# def is_even(number):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"
    
#     print(is_even(4))
# def is_even(number):
#     return "Juft" if number % 2 == 0 else "Toq"

# print(is_even(4))
# print(is_even(7))

# vowels = ["a", "o", "i", "u", "e"]
# def count_vowels(text):
#     count = 0
#     for char in text:
#         if char == vowels[0] or char == vowles[1] or char == vowles[2] or char == vowles[3] or char == vowels[4]:
#         count += 1

#         return count
    
#     print(count_vowels("javascript"))
#     print(count_vowels("frontender"))
#     print(count_vowels("bbbb"))

# vowels = ["a", "o", "i", "u", "e"]
# def count_vowels(text):
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1

#     return count

# print(count_vowels("javascript"))
# print(count_vowels("frontender"))
# print(count_vowels("bbbb"))

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
print(avto1)
print(avto2)
avtolar = [avto1, avto2]