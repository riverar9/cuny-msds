# %%
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def q1(df, x):
# 1. How do you plot a histogram in Seaborn?  
    sns.histplot(
        data = df,
        x = x
    )

    plt.show()
    
def q2(df, x):
# 2. Plot a histogram with NAs dropped.
    t_df = df.loc[df[x].notna()]
    
    sns.histplot(
        data = t_df,
        x = x
    )

    plt.show()

def q3(df, x, color = 'green'):
# 3. How do you set the color for a histogram?
    sns.histplot(
        data = df,
        x = x,
        color = color
    )
    
    plt.show()
    
def q4(df, x, y):
# 4.  What type of plot would allow you to compare two continuous features?  Give an example of code.
    print("A scatterplot allows you to comopare two continious features.")

    sns.scatterplot(
        data = df,
        x = x,
        y = y
    )
    
    plt.show()

def q5(df):
# 5. Give example of a correlation plot.
    corr = df.select_dtypes(include='number').corr()

    sns.heatmap(corr, annot=True, cmap='coolwarm')

    plt.show()

def q6(df, x):
    sns.set_theme(rc={'figure.figsize':(15, 9)})
    sns.histplot(
        data = df,
        x = x
    )

    plt.show()
# 6. Change the figure size of your plot(s).
# You can use any dataset for examples to these questions. Some datasets can be found using seaborn: https://seaborn.pydata.org/generated/seaborn.load_dataset.html 
# %%
def download_file(url):
    import requests, os
    filename = os.path.basename(url)
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)
    return filename

def unzip_file(zip_file_path):
    import zipfile, os
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
        extracted_files = zip_ref.namelist()
    return extracted_files[0] if extracted_files else None

def main():
    data_url = "https://maven-datasets.s3.amazonaws.com/US+Candy+Distributor/US+Candy+Distributor.zip"
    
    downloaded_file_path = download_file(data_url)
    unzipped_file = unzip_file(downloaded_file_path)

    df = pd.read_csv(unzipped_file)

    q1(df, 'population')
    q2(df, 'population')
    q3(df, 'population', color = 'red')
    q4(df, 'population', 'density')
    q5(df)
    q6(df, 'population')

# %%
if __name__ == "__main__":
    main()
# %%
