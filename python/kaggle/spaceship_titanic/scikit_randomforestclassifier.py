"""Kaggle Spaceship Titanic competition using scikit-learn RandomForestClassifier.

https://www.kaggle.com/competitions/spaceship-titanic
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
train_orig = pd.read_csv("/home/a/kaggle/spaceship-titanic/input/train.csv")
COL_ID = "PassengerId"
COL_LABEL = "Transported"
COLS_UNIQUE = ["Name"]
COLS_ENUMS_BINARY = ["VIP"]
COLS_ENUMS_FEW = ["HomePlanet", "Destination"]
COLS_ENUMS_MANY = ["Cabin"]
COLS_BOOLEAN = ["CryoSleep"]
COLS_SCALE = ["Age", "RoomService", "FoodCourt", "ShoppingMall"]

labels = train_orig[COL_LABEL]
logger.debug("Train data loaded")
logger.debug(train_orig.describe())
logger.debug("\t%s", train_orig.head().to_string().replace("\n", "\n\t"))
logger.debug(train_orig.info())

## Define pipeline
pipeline = pipeline.Pipeline([
    (
        "drop_columns",
        pipeline.FunctionTransformer(lambda x: x.drop(
            columns=[COL_ID, COL_LABEL, *COLS_UNIQUE, *COLS_ENUMS_MANY, "VRDeck"],
            errors="ignore",
        )),
    ),
    (
        "one_hot_encode",
        pipeline.FunctionTransformer(lambda x: pd.get_dummies(
            data=x,
            columns=[*COLS_ENUMS_BINARY, *COLS_ENUMS_FEW, *COLS_BOOLEAN],
        )),
    ),
    (
        "fill_na",
        pipeline.FunctionTransformer(lambda x: x.fillna(0)),
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
test_orig = pd.read_csv("/home/a/kaggle/spaceship-titanic/input/test.csv")
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
    COL_ID: test_orig[COL_ID],
    COL_LABEL: prediction,
})
output.to_csv("/home/a/kaggle/spaceship-titanic/submission.csv", index=False)
logger.info("Predictions saved")
