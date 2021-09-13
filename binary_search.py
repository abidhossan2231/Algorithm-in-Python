#Abid Hossan Hridoy
# abidhossan2231 - Github, Twitter, Instagram, HackerEarth, Pinterest, stack overflow, website

def binary_sort(sorted_list, length, key):
    start = 0
    end = length - 1
    while start <= end:
        mid = int ((start + end) / 2)

        # If found at mid, then return it
        if key == sorted_list[mid]:
            print ("\nEntered number %d is present at position: %d" % (key, mid+1))
            return -1

        # Search the left half
        elif key < sorted_list[mid]:
            end = mid - 1

        # Search the right half
        elif key > sorted_list[mid]:
            start = mid + 1

    print ("\nElement not found!")
    return -1

if __name__ == '__main__':
    lst = []
    size = int (input ("Enter size of list: \t"))

    for n in range (size):
        numbers = int (input ("Enter any number: \t"))
        lst.append (numbers)

    lst.sort ()
    print ('\n\nThe list will be sorted, the sorted list is:', lst)

    x = int (input ("\nEnter the number to search: "))

    binary_sort (lst, size, x)