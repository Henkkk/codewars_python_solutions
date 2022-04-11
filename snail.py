def layer_length(array):
    dimension = len(array)
    li = []
    if dimension % 2 != 0:
        n_i = int(dimension/2)
        v = (dimension ** 2) - 1
        for i in range(n_i):
            v -= 8 * i
            li.append(v)
    else:
        n_i = int((dimension-2)/2)
        a,b = dimension, dimension - 2
        v = 0
        for i in range(n_i):
            v += (a - 2 * i) * 2 + (b - 2 * i) * 2
            li.append(v)
    return li



def snail(snail_map):
    
    m = len(snail_map)
    min, max = 0, len(snail_map)-1
    flat = []
    x,y = 0,0
    p_check = []
    
    if len(snail_map) == 1:
        return snail_map[0]
    else:
        while len(flat) != m**2:
            p = (x,y)
            if p in p_check and x == min and y != max:
                y += 1
                p_check.append((x,y))
                flat.append(snail_map[x][y])
            elif p in p_check and x!= max and y == max:
                x += 1
                p_check.append((x,y))
                flat.append(snail_map[x][y])
            elif p in p_check and x == max and y <= max and y != min:
                y -= 1
                p_check.append((x,y))
                flat.append(snail_map[x][y])
            elif p in p_check and x <= max and y == min:
                x -= 1
                p_check.append((x,y))
                flat.append(snail_map[x][y])
            else:
                p_check.append((x,y))
                flat.append(snail_map[x][y])

            if len(flat) in layer_length(snail_map):
                min += 1
                max -= 1 
            
    return flat

