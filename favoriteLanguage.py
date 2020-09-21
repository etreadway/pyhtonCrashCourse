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
for name, language in favLanguage.items():
    print(name.title() + '\'s favorite language is '
          + language.title() + '.')