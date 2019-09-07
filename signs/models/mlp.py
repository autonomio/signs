from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Embedding
from kerasplotlib import TrainingLog


def mlp(x,
        y,
        vocab_size,
        vector_dims,
        embedding_matrix,
        epochs=50,
        layers=0,
        dropout=0,
        batch_size=10,
        inner_neurons=None,
        loss='binary_crossentropy',
        x_test=None,
        y_test=None):

    '''Trains a basic MLP style neural network
    with embedding_matrix from Embeds().layer()'''

    model = Sequential()
    model.add(Embedding(vocab_size,
              vector_dims,
              weights=[embedding_matrix],
              input_length=x.shape[1],
              trainable=False))
    model.add(Flatten())
    model.add(Dropout(dropout))

    # add layers
    if layers > 0:
        for i in range(layers):
            model.add(Dense(inner_neurons))
            model.add(Dropout(dropout))

    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss=loss, metrics=['acc'])
    model.fit(x, y,
              epochs=epochs,
              batch_size=batch_size,
              verbose=0,
              validation_split=.3,
              callbacks=[TrainingLog()])
    # loss, accuracy = model.evaluate(x, y, verbose=0)

    return model
