from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
import logging

logger = logging.getLogger('mushroom_classification')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read(path):
    """This Function reads csv file with the help of pandas module
        INPUT : Path of the csv file
        OUTPUT : Data"""
    try:
        data = pd.read_csv(path)  # reads data from the csv file
        logger.debug(f'CSV file loaded successfully\nData:\n{data}')
        return data
    except:
        logger.exception("file not found in the given path")


def encode(data):
    """This Function encode data from objects to categorical data
        INPUT : data to encode
        OUTPUT : encoded data"""

    label_encoder = LabelEncoder()  # initialise the encoder
    logger.debug('label encoder initialized')

    try:
        for col in data.columns:
            data[col] = label_encoder.fit_transform(data[col])
        logger.debug(f'Data encoded successfully\nEncoded data:\n{data}')
        return data

    except:
        logger.exception('data not found')


def split(encoded_data):
    """This function splilt data into features(X) and labels(y)
    This function calls the encode_data function to get encoded data
    INPUT :  encoded data
    OUTPUT : returns features as 'X' variable and labels as 'y'"""

    try:
        X = encoded_data.drop('class', axis=1)
        logger.debug(f'label dropped and features loaded successfully into X variable.\nX:\n{X}')

        y = encoded_data['class']
        logger.debug('label loaded successfully to y variable\ny:\n{y}')
        return X, y

    except:
        logger.exception('encoded data not found')


def split_trainTest(X, y, test_size=0.4, random_state=42):
    """This function split data into training and testing data
    It calls the split_data() function to first split data into features and labels
    INPUT : features, labels, test data size(default=0.4), random state(default=42)
    OUTPUT : X_train(training features), X_test(testing features), y_train(training labels), y_test(testing labels)"""

    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        logger.debug(
            f'X_train, X_test, y_train, y_test loaded successfully.\nX_train shape: {X_train.shape}, X_test shape: {X_test.shape}, y_train shape: {y_train.shape}, y_test shape: {y_test.shape}')
        return X_train, X_test, y_train, y_test

    except:
        logger.exception('features and labels not found')


def train_predict(X_train, y_train, X_test, clf=RandomForestClassifier()):
    """This function trains the model and predict the labels for test data and return the prediction
    INPUT : X_train(training features), y_train(training labels), X_test(features for testing), clf(classifier, default is randomforest)
    OUTPUT : clf(trained classifier), prediction"""

    try:
        clf.fit(X_train, y_train)
        logger.debug(f'classifier trained successfully, classifier name: {clf.__class__.__name__}')
        pred = clf.predict(X_test)

        logger.debug(f'labels of testing data predicted successfully, predictions shape: {pred.shape}')
        return clf, pred

    except:
        logger.exception('something is not right')


def score(prediction, y_test, scorer=accuracy_score):
    """This function takes predictions and original labels and return accuracy score if the
    scorer is set to accuracy score or classification_report if scorer is set to classification_report
    INPUT : prediction(prediction of the test data features), y_test(actual labels of test data), scorer(accuracy(default), classification report)
    OUTPUT : score/report"""

    if scorer == accuracy_score:
        score = accuracy_score(y_test, prediction)
        logger.debug(f'accuracy score calculated successfully, accuracy score: {score}')
        return score

    elif scorer == classification_report:
        report = classification_report(y_test, prediction)
        logger.debug(f'classification report generated successfully, classification report: {report}')
        return report


def save_model(trained_clf, model_name):
    """This function takes trained classifier and model name as input and saved the model
    INPUT = trained classifier, name you want to give to your model"""

    try:
        pickle.dump(trained_clf, open(model_name, 'wb'))
        logger.debug(f'model saved successfully, model name: {model_name}')

    except:
        logger.exception('something is not right')


def do_this_fast(path):
    """This function will perform all the necessary steps and returns the prediction score and saves the model as model.sav"
    INPUT : data file path"""

    try:
        data = read(path)
        encoded_data = encode(data)
        X, y = split(encoded_data)
        X_train, X_test, y_train, y_test = split_trainTest(X, y, test_size=0.4, random_state=42)
        clf, prediction = train_predict(X_train, y_train, X_test, clf=RandomForestClassifier())
        prediction_score = score(prediction, y_test, scorer=accuracy_score)
        save_model(clf, "model.sav")
        return prediction_score

    except:
        logger.exception('something is not right')
