s = '25525511135'
s_arr = list(s)
valid_ips = []
it1 = 1
it2 = 3
it3 = 5
s_arr.insert(it1, '.')
s_arr.insert(it2, '.')
s_arr.insert(it3, '.')

# посмотреть логику внимательно)))
def valid(arr):
    iterator = 0
    s = ''
    while iterator < len(arr):
        if arr[iterator] != '.':
            s += arr[iterator]
            iterator += 1
            if iterator == len(arr):
                if len(s) > 0 and s[0] == 0:
                    return False
                n = int(s)
                if n < 0:
                    return False
                if n > 255:
                    return False

        elif arr[iterator] == '.':
            if len(s) > 0 and s[0] == 0:
                return False
            n = int(s)
            if n < 0:
                return False
            if n > 255:
                return False
            iterator += 1
            s = ''
    return arr


while it1 < len(s_arr)-6:
    while it2 < len(s_arr)-4:
        while it3 < len(s_arr)-2:
                    valid_ips.append(valid(s_arr))
                    s_arr[it3], s_arr[it3+1] = s_arr[it3+1], s_arr[it3]
                    it3 += 1
        s_arr[it2], s_arr[it2+1] = s_arr[it2+1], s_arr[it2]
        it2 += 1
        s_arr.pop(len(s_arr)-2)
        s_arr.insert(it2 + 2, '.')
        it3 = it2 + 2
    s_arr[it1], s_arr[it1+1] = s_arr[it1+1], s_arr[it1]
    it1 += 1
    s_arr.pop(len(s_arr)-4)
    s_arr.insert(it1 + 1, '.')
    it2 = it1 + 1


print(valid_ips)
