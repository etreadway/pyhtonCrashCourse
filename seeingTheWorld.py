# places I'd like to visit
vacationSpots = ['japan', 'australia', 'mediterranean', 'burning man', 'canada']
print(vacationSpots)
print('\n' + '-' * 20)

# sorting without changing the order
print(sorted(vacationSpots))
print(vacationSpots)
print('\n' + '-' * 20)

# reversing the order
vacationSpots.reverse()
print(vacationSpots)
print('\n' + '-' * 20)

# changing it back
vacationSpots.reverse()
print(vacationSpots)
print('\n' + '-' * 20)

# changing the actual order of the list to be alpha
vacationSpots.sort()
print(vacationSpots)

# changing the actual order of the list to be reverse alpha
vacationSpots.sort(reverse=True)
print(vacationSpots)