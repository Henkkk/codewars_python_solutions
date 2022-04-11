import numpy as np

def rotate_90_degree_anticlckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], matrix)))
    return new_matrix


def who_is_winner(pieces_position_list):
    f_m = [[],[],[],[],[],[],[]]

    for step in pieces_position_list: #add the steps into the matrix
        if step.split('_')[0] == 'A': f_m[0].append(step.split('_')[1])
        elif step.split('_')[0] == 'B': f_m[1].append(step.split('_')[1])
        elif step.split('_')[0] == 'C': f_m[2].append(step.split('_')[1])
        elif step.split('_')[0] == 'D': f_m[3].append(step.split('_')[1])
        elif step.split('_')[0] == 'E': f_m[4].append(step.split('_')[1])
        elif step.split('_')[0] == 'F': f_m[5].append(step.split('_')[1])
        elif step.split('_')[0] == 'G': f_m[6].append(step.split('_')[1])

        total_length = sum(len(row) for row in f_m)

        while total_length < 42:
            for v in range(7):
                if len(f_m[v]) < 6:
                    f_m[v].append('0')

            total_length = sum(len(row) for row in f_m)

        r_m = rotate_90_degree_anticlckwise(f_m)
        

        #vertical check
        switch = False
        result = 'Draw'
        if switch == False:
            for i in range(7):
                yell_counts = 0
                red_counts = 0
                for v in range(6):
                    if r_m[v][i] == 'Red': red_counts += 1
                    else: red_counts = 0

                    if red_counts == 4:break

                    if r_m[v][i] == 'Yellow': yell_counts += 1
                    else: yell_counts = 0

                    if yell_counts == 4:break
                
                if red_counts == 4 or yell_counts == 4: 
                    switch = True
                    
                if switch == True: 
                    if red_counts == 4: result = 'Red'
                    else: result = 'Yellow'
                    break

        if switch == True: break
        
        
        #horizontal check
        if result == 'Draw':
            switch = False
            if switch == False:
                for i in range(6):
                    yell_counts = 0
                    red_counts = 0
                    for v in range(7):
                        if r_m[i][v] == 'Red': red_counts += 1
                        else: red_counts = 0

                        if red_counts == 4: break

                        if r_m[i][v] == 'Yellow': yell_counts += 1
                        else: yell_counts = 0

                        if yell_counts == 4: break

                    if red_counts == 4 or yell_counts == 4: 
                        switch = True

                    if switch == True: 
                        if red_counts == 4: result =  'Red'
                        else: result =  'Yellow'
                        break

            if switch == True: break

        
        #diagonal check
        if result == 'Draw':
            switch = False
            a = np.array(r_m)
            diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
            diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
            diagonal = [n.tolist() for n in diags if len(n.tolist()) >= 4]

            for li in diagonal:
                yell_counts = 0
                red_counts = 0
                for item in li:
                    if item == 'Red': red_counts += 1
                    else: red_counts = 0

                    if red_counts == 4:
                        break

                    if item == 'Yellow': yell_counts += 1
                    else: yell_counts = 0

                    if yell_counts == 4:
                        break

                if red_counts == 4 or yell_counts == 4: switch = True
                if switch == True:
                    if red_counts == 4: result = 'Red'
                    else: result = "Yellow"
                    break

            if switch == True: break
        
        for items in f_m:
            try:
                while True:
                    items.remove('0')
            except ValueError:
                pass

    return result