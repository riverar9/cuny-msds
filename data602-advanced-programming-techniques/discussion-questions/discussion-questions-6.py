import pandas as pd
import numpy as np
# 1. What are the similarities and differences between pandas and numpy? Include some type of example with code.
def q1():
    """
    Similarities:
        - Both are good for and are used for data mainpulation and analysis
        - Both support mathematical operations
        - Both use arrays allowing for slicing
    
    Differences:
        - Pandas only allows for use with 2 dimensional arrays
        - Numpy allows for n-th dimensional arrays
        - All elements in a numpy array must be of the same type
        - Pandas uses labeled rows and columns
        - Pandas is better for work with tabular data (excel, .csv, etc)
    """

    # Numpy example:
    # Creating a 2x2x2 NumPy array
    arr = np.array([[[1, 2], [3, 4]], 
                    [[5, 6], [7, 8]]])

    print("Original 3D Array:\n", arr)

    # Multiply all elements by 2
    arr = arr * 2

    print("\nUpdated 3D Array (after multiplication):\n", arr)

    # Pandas Example:
    # Creating a Pandas DataFrame
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

    print("Original DataFrame:\n", df)

    # Multiply all elements by 2
    df = df * 2

    print("\nUpdated DataFrame (after multiplication):\n", df)


# 2. What is the ndarray in numPy?
def q2():
    """
    the ndarray is an object in numpy which can hold a multi-dimensional array.
    """
    pass
# 3. Create a 1D array of numbers from 0 to 9 
# Desired Output: 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def q3():
    arr = np.arange(10)
    print(arr)
# 4. Extract all odd numbers from array1 
def q4():
    array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    odd_list = []
    for element in array1:
        if element % 2 == 1:
            odd_list.append(element)
    array2 = np.array(odd_list)
    print(array2)
# 5. Get the common items between a and  b  
# input
# #Desired Output:
# array([2, 4])
def q5():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])

    print(np.intersect1d(a, b))
# 6. From array a remove all items present in array  b 
# Desired Output:
# array([1,2,3,4])
def q6():
    a = np.array([1,2,3,4,5])
    b = np.array([5,6,7,8,9])

    output_list = []

    for e_a in a:
        if e_a not in b:
            output_list.append(e_a)
    
    print(np.array(output_list))
# 7. Find out if iris has any missing values. 
def q7():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

    has_nans = np.isnan(iris).any()

    if has_nans:
        print("There are missing values in the iris dataset.")
    else:
        print("There are no missing values in the iris dataset.")


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()

if __name__ == "__main__":
    main()