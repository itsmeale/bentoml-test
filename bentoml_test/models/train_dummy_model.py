from sklearn.datasets import iris
from sklearn.ensemble import RandomForestClassifier


X = iris.data
Y = iris.target

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
