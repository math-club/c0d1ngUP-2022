#init
pops = {
    "chauves_souris": 0,
    "skellingtons": 0,
    "zombies": 0,
    "fantomes": 0
}

spawn_time = {
    "chauves_souris": [2, 2],
    "skellingtons": [5, 5],
    "zombies": [6, 6],
    "fantomes": [10, 10]
}

spawn = {
    "chauves_souris": 10,
    "skellingtons": 5,
    "zombies": 4,
    "fantomes": 3
}

kill_time = {
    "chauves_souris": [6, 6],
    "skellingtons": [20, 20],
    "zombies": [30, 30],
    "fantomes": [40, 40]
}

kill = {
    "chauves_souris": 2,
    "skellingtons": 1,
    "zombies": 1,
    "fantomes": 1
}

UPGRADE = 240
upgrade = 1
ticker = 1

while ticker < 50*60:
    for mob in pops.keys():
        spawn_time[mob][1] -= 1
        if spawn_time[mob][1] == 0:
            spawn_time[mob][1] = spawn_time[mob][0]
            pops[mob] += spawn[mob]

        kill_time[mob][1] -= 1
        if kill_time[mob][1] == 0:
            kill_time[mob][1] = kill_time[mob][0]
            pops[mob] -= kill[mob]

    if upgrade == UPGRADE:
        upgrade = 1
        for mob in pops.keys():
            if mob == "chauve_souris":
                kill[mob] += 2
            else:
                kill[mob] += 1
    upgrade += 1
    ticker += 1

    print(pops.values())
    print(upgrade)
    print(ticker)


print(pops.values())