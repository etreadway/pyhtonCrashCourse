def printModels(unprinted, completed):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed after printing.
    '''
    while unprinted:
        current = unprinted.pop()

        # simulate creating a 3d print from the design.
        print('Printing model: ' + current)
        completed.append(current)

def showcomplete(completed):
    '''Show all the models that were printed.'''
    print('\nThe followint models have been printed:')
    for thing in completed:
        print(thing)

# Start with some designs that need to be printed.
unprintedDesigns = ['iphone case', 'robot pendant', 'dodecahedron']
completedModels = []

printModels(unprintedDesigns[:], completedModels)
showcomplete(completedModels)
print(unprintedDesigns)