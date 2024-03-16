from yahooquery import Ticker
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import random 
random.seed(42)


tickers = Ticker(['aapl'])
df = tickers.history(period='max')

df.drop(['dividends','splits'], axis=1, inplace=True)


# train, test split
Train, test = train_test_split(df, test_size=0.2, shuffle=False)
train, val = train_test_split(Train, test_size=0.2, shuffle=False)


# normalization
scaler = StandardScaler()
s_train = scaler.fit_transform(train)
s_val = scaler.transform(val)
s_test = scaler.transform(test)


# x, y split
x_train = s_train[:,:-1]
y_train = s_train[:,-1]

x_val = s_val[:,:-1]
y_val = s_val[:,-1]

x_test = s_test[:,:-1]
y_test = s_test[:,-1]



