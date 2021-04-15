from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from bentoml_test.app.main import MyClassifier

iris = load_iris()

X = iris.data
Y = iris.target

model = RandomForestClassifier(n_estimators=100)
model.fit(X, Y)

classifier_service = MyClassifier()
classifier_service.pack("model", model)
saved_path = classifier_service.save()
