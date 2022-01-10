class Cat:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def infoCats(self):
        print('Name: {}. Gender: {} , Age: {}'.format(self.name, self.gender, self.age))