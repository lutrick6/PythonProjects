import random as r


char_race = {
    'Dwarf',
    'Human',
    'Elf',
}
char_class = {
    'Warrior',
    'Mage',
    'Rogue',
}

race_select, class_select = r.choice(list(char_race)), r.choice(list(char_class))

character = {
    'Name': 'Robert',
    'Race': '{}'.format(race_select),
    'Class': '{}'.format(class_select),
    'Special': '{}'.format(special_select),
    'Stats': {
        'HP': 100,
        'Attack': 8,
        'Defense': 5,
        'Speed': 3,
        'Heal': 2,
        'Level': 1,
    }
}
def CHARACTER(Name, Race, Class, Special, Stats): 

    print('Name: ', character['Name'])
    print('Race: ',character['Race'])
    print('CLass: ', character['Class'])
    print('Level: ', character['Stats']['Level'])
    print('Health: ',character['Stats']['HP'])
    print('Attack: ', character['Stats']['Attack'])
    print('Defense: ', character['Stats']['Defense'])
    print('Speed', character['Stats']['Speed'])
    print('Heal: ', character['Stats']['Heal'])
