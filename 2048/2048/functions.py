ms = 4
def check(matr):
    larg = 2
    cond = 0
    for r in range(ms):
        for c in range(ms):
            if matr[r][c] == 0: cond +=1
            elif matr[r][c] == 2048: return "OVER", 2048

            if matr[r][c] > larg: larg = matr[r][c]
    if cond > 0:    return "True", 0
    else:   return "False", larg

def merge(row):
    #moving
    for i in range(ms-1):
        for j in range(ms-1, 0, -1):
            if row[j-1] == 0:
                row[j-1] = row[j]
                row[j] = 0

    #merging
    for i in range(ms-1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0

    #moving back
    for i in range(ms-1):
        for j in range(ms-1, 0, -1):
            if row[j-1] == 0:
                row[j-1] = row[j]
                row[j] = 0

    return row

def reverse(row):
    row = row[::-1]
    return row

def transpose(matr):
    for r in range(ms):
        for c in range(r, ms):
            if not r==c:
                temp = matr[r][c]
                matr[r][c] = matr[c][r]
                matr[c][r] = temp
                 
