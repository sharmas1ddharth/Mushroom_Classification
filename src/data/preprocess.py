from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

class Preprocessing():
    def __init__(self, path, X, y ,t_size=0.4, random_state_value=42, ):
        data = pd.read_csv(path)
        self.data = data
        self.encode_data()
        self.distribute_data()
        # self.train_and_test(X, y, t_size, random_state_value)

    def encode_data(self):
        label_encoder = LabelEncoder()
        for col in self.data.columns:
            self.data[col] = label_encoder.fit_transform(self.data[col])
        # data.drop('veil-type', axis=1, inplace=True)
        return self.data


    def distribute_data(self):
        X = self.data.drop('class', axis=1)
        y = self.data['class']
        return X, y

    # this function is not working fix it
    #  def train_and_test(self,X, y, t_size, random_state_value):
    #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_size, random_state=random_state_value)
    #     return X_train, X_test, y_train, y_test