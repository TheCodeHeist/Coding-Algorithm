# Python program for implementation of Bubble Sort

# Logic
def BubbleSort(list):
    tempList = list  # Store a snapshot of the list in a temporary variable

    # Iterate through the list, where "i" is the index of the list
    for i in range(len(tempList)):
        j = 1  # Set the value of "j" to 1, to compare the second element with the first element

        # Bruteforcing the list, where "j" is the current index of the list.
        # While "j" is less than the length of the list minus 1, compare the current element with the previous element
        while j < len(tempList) - i:
            # Compare the current element with the previous element
            if tempList[j] < tempList[j - 1]:
                tempList[j], tempList[j - 1] = tempList[j -
                                                        1], tempList[j]  # Swap the elements if the current element is less than the previous element

            j += 1  # Increment the value of "j" by 1, to proceed to the next iteration

    return tempList  # Return the sorted list


# Test
list = [64, 34, 25, 12, 22, 11, 90]  # Create a demo list

sortedList = BubbleSort(list)  # Sort the list, with our function "BubbleSort"

print("Sorted array is:", sortedList)  # Print the sorted list!
