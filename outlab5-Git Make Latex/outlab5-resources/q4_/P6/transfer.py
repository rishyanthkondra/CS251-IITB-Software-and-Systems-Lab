import random
import json


def makeDatabase():

    data = {}
    jerseys = random.sample(range(1, 1001), 100)
    it = 0

    for ch in range(65, 75):
        curr = chr(ch)
        data[curr] = {}

        for _ in range(10):
            data[curr][jerseys[it]] = random.randint(0, 10)
            it += 1
    try:
        with open('players.json', 'x') as f:
            json.dump(data, f, indent=4)
    except FileExistsError:
        pass


def make_transfers():
    with open('players.json', 'r') as f:
        data = json.load(f)

    with open('transfer.txt', 'r') as f:
        line = f.readline()
        count = 0
        while line:
            curr = line.split()

            try:
                if curr[0] not in data:
                    raise ValueError("Wrong team name")

                minEl = min(data[curr[0]].items(), key=lambda x: x[1])

                if minEl[1] > 7:
                    raise ValueError('No player in team ' + minEl[0] + ' with loyalty <=7')

                flag = 0

                for i in data:
                    if i != curr[0]:
                        if curr[1] in data[i]:
                            if data[i][curr[1]] <= 7:
                                data[curr[0]][curr[1]] = data[i][curr[1]]
                                data[i][minEl[0]] = minEl[1]
                                flag = 1
                                del data[i][curr[1]]
                                del data[curr[0]][minEl[0]]
                                count += 1
                                break
                            else:
                                raise ValueError("Player has loyalty >7")

                if flag != 1:
                    raise ValueError("Wrong player name")

                else:
                    print("Transfer Complete")

            except ValueError as err:
                print("Try another transfer", '(', err, ')', sep='')

            line = f.readline()

    with open('players.json', 'w+') as f:
        json.dump(data, f, indent=4)

    return count


def main():
    makeDatabase()
    print(str(make_transfers()))


if __name__ == '__main__':
    main()

