"""

Pandas tests

https://chrisalbon.com/
http://www.datasciencemadesimple.com/python-pandas-data-structure/
https://www.dataquest.io/blog/pandas-cheat-sheet/

"""

import pandas
import pandas as pd
import numpy as np
from datetime import datetime


def println(string):
    """
    print with a \n

    :param string:
    :return:
    """
    print(string)
    print('\n')


# Create a dataframe
raw_data = {'first_name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns=['first_name', 'nationality', 'age'])

# Create variable with TRUE if nationality is USA
american = df['nationality'] == "USA"

# Create variable with TRUE if age is greater than 50
elderly = df['age'] > 50

# Select all cases where nationality is USA and age is greater than 50
df[american & elderly]

# Select all cases where the first name is not missing and nationality is USA
df[df['first_name'].notnull() & (df['nationality'] == "USA")]

if __name__ == "__main__":
    """ main """
    # By setting sep=None and engine='python' we use the csv_sniffer to auto detect the separator
    df = pandas.read_csv("test.csv", sep=None, engine='python')
    println(df)
    println(df.columns.tolist())
    println(df.get_values())

    print('----------------------------------------')
    println(map(lambda x: datetime.strptime(x, "%Y-%m-%d").date().strftime("%d/%m/%Y"), df[df.columns[0]]))
    println(map(float, df['Money']))
    println(df.ix[1])

    print('----------------------------------------')
    # Print the row that match this equality
    criteria = df['Date'] == '2016-11-24'
    println(df[criteria])

    print('----------------------------------------')
    # Get the date value when types == A
    # Get the Money Value when Other == A
    test_value = df[["Date", "Money"]].values[df[["Types", "Other"]] == "A"]
    print(test_value[1])
    println(test_value)

    print('----------------------------------------')
    # header = 0  will set the header to the value of the raw[0] in the csv
    # names = ["whatever', ...] will rename the header's names
    df2 = pandas.read_csv("output.csv", sep=None, engine='python', header=0, names=['I', 'choose', 'the', 'name'])
    println(df2)
    println(df2['I'])
    println(df2[df2.columns[0]])

    print('----------------------------------------')
    # Other pandas tests
    df3 = pandas.DataFrame({'a': [1, 2], 'b': [3, 4]})
    print(df3)
    df3['c'] = [3, 4]
    print(df3)
    print(df3.iat[0, 0])
    print(df3.at[0, 'a'])

    # Append dataframe to another one
    df1 = pd.DataFrame()  # Empty dataframe
    df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
    df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
    df3 = pd.DataFrame([[5, 6], [7, 8]], columns=list('CD'))
    println(df.append(df2))
    println(df.append(df2, ignore_index=True))
    println(df.append(df3, ignore_index=True))
