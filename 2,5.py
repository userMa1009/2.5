def get_matrix(n,m,value):
    a=[]
    for i in range(n):
        s=[]
        for j in range(m):
            s.append(value)
        a.append(s)
    return a
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)