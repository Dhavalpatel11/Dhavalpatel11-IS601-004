a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): ".format(num))
    print(arr)
    print("\nPositive Output:")
    # TODO add new code here to print the desired result
    for i in range(len(arr)):
        arr[i]=int(arr[i])
        if arr[i] >=0:
            print(arr[i])


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
