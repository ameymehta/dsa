#```
# given a string S and character X within string, output the distance to nearest X for each character in S.
#e.g.
#```
# S = "abxacefa"
# X = "a"
# Output = [0, 1, 1, 0, 1, 2, 1, 0]

# S = "abcdef"
# X = "a"
# Output = [0,1,2,3,4,5]

# S = "bcdef"
# X = "a"
# output = [-1,-1...]
#```

def find_distance(s, x):
    # abxacefa
    indexes_of_x = []
    for i in range(len(s)):
        if(s[i] == x):
            indexes_of_x.append(i)
    #[0, 3, 7]
    output = []
    if len(index_of_x) > 0:
        in_x = 0 
    else:
        return [-1 for i in range(len(s))]
    
    # when ind = 3
    # output = [0,1,1,0, ]
    for ind in range(len(s)):
        if ind in indexes_of_x:
            output.append(0)
            if():
                in_x += 1
            break
        if(index_of_x[in_x+1]):
            output.append(min(ind-indexes_of_x[in_x], index_of_x[in_x + 1]-ind))
        else:
            output.append(ind-indexes_of_x[in_x])