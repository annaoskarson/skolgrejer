import random, sys, time
import termcolor
import os

# Gör ett glosförhörsprogram, glosor matas in per vecka, default när man kör är senaste veckan. json-fil?
# Om man svarar fel får man reda på svaret och om man medan man ser det skriver det rätt så får man fortsätta.
# Då ligger frågan kvar tills man svarat rätt en gång utan att få se det.

def main():

    def fireworks(string):
        col = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        for t in range(30):
            clear()
            print(string)
            for i in range(height-8):
                row = ' ' * random.randrange(width-1)
                print(row + termcolor.colored('*',random.choice(col)))
            time.sleep(0.3)

    def scoring(score, car):
        behind = int(round(score * (width-10)))
        ahead = int(round(width - behind-10))
        #print('test', width, ahead, behind)
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
            road = termcolor.colored('░', 'white')
            goal = '🗻'

        path = road * ahead
        after = road * behind
        return('\n\n '
            + goal + path + car + after + start
            + '\n\n')

    clear = lambda: os.system('clear')
    width = os.get_terminal_size()[0]
    height = os.get_terminal_size()[1]

    if len(sys.argv) == 1:
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

    question = random.choice(questions)
    total = len(questions)
    practise = False
    while True:
        score = (len(correct) + (total-len(questions))) / (2*total)
        clear()
        print(scoring(score, car))
        t0 = time.time()
        ans = input('     ' + str(question[0]) + ' ⋅ ' + str(question[1]) + ' = ')
        if not(ans.isnumeric()):
            print('\n     Du måste skriva siffror. Försök igen.\n\n     Tryck på enter (⮐ ) för att fortsätta.')
            input('\n     ')
        elif int(ans) == question[0]*question[1]:
            t1 = time.time()
            tdiff = t1-t0
            if practise:
                practise = False
            elif question in correct:
                questions.remove(question)
            else:
                correct.append((question))
                if tdiff < 6:
                    questions.remove(question)
            if len(questions) > 0:
                question = random.choice(questions)
            else:
                clear()
                score = 1
                string = 'Du kan det här bra nu. Grattis!'
                padding = ' ' * int(round(width - len(string)) /2)
                fireworks(scoring(score, car) + padding + string)
                return()
        else:
            clear()
            practise = True
            print(scoring(score, car))
            print('     ' + str(question[0]) + ' ⋅ ' + str(question[1]) + ' ≠ ' + ans)
            print('\n     Rätt svar är ' + str(question[0]*question[1]) + '.')
            print('\n     Försök igen! Tryck på enter (⮐ ) för att fortsätta.')
            input('\n     ')

main()
