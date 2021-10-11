import time, datetime, math
import os

def main():

    (walk, bike, boat) = ('🚶', '🚴', '⛴')
    clear = lambda: os.system('clear')
    timetable = {'Rödsten': ['07:03', '07:47', '08:31', '09:50', '10:55', '12:26', '15:55'],
                'Husvik': ['07:42', '10:46', '15:23', '16:12', '18:21']}

    def center(str):
        padding = (width - len(str))//2
        return(' ' * padding + str + ' ' * padding)

    while True:
        now = datetime.datetime.now()
        (width, height) = os.get_terminal_size()[0:2]

        if now.isoweekday() in [1, 3, 5]:
            (boatstop, Alvar) = ("Rödsten", walk)
        elif now.isoweekday() in [2, 4]:
            (boatstop, Alvar) = ("Husvik", bike)
        else:
            print('\n\n')
            print(center('Helg.'))
            print('\n\n')
            return()

        boattime = next((datetime.datetime(year=now.year, month=now.month, day=now.day, hour=int(x.split(':')[0]), minute=int(x.split(':')[1])) for x in timetable[boatstop]
                if datetime.datetime(year=now.year, month=now.month, day=now.day, hour=int(x.split(':')[0]), minute=int(x.split(':')[1])) > now), '')

        if boattime == '':
            timeleft = 'Ingen mer båt ikväll.'
        else:
            timeleft = str(math.floor((boattime - now).seconds / 60)) + ' minuter'

        clear()
        paddingtop = (height-4)//2
        print('\n' * paddingtop)
        print(center(timeleft + '\n\n'))
        print(center(boatstop + '  ' + boat + '  ' + Alvar))
        time.sleep(5)

main()
