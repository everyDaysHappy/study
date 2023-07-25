with open('Login.csv', mode='r') as f:
    for line in f:
        info = line.strip().split(' ')[0]
        print(info)