class Animal:
    Legs=4
    def __init__(self):
        eyes=2
        print(eyes)
    def type1(self):
        return "Animal Kingdom"
class Lion(Animal):
    def characters(self):
        return "King of Jungle"

l=Lion()
print("Legs:",l.Legs)

print("Hierarchy:",l.type1())
print("Speciality:",l.characters())