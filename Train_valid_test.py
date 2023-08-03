from fast_ml.model_development import train_valid_test_split 
X_train, y_train, X_valid, y_valid, X_test, y_test = train_valid_test_split(df, target = target, train_size=0.8, valid_size=0.1, test_size=0.1)
# Get the shape of all the datasets 
print(X_train.shape), 
print(y_train.shape) 
print(X_valid.shape)
print(y_valid.shape)
print(X_test.shape)
print(y_test.shape)
