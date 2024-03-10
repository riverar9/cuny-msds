# %%
import pandas as pd
import sqlite3

def write_to_sqlite(dataframe, file_path, table_name='data_table', index=False, if_exists='replace'):
    """
    Write a DataFrame to an SQLite database.

    Parameters:
    - dataframe: pandas DataFrame
    - file_path: str, path to the SQLite file
    - table_name: str, name of the table to be created in the SQLite database
    - index: bool, whether to write DataFrame index as a column
    - if_exists: str, {'fail', 'replace', 'append'}, default: 'replace'
        - 'fail': If the table exists, do nothing.
        - 'replace': If the table exists, drop it, recreate it, and insert data.
        - 'append': If the table exists, insert data. Create if does not exist.

    Returns:
    - None
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(file_path)

    # Write the DataFrame to SQLite
    dataframe.to_sql(table_name, conn, index=index, if_exists=if_exists)

    # Close the database connection
    conn.close()

def encode_columns(dataframe, column_names):
    # Create a copy of the original DataFrame to avoid modifying the original data
    encoded_df = dataframe.copy()

    # Create reference DataFrames for each column
    reference_dfs = []
    for col in column_names:
        # Encode the column and add it to the DataFrame
        encoded_column = encoded_df[col].astype('category').cat.codes
        encoded_df[col + '_id'] = encoded_column

        # Create a reference DataFrame
        reference_df = pd.DataFrame({
            'Original_' + col: encoded_df[col],
            'Encoded_' + col: encoded_column
        })

        reference_dfs.append(reference_df)

    # Remove the original columns from the encoded DataFrame
    encoded_df = encoded_df.drop(columns=column_names)

    # Return the list of DataFrames [encoded_df, reference_df1, reference_df2, ...]
    return [encoded_df] + reference_dfs
# %%
def main():
    # %%
    # Import our packages we need
    import os
    import pandas as pd
    # %%
    # Read in our files
    linkedin_skills = pd.read_csv(
        'https://raw.githubusercontent.com/riverar9/cuny-msds/main/data607/projects/project-3/Part%201/linkedin_skills_example.csv'
    )

    linkedin_skills.head()

    # %%
    reddit_comments = pd.read_csv(
        'https://raw.githubusercontent.com/riverar9/cuny-msds/main/data607/projects/project-3/Part%201/reddit_ds_scrape_sample.txt'
        , sep = '\t'
    )

    reddit_comments = reddit_comments[reddit_comments['date'].notna()]

    reddit_comments.head()

    comments, authors, posts = encode_columns(
        reddit_comments,
        [
            'author',
            'url'
        ]
    )

    # %%
    write_to_sqlite(
        comments
        , "reddit.sqllite"
        , table_name='comments'
        , index=False
        , if_exists='replace'
    )

    write_to_sqlite(
        authors
        , "reddit.sqllite"
        , table_name='authors'
        , index=False
        , if_exists='replace'
    )

    write_to_sqlite(
        posts
        , "reddit.sqllite"
        , table_name='posts'
        , index=False
        , if_exists='replace'
    )
    
# %%
if __name__ == "__main__":
    main()