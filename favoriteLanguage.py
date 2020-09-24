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

# printing using a for loop
friends = ['phil', 'sarah']

for name, language in favLanguage.items():
    if name not in friends:
        print(name.title() + ': ' + language)
    else:
        print('Hi ' + name.title() + ', I see your favorite language is ' +
              favLanguage[name].title() + '!')

if 'erin' not in favLanguage.keys():
    print('Erin, please take the programming language poll!')

# Using the sorted function
for name in sorted(favLanguage.keys()):
    print(name.title() + ', thank you for taking the poll!')

# Looping through values
print('\nThe following languages have been mentioned:')
for language in set(favLanguage.values()):
    print(language)