# 1. Encapsulation in Python
# RPG Player Character
# We bind the methods and attributes in one object

class PlayerCharacter:
  def __init__(self, name, age, is_human):
    if(is_human):
      self.name = name
      self.age = age
    else:
      print('You type the wrong answer on the question!')

math_questions = [
  '1+4', '5+7', '6+4', '10+2'
]
math_answers = []

for item in math_questions:
  math_answers.append(eval(item))
  print(math_answers)
answer = int(input(f'Type the corrent answer on the following question: {math_questions[0]}\n'))
if(answer == math_answers[0]):
  player1 = PlayerCharacter('John', 22, answer)

print(player1.name, player1.age)

# 1. Abstraction in Python
# RPG Player Character
# We bind the methods and attributes in one object

class PlayerCharacter1:
  def __init__(self, name, age, is_human):
    if(is_human):
      self.name = name
      self.age = age
    else:
      print('You type the wrong answer on the question!')

math_questions = [
  '1+4', '5+7', '6+4', '10+2'
]
math_answers = []

for item in math_questions:
  math_answers.append(eval(item))
  print(math_answers)
answer = int(input(f'Type the corrent answer on the following question: {math_questions[0]}\n'))
if answer == math_answers[0]:
  player1 = PlayerCharacter1('John', 22, answer)

print(player1.name, player1.age)


# 3. Inheritance in Python
# Role-Playing Game
# In this game users can be: archers, wizards, warriors, etc...

class PlayerClass:
  def sign_in(self):
    print('logged in')

class Wizard(PlayerClass): # that's the way how we can inheritance one class from another
  has_magic = True
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Warrior(PlayerClass): # that's the way how we can inheritance one class from another
  has_strength = True
  def __init__(self, name, weapon):
    self.name = name
    self.weapon = weapon
  def attack(self):
    print(f'attacking with {self.weapon}')

wizard1 = Wizard('Glok', 'fire')
print(wizard1.has_magic)
Wizard.has_magic = False
print(wizard1.has_magic)
warrior1 = Warrior('Gram', 'axe')

# Each of this Classes has its own 'attack' method

wizard1.attack()
warrior1.attack()


print(isinstance(warrior1, PlayerClass))