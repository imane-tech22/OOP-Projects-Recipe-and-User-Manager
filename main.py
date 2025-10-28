import time
class Recipe:
    def __init__(self,name,ingredients,times,instructions):
        self.name=name
        self.ingredients=ingredients
        self.times=times
        self.instructions=instructions
    def display_recipe(self):
        print(f'Name: {self.name}\nIngredients: {self.ingredients}\nTime: {self.times}\nInstructions: {self.instructions}')
def info():
    name=input('enter the name of recipe:')
    ingredients=input('Enter the ingredients(separated by comma):')
    times=input('Enter cooking time:')
    instructions=input('Enter cooking instructions:')
    return Recipe(name,ingredients,times,instructions)
recipe_info= info()
print('\nDisplaying recipe....\n')
time.sleep(3)
print(f'{'-'*10}')
recipe_info.display_recipe()
print(f'{'-'*10}')


print("project two...")
time.sleep(3)



class User:
    def __init__(self,first_name,last_name,email,password):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
    def display_user(self):
        print(f'First name: {self.first_name}\nLast name: {self.last_name}\nEmail: {self.email}\nPassword: {self.password}')
def input_information():
    first_name=input('enter your first name')
    last_name=input('enter your last name')
    email=input('enter your email')
    password=input('Enter your password')
    return User(first_name,last_name,email,password)
user_info=input_information()
user_info.display_user()








