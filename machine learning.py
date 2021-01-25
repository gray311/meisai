from __future__ import print_function
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression # 处理线性回归的model
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing  #标准化数据
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC #处理分类问题的model


iris = datasets.load_iris()

iris_X = iris.data
iris_y = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

##print(knn.predict(X_test))
##print(y_test)


loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

X, y = datasets.make_regression(n_samples=1000, n_features=1, n_targets=1, noise=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.predict(X_test[:4]))
print(y_test[:4])

X1 = X_test
y1 = model.coef_ * X1 + model.intercept_

plt.plot(X1, y1, color='yellow' )
plt.scatter(X_train, y_train)
#plt.scatter(X_test, y_test,color= 'red')
plt.show()


print(model.coef_)  #y=0.5x+1 输出 0.5 
print(model.intercept_) #输出 1
print(model.get_params()) #给model 定义的参数
print(model.score(X_test,y_test)) #给测试数据打分，看处理效果 ，方法是R^2检验，回归系数


##print(model.predict(data_X[:4, :]))
##print(data_y[:4])

'''
X, y = datasets.make_regression(n_samples=100, n_features=2, n_targets=1, noise=2)

plt.scatter(X[:,:1], y , color ='red')
plt.scatter(X[:,1:2], y)
plt.show()
'''

'''标准化数据'''

a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)
print(a)
print(preprocessing.scale(a))

X, y = make_classification(n_samples=300, n_features=2 , n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)
'''
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show() '''

X = preprocessing.scale(X)  #压缩到0，1的范围
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
