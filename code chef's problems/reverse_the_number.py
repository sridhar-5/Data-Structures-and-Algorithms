def main():
    testcases = int(input())

    if testcases < 1 or testcases > 1000:
        return 0

    x = 0

    while x < testcases:
        input_no = int(input())

        if input_no < 1 or input_no > 1000000:
            return 0
        else:
            rev = 0
            while input_no > 0:
                rem = input_no % 10
                rev = rev * 10 + rem
                input_no = int(input_no / 10)

            print(rev)
        x += 1


if __name__ == '__main__':
    main()
