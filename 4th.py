for i in range(1,11):
    if i==3:
        continue
    print(i)
    for i in range(5):
        if i==2:
            pass
        print(i)
        for i in range(5):
            print(i)
        else:
            print("this is else block")