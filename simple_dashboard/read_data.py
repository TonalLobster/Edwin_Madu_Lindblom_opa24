import pandas as pd

def read_olympics_data(url):
    df = pd.read_html(url)[2]

    # data cleaning
    df = df[13:-3] # use slicing to select rows
    df["Year"] = df["Games"].str[:4] # use to select character from a column
    df["Year"] == df["Year"].astype(int)
    df["Total"] == df["Total"].astype(int)
    df = df[["Year", "Total"]] # select subset of columns

    return df


if __name__ == "__main__":
    # for testing purpose
    url = "https://en.wikipedia.org/wiki/Sweden_at_the_Olympics"
    df = read_olympics_data(url)
    print(df)
    
