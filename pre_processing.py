import pandas as pd
from datetime import date, datetime

logo = {
    "Indian Institute of Technology Madras":'https://upload.wikimedia.org/wikipedia/en/6/69/IIT_Madras_Logo.svg',
    "Indian Institute of Technology Delhi": 'https://upload.wikimedia.org/wikipedia/en/f/fd/Indian_Institute_of_Technology_Delhi_Logo.svg',
    "Indian Institute of Technology Bombay":'https://upload.wikimedia.org/wikipedia/en/1/1d/Indian_Institute_of_Technology_Bombay_Logo.svg',
    "Indian Institute of Technology Kanpur":'https://upload.wikimedia.org/wikipedia/en/a/a3/IIT_Kanpur_Logo.svg',
    "Indian Institute of Technology Kharagpur":'https://upload.wikimedia.org/wikipedia/en/1/1c/IIT_Kharagpur_Logo.svg',
    "Indian Institute of Technology Roorkee":'https://upload.wikimedia.org/wikipedia/en/6/6f/Indian_Institute_of_Technology_Roorkee_logo.png',
    }

def read_2019():
    df = pd.read_csv('./NIRF2019.csv')
    df = df.iloc[:,1:]
    names = df.iloc[0:5,1]
    return df,list(names)

def read_2020():
    df = pd.read_csv('./NIRF2020.csv')
    df = df.iloc[:, 1:]
    names = df.iloc[0:5, 1]
    return df, list(names)

def read_2021():
    df = pd.read_csv('./NIRF2021.csv')
    df = df.iloc[:, 1:]
    names = df.iloc[0:5, 1]
    return df, list(names)

def Top_15():
    top_15 = pd.read_csv('./top15.txt')
    top_15['Date_of_establishment'] = pd.to_datetime(top_15['Date_of_establishment'])

    def from_dob_to_age(born):
        today = pd.to_datetime('2021-10-01')
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    top_15['Age'] = top_15['Date_of_establishment'].apply(lambda x: from_dob_to_age(x))
    return top_15