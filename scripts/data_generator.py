"""
real word errors

data-generator

@author Daniel Bravo daniel.bravo@um.es
@author Jesica López <jesica.lopez@um.es>
@author José Antonio García-Díaz joseantonio.garcia8@um.es
@author Fernando Molina-Molina <fernando.molina@vocali.net>
@author Francisco García Sánchez <frgarcia@um.es>
"""

import numpy as np
from tensorflow import keras

class DataGenerator (keras.utils.Sequence):

    def __init__ (self, list_IDs, labels, batch_size=256, dim=50, n_classes=10, shuffle=False):
  
        self.dim = dim
        self.batch_size = batch_size
        self.labels = labels
        self.list_IDs = list_IDs
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.on_epoch_end()
 
    def on_epoch_end (self):
        #Updates indexes after each epoch
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)
  
    def __data_generation(self, list_IDs_temp):
  
        X = np.empty((self.batch_size, self.dim))
        y = np.empty((self.batch_size), dtype=int)
        for i, ID in enumerate(list_IDs_temp):
            X[i,] = np.load('./spanishText_10000_15000/' + ID + '.npy')
            y[i] = self.labels[ID]
  
        return X, keras.utils.to_categorical(y, num_classes=self.n_classes)
  
 
    def __len__(self):
        # Denotes the number of batches per epoch
        return int(np.floor(len(self.list_IDs)/self.batch_size))
 
    def __getitem__(self, index):
        # Generate one batch of data
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
  
        #Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]
        
        #Generate data
        X, y = self.__data_generation(list_IDs_temp)
  
        return X, y
   