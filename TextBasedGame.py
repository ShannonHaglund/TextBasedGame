# A dictionary for the Shannon's Adventure Game
# The dictionary links a room to other rooms and items
rooms = {
    'Cottage': {
        'Direction': {
            'West': 'Blacksmith'}
    },
    'Blacksmith': {
        'Direction': {
            'East': 'Cottage',
            'North': 'Village Center'},
        'Item': 'Shield'
    },
    'Village Center': {
        'Direction': {
            'South': 'Blacksmith',
            'West': 'Armory',
            'North': 'Forest',
            'East': 'Tavern'},
        'Item': 'Slingshot',
        },
    'Armory': {
        'Direction': {
            'East': 'Village Center'},
        'Item': 'Sword',
    },
    'Tavern': {
        'Direction': {
            'West': 'Village Center',
            'North': 'River'},
        'Item': 'Porridge',
    },
    'River': {
        'Direction': {
            'South': 'Tavern'},
        'Item': 'Fairy Dust',
    },
    'Forest': {
        'Direction': {
            'South': 'Village Center',
            'East': 'Mountain'},
        'Item': 'Healing Potion',
    },
    'Mountain': {
        'Direction': {
            'West': 'Forest'},
        'Villain': 'Troll'
    }
}


# Define the welcome message function
# Explain valid moves
def welcome_message():
    print('Welcome to Shannon\'s Adventure Game')
    print('***')
    print('Your village is being terrorized by the troll that lives in the mountain! \nYou have been chosen by the '
          'village to defeat the terrible troll. \nBefore you can battle the troll, you must collect a shield from the '
          'blacksmith, \na slingshot from the village center, a healing potion in the \nforest, porridge from the '
          'tavern, fairy dust from the river, \nand a sword from the armory.  If you collect all six items, '
          'you can defeat the troll.')
    print('***')
    print('Valid Commands:  Go North, Go South, Go East, Go West, Get item, and Exit')
    print('***')


def show_status(location, inventory):
    # Print player location accessing room dictionary
    print('You are at the {}'.format(location))
    print('Inventory:', inventory)
    print('-----------------')


def gameplay_loop():
    inventory = []  # Define empty inventory array
    location = 'Cottage'

    # While loop does not equal exit
    while location != 'Exit':
        show_status(location, inventory)

        if 'Item' in rooms[location].keys():
            print('You see a {}'.format(rooms[location]['Item']))

        # Get player command input
        command = input('Enter your command: ').split()
        if command[0] == 'Exit':
            location = 'Exit'

        # If command is valid, change room locations
        elif command[0] == 'Go':
            if command[1] in rooms[location]['Direction']:
                location = rooms[location]['Direction'][command[1]]
            else:
                print('Invalid direction')

        elif command[0] == 'Get':
            if command[1] in rooms[location]['Item']:
                inventory.append(rooms[location]['Item'])
                print('You have the {}'.format(rooms[location]['Item']))
                del rooms[location]['Item']
            else:
                print('Invalid command.')
        else:
            print('Invalid command.')

        if location == 'Mountain' and len(inventory) == 6:
            print('You have defeated the troll!  You won the game!')
            location = 'Exit'
        elif location == 'Mountain' and len(inventory) < 6:
            print('The troll defeats you! You lose.')
            location = 'Exit'


welcome_message()
gameplay_loop()

print('Thanks for playing! The game has ended.')