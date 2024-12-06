def Odd(K):
    """
    K - integer number.
    Return True if K is odd, otherwise return False.
    """
    return K % 2 != 0

def CountOddNumbers(in_lst):
    """
    in_lst - list of integers.
    Return the count of odd numbers in the list.
    """
    count = 0
    for num in in_lst:
        if Odd(num):
            count += 1
    return count

def Proc24():
    """
    Input data, call function for counting odd numbers
    output results.
    """
    in_data = []
    for i in range(5):
        temp = int(input("Number: "))
        in_data.append(temp)
    odd_count = CountOddNumbers(in_data)
    print("Count of odd numbers: ", odd_count)

# Виклик функції Proc24 для виконання програми
Proc24()
