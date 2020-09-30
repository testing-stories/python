def main():
    a_string = "test"
    value_a = to_string(a_string)
    b_bytes = b"test"
    value_b = to_string(b_bytes)

    if value_a == value_b:
        print("ok")

    if value_a is not value_b:
        print("that's true")
    index = 0
    for i in a_string:
        print(f"index:{index} {i}")
        index +=1

    for i in b_bytes:
        value = ascii_to_string(i)
        print(f"index:{index} {i} --> {value}")
        index += 1


def char_to_ascii(char='B'):
    return ord(char)


def ascii_to_string(ascii='66'):
    return chr(ascii)


def to_string(bytes_or_string):
    if isinstance(bytes_or_string, bytes):
        value = bytes_or_string.decode('utf-8')
    else:
        value = bytes_or_string
    return value

if __name__== "__main__" :

    main()
