import random as r
RPS = [
    'Rock', 'Paper', 'Scissors'
]
SCORE = {
    'WIN': 0, 'LOSE': 0
}
QUIT = [
    'yes', 'y', 'exit', 'quit', 'q', 'give up', 'you win'
]


def VS(user, pc):
    US_CHOICE = '{}'.format(user)
    PC_CHOICE = '{}'.format(pc)
    print(US_CHOICE, 'vs', PC_CHOICE)
    if US_CHOICE == 'Rock' and PC_CHOICE == 'Scissors':
        print('YOU WIN!')
        SCORE['WIN'] += 1
    elif US_CHOICE == 'Scissors' and PC_CHOICE == 'Paper':
        print('YOU WIN')
        SCORE['WIN'] += 1
    elif US_CHOICE == 'Paper' and PC_CHOICE == 'Rock':
        print('YOU WIN')
        SCORE['WIN'] += 1
    elif US_CHOICE == 'Rock' and PC_CHOICE == 'Paper':
        print('YOU LOSE')
        SCORE['LOSE'] += 1
    elif US_CHOICE == 'Paper' and PC_CHOICE == 'Scissors':
        print('YOU LOSE')
        SCORE['LOSE'] += 1
    elif US_CHOICE == 'Scissors' and PC_CHOICE == 'Rock':
        print('YOU LOSE')
        SCORE['LOSE'] += 1
    else:
        print('DRAW')


def main():
    while True:
        computer = r.choice(list(RPS))
        user = input("Choose: Rock, Paper, Scissors ").capitalize()
        VS(user, computer)
        for key, value in SCORE.items():
            print(key, ':', value)
        PLAY = input('Give up? ').lower()
        if PLAY in QUIT:
            break



if __name__ == '__main__':
    main()
