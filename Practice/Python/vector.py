class MyVector():

    def __init__(self, d):
        # Create d-dimensional vector of zeros.
        self.coords = d

    def len(self):
        # Return the dimension of the vector.
        return len(self.coords)

    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self.coords[j]

    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self.coords[j] = val

    def addvectors(self, v2):
        add = []
        # Add v2 to current vector and print resulting vector.
        for i in range(0, v2.len()):
            add.append(self.coords[i] + v2[i])
        return add

    def difference(self, v2):
        diff = []
        # find the difference of two vectors and print result
        for i in range(0, v2.len()):
            diff.append(self.coords[i] - v2[i])
        return diff

    def dotproduct(self, v2):
        dot = []
        # find the dotproduct of two vectors and print result
        for i in range(0, v2.len()):
            dot.append(self.coords[i] * v2[i])
        s = sum(dot)

        return (s)

    def scalarproduct(self, c):
        scalar = []
        # find the dotproduct of two vectors and print result
        for i in range(0, len(self.coords)):
            scalar.append(self.coords[i] * c)
        return (scalar)

    def __str__(self):
        return ','.join(map(str, self.coords))


def testvector():
    # read space seperated vector points
    l = []
    v1 = MyVector(list(map(int, input().split())))
    v2 = MyVector(list(map(int, input().split())))
    if (v1.len() != v2.len()):
        print("Incompatible")
        return
    n = int(input())
    k = n
    while (n > 0):
        operation = input()
        if (operation == 'A'):
            result = v1.addvectors(v2)
        if (operation == 'D'):
            result = v1.dotproduct(v2)
        if (operation == 'M'):
            result = v1.difference(v2)
        if (operation == 'S'):
            scale = int(input())
            result = v1.scalarproduct(scale)
        l.append(result)

        n = n - 1
    for i in range(0, k):
        print(l[i])


def main():
    testvector()


if __name__ == '__main__':
    main()