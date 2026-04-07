from operator import index


text = "Hey guys, welcome to my course!"
# print(len(text))
# string ichidagi harflar va bo`shliq ham hisobga olinadi
# string ichidagi belgilar 0 dan boshlab indekslanadi
# print(text[0])  # H
# print(text[1])  # e 
# print(text[2])  # y
# print(text[3])  #       
# print(text[4])  # g
# print(text[5])  # a
# print(text[-1]) # !
# print(text[-2]) # e
# lenght = len(text)
# Oxirgi belgini olish uchun lenght - 1 indeksidan foydalanamiz
# print(text[lenght - 1]) # !

# 1-usul
# for char in text:
#     print(char)

# 2-usul
# for i in range(len(text)):
#     print(i, text[i])

print("welcome" in text) # True
print("het" in text) # False
