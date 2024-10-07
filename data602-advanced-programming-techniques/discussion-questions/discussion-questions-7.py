import pandas as pd
# 1. What is pandas and why use it?
def q1():
    print("Pandas is a software library written for pythyon that is used for data manipulation and analysis. It uses dataframes which represent a two-dimensional table with rows and columns. These dataframes are collections of Series, which are one dimensional arrays.")
# 2. Give an example of how to import a csv file using pandas
def q2():
    df = pd.read_csv('https://raw.githubusercontent.com/riverar9/cuny-msds/refs/heads/main/data602-advanced-programming-techniques/assignments/assignment-06/data.csv')
    return df
# 3. Show how to view the first 10 rows of a dataset using pandas
def q3():
    df  = q2()
    print(df.head())
# 4. Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
def q4(s1, s2):
    return s1 == s2
# 5. Change the first character of each word to upper case in each word of df1
# df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
def q5(df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])):
    df1 = df1.str.title()
    return df1

def main():
    q1()
    print(q2().head())
    q3()
    print(q4(q2()['name'], q2()['name']))
    print(q5())

if __name__ == "__main__":
    main()