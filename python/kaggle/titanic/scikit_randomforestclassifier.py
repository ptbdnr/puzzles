"""Kaggle Titanic competition using scikit-learn RandomForestClassifier.

url: https://www.kaggle.com/competitions/titanic
"""

import logging

import pandas as pd
from sklearn import pipeline
from sklearn.ensemble import RandomForestClassifier

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="%(message)s")

pd.set_option("display.max_columns", None)

## Load train data
train_orig = pd.read_csv("/home/a/kaggle/titanic/input/train.csv")
labels = train_orig["Survived"]
logger.debug("Train data loaded")
logger.debug(train_orig.describe())
logger.debug("\t%s", train_orig.head().to_string().replace("\n", "\n\t"))
logger.debug(train_orig.info())

## Define pipeline
pipeline = pipeline.Pipeline([
    (
        "drop_columns",
        pipeline.FunctionTransformer(lambda x: x.drop(
            columns=["PassengerId", "Survived", "Name", "Ticket", "Cabin", "Embarked", "Parch"],
            errors="ignore",
        )),
    ),
    (
        "fill_na",
        pipeline.FunctionTransformer(lambda x: x.fillna(0)),
    ),
    (
        "one_hot_encode",
        pipeline.FunctionTransformer(lambda x: pd.get_dummies(x, columns=["Sex", "Pclass", "SibSp"])),
    ),

])
logger.info(pipeline)

## Transform train data
train = pipeline.fit_transform(train_orig)
logger.info("Train data transformed")
logger.info(train.info())

## Train model
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(
    X=train,
    y=labels,
)

## Load test data
test_orig = pd.read_csv("/home/a/kaggle/titanic/input/test.csv")
logger.info("Test data loaded")

## Transform test data
test = pipeline.transform(test_orig)
logger.info("Test data transformed")
logger.info(test.info())

## Make predictions
prediction = model.predict(
    X=test,
)

## Save predictions
output = pd.DataFrame({
    "PassengerId": test_orig["PassengerId"],
    "Survived": prediction,
})
output.to_csv("/home/a/kaggle/titanic/submission.csv", index=False)
logger.info("Predictions saved")
