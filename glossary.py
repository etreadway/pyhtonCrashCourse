# small list of terms and their meanings

glossary = {'concatenate': 'To link things together in a chain or series.',
            'loop': 'A programming structure that repeats a sequence of '
                    'instructions until a specific condition is met.',
            'tuple': 'A collection of objects that is ordered and immutable',
            'key-value pair': 'A set of values associated with each other in a dictionary.',
            'list': 'A method of storing values in an indexed order.'}

# looping through to print words and their defonitions
for word in glossary:
    print('\n' + word.title() + ': ' + glossary[word])