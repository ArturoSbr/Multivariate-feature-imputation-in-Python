import numpy as np
from sklearn.tree import DecisionTreeRegressor

def impute(data, to_impute, max_depth=5, max_features=5, random_state=None):
    '''
    Multivariate feature imputation method that imputes the missing values of a feature using Classification and
    Regression Trees. One independent variable is modeled as a function of other independent variables and
    its missing values are filled in accordance to the resulting model.
    
        Parameters
        ----------
                data : pandas.DataFrame object
                    The dataset that contains *all* the independent variables, *including* the feature containing missing values.
                to_impute : str
                    The name of the feature to be modeled as a function of the other independent variables. `to_impute` must
                    be a column in `data`.
                max_depth : int, default `5`
                    The maximum depth of the resulting decision tree.
                max_features : int, default `5`
                    The maximum number of features used to model `to_impute`.
        Returns
        -------
                numpy.array
                    The output is a numpy array that matches the length of the original dataset.
                    Entries that were not empty retain their original value.
                    Entries that used to be `NaN` are filled in by the predicted value of the regressor/classifier.
        Example
        -------
                df['feature_1_imputed'] = decision_tree_imputer(data=df, to_impute='feature_1')
        GitHub
        ------
                Visit https://github.com/ArturoSbr/ for more content
    '''
    features = data.columns.tolist()
    features.remove(to_impute)
    X = data.loc[data[to_impute].notna(), features].copy()
    y = data.loc[data[to_impute].notna(), to_impute].copy()
    m = data[features].isna().sum()
    X = X.drop(m[m > 0].index, axis=1)
    features = X.columns
    if len(features) == 0:
        raise 'All the independent features have missing values. At least one feature must be completely filled in.'
    else:
        if len(features) == 1:
            X = X.values
            clf = DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=max_depth,
                                        max_features=max_features, random_state=random_state)
            clf.fit(X, y)
            return np.where(data[to_impute].isna(),
                            clf.predict(data[features].values),
                            data[to_impute].values)
        else:
            clf = DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=max_depth,
                                        max_features=max_features, random_state=random_state)
            clf.fit(X, y)
            return np.where(data[to_impute].isna(),
                            clf.predict(data[features]),
                            data[to_impute].values)