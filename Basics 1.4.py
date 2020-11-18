n = int(input())
getting = {'global': []}
qty = {'global': None}
name = []

for _ in range(n):
    com, ns, var = input().split()
    if com.lower() == 'create':
        qty[ns] = var
        getting[ns] = []
    elif com.lower() == 'add':
        getting[ns].append(var)
    elif com.lower() == 'get':
        namespace = ''
        numb = ns
        while namespace == '':
            if var in getting[numb]:
                namespace = numb
            else:
                if qty[numb] == None:
                    namespace = 'None'
                else:
                    numb = qty[numb]
        name.append(namespace)
        
for i in name:
    print(i)
