milk = "leite"
volume = 2

print(type(milk))
print(type(volume))

preparation1 = volume + 1
preparation2 = milk + str(volume)

print(preparation1)
print(preparation2)

life_cat = str(volume + 5)

print("O gato bebe " + milk)
print("E tem " + life_cat + " vidas")

print("O gato bebe " + milk + " e tem " + life_cat + " vidas")

print(f"O gato bebe {milk} e tem {life_cat} vidas")

name = "Torquato"
age = 45
is_admin = True #boolean True or False

print(is_admin)
print(type(is_admin))

# Structural Types (Collections)

animes = ["Drago Ball", "Naruto", "Jojo", "Death Note"]
# posição   =>  0           1        2          3  não Null
          # <= -4          -3       -2         -1  Null

print(animes)
print(type(animes))
print(animes[0])
print(animes[3])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[-1])
print(list[3][0])
print(list[-1][1])

list[2] = False
list[-1][0] = "D"
print(list)
print(len(list)) #length

# tuple
tuple = ("A", 123, True)
print(tuple[0])

#tuple[1] = 789 error:  tuple is immtable

print(tuple)

#dict
dict = {
    "name": "Torquato",
    "age": 45,
    "is_admin": True
}
print(dict)
print(type(dict))

print(dict["name"])
print(dict["age"])
print(dict["is_admin"])