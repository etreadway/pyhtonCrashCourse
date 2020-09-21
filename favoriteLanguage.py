# Using a dict to store info on many objects

favLanguage = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# # printing individually
# print('Sarah\'s favorite language is ' +
#       favLanguage['sarah'].title() +
#       '.')

# # printing using a for loop
# for name, language in favLanguage.items():
#     print(name.title() + '\'s favorite language is '
#           + language.title() + '.')
#
#
# print('-' * 20)
# print('This is how I was doing it')
# print('\n')
# for name in favLanguage:
#     print(name.title())
#
# # this does the same thing but is more explicit
# print('-' * 20)
# print('This is the .keys() method')
# print('\n')
# for name in favLanguage.keys():
#     print(name.title())

# using an if loop to deal with specific keys
friends = ['phil', 'sarah']
for name in favLanguage.keys():
    print(name.title())
    if name in friends:
        print(' Hi ' + name.title() + ', I see your favorite language is ' + favLanguage[name].title() + '!')

if 'erin' not in favLanguage.keys():
    print('Erin please take our pole about languages')
