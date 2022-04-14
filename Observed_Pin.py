import itertools

def get_adjacent_indices(i, j):
    adjacent_indices = []
    
    if i > 0 or i == 3:
        adjacent_indices.append((i-1,j))
    if i < 2 or i == 2 and j == 1:
        adjacent_indices.append((i+1,j))
    if j > 0 and i != 3:
        adjacent_indices.append((i,j-1))
    if j+1 < 3 and i != 3:
        adjacent_indices.append((i,j+1))
        
    return adjacent_indices

def get_pins(observed):
    
    keypad = [[1,2,3],[4,5,6],[7,8,9],['$',0,'$']]
    li_pins = list(map(lambda x:int(x), list(observed)))
    hold = []

    for li in range(len(li_pins)):
            index = [(index, row.index(li_pins[li])) for index, row in enumerate(keypad) if li_pins[li] in row]
            i = index[0][0]
            j = index[0][1]

            hold.append(get_adjacent_indices(i,j))
            
    li_2 = []
    for indexing in range(len(hold)):
        for tup in hold[indexing]:
            x = tup[0]
            y = tup[1]

            li_2.append(keypad[x][y])
            li_2.append(li_pins[indexing])

        hold[indexing] = list(set(li_2))
        li_2 = []

    hold = ([list(map(str,i) ) for i in hold])
    
    pin_set = list(itertools.product(*hold))
    
    return [''.join(sets) for sets in pin_set]
