import datetime as dt

POINT_DISTRIBUTION = [25,18,15,12,10,8,6,4,2,1]

'''
data = open('championship.txt', 'r')
#Load races
races = data.next().split(',')

#Load Scoring Racers
racers = []
for item in range(len(races)):
    racers = racers + data.next().split(',')
racers = list(set(racers))
'''

'''
data in
'''

def register_race_manual(racename,flag = 'DNF_DEATH'):
    race = {0:racename,1:[]}
    for player in range(10):
        name = input('Racer Name: \n')
        m,s,ms = input('Qualification Time: min:sec:msec]\n').split(':')
        race.update({name:[0,dt.timedelta(minutes=int(m),seconds=int(s),milliseconds=int(ms)*10)]})
    if (flag == 'DNF_DEATH'):
        dnf = '0'
        while dnf != '0':
            dnf = input('Disqualified: (0 to end)\n')
            race[0].append(dnf)
    return race
        
def register_race_txt(racename,flag = 'DNF_DEATH'):
    rdata = open(racename+'.txt', 'r')
    race = {0:racename,1:[]}
    racers = rdata.readline()[:-1].split(',')
    times = rdata.readline()[:-1].split(',')
    for i in range(len(racers)):
        m,s,ms = times[i].split(':')
        race.update({racers[i]:dt.timedelta(minutes=int(m),seconds=int(s),milliseconds=int(ms)*10)})
    if (flag == 'DNF_DEATH'):
        dnf = rdata.readline()[:-1].split(',')
        race[1] = dnf
    return race

def championship(races):
    board = {}
    racers = []
    #Find players
    for race in races:
        racers = racers + list(race.keys()) + race[1]
    racers = list(set(racers))
    racers.remove(0);racers.remove(1)

    #Populate Board
    for racer in racers:
        board.update({racer:[0,[]]})

    #Check results and assign points
    for race in races:
        #Do point distribution on qualified racers
        qplayers = list(race.keys())
        qplayers.remove(1);qplayers.remove(0)
        qtimes = [race[key] for key in qplayers]
        i=0
        while qplayers != []: #Get the id of the lowest time on the list, register to board and delete name and time
            pid = qtimes.index(min(qtimes))
            board[qplayers[pid]][0] += POINT_DISTRIBUTION[i]
            i+=1
            board[qplayers[pid]][1].append(qtimes[pid])
            qplayers.remove(qplayers[pid]);qtimes.remove(qtimes[pid])
        for racer in racers:
            if(racer in race[1]):
                board[racer][1].append('DNF')
            elif(racer not in list(race.keys())):
                board[racer][1].append('EDR')
    #Return Leaderboard Dictionary
        return board
    




