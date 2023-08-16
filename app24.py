def greet_user (first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


greet_user('Rafa', 'Gubert')
greet_user('Mary', 'Bitch')

# FOR THE MOST PART USE POSITIONAL ARGUMENTS, BUT IF YOU ARE DEALING WITH NUMERICAL VALUES AND IT IS EXACTLY CLEAR
# WHAT THEY MEAN USE KEYWORD ARGUMENTS (EXAMPLE BELOW), AND IF YOU USE BOTH, POSITIONAL COMES BEFORE

cost (item = 50, shipping = 5, tax = 1.25)
