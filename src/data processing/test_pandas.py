"""

Pandas tests

"""

import pandas
from datetime import datetime


def println(string):
    """
    print with a \n

    :param string:
    :return:
    """
    print(string)
    print('\n')


if __name__ == "__main__":
    """ main """
    # By setting sep=None and engine='python' we use the csv_sniffer to auto detect the separator
    df = pandas.read_csv("test.csv", sep=None, engine='python')
    println(df)
    println(df.columns.tolist())
    println(df.get_values())
    println(map(lambda x:  datetime.strptime(x, "%Y-%m-%d").date().strftime("%d/%m/%Y"), df[df.columns[0]]))
    println(map(float, df['Money']))
    println(df.ix[1])

    # Get the date value when types == A
    # Get the Money Value when Other == A
    test_value = df[["Date", "Money"]].values[df[["Types", "Other"]] == "A"]
    print(test_value[1])
    println(test_value)

    # header = 0  will set the header to the value of the raw[0] in the csv
    # names = ["whatever', ...] will rename the header's names
    df2 = pandas.read_csv("output.csv", sep=None, engine='python', header=0, names=['I', 'choose', 'the', 'name'])
    println(df2)
    println(df2['I'])
    println(df2[df2.columns[0]])
