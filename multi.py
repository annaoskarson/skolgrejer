import random, sys, time
import termcolor
import os

def main():
    clear = lambda: os.system('clear')

    if len(sys.argv) == 1:
        print("Testar alla tabellerna, 1-10.")
        print("För att välja tabeller, skriv '1-4' eller '2,6,5' som argument.")
        tables = list(range(11))
    elif '--' in sys.argv[1]:
        print("\nFör att välja tabeller, skriv '1-4' eller '2,6,5' som argument.")
        print("Skriver du inget, testas tabellerna 0-10.\n")
        return()
    elif ',' in sys.argv[1]:
        tables = list(map(int, sys.argv[1].split(',')))
    elif '-' in sys.argv[1]:
        fr,to = map(int, sys.argv[1].split('-'))
        tables = list(range(fr,to+1))
    elif sys.argv[1].isnumeric():
        tables = [int(sys.argv[1])]

    questions = []
    for i in tables:
        for j in range(11):
            questions.append((i,j))

    correct = []
    car = random.choice(['🚃','🚌','🚕','🚐','🚑','🚒','🚓','🚴','🚶','🛻',
                    '🛸','🚗','🚚','🚙','🚜','🚂','🛥','🛺','🛰','🚣','🚤',
                    '🛷','⛷','🛶'])

    def fireworks(string):
        col = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        for t in range(30):
            clear()
            print(string)
            space = ''
            for i in range(14):
                row = ' ' * random.randrange(61)
                print(row + termcolor.colored('*',random.choice(col)))
            time.sleep(0.3)

    def scoring(score, car):
        left = 60 - score
        # Defaults
        goal = '🏁'
        start = '🚦'
        road = '_'
        if car in ['🛥','🚣','🚤','🛶']:
            road = termcolor.colored('𛲗', 'blue')
        elif car in ['🛸']:
            road = termcolor.colored('☁', 'grey')
            goal = '✧'
        elif car in ['🛰']:
            road = '.'
            goal = '🌍'
        elif car in ['🚒']:
            goal = '🔥'
        elif car in ['🚜']:
            goal = '💩🚧'
        elif car in ['🚓']:
            goal = '🚶'
        elif car in ['🚌']:
            goal = '🚏'
        elif car in ['🚃','🚂']:
            goal = '🚉'
        elif car in ['🚑']:
            goal = '🏥'
        elif car in ['🚶']:
            goal = '🚽🚪'
        elif car in ['🛷']:
            goal = '☃'
        elif car in ['⛷']:
            road = '░'
            goal = '🗻'

        path = road * left
        after = road * score
        return('\n\n\n   '
            + goal  + path + car + after + start
            + '\n\n\n')


    question = random.choice(questions)
    total = len(questions)
    while True:
        score = (len(correct) + (total - len(questions)))*60 // (2*total)
        clear()
        print(scoring(score, car))
        ans = input('     ' + str(question[0]) + ' * ' + str(question[1]) + ' = ')
        if not(ans.isnumeric()):
            print('     Du måste skriva siffror. Försök igen.\n\n     Tryck på enter (⮐ ) för att fortsätta.')
            input()
        elif int(ans) == question[0]*question[1]:
            if question in correct:
                questions.remove(question)
            else:
                correct.append((question))
            if len(questions) > 0:
                question = random.choice(questions)
            else:
                clear()
                score = 60
                string = 'Du har klarat alla uppgifter två gånger. Grattis!'
                fireworks(scoring(score, car) + '     ' + string)
                return()
        else:
            clear()
            print(scoring(score, car))
            print('     ' + str(question[0]) + ' * ' + str(question[1]) + ' ≠ ' + ans)
            print('\n     Rätt svar är ' + str(question[0]*question[1]) + '.')
            print('\n     Försök igen! Tryck på enter (⮐ ) för att fortsätta.')
            input()

main()