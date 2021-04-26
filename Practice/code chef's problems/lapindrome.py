def main():
    testcases = int(input())
    x = 0
    while x < testcases:

        input_string = str(input())
        length = len(input_string)

        string_half = length // 2

        if length % 2 == 0:
            if sorted(input_string[:string_half]) == sorted(input_string[string_half:]):
                print("YES")
            else:
                print("No")
        else:
            if sorted(input_string[:string_half]) == sorted(input_string[string_half + 1:]):
                print("YES")
            else:
                print(length)
                print(input_string[:string_half])
                print(input_string[string_half+1:])
                print("NO")

        x += 1


if __name__ == '__main__':
    main()
