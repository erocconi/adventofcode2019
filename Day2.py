
def do_work(position):
    global data
    first = data[data[(position + 1)]]
    second = data[data[(position + 2)]]
    if data[position] == 1:
        result = first + second
    elif data[position] == 2:
        result = first * second
    else: 
        print("Something went wrong. {}".format(position))
    data[data[(position + 3)]] = result

with open('Day2-Input.txt', 'r') as input:
    data = [int(x) for x in input.read().split(',')]
    incomplete = True
    inst = 0
    while incomplete == True:
        if data[inst] == 99:
            print("Tyranny of the Rocket Equation: {}".format(data[0]))
            incomplete = False
        else:
            do_work(inst)
            inst += 4