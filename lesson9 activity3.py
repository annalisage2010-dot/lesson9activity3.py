class parrot:
    species = "bird"
    def __init__(self, name, age):
     self.name = name
     self.age = age

Gina= parrot("Gina", 20)
Dally= parrot("Dally", 40)
print("Gina is a {}".format(Gina.species))
print("Dally is also a {}".format(Dally.species))
print("{} is {} years old".format(Gina.name,Gina.age))
print("{} is {} years old".format(Dally.name,Dally.age))