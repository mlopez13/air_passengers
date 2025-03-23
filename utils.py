import pandas as pd


def get_data():
    path = 'data/AirPassengers.csv'
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Month'], format='%Y-%m')
    df = df.drop(columns=['Month'])
    df = df.set_index('Date')
    return df

def train_val_test_split(df, cutoffs):

    train = df.copy().reset_index()
    val = df.copy().reset_index()
    test = df.copy().reset_index()

    train = train[
        (train['Date'] >= pd.to_datetime(cutoffs[0], format='%Y')) &
        (train['Date'] < pd.to_datetime(cutoffs[1], format='%Y'))
    ]
    val = val[
        (val['Date'] >= pd.to_datetime(cutoffs[1], format='%Y')) &
        (val['Date'] < pd.to_datetime(cutoffs[2], format='%Y'))
    ]
    test = test[test['Date'] >= pd.to_datetime(cutoffs[2], format='%Y')]

    train = train.set_index('Date')
    val = val.set_index('Date')
    test = test.set_index('Date')

    return train, val, test
