import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn import svm 
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import median_absolute_error
df = pd.read_csv('/home/hugues/Documents/eclipse/runtime-EclipseXtext/testmml/src/Boston.csv')
X = df.drop(columns=['medv'])
y = df['medv']

clf = svm.SVR(kernel='rbf')
test_size = 0.03
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
clf.fit(X_train, y_train)
y = clf.predict(X_test)

print 'mean_absolute_error: {}'.format(mean_absolute_error(y, y_test))
print 'mean_squared_error: {}'.format(mean_squared_error(y, y_test))
print 'mean_absolute_percentage_error: {}'.format(median_absolute_error(y, y_test))
