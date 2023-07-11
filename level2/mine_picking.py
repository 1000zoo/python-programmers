def solution(picks, minerals):
    answer = 0
    tired = {
        'diamond': {
            'diamond': 1,
            'iron': 1,
            'stone': 1,
        },
        'iron': {
            'diamond': 5,
            'iron': 1,
            'stone': 1,
        },
        'stone': {
            'diamond': 25,
            'iron': 5,
            'stone': 1,
        }
    }

    pick = {
        'diamond': picks[0], 'iron': picks[1], 'stone': picks[2]
    }
    total = sum(picks)
    devided = divide(minerals, total)
    sort_index = list(range(len(devided)))
    sort_index.sort(key=lambda x: (count(devided[x])[0], count(devided[x])[1], count(devided[x])[2]))
    print(sort_index)

    return answer


def count(arr):
    d = i = s = 0
    for a in arr:
        if a == 'diamond':
            d += 1
        elif a == 'iron':
            i += 1
        else:
            s += 1

    return d, i, s


def divide(sarr, total):
    temp = []
    for i in range(total):
        if 5 * (i + 1) <= len(sarr):
            temp.append(list(sarr[5 * i:5 * (i + 1)]))
        else:
            temp.append(list(sarr[5 * i:]))
            break

    return temp



if __name__ == '__main__':
    a = [[1,2], [2,3], [1,5]]
    a.sort(key=lambad())