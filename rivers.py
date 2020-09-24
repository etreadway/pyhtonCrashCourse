rivers = {'mississippi river': 'the united states',
          'nile': 'egypt',
          'ganges': 'india and bangladesh',
          'amazon river': 'south america',
          'niger river': 'west africa',
          }

# printing a sentence  about the river and location
for river, place in rivers.items():
    print('The ' + river.title() + ' runs through ' + place.title())

# printing the names of each river individually
for river in rivers.keys():
    print('The ' + river.title())

# printing the locations
for place in rivers.values():
    print(place.title())