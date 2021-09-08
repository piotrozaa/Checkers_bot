def possible_moves(state,d):
    i=1
    a = []
    while i<=10:
        j=1
        while j<=10:
            if state[i][j]==1:
                if state[i+1][j+1]==0:
                    a.append((i,j,i+1,j+1))
                if state[i+1][j-1]==0:
                    a.append((i,j,i+1,j-1))

            j = j+1
                

        i = i+1
    
    return a

def heuristic_value(state):
    b = 1
    return b

def next_state(state, move):
    c = 1
    return c

state = [[1,0,1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0,1,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,2,0,2,0,2,0,2,0,2],
         [2,0,2,0,2,0,2,0,2,0],
         [0,2,0,2,0,2,0,2,0,2]
         ]
depth = input()
d=0

def min_max(state,d):

    value=0
    if d==depth:
        return heuristic_value(state)
    
    for x in possible_moves(state,d):
        value=max(value, 1-min_max(next_state(state,x),d+1))

    return value

        

    



