def main():
    # !/usr/bin/python

    a = 60
    b = 13
    c = 0

    c = a & b;
    kwargs = {"bin":c}
    kwargs = {"bin": c} #, "arg2": "two", "arg1": 5}
    print_log(**kwargs)

    c = a | b;
    print
    print("Value of c is ", c)

    c = a ^ b;
    print
    print("Value of c is ", c)

    c = ~a;  # -61 = 1100 0011
    print
    "Line 4 - Value of c is ", c

    c = a << 2;  # 240 = 1111 0000
    print("Value of c is ", c)

    c = a >> 2;  # 15 = 0000 1111
    print
    print("Value of c is ", c)
##Write a function:

def solution(N):
        print(f"Given value: {N}")
        binary = bin(N)
        print(f"As a binary: {binary}")

        count = 0
        count_so_far = 0
        best_count = 0
        for i, digit in enumerate(binary):
            if i > 1:
                print(digit)
                if digit == '0':
                    count += 1

                if best_count < count:
                    best_count = count

                if digit == '1':
                    count = 0

        return best_count



##that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap

def print_log(**kwargs):

    bin_int = kwargs["bin"]
    binary = bin(bin_int)
    print(f"bin: {bin_int} --> {binary}")




if __name__== "__main__" :

    best_count = solution(10000000)
    print(f"best_count: {best_count}")
