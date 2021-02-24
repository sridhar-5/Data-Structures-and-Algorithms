def main():
    
    testcases = int(input())

    x = 0
    while x < testcases:

        num = int(input())

        if num >= pow(10,9):
            return 0

        i = 5
        count = 0
        while int(num/i) > 0:
            count += int(num/i)
            i = i * 5

        print(count)

        x += 1    

if __name__ == '__main__':
    main()    