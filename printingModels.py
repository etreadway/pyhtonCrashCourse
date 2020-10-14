import printingFunctions as pf
# Start with some designs that need to be printed.
unprintedDesigns = ['iphone case', 'robot pendant', 'dodecahedron']
completedModels = []

pf.printModels(unprintedDesigns[:], completedModels)
pf.showcomplete(completedModels)
print(unprintedDesigns)
