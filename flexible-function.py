# # Return function
# def sum_list(lst):
#     s = 0
#     for element in lst:
#         s += element

#     return s

# print(sum_list([18, 75, -89, 7, 10])) # Natija: 21


# flexible(moslashuvchan) function
# args usuli

# def summa(*numbers):
#     print(numbers)

#     summa(12, 50, 89, 0, -5) # Natija: (12, 50, 89, 0, -5)
#     s = 0
#     for element in numbers:
#         s += element

#     return s
# print(summa(12, 50, 89, 0, -5)) # Natija: 146

# def my_func(*people):
#     print(f"The youngest person is: {people[1]}")

# my_func("G'ulomjon", "Dilbek", "Gulbahor") 
# my_func("Sardor", "Olim", "Dilshod")

# def summa(x, y, *numbers):
#      return x + y + sum(numbers)

# print(summa(1, 7, 8, -26, 18, -5, 74, -100))
# print(summa(5, 12))

# **kwargs(keyword arguments) usuli
# def avto_info(kompaniya, modeli, **malumotlar):
#     # print(malumotlar) {'key' : value}
#     # print(type(malumotlar)) dect
#     malumotlar['Kompaniya'] = kompaniya
#     malumotlar['model'] = modeli

#     return malumotlar

# print(avto_info("GM Uzbekistan", "Cobalt", rangi="Oq", narxi=156000)) 
# print(avto_info("Merc", "Gelikvogen", rangi="Qora", narxi=350000)) 

# def my_function(**kid):
#     print("His last name is" + kid["lname"])

# my_function(fname = "Tobias", Iname = "Refsnes")

# 1 Amaliyot
# def kopaytma(lst):
#     s = 1
#     for number in lst:
#         s *= number

#     return s

# print(kopaytma([1, 5, 1, 7, 2]))

# 2 Amaliyot
def student_info(name, lastname, **data):
    data ['name'] = name
    data ['lastname'] = lastname
    return data
print(student_info("Jumagul", "Raximboyeva", year = 2005, height = 1.65))