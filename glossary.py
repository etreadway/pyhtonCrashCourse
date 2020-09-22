# small list of terms and their meanings

glossary = {'concatenate': 'To link things together in a chain or series.',
            'loop': 'A programming structure that repeats a sequence of '
                    'instructions until a specific condition is met.',
            'tuple': 'A collection of objects that is ordered and immutable',
            'key-value pair': 'A set of values associated with each other in a dictionary.',
            'list': 'A method of storing values in an indexed order.',
            'set': 'An ordered collection of data types that is iterable, mutable, and without duplicate elements.',
            'items()': 'A method used to return the list of all keys and values in a dictionary.',
            'dictionary': 'An unordered collection of data; used to store data like a map with a key for each value.',
            'element': 'Another term for an item in python.',
            'boolean': 'A binary variable, having two possible values; "True" and "False". Named after George Boole.',
            }

# looping through to print words and their definition
for word, definition in glossary.items():
    print('\n' + word.title() + ': ' + definition)