def main():
    is_fibonacci(6)
    #1,1,2,3,5,8,13,21,34
    value = get_fibonacci_value(2)
    print(value)

def is_fibonacci(value, max_sequence=100):
    n1 = 0
    n2 = 1
    count = 0
    verdict = False
    if value == n1 or value == n2:
        print(f"Number {value} is fibonacci value")
        verdict = True
    else:
        while count < max_sequence:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            if nth == value:
                print(f"Number {value} is fibonacci value")
                verdict = True
                break
            if nth > value:
                print(f"Number {value} is not fibonacci value")
                print(f"{n1} is closest fibonacci value and sequence number is {count}")
                verdict = False
                break

    return verdict


def get_fibonacci_value(n):
    if not isinstance(n, int):
        raise ValueError("Not integer")
    n1 = 0
    n2 = 1
    count = 2
    if n == n1:
        return n1
    elif n == n2:
        return n2
    else:
        while count <= n:
            nth = n1 + n2
            print(f"sequence: {count}, fibonacci number: {nth}")
            # update values
            n1 = n2
            n2 = nth
            count += 1
        return nth


if __name__== "__main__" :
    main()
