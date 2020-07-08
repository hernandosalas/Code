'''

pip install mljar-supervised

'''

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

data = datasets.load_iris()
X = pd.DataFrame(data["data"], columns=data["feature_names"])
y = pd.Series(data["target"], name="target").map({i:v for i, v in enumerate(data["target_names"])})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

automl = AutoML(algorithms=["Decision Tree", "Linear", "Random Forest"],
                total_time_limit=5*60)
automl.fit(X_train, y_train)