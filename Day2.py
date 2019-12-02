

def do_work(position):
    global data
    first = data[data[(position + 1)]]
    second = data[data[(position + 2)]]
    if data[position] == 1:
        result = first + second
        #print("Iteration {}: {} + {} = {}. Stored at location {}".format(count,first, second, result, data[(position + 3)]))
    elif data[position] == 2:
        result = first * second
        #print("Iteration {}: {} * {} = {}. Stored at location {}".format(count,first, second, result, data[(position + 3)]))
    else: 
        print("Something went wrong. {}".format(data[position]))
    data[data[(position + 3)]] = result

with open('Day2-Input.txt', 'r') as input:
    data = [int(x) for x in input.read().split(',')]
    incomplete = True
    locale = 0
    count = 1
    while incomplete == True:
        if data[locale] == 99:
            print(data[0])
            #print(data)
            incomplete = False
        else:
            do_work(locale)
            locale += 4
            count += 1