
#IMPORT 
import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
#data 
df = pd.read_csv('./TripData.csv') 
# print(df.head(5)) 

#delete col "medallion" & "hack_license" 
df = df.drop(['medallion', 'hack_license'], axis= 1) 



# CHECK SPECIAL CASE 

#check null 
df.dropna(inplace= True)

#check and drop duplicates 
df.drop_duplicates(inplace= True)
# print(len(df)) 

#check missing value 
# print(df.isnull().sum()) 

#check passenger_count >= 1 && fare_amount > 0
df = df[df['passenger_count'] >= 1]  
df = df[df[' fare_amount'] > 0] 
# print(len(df)) 



# COMPARE 

# # 1. compare: fare_amount - passenger_count 

# fig = plt.figure(figsize = (16, 9)) 
# plt.xlabel('Fare ($)')
# plt.ylabel('Passenger (per)') 
# plt.show() 

# # --> no rela 

# # 2. compare: fare_amount - trip_distance

# fig = plt.figure(figsize = (16, 9)) 
# sns.scatterplot(x= 'trip_distance', y= ' fare_amount', data= df).set_title('Distance & Fare') 
# plt.xlabel('Distance (m)') 
# plt.ylabel('Fare ($)')
# plt.show() 

# # --> maybe  

# 3. convert time (in the same year?)
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['weekday'] = df['pickup_datetime'].dt.dayofweek 
df['time'] = df['pickup_datetime'].dt.hour 

# 3.1. compare: fare - weekdays 

# df.pivot_table(' fare_amount', index= 'weekday').plot(figsize= (16,9)) 
# plt.title('Fare by weekday')
# plt.xlabel('Weekday')
# plt.ylabel('Fare')
# plt.show() 

# --> Peak at Wednesday, Saturday 

# 3.2. compare: fare - hours  

# df.pivot_table(' fare_amount', index= 'time').plot(figsize= (16,9)) 
# plt.title('Fare by time of day')
# plt.xlabel('Time')
# plt.ylabel('Fare')
# plt.show() 

# # --> Peak at 1h, 5h, 17h, 20h, 24h 



# TRAIN & TEST DATA 

# Split data 
x_fare = df[['weekday', 'time', 'trip_distance']]
y_fare = df[' fare_amount'].values
x_train, x_test, y_train, y_test = train_test_split(x_fare, y_fare, test_size= 0.3, random_state= 69) 

# 10th degree regression 
poly = PolynomialFeatures(degree= 5, include_bias= True)
x_train_poly = poly.fit_transform(X=x_train)
reg = LinearRegression() 
reg.fit(x_train_poly, y_train) 
def fare_predict(args):
    inp = poly.fit_transform(pd.DataFrame({"weekday": [args[0]], "time": [args[1]], "trip_distance": [args[2]]}))
    return reg.predict(inp)

def plot_all():
    fig, axes = plt.subplots(2, 2)
    fig.subplots_adjust(hspace=0.3,wspace= 0.3)
    axes[0, 0].scatter(df['weekday'].values, df[' fare_amount'].values,c = 'g', marker = '^')
    axes[0, 0].set_title("fares by weekdays")
    axes[1, 0].scatter(df['time'].values, df[' fare_amount'].values, c = 'r')
    axes[1, 0].set_title("fares by hours")
    axes[0,1].scatter(df['trip_distance'].values, df[' fare_amount'].values, c = 'y', marker = '.')
    axes[0,1].set_title("fares by miles")
    axes[1,1].scatter(df['passenger_count'].values, df[' fare_amount'].values, c = 'black', marker= 'v')
    axes[1,1].set_title("fares by head count")
    plt.show()
