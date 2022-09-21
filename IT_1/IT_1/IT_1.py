#На вход программы подается последовательность имволов заканчивающаяся нулем.Ноль в этой апоследовательность единственный среди символов оюязательно есть другие десятичные цифры.
#Требуется написать програссу каторая составряет з этиз цмфр чмсло палиндром максимальной длины.(если таких чисел несколько выбрать наименьшее)

list_digit = []
i = int(input())
while i != 0:
    list_digit.append(i)
    i = int(input())
print(list_digit)

count_list = []

i = 0

while i < len(list_digit):
    count = 0
    j = 0
    while j <len(list_digit):
        if list_digit[i] == list_digit[j]:
            count += 1
        j += 1
    count_list.append([list_digit[i], count])

    dead_note = list_digit[i]
    k = 0
    
    while k < len(list_digit):
        if dead_note == list_digit[k]:
            list_digit.remove(list_digit[k])
        else:
            k += 1
    i += 1


i = 0
answer = ""
while i < len(count_list):
    if count_list[i][1] < 2:
        count_list.remove(count_list[i])
    i += 1

count_list = sorted(count_list, key = lambda i : i[0])

count_list = list(map(lambda x : [x[0], x[1] // 2], count_list))

i = 0
sum = sum(n for _, n in count_list)

while sum > 0:
    if(count_list[i][1] > 0):
        answer += str(count_list[i][0])
        count_list[i][1] -= 1
        sum -= 1
    else:
        i += 1

answer += answer[::-1]

print(answer)
    




