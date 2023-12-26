import sys
def get_abc():
    try:
        arr = [float(sys.argv[i]) for i in range(1, 4)]
    except:           
        print("не подходящие данные")
        flag = 1
        while(flag == 1):
            try:
                s = str(input())
                s1 = s.split()
                arr = [float(s1[i]) for i in range(3)]
                flag = 0
            except:
                print("не подходящие данные")
    return arr
def get_decision(arr):
    decision = []
    if (arr[0] != 0 and len(arr) == 3): 
        a = float(arr[0])
        b = float(arr[1])
        c = float(arr[2])
        d = b ** 2 - 4 * a * c 
        if (d > 0): 
            print("\nсуществует два действительных корня\n")
            decision.append((-b - d ** (1 / 2)) / (2 * a))
            decision.append((-b + d ** (1 / 2)) / (2 * a))
        elif (d == 0):
            decision.append(-b / (2 * a))
        else: 
            print("\nнет действительных корней\n")
        return decision
    else:
        print("уравнение не биквадратное")
        return decision
arr1 = get_abc()
print(arr1)
print(get_decision(arr1))   