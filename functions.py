minumim = 0
maximum = 0
fake_sum = 0
another_sum = 1


def Mimim(list):
    for i in range(0, len(list)):
        if i == 0:
            minumim = list[0]
        else:
            if list[i] < minumim:
                minumim = list[i]
    return minumim


def Maxim(list):
    for i in range(0, len(list)):
        if i == 0:
            maximum = list[0]
        else:
            if list[i] > maximum:
                maximum = list[i]
    return maximum


def Sum(list, fake_sum=0):
    for i in list:
        fake_sum += int(i)
    return fake_sum


def NotSum(list, another_sum=1):
    for i in list:
        another_sum *= int(i)
    return another_sum


def realNotSum(list, NotSum=1):
    for i in range(0, len(list)):
        NotSum *= i
    return NotSum


aboba = []


def importfile():
    with open('input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            s1 = line.strip()
            s = s1.split()
            for i in s:
                aboba.append(int(i))
    return aboba


importfile()
