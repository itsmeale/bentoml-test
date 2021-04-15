from bentoml import BentoService, api, artifacts, env
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact("model")])
class MyClassifier(BentoService):
    @api(input=DataframeInput(), batch=True)
    def predict(self, values):
        return self.artifacts.model.predict(values)
