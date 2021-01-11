#creating Dictionary with User Data
users_database = {
  'jakomo' : {
    'name' : 'Aria',
    'surname' : 'Griffin',
    'age' : 21,
    'email' : 'asnnd@fja.com',
    'phone' : '+44455121',
    'country' : 'Jamaica',
    'user login' : 'jakomo'
  },
  'breni' : {
    'name' : 'Jack',
    'surname' : 'Flist',
    'age' : 42,
    'email' : '112sdfsgyy@asxafafxza.net',
    'phone' : '+158846656589',
    'country' : 'USA',
    'user login' : 'breni'
  },
}

welcome_text = 'Welcome, User!'

#Writing user data
def get_user_data():
  user_data = {
    'user_name' : input('Please type your name: '),
    'user_surname' : input('Please type your surname: '),
    'user_age' : int(input('Please type your age: ')), #Converting an input value from string to integer
    'user_email' : input('Please type your email: '),
    'user_phone' : int(input('Please type your phone (without \'+\' sign): ')), #Converting an input value from string to integer
    'user_country' : input('Please type your country: '),
  }
  return user_data

#Create a user login and check that isn't already exist in users_database
def create_uniq_username():
  i = 0
  while(i != 1):
    user_login = input('Please type your username (It must be unique!): ')
    if((user_login not in users_database.keys())):
      i=1
      print(f'Your login \'{user_login}\' is unique.')
      return user_login
    else:
      i = 0
      print(f'Your login \'{user_login}\' is already exist. Try another one.')

new_user_data = get_user_data()

print(
  f'''
Please verify your entered data:

  Name: {new_user_data['user_name']}
  Surname: {new_user_data['user_surname']}
  Age: {new_user_data['user_age']}
  Email: {new_user_data['user_email']}
  Phone: +{new_user_data['user_phone']}
  Country: {new_user_data['user_country']}
  '''
)

def create_new_user(name, surname, age, email, phone, country):
  username = {
    'name' : name,
    'surname' : surname,
    'age' : age,
    'email' : email,
    'phone' : phone,
    'country' : country,
    'user login' : create_uniq_username()
  }
  return username

#Checking if the data is correct
print('\nIf all data is correct enter \'Confirm\' below. If something is wrong, type \'Correct\' to correct your data.')
number = 0
while(number != 1):
  confirmation_word = input('\nType \'Confirm\'  or \'Correct\' here: ')
  #if the data is correct then add a new user into users_database
  if(confirmation_word == 'Confirm'):
    number += 1
    new_user = create_new_user(new_user_data['user_name'], new_user_data['user_surname'], new_user_data['user_age'], new_user_data['user_email'], new_user_data['user_phone'], new_user_data['user_country'])
    users_database[new_user['user login']] = new_user
    print('\nEverything is OK!')
  #if some data isn't correct
  elif(confirmation_word == 'Correct'):
    number = 0
    new_user_data = get_user_data()
  #if something goes wrong.
  else:
    number = 0
    print('Try again!')
print('\n')
print(users_database)