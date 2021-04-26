def findMissing(N, stringOfRolls):
    missingStatus = "All Present"
    x = stringOfRolls.split(" ")
    for i in range(0, len(x)):
        x[i] = int(x[i])

    use_for_comparision = []
    for i in range(N):
        use_for_comparision.append(i + 1)

    difference = []
    difference = list(set(use_for_comparision) - set(x))

    if len(difference) == 0 :
        missingStatus = "All Present"
    else:
        missingStatus = difference[0]
    return missingStatus

N = int(input())
stringOfRolls = input()
missingRoll = findMissing(N, stringOfRolls)
print(missingRoll)


def deleteAfter(self, u):
    # @start-editable@

    if self.head != None:
        pointer = self.head
        while (pointer.next != None and pointer.element != u):
            pointer = pointer.next
        if pointer.element == u:
            if pointer.next == None:
                return
            if pointer.next and pointer.next.next == None:
                self.deleteLast()
                return
            elif pointer.next and pointer.next.next != None:
                temp = pointer.next
                temp.next.prev = pointer
                pointer.next = temp.next
                del temp
                self.sz -= 1
                return
    print('Node to delete after not found')
    return

    # @end-editable@
