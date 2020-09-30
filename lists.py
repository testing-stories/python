def neg_out(x):
    if x>0:
        return True
    else:
        return False

def main(a):
    print(f"original list: {a}")
    #sort
    a.sort()
    print(f"sorted list: {a}")
    #reverse sort
    a.sort(reverse=True)
    print(f"sorted list, reverse: {a}")
    #max
    maximum = max(a)
    print(f"maximum: {maximum}")
    #min
    minimun = min(a)
    print(f"minimun: {minimun}")
    #
    #duplicates
    #remove dupes
    #smallest missing one
    setti = set(a)
    setti = list(filter(neg_out, a))
    setti = set(setti)

    missing = 0
    for index, i in enumerate(setti, start = 1):
        print(index)
        print(i)
        if i>index:
            missing = index
            break
    if missing == 0:
        missing = len(setti) +1
    print(f"smallest missing is {missing}")






    #loop list
    for item in a:
        print(f"item in list: {item}")

    for index, item in enumerate(a):
        print(f"index:{index}, item:{item}")

    #set
    a_set = list(set(a))
    print(f"remove dupes: {a_set}")
    count = 0
    for i in a_set:
        print(f"looking for num: {i}")
        for j in a:
            if i==j:
                count += 1
        print(f"count: {count}")
        count =0





if __name__== "__main__" :
    a = [-1,-2, 3,6,5,2,4,1,1,3,3]

    main(a)