
def add():
    r = int(input("Enter added person age : \t"))
    data.append(r)
    print("New person list in Orphanage ------")
    print(data)

def relished():
    r = int(input("Enter relished person's room number : \t"))
    data.pop(r)
    print("New person list in Orphanage ------")
    print(data)

def finding():
    def binary_sort(sorted_list, length, key):
        start = 0
        end = length - 1
        while start <= end:
            mid = int((start + end) / 2)

            # If found at mid, then return it
            if key == sorted_list[mid]:
                print("\nSearching person %d is present at room number: %d" % (key, mid + 1))
                return -1

            # Search the left half
            elif key < sorted_list[mid]:
                end = mid - 1

            # Search the right half
            elif key > sorted_list[mid]:
                start = mid + 1

        print("\nPerson not found!")
        return -1

    data.sort()
    x = int(input("\nEnter the person's age to search: "))
    binary_sort(data, i, x)

def mael():
    def partition(array, low, high):
        pivot = array[high]

        i = low - 1

        for j in range(low, high):

            if array[j] <= pivot:
                i += 1

                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)

            quickSort(array, low, pi - 1)

            quickSort(array, pi + 1, high)

    i = len(data)

    quickSort(data, 0, i - 1)

    print('Taking meal in ascending order ------')
    print(data)

def play():
    def mergeSort(data):
        if len(data) > 1:

            M = len(data) // 2
            L = data[:M]
            R = data[M:]

            mergeSort(L)
            mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] > R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1

    def printList(data):
        for i in range(len(data)):
            print(data[i], end=" ")
        print()
    mergeSort(data)

    print("Playground line in descending order ------ ")
    printList(data)

if __name__ == '__main__':
  data = []
  for i in range(int(input("How many people are in Orphanage : "))):
      n = str(i+1)
      numbers = int(input("Enter "+n+" person age : \t"))
      data.append(numbers)
print("Here All person Input age : ")
print(data)
print("Press 1 to add new person. \nPress 2 to relished a person. \nPress 3 to find a person. \nPress 4 to take meal in ascending order. \nPress 5 to playing in descending order. \nPress 0 to Holiday.")
k=1
while k!=0:
    j = int(input("Enter your choose number : \t"))
    if j == 1:
        add()
    elif j == 2:
        relished()
    elif j == 3:
        finding()
    elif j == 4:
        mael()
    elif j == 5:
        play()
    elif j == 0:
        exit()
    else:
        print("wrong Input.\nPlease input correct number")
    k += 1