favLanguage = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['elliot', 'hannah', 'jen', 'sarah', 'bryan', 'andy', 'edward', 'phil']

for name in people:
    if name in favLanguage.keys():
        print(name.title() + ', thank you for taking the poll. ' + favLanguage[name].title() + ' is a great language.')
    else:
        print(name.title() + ', please take the poll.')