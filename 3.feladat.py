def csatolas(fej,elem):
    result=[]
    if len(elem)==0:
        return fej
    for t in elem:
        result.append([fej]+t)
    return result
# print(csatolas(1,[[2,3],[4,5]]))
# print(csatolas(1,[]))

def randomvalues(values):
    if len(values)==0:
        return [[]]
    else:
        res = randomvalues(values[1:])
        return csatolas(values[0], res) + csatolas(-values[0], res)
# print(randomvalues(range(1,4)))
# print(randomvalues([1]))

def get_ones_zeros(size):
    if size==0:
        return [[]]
    else:
        res = get_ones_zeros(size - 1)
        return csatolas(0, res) + csatolas(1, res)
# print(get_ones_zeros(1))
# print(get_ones_zeros(3))

def nothing(values,nothing):
    index_i = 0
    index_j = 0
    size = len(values)
    result = []
    value_stack = values[0]
    while index_i < size:
        if index_i + 1 >= size:
            result.append(value_stack)
            break
        new_value = values[index_i + 1]
        if nothing[index_j] == 0:
            result.append(value_stack)
            value_stack = new_value
        else:
            value_stack = value_stack * 10 + new_value
        index_i += 1
        index_j += 1
    return result
# print(nothing([1,2,3,4,5,6,7,8,9],[1,0,0,0,0,0,0,0,0]))

def get_numbers(stop=9):
    values = range(1, stop + 1)
    one_zeros = get_ones_zeros(stop)
    result = []
    for one_zero in one_zeros:
        res = nothing(values, one_zero)
        result.append(tuple(res))
    return set(result)
# print(get_numbers(3))
# print(get_numbers(9))

def solution(stop=9,goal=100):
    numbers = get_numbers(stop)
    for number in numbers:
        variations = map(lambda y: [number[0]] + y, randomvalues(number[1:]))
        for v in variations:
            SumValue= sum(v)
            if goal == SumValue:
                print(v)
solution()