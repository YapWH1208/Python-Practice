class Cat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self, sentence):
        self.sentence = sentence
        return self.sentence

cat1 = Cat("SB", 2, "White")

print(f"Name: {cat1.name}\nAge: {cat1.age}\nColor: {cat1.color}")