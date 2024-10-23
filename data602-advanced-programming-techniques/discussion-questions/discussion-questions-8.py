# %%
import pandas as pd

# 1. How would you delete:
def q1(df, col_to_delete, index_of_row_to_delete):
    # An index from your dataframe
    df = df.reset_index(
        drop = True
    )
    
    # A column from your dataframe
    df = df.drop(
        columns = col_to_delete
    )
    
    # A row from your dataframe
    df = df.drop(index_of_row_to_delete)

    return df
    
# 2. How do you iterate over a pandas dataframe?
def q2(df, column_to_iterate):
    for index, row in df.iterrows():
        print(index, row[column_to_iterate])

# 3. How would you convert a string to a date?
def q3(df, string_to_date_column):
    df[string_to_date_column] = pd.to_datetime(df[string_to_date_column])
    return df

# 4. What is data aggregation?  Give an example in Python. 
def q4(df, group_column):
    print("""
    Data Aggregation is summarizing data, typically using a group. For example, an accounting department would be interested in aggregating expenses by individual to see the total expenses per individual.
    """)

    aggregated_data = df.groupby(group_column).sum()

    return aggregated_data

# 5. What is GroupBy in Pandas (groupby()). Give an example in Python.
def q5(df, group_column):
    print(
        """
    Group by in Pandas is a method that allows you to split data into groups. It enables for aggregations to be performed across the groups. 
    """)

    aggregated_data = df.groupby(group_column).sum()

    return aggregated_data

# %%
def main():
    df = pd.read_csv('https://raw.githubusercontent.com/riverar9/cuny-msds/refs/heads/main/data624-predictive-analytics/homework/homework-1/tute1.csv')

    q1(df, 'AdBudget', 5)
    q2(q1(df, 'AdBudget', 5).head(10), 'Sales')
    q3(q1(df, 'AdBudget', 5), 'Quarter')
    q4(q3(q1(df, 'AdBudget', 5), 'Quarter'), 'Quarter')
    q5(q3(q1(df, 'AdBudget', 5), 'Quarter'), 'Quarter')

if __name__ == "__main__":
    main()