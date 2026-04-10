import random
import math
import time
import builtins
words = [
    "apple", "river", "mountain", "shadow", "crystal", "flame", "ocean", "forest",
    "storm", "cloud", "stone", "ember", "glow", "breeze", "thunder", "lightning",
    "valley", "meadow", "desert", "island", "canyon", "cliff", "wave", "current",
    "drift", "echo", "whisper", "spark", "frost", "mist", "rain", "snow",
    "hail", "wind", "dust", "sand", "leaf", "branch", "root", "bark",
    "flower", "petal", "seed", "bloom", "vine", "grass", "moss", "fern",
    "wolf", "tiger", "eagle", "hawk", "falcon", "bear", "fox", "deer",
    "rabbit", "otter", "whale", "shark", "dolphin", "octopus", "crab", "lobster",
    "ant", "beetle", "spider", "butterfly", "dragonfly", "bee", "wasp", "hornet",
    "fire", "water", "earth", "air", "metal", "wood", "light", "dark",
    "time", "space", "void", "energy", "matter", "gravity", "force", "motion",
    "signal", "cipher", "code", "logic", "binary", "vector", "matrix", "kernel",
    "thread", "process", "system", "network", "packet", "server", "client", "proxy",
    "random", "chaos", "order", "pattern", "shape", "form", "structure", "design",
    "alpha", "beta", "gamma", "delta", "omega", "sigma", "theta", "lambda",
    "pixel", "canvas", "render", "shader", "texture", "frame", "sprite", "layer",
    "clock", "gear", "engine", "motor", "circuit", "wire", "voltage", "current",
    "book", "page", "chapter", "story", "poem", "verse", "letter", "symbol",
    "dream", "thought", "memory", "vision", "idea", "mind", "soul", "spirit"
    ]
def cptl(letter_str, width=None):
    lines = letter_str.strip("\n").split("\n")
    min_leading = min((len(line) - len(line.lstrip(' ')) for line in lines if line.strip()),default=0)
    lines = [line[min_leading:] for line in lines]
    lines = [line.rstrip() for line in lines]
    while len(lines) < 7:
        lines.insert(0, "")
    if width is None:
        width = max(len(line) for line in lines)
    return [list(line.ljust(width)) for line in lines]
def getmaze(d):
    def makegrid(d):
        row = ['⬜']+(['⬛','⬜']*(d-1))
        final = [row.copy() if i%2==0 else ['⬛']*(d*2-1) for i in range(d*2-1)]
        return final
    grid=makegrid(d)
    def printgrid(grid):
        for i in grid:
            print(' '.join(i))
    cx=(cx:=random.randint(0,d*2-2))+cx%2
    cy=(cy:=random.randint(0,d*2-2))+cy%2
    grid[cy][cx]="🟧"
    error = False
    path = []
    while True:
        accdir=[]
        for i in range(4):
            if i==0 and cy>1:
                if grid[cy-2][cx] == '⬜':
                    accdir.append((cy-2,cx))
            if i==1 and cx<d*2-3:
                if grid[cy][cx+2]=='⬜':
                    accdir.append((cy,cx+2))
            if i==2 and cy<d*2-3:
                if grid[cy+2][cx]=='⬜':
                    accdir.append((cy+2,cx))
            if i==3 and cx>1:
                if grid[cy][cx-2]=='⬜':
                    accdir.append((cy,cx-2))
        if len(accdir)>0:
            choice=random.choice(accdir)
            grid[int((choice[0]+cy)/2)][int((choice[1]+cx)/2)]='🟧'
            cx=choice[1]
            cy=choice[0]
            grid[cy][cx]="🟧"
            path.append((cy,cx))
        else:
            grid[cy][cx]='🟦'
            try:
                path.pop(-1)
                cy, cx = path[-1]
                grid[cy][cx]='🟦'
            except:
                break
    final=[['⬜' if j in ["🟦","🟧"] else "⬛" for j in i] for i in grid]
    return final
def printgrid(grid):
    for i in grid:
        print(' '.join(i))
def oprintgrid(grid):
    for i in grid:
        print(''.join(i))
def printlocs(locations):
    print('			'.join(locations))
def getct(starttime):
    ct = time.time()-starttime
    hours = int(((ct//30)+12)%24)
    minutes = int((ct%60)//1)
    pm = hours>=12
    if pm:
        if hours >=13:
            hours-=12
        return (f"{'0' if hours<10 else ''}{str(hours)}", f"{'0' if minutes<10 else ''}{str(minutes)}", "P.M.")
    return (f"{'0' if hours<10 else ''}{str(hours)}", f"{'0' if minutes<10 else ''}{str(minutes)}", "A.M.")

def getcon(map, location):
    if "requirements" in map[location].keys():
        return eval(map[location]["requirements"])
    return True
def cmds():
    print('Commands:\n north/east/south/west  - moves that direction')
    print(' in/enter               - enters thing')
    print(' view                   - reads location description')
    print(' look                   - displays items in current location')
    print(' grab/take/pick up      - grabs an item')
    print(' drop                   - drops an item')
    print(' fight                  - fights a creature')
    print(' stats                  - prints the players stats')
    print(' backpack/inv/inventory - prints players backpack')
    print(' collect                - collects gold at an area')
    print(' buy                    - purchases a specified item')
    print(' equip                  - equips the specified item')
    print(' talk                   - used exclusively to talk to the shopkeeper')
    print(' Tip: sometimes if an enemys speed stat is higher than yours it will attack first')

def view(map, location):
    print(f"You are in the {location}.\n{map[location]['description']}")
def getstats(player):
    print("Name: "+player["name"])
    print('---------------------')
    print('Gold: '+str(player['money']))
    print('Keys: '+ (', '.join(player['keys']) if len(player['keys'])>0 else 'none'))
    print("Health: "+str(player["health"]))
    print("Max Health: "+str(player["maxhealth"]))
    print("Strength: "+str(player["strength"]))
    print("Resilience: "+str(player["resilience"]))
    print("Accuracy: "+str(player["accuracy"]))
    print("Speed: "+str(player['speed']))
    print("Weapon: ")
    print("	Name: "+player["weapon"]["name"])
    print("	Damage: "+str(player["weapon"]["damage"]))
    print("Armor: ")
    print("	Name: "+player["armor"]["name"])
    print("	Defense: "+str(player['armor']['def']))
def move(map, location, direction):
    return map[location]["directions"][direction]
def backpack(player):
    print("Backpack: ")
    print('[',end='')
    print(']	\n['.join(player["backpack"]),end='')
    print(']')

def pickup(map, location, item, player):
    backpack = player["backpack"]
    if (b:=backpack.index(''))>=0 and (item in map[location].keys()):
        backpack[b] = item
    return backpack

def drop(map,location,item,player):
    if item in (backpack:=player["backpack"]):
        backpack[backpack.index(item)]=''
        map[location]["items"].append(item)
    return (backpack, map)
def fight(map, location, player, enemy, enemies):
    if enemy in map[location]["entities"]:
        if enemies[enemy]["speed"]>player["speed"]:
            input("press enter to start fight")
            print(f'the {enemy} was faster than you, the {enemy} attacked you for {enemies[enemy]["damage"]} damage!')
            player["health"]-=enemies[enemy]["damage"]
        while enemies[enemy]["health"]>0 and player["health"]>0:
            print('''

            ''')
            j=input("attack/flee/items")
            if "attack" in j:
                enemies[enemy]["health"]-=player["weapon"]["damage"]
                print(f'you attacked {enemy} for {player["weapon"]["damage"]} Damage!')
            elif "items" in j:
                while True:
                    print(">>>> ")
                    for q in player["backpack"]:
                        if q != '':
                            print("-", q)
                    x = input("use/exit: ")
                    if "exit" in x:
                        break
                    elif "use" in x:
                        z = input(">>>> ")
                        if z in player["backpack"]:
                            if "health potion" in z:
                                player["health"] += 15
                                player["backpack"].remove(z)
                                print("used item")
                            elif "speed potion" in z:
                                player["speed"] += 5
                                player["backpack"].remove(z)
                                print("used item")
                            elif "strength potion" in z:
                                player["weapon"]["damage"] *= 2
                                player["backpack"].remove(z)
                                print("used item")
                            elif "death potion" in z:
                                print("you died")
                                player["health"] = 0
                            else:
                                print("nothing happened")
                        else:
                            print("you dont have this item")
            elif "flee" in j:
                if player["speed"] >= enemies[enemy]["speed"]:
                    print(f"You successfully fled from the {enemy}!")
                    return
                else:
                    print(f"You failed to flee from the {enemy}!")
            if enemies[enemy]["health"]>0:
                player["health"]-=enemies[enemy]["damage"]
    elif enemy not in map[location]["entities"]:
        print("Enemy not here")
    if player['health']<=0:
        return ('dead', f'You Died! You were killed by a {enemy}!')
def derivative(f,x):
    return (f(x+1e-6)-f(x))/1e-6
def claim(killmap,m):
    gold=0
    key=0
    for i in killmap:
        gold+=i[0]*(i[1]+random.randint(-5,5))
        for j in range(i[0]):
            if random.randint(0,i[0])==0:
                key+=1
    gold*=2**m
    return (gold,key)
def dungeonfight(killmap,player):
    m=1
    print("\n-------------------\nYou were attacked by an ancient spirit!\n-------------------\n")
    try:
        mult=(2*(math.log(killmap[-1][0])-1/(2*killmap[-1][0]))+1.2+random.randint(-20,20)/10)//.1
    except:
        mult=1
    enemy={
        "health" : 7*mult,
        "damage" : 5*mult,
        "speed" : 6*mult,
    }
    if enemy['speed']>player['speed']:
        print(f'The ancient spirit attacked you for {(dam:=enemy["damage"]+random.randint(-20,20)/10)}!')
        player['health']-=dam
    while enemy["health"]>0 and player["health"]>0:
        dfi=''
        while dfi not in ['flee','escape','attack','run','fight','items']:
            dfi=input('What would you like to do? (flee/attack/items) ')
            if dfi not in ['flee','escape','attack','run','fight','items']:
                print('That is not an option!')
        if dfi in ['flee','escape','run']:
            print('You cannot escape from dungeon encounters')
        if dfi in ['fight','attack']:
            print(f'You attacked the ancient spirit for {(dam:=player["weapon"]["damage"]+random.randint(-20,20)/10)}!\n')
            enemy['health']-=dam
            if enemy['health']<=0:
                print('You see the ancient spirit flail in pain, eventually returning to nothing but a pile of ashes on the floor.\n')
                if random.randint(0,1)==0:
                    print('You feel invigorated at the sight of the thing dying.')
                return (True,m)
            else:
                print(f'The ancient spirit attacked you for {(dam:=enemy["damage"]+random.randint(-20,20)/10)}!\n')
                player['health']-=dam
            if player['health']<=0:
                print("The ancient spirit lashes out at you with all it's might. You succumb to the forces of the spirit. You died.")
                return (False,0)
        if dfi=='items':
            # speed potion, death potion, strength potion, money potion
            print('\n   '.join(player['backpack'].join(' ').split(' ')))
            dfit=input('What would you like to use?')
            if 'health' in dfit and 'health potion' in player['backpack']:
                player['health']+=5
                player['backpack'].pop(player['backpack'].index('health potion'))
            elif 'speed' in dfit and 'speed potion' in player['backpack']:
                player['speed']+=5
                player['backpack'].pop(player['backpack'].index('speed potion'))
            elif 'death' in dfit and 'death potion' in player['backpack']:
                player['backpack'].pop(player['backpack'].index('death potion'))
                print('You die.')
                return (False,0)
            elif 'money' in dfit and 'money potion' in player['backpack']:
                m+=1
                killmap[-1][-1]+=(gain:=random.randint(-30,30)/10)
                print(f'You will gain {killmap[-1][0]*(gain-5)} to {killmap[-1][0]*(gain+5)} gold (if you make it out alive.)')
                player['backpack'].pop(player['backpack'].index('speed potion'))
            elif 'strength' in dfit and 'strength potion' in player['backpack']:
                player['weapon']['damage']*=2
                player['backpack'].pop(player['backpack'].index('speed potion'))
            else:
                print('That has no use here!')
def dungeonsys(player):
    m=1
    mapf=builtins.map
    dim=10
    killmap=[[0,0]]
    dungeon=getmaze(dim)
    dungeon[dim-1][dim-1]='🟧'
    enemyct=list(range(random.choice([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,15,15,15,15,15,15,16,16,16,16,16,17,17,17,17,18,18,18,19,19,20])))
    for i in enemyct:
        cx=(cx:=random.randint(0,dim*2-2))
        cy=(cy:=random.randint(0,dim*2-2))
        if dungeon[cy][cx]=='⬜' and (cy,cx)!=(0,dim*2-2):
            dungeon[cy][cx] = '🟥' 
        else:
            enemyct.append(len(enemyct))
    pos = [0,dim*2-2]
    surroundings=[[],[],[]]
    flag = False
    rflag=False
    fflag=False
    while True:
        if rflag:
            dungeon=getmaze(dim)    
            dungeon[dim-1][dim-1]='🟧'
            enemyct=list(range(random.choice([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,15,15,15,15,15,15,16,16,16,16,16,17,17,17,17,18,18,18,19,19,20])))
            for i in enemyct:
                cx=(cx:=random.randint(0,dim*2-2))
                cy=(cy:=random.randint(0,dim*2-2))
                if dungeon[cy][cx]=='⬜' and (cy,cx)!=(0,dim*2-2):
                    dungeon[cy][cx] = '🟥' 
                else:
                    enemyct.append(len(enemyct))
            pos = [0,dim*2-2]
            surroundings=[[],[],[]]
            ex=False
            flag = False
            rflag=False
        if not flag:
            if fflag:
                outcome=dungeonfight(killmap,player)
                if not outcome[0]:
                    return outcome
                else:
                    killmap[-1][-1]+=1
                    m+=outcome[-1]
            surroundings=[[],[],[]]
            pastpos=pos.copy()
            def printsurroundings():
                surroundings=[[],[],[]]
                try:
                    1/pos[0]
                    1/pos[1]
                    surroundings[0].append(dungeon[pos[0]-1][pos[1]-1])
                except:
                    surroundings[0].append('⬛')
                try:
                    1/pos[0]
                    surroundings[0].append(dungeon[pos[0]-1][pos[1]])
                except:
                    surroundings[0].append('⬛')
                try:
                    1/pos[0]
                    surroundings[0].append(dungeon[pos[0]-1][pos[1]+1])
                except:
                    surroundings[0].append('⬛')
                try:
                    1/pos[1]
                    surroundings[1].append(dungeon[pos[0]][pos[1]-1])
                except:
                    surroundings[1].append('⬛')
                surroundings[1].append('⬜')
                try:
                    surroundings[1].append(dungeon[pos[0]][pos[1]+1])
                except:
                    surroundings[1].append('⬛')
                try:
                    1/pos[1]
                    surroundings[2].append(dungeon[pos[0]+1][pos[1]-1])
                except:
                    surroundings[2].append('⬛')
                try:
                    surroundings[2].append(dungeon[pos[0]+1][pos[1]])
                except:
                    surroundings[2].append('⬛')
                try:
                    surroundings[2].append(dungeon[pos[0]+1][pos[1]+1])
                except:
                    surroundings[2].append('⬛')
                surroundings = [['⬜' if j in ["🟥","⬜"] else j for j in i] for i in surroundings]
                surroundings[1][1]='🟥'
                print('\n'.join(list(mapf(lambda x: ''.join(x), surroundings))))
            printsurroundings()
            dungeondirection=input('Which way would you like to go?')
            if ('north' in dungeondirection or dungeondirection in ['n','go n','up','go up','u']) and pos[0]>0 and dungeon[pos[0]-1][pos[1]]!='⬛':
                    pos[0]-=1
            elif ('east' in dungeondirection or dungeondirection in ['e','go e','right','go right','r']) and pos[1]<dim*2-2 and dungeon[pos[0]][pos[1]+1]!='⬛':
                    pos[1]+=1
            elif ('south' in dungeondirection or dungeondirection in ['s','go s','down','go down','d']) and pos[0]<dim*2-2 and dungeon[pos[0]+1][pos[1]]!='⬛':
                    pos[0]+=1
            elif ('west' in dungeondirection or dungeondirection in ['w','go w','left','go left','l']) and pos[1]>0 and dungeon[pos[0]][pos[1]-1]!='⬛':
                    pos[1]-=1
            if pos==pastpos:
                print('You cant go that way!')
            if pos==[dim-1,dim-1]:
                flag=True
            if dungeon[pos[0]][pos[1]]=='🟥':
                fflag=True
        else:
            tex=''
            while tex not in ['exit','continue','stay']:
                tex=input("You've reached the end! What would you like to do? (exit/continue/stay) ")
            if tex=='exit':
                return claim(killmap)
            if tex=='continue':
                killmap.append([killmap[-1][0]+1,0])
                rflag=True
            flag=False
def run(deathtext):
    dungeon = getmaze(5)
    cpt = {
    'a': '''
             /\\
            /  \\/\\
           /      \\/\\
          /          \\/\\ 
         /              \\/\\
        /                  \\ 
    ''',

    'b': '''
            /\\
           /  \\/\\
          /      \\/\\ 
         /          \\/\\
        /              \\ 
    ''',

    'c': '''
           /\\
          /  \\/\\ 
         /      \\/\\
        /          \\ 
    ''',

    'd': '''
          /\\ 
         /  \\/\\
        /      \\ 
    ''',

    'e': ''' 
         /\\
        /  \\ 
    ''',

    'f': '''
               /\\
              /  \\/\\
             /      \\/\\
          /\\/          \\/\\ 
         /                \\/\\
        /                    \\ 
    ''',

    'g': '''
              /\\
             /  \\/\\
          /\\/      \\/\\ 
         /            \\/\\
        /                \\ 
    ''',

    'h': '''
             /\\
          /\\/  \\/\\ 
         /        \\/\\
        /            \\ 
    ''',

    'i': '''
            /\\ 
         /\\/  \\/\\
        /        \\ 
    ''',

    'j': '''
            /\\ 
         /\\/  \\
        /      \\ 
    ''',

    'k': '''
                 /\\
                /  \\/\\
             /\\/      \\/\\
            /            \\/\\ 
         /\\/                \\/\\
        /                      \\ 
    ''',

    'l': '''
                /\\
             /\\/  \\/\\
            /        \\/\\ 
         /\\/            \\/\\
        /                  \\ 
    ''',

    'm': '''
               /\\
            /\\/  \\/\\ 
         /\\/        \\/\\
        /              \\ 
    ''',

    'n': '''
               /\\
            /\\/  \\ 
         /\\/      \\/\\
        /            \\ 
    ''',

    'o': '''
               /\\
            /\\/  \\ 
         /\\/      \\
        /          \\ 
    ''',

    'p': '''
                   /\\
                  /  \\/\\
               /\\/      \\/\\
            /\\/            \\/\\ 
         /\\/                  \\/\\
        /                        \\ 
    ''',

    'q': '''
                  /\\
               /\\/  \\/\\
            /\\/        \\/\\ 
         /\\/              \\/\\
        /                    \\ 
    ''',

    'r': '''
                  /\\
               /\\/  \\/\\
            /\\/        \\/\\ 
         /\\/              \\
        /                  \\ 
    ''',

    's': '''
                  /\\
               /\\/  \\
            /\\/      \\/\\ 
         /\\/            \\
        /                \\ 
    ''',

    't': '''
                  /\\
               /\\/  \\
            /\\/      \\ 
         /\\/          \\
        /              \\ 
    ''',

    'u': '''
                     /\\
                  /\\/  \\/\\
               /\\/        \\/\\
            /\\/              \\/\\ 
         /\\/                    \\/\\
        /                          \\ 
    ''',

    'v': '''
                     /\\
                  /\\/  \\/\\
               /\\/        \\/\\
            /\\/              \\/\\ 
         /\\/                    \\
        /                        \\ 
    ''',

    'w': '''
                     /\\
                  /\\/  \\
               /\\/      \\/\\
            /\\/            \\/\\ 
         /\\/                  \\
        /                      \\ 
    ''',

    'x': '''
                     /\\
                  /\\/  \\
               /\\/      \\
            /\\/          \\/\\ 
         /\\/                \\
        /                    \\ 
    ''',

    'y': '''
                     /\\
                  /\\/  \\
               /\\/      \\
            /\\/          \\ 
         /\\/              \\
        /                  \\ 
    ''',

    'z': '''
                        /\\
                     /\\/  \\
                  /\\/      \\/\\
               /\\/            \\/\\
            /\\/                  \\/\\ 
         /\\/                        \\/\\
        /                              \\ 
    '''
    }
    import random
    import time
    import math
    import builtins
    mapf=builtins.map
    
    starttime = time.time()
    money = 1000
    ###############################
    #	   	    Entities          #
    ###############################

    first = ["Bronster","Brownarry","Browiz","Brohat","Elmbrown","Gwydjade","Jadewise","Gandalf","Brownspell","Jadelegend","Merlde","Wandrown","Jabus"]
    last = ["Harkjade","Grangrown","Jadedore","Harkde","Grangjade","Brownden","Brownspell","Jashot","Harkrown","Grangrown","Dumblebrown","Harkrown","Rongspell"]

    player = {
    "stage":0,
    "name": f"{random.choice(first)} {random.choice(last)}",
    "keys":[],
    "speed":5,
    "health":10,
    "strength":0,
    "resilience":0,
    "maxhealth":10,
    "backpack" : ['','','','','','','','','',''],
    "accuracy":80,
    "money":money,
    "diddungeon":False,
    "weapon":{
        "name": "fists",
        "damage" : 1,
        },
    "armor":{
        "name":"none",
        "def":0,
    },
    }
    enemies = {
    "guard":{
        "health":15,
        "damage":4,
        "speed":5
    },
    "knight":{
        "health":20,
        "damage":6,
        "speed":7
    },
    "troll":{
        "health":12,
        "damage":7,
        "speed":2
    },
    "goblin":{
        "health":5,
        "damage":5,
        "speed":8,
    },
    "wizard":{
        "accuracy":75,
        "health":30,
        "damage":7,
        "speed":2
    },
    "gnome":{
        "health":2,
        "damage":2,
        "speed":6
    },
    "giant lizard":{
        "accuracy":50,
        "health":40,
        "damage":10,
        "speed":1
    },
    "magic golem" : {
        "health" : 100,
        "damage" : 10,
        "speed" : 0,
    },
    "ancient spirit" : {
        "health" : 7,
        "damage" : 5,
        "speed" : 6,
    },
    "hydra":{
        "accuracy": 50,
        "health":60,
        "damage":15,
        "speed":6,
    },
    "shopkeeper":{
        "health":100,
        "damage":100,
        "speed":100,
    },
    "lord":{
        "health":7, #hes weak and fat
        "damage":0,
        "speed":0,
    },
    "mimic":{
        "health":10,
        "damage":4,
        "speed":1,
    },
    }

    items = {
    
        "weapons":{
          "sword":{
            "damage":5
          },
          "polished sword":{
           "damage": 10 
          },
          "ancient staff":{
            "damage":7
          },
          "common sword":{
            "damage":7
          }
        },
        "keys": ['dungeon key', 'shop key'],
        "misc": ['figure'],
        "shop":{
            'common sword':{
                "cost":10
            },
            'speed potion':{
                'cost':5
            },
            'death potion':{
                'cost':0
            },
            'strength potion':{
                'cost':7
            },
            'leather armor':{
                'cost':10
            },
            'money potion':{
                'cost':5
            },
            'resilience potion':{
                'cost':8
            }
        },
        'consumables':{
            'speed potion':{
                'stat':'speed',
                'amount':2
            },
            'strength potion':{
                'stat':'strength',
                'amount':3
            },
            'resilience potion':{
                'stat':'resilience',
                'amount':5
            }
        },
        "armor":{
          "leather armor":{
            "defense":10
          },
          "sturdy armor":{
            "defense":20
          }
        }
    }

    ###############################
    #		   Template 		  #
    ###############################

    # "__": {
    #     "description": "__.",
    #     "directions": {"__":"__", "__":"__", "__":"__", "__":"__"},
    #     "items": [],
    #     "requirements": 
    #     "entities": ["__"]
    #     },

    # "__":{
    #     "health":__,
    #     "damage":_,
    #     "speed":_,

    ###############################
    #		  Dictionaries		  #
    ###############################

    map = {
    "dungeon":{
        "description": "You are in a cold, darlk, wet room, you can barely see a few feet in front of your face. The door has closed behind you.",
        "directions": {"east":"castle courtyard", "south":"dungeon entrance", "west":"forest clearing", "north":"forest wall"},
        "items": [],
        'gold':0,
        "entities": ["guard"]
    },
    "west castle entrance": {
        "description": "A large iron gate protects the castle entrance. There is a guard standing nearby.",
        "directions": {"east":"castle courtyard", "south":"dungeon entrance", "west":"forest clearing", "north":"forest wall"},
        "items": [],
        'gold':0,
        "entities": ["guard"]
        },
    "east castle entrance": {
        "description": "A large iron gate protects the castle entrance. There is a guard standing nearby.",
        "directions": {"west":"castle courtyard", "south":"wall", "north":"well", "east":"den of the giant lizard"},
        "items": [],
        'gold':0,
        "entities": ["guard"]
        },
    "castle courtyard": {
        "description": "The courtyard is overgrown with weeds. You see a rusty broken sword in a mound nearby",
        "directions": {"west":"west castle entrance", "south":"north of the mansion", "east":"east castle entrance", "north":"shop"},
        "items": ["sword"],
        'gold':0,
        "entities": ["knight"]
        },
    "forest clearing": {
        "description": "a thick forest. theres a sound coming from the ",
        "directions": {"north":"magic tower", "south":"forest wall", "east":"west castle entrance", "west":"wall"},
        "items": [],
        'gold':0,
        "entities": ["troll", "goblin"]
        },
    "shop": {
        "description": "sells a variety of items. There is a shopkeeper standing before you, it would not be wise to attack him.",
        "directions": {"north":"wall", "south":"castle courtyard", "east":"wall", "west":"wall", "in":"secret room"},
        "items": [],
        'gold':0,
        #ex: ("common sword", 5)
        "objects": ["common sword","speed potion","death potion (safe)","strength potion","leather armor","money potion","resilience potion"],
        "requirements": "True if (getct(starttime)[:3] in ['08','09','10','11'] and 'A.M.' in getct(starttime)) or (getct(starttime)[:3] in ['12','01','02','03','04','05']) else False",
        "entities": ["shopkeeper"]
        },
    "night shop": {
        "description": "An empty shop, items line the walls.",
        "directions": {"north":"wall", "south":"castle courtyard", "east":"wall", "west":"wall", "in":"secret room"},
        "items": ["common sword","speed potion","death potion","strength potion","leather armor","money potion","resilience potion"],
        'gold':0,
        "objects": [""],
        "entities": [],
        },
    "secret room": {
        "description": "A,secret room within the town shop, items are scattered on the floor. only take one or the owner might notice",
        "directions": {"north":"wall", "south":"shop", "east":"wall", "west":"wall", "out":"shop"},
        "items": [],
        "gold": 3,
        "requirements":"True if 'shop key' in player['backpack'] ",
        "objects": [""],
        "entities": []
        },
    "den of the giant lizard": {
        "description": "as you walk in to a cave you see a gargantuan shadowy figure on a mound of skulls.",
        "directions": {"north":"wall", "south":"wall", "east":"boss room", "west":"east castle entrance"},
        "items": ["polished sword"],
        "objects": [],
        'gold':0,
        "entities": ["giant lizard"]
        },
    "north of the mansion": {
        "description": "You see a large mansion to the south. There are two knights on either side of the door.",
        "directions": {"north":"castle courtyard", "east":"east of the mansion", "south":"mansion interior", "west":"west of the mansion", "in":"mansion interior"},
        "items": [],
        'gold':0,
        "entities": ["knight","knight"]
        },
    "west of the mansion": {
        "description": "The mansion is now to your east. There is nothing interesting on the side of the mansion; however, you see a small storage shed to the west.",
        "directions": {"north":"north of the mansion", "east":"wall", "south":"south of the mansion", "west":"storage shed"},
        "items": [],
        'gold':0,
        "entities": []
        },
    "storage shed": {
        "description": "A small, surprisingly empty storage shed. You see a small porcelain figure on a shelf, once broken, but it seems to have been fixed. There might be a coin under the shelves",
        "directions": {"north":"west castle entrance", "east":"storage shed", "south":"wall", "west":"west of the mansion"},
        "items": ["figure"],
        "objects": [],
        'gold':0,
        "entities": []
        },
    "south of the mansion": {
        "description": "The mansion is now to your north. You see the white paint chipping, revealing rotted wood, this mansion is quite old.",
        "directions": {"north":"wall", "east":"east of the mansion", "south":"wall", "west":"west of the mansion"},
        "items": [],
        "gold": 0,
        "entities": []
        },
    "east of the mansion": {
        "description": "The mansion is now to your west. This side of the mansion is surprisingly pristine, offering a nice change of scenery. You see a bed of flowers, some of the flowers are thriving, and others are wilting.",
        "directions": {"north":"north of the mansion", "east":"wall", "south":"south of the mansion", "west":"wall"},
        "items": [],
        "gold": 0,
        "entities": ["gnome"]
        },
    "magic tower": {
        "description": "A large magic tower stands to your north. Inside you see a wizard keeping to his studies.\nA large, mossy stone golem stands before you. As you stand before the tower, the golem begins to wake.",
        "directions": {"north":"magic tower interior", "east":"forest wall", "south":"forest clearing", "west":"wall", "in":"magic tower interior"},
        "items": [],
        "gold": 0,
        "entities": ["magic golem"]
        },
    "magic tower interior": {
        "description": "You are now inside the the magic tower. The wizard is now facing you.",
        "directions": {"north":"wall", "east":"wall", "south":"magic tower", "west":"wall"},
        "items": ["ancient staff",],
        "gold": 3,
        "entities": ["wizard"]
        },
    "well": {
        "description": "You are inside the well. It is cold, dark, and very wet. There are some coins at the bottom.",
        "directions": {"north":"wall", "east":"wall", "south":"magic tower", "west":"wall"},
        "items": [],
        "gold": 5,
        "entities": []
        },
    "boss room": {
        "description": "a damp cave light by torches on the walls. theres a hideos monster with 3 scaly heads.",
        "directions": {"north":"wall", "east":"wall", "south":"wall", "west":"den of the giant lizard", "out":"den of the giant lizard"},
        "gold": 15,
        "entities": ["hydra",]
        },
    "mansion interior": {
        "description": "ornate interior of the city mansion. the lord is sitting his desk doing paperwork. ",
        "directions": {"north":"north of the mansion ", "south":"wall", "east":"wall", "west":"wall"},
        "items": ["sturdy armor",],
        "gold": 15,
        "requirements": "player['diddungeon']",
        "entities": ["lord"]
        },
    "dev": {
        "description": " ",
        "directions": {"north":"castle courtyard", "south":"castle courtyard", "east":"castle courtyard", "west":"castle courtyard"},
        "items": ["sturdy armor","polished sword"],
        "gold": 10000,
        "entities": ["goblin"]
        },
    "dungeon entrance": {
      "description": "You are in a large, moist corridor. The bricks to your sides are covered in moss. You see a large door in front of you.",
        "directions": {"north":"west castle entrance", "south":"dungeon", "east":"wall", "west":"wall", "in":"dungeon"},
        "items": [],
        "gold": 7,
        "entities": []
    }
    }

    ###############################
    #		  Functions 		  #
    ###############################
    def zork():
        plaintext=random.choice(words)
        word=None
        for i in plaintext:
            if word is None:
                word=cptl(cpt[i])
            else:
                letterrect=cptl(cpt[i])
                for j in range(7):
                    word[j]+=letterrect[j] 


        ###############################
        #		  variables 		  #
        ###############################


        
        crimes_commited = 0
        past_locations = ['castle courtyard', ]
        location = "castle courtyard"
        printloc = True
        alive = True

        ###############################
        #		  Game loop			  # 
        ###############################

        print("\n")

        h = True
        if deathtext!='none':
            print('''
                ###################################################### 
                ##                    YOU DIED                      ##
                ###################################################### 
            ''')
            print(deathtext)
            print('\n----------------------------------------------------------------------\n')
        cmds()
        print()
        input("press enter to start  ")
        while player["health"]>0:
            if location=='dungeon':
                outcome=dungeonsys(player)
                if outcome==False:
                    run("You lost a fight in the dungeon. Return once you're more prepared")
                else:
                    player['money']+=outcome[0]
                    if 'dungeon keys' in player.keys():
                        player['dungeon keys']+=outcome[1]
                    else:
                        player['dungeon keys']=outcome[1]
            tct=getct(starttime)
            tl='noneaction'
            condition=False
            act=input("\n\n>>>> ")
            # print("\033c", end= "")
            print('\n----------------------------------------------------------------------\n')
            print(f"it is {getct(starttime)[0]} {getct(starttime)[-1]}\n")
            if 'help' in act:
                cmds()
            elif ('inv' in act or 'inventory' in act or 'backpack' in act):
                backpack(player)
            elif 'stats' in act:
                getstats(player)
            elif 'view' in act:
                view(map, location)
            elif 'look' in act:
                if location == 'shop':
                    print('		'.join(map[location]["objects"]))
                elif location == 'night shop':
                    print('		'.join(map[location]["items"]))
                else:
                    print('only usable in the shop!')
            elif 'buy ' in act:
                if location=='shop':
                    act=act.split(' ')
                    if (item:=' '.join(act[act.index('buy')+1:])) in items['shop']:
                        if player['money']>=items['shop'][item]['cost']:
                            if '' in player['backpack']:
                                player['money']-=items['shop'][item]['cost']
                                player['backpack'][player['backpack'].index('')]=item
                                print(f'You have successfully purchased the {item}. Have a nice day!')
                                if 'money' not in item:
                                    l=True
                                    lind=0
                                    while l:
                                        if map['shop']['objects'][lind][:4]==item[:4]:
                                            del items['shop'][item]
                                            del map['shop']['objects'][lind]
                                            l=False
                                        lind+=1
                            else:
                                print('Your backpack is too full!')
                        else:
                            if random.randint(1,100)!=74:
                                print('You dont have enough money to purchase that item.')
                            else:
                                print('You dont have enough money to purchase that item.')
                                print('brokie')
                    else:
                        print("That item isn't for sale.")
                else:
                    print('You can only use this at the shop')
            elif 'equip' in act:
                act=act.split(' ')
                item=' '.join(act[act.index('equip')+1:])
                if item in items['weapons']:
                    player['weapon']['name']=item
                    player['weapon']['damage']=items['weapons'][item]['damage']+player['strength']
                    player['backpack'].remove(item)
                    player['backpack'].append('')
                    print(f'You have successfully equipped the {item}')
                if item in items['armor']:
                    player['armor']['name']=item
                    player['armor']['def']=items['armor'][item]['defense']
                    player['health']=10+player['armor']['def']+player['resilience']
                    player['maxhealth']=10+player['armor']['def']
                    player['backpack'].remove(item)
                    player['backpack'].append('')
                    print(f'You have successfully equipped the {item}')
            elif 'drink' in act:
                act=act.split(' ')
                item=' '.join(act[act.index('drink')+1:])
                if item in player['backpack']:
                    if item=='money potion':
                        icby=random.randint(0,10)
                        player['money']+=icby
                        print(f"You gained {icby} gold!")
                    elif item=='death potion':
                        run('You died! maybe dont drink a death potion next time.')
                    else:
                        player[items["consumables"][item]['stat']]+=items['consumables'][item]['amount']
                        if 'strength' in item:
                            player['weapon']['damage']+=items['consumables'][item]['amount']
                        if 'resilience' in item:
                            player['armor']['def']+=items['consumables'][item]['amount']
                            player['health']+=items['consumables'][item]['amount']
            elif 'talk' in act:
                if location=='shop':
                    if player["stage"]==0:
                        print("You: Hello!")
                        print("Shopkeeper: If you wish to take my key, first you must solve my riddles three.")
                        print("The shopkeeper hands you a note. It appears to be some poorly drawn mountains:")
                        oprintgrid(word)
                        print('What does it mean? You may leave and then return if mandatory.')
                        guess=input('You: ')
                        if plaintext in guess:
                            player['stage']+=1
                        player['stage']+=1
                    if player['stage']==1:
                        oprintgrid(word)
                        print("Shopkeeper: You have returned! Have you come to an answer?")
                        guess=input('You: ')
                        if plaintext in guess.lower():
                            player['stage']+=1
                        elif guess.lower() in ['n','no','not yet']:
                            print('Shopkeeper: Return when you have.')
                        elif guess.lower() in ['y','yes','i have']:
                            print('Shopkeeper: Then what is it?')
                            guess=input('You: ')
                            if plaintext in guess.lower():
                                player['stage']+=1
                        else:
                            print("Shopkeeper: Wrong!")
                    if player['stage']==2:
                        print('Shopkeeper: Correct!')
                        plaintext=random.choice(words)
                        word=None
                        for i in plaintext:
                            if word is None:
                                word=cptl(cpt[i])
                            else:
                                letterrect=cptl(cpt[i])
                                for j in range(7):
                                    word[j]+=letterrect[j]
                        print('Shopkeeper: Time for the next puzzle!')
                        oprintgrid(word)
                        print('How about this one?')
                        guess=input('You: ')
                        if plaintext in guess:
                            player['stage']+=1
                        else:
                            print("Shopkeeper: Wrong!")
                        player['stage']+=1
                    if player['stage']==3:
                        oprintgrid(word)
                        print("Shopkeeper: Have you come to an answer?")
                        guess=input('You: ')
                        if plaintext in guess.lower():
                            player['stage']+=1
                        elif guess.lower() in ['n','no','not yet']:
                            print('Shopkeeper: Return when you have.')
                        elif guess.lower() in ['y','yes','i have']:
                            print('Shopkeeper: Then what is it?')
                            guess=input('You: ')
                            if plaintext in guess.lower():
                                player['stage']+=1
                        else:
                            print("Shopkeeper: Wrong!")
                    if player['stage']==4:   
                        print('Shopkeeper: Correct!')
                        plaintext=random.choice(words)
                        word=None
                        for i in plaintext:
                            if word is None:
                                word=cptl(cpt[i])
                            else:
                                letterrect=cptl(cpt[i])
                                for j in range(7):
                                    word[j]+=letterrect[j]
                        print('Shopkeeper: Time for the next puzzle!')
                        oprintgrid(word)
                        print('How about this one?')
                        guess=input('You: ')
                        if plaintext in guess:
                            print('Shopkeeper: Correct!')
                            print("Shopkeeper: Take my key.")
                            player['keys'].append('shop')
                        else:
                            print("Shopkeeper: Wrong! Try again!")
                    if player['stage']==5:
                        oprintgrid(word)
                        print("Shopkeeper: Have you come to an answer?")
                        guess=input('You: ')
                        if plaintext in guess.lower():
                            print('Shopkeeper: Correct!')
                            print("Shopkeeper: Take my key.")
                            player['keys'].append('shop')
                        elif guess.lower() in ['n','no','not yet']:
                            print('Shopkeeper: Return when you have.')
                        elif guess.lower() in ['y','yes','i have']:
                            print('Shopkeeper: Then what is it?')
                            guess=input('You: ')
                            if plaintext in guess.lower():
                                print('Shopkeeper: Correct!')
                                print("Shopkeeper: Take my key.")
                                player['keys'].append('shop')
                        else:
                            print("Shopkeeper: Wrong!")
            elif ('grab' in act or 'take' in act or 'pick up' in act):
                if 'grab' in act:
                    w='grab'
                if 'take' in act:
                    w='take'
                if 'pick up' in act:
                    w='up'
                tindex = act.index(w)+len(w)
                if act[tindex+1:] in map[location]["items"]:
                    player["backpack"][player["backpack"].index('')]=map[location]["items"].pop(map[location]["items"].index(act[tindex+1:]))
                    print(f'{act[tindex+1:]} picked up.')
                else:
                    print(act[tindex+1:], end=' ')
                    print('is not here!')
            elif 'drop' in act:
                act=act.split(' ')
                item=act[act.index('drop')+1:][0]
                if item in player['backpack']:
                    if item!='figure':
                        map[location]['items'].append(item)
                        player['backpack'].remove(item)
                        player['backpack'].append('')
                    else:
                        player['backpack'].remove(item)
                        print('You drop the figure, and it shatters immediately upon hitting the ground, revealing a very old key.')
                        print('You pick up the key.')
                        player['keys'].append('dungeon')
                else:
                    print('you dont have that item')
            elif 'fight' in act or 'attack' in act:
                enemy=act.split('fight ')[-1]
                f=fight(map,location,player,enemy,enemies)
                if type(f)==tuple:
                    print(f[1])
                    zork()
            elif 'collect' in act:
                player['money']=player['money']+map[location]['gold']
                print(f"You collected {map[location]['gold']} gold.")
            elif 'time' in act:
                print(f'{tct[0]}:{tct[1]} {tct[2]}\n')
            elif ('north' or "up") in act or act in ['n','go n','u','go u']:
                tl='north'
            elif ('east' in act or 'right' in act) or act in ['e','go e','r','go r']:
                tl='east'
            elif ('south' in act or 'down' in act) or act in ['s','go s','d','go d']:
                tl='south'
            elif ('west'  in act or 'left'  in act):  
                tl='west'
            elif ('in' in act or 'enter' in act):
                if location in ['shop' , 'night shop' , 'north of the mansion' , 'magic tower' , 'dungeon entrance']:
                    tl='in'
                else:
                    print("you cant go in here!")
            if tl!='noneaction':
                if location=='castle courtyard' and tl=='north':
                    if tct[0] in ['8','9','10','11'] and tct[-1]=='A.M.' or tct[0] in ['12','01','02','03','04','05'] and tct[-1]=='P.M.':
                        location='shop'
                        print(f'You are now at the {location}!\n')
                        view(map,location)
                    elif 'shop' in player['keys']:
                        location='night shop'
                        print(f'You are now at the {location}!\n')
                        view(map,location)
                elif "wall" not in map[location]['directions'][tl]:
                    location = map[location]['directions'][tl]
                    past_locations+=[location]
                    print(f'You are now at the {location}!\n')
                    view(map,location)
                    if location == 'den of the giant lizard':
                        print('You look around, getting more anxious the longer the silence of the tense, moist air of the cave is unbroken. Suddenly, you see the large figure stand up and face you.')
                        f=fight(map,location,player,'giant lizard',enemies)
                        if type(f)==tuple:
                            print(f[1])
                    if location == 'boss room':
                        print('This is it. This is what you came here to do. The hydra turns to face you. You realize you can no longer turn back.')
                        f=fight(map,location,player,'hydra',enemies)
                        if type(f)==tuple:
                            print(f[1])
                else:
                    print("There is a wall blocking your path.")
            elif 'hhhhhhb' in act:
                location = 'dev'
            h = False
        run('none')
    zork()
run('none')
