class Chef:
    def makeChicken(self):
        print("chicken")

class SpecialChef(Chef):
    def makeRice(self):
        print("rice")

brooks = Chef()
z23 = SpecialChef()

brooks.makeChicken()
z23.makeChicken()
z23.makeRice()