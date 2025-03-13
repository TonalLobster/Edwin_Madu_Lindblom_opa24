import pandas as pd
from pathlib import Path # import a class called Path from library pathlib. pathlib is OOP oriented

def read_data():
    data_path = Path(__file__).parent /"data" #för att hitta en annan fil i en undermapp så kan du skriva 'parents[1] / "data"'.
    df = pd.read_excel(data_path/"resultat-ansokningsomgang-2024 (2).xlsx", skiprows=5, sheet_name="Tabell 3")
    return df



if __name__ == "__main__":
    #testing purpose
    df = read_data()
    print(df.columns)

