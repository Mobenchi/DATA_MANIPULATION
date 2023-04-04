import numpy as np 

np.random.seed(0)

X = [[0.5, -0.1, 6, 2.5],
     [0.8, 4.2, -2.1, -0.9],
     [1.1, -3.7, 5.2, 7]]

class layer_func:

    def __init__(self, n_inputs, n_neurons):

        #making weights and biases for each neuron based on the paramters given to it: 
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):

        #doing the basic function of the neuro links based on the data paramters (inputs) giving to it:
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = layer_func(4, 5)
layer2 = layer_func(5, 4)
layer3 = layer_func(4, 2)

layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)
print(layer3.output)

