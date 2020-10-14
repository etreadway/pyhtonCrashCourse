# Use from to specify file name
# "import" can be used on whole file or specific function when using "from"
# Use "as" to name a function to make things easier
# Can also use "as" to give identity to module
from pizza import makePizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')