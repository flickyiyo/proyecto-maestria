from tensorflow import keras
from tensorflow.keras.optimizers import Optimizer

class MetaHeuristicOptimizer(Optimizer):
    def __init__(self, learning_rate, name='MHOptimizer', **kwargs):
        super().__init__(name, **kwargs)
        self._set_hyper("learning_rate", kwargs.get('lr', learning_rate))
        self._is_first = True