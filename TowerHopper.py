tower = [1,2,0,1,2,2,0]


def func(index, tower):
    steps = tower[index]
    while steps > 0:
        next_position = index+steps 
        if next_position >= len(tower):
            return True
        if func(index+steps, tower):
            return True
        steps = steps-1
    return False
    
print(func(0,tower)) 
