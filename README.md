# sudhi9sharma

I used the The German Traffic Sign Recognition Benchmark (GTSRB) database.
Tested the effects of hidden layers on the accuracy of the model.
# Hidden Layers Added with a dropout of 0.2
tf.keras.layers.Dense(NUM_CATEGORIES * 32, activation="relu"),
        tf.keras.layers.Dropout(0.2)
tf.keras.layers.Dense(NUM_CATEGORIES * 16, activation="relu")
 tf.keras.layers.Dense(NUM_CATEGORIES * 8, activation="relu")
# Result- 94% with a loss of 21%
The model appears to fit the training data well without overfitting, and generalises well to the testing data.

# What else could have been done for better result-
To investigate this problem fully it would make sense to implement a more in depth algorithm as it is an iterative process which could be framed as an optimisation problem.
A model found to have very high accuracy on the training and testing data was with 2 sequential layers of 64 3x3 convolution and 2x2 pooling. This had mean training and testing accuracy of 99.8% and 98.9% over 3 runs.
