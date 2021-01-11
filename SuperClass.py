class User():
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # There are 2 ways that we can use methods and arguments from Parent Method
        # The first one: "User.__init__(self, email)" but it doesn't look clean
        # The second one:
        super().__init__(email) # It looks better and we also shouldn't give "self" as an argument.
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)