import numpy as np

'''
    @author Dmytro Gnatyk
    Simple Perceptron using Numpy
'''

INPUT_LAYER = 3
HIDDEN_LAYER = 4
OUTPUT_LAYER = 1
L_RATE = 1e-2

# Test Data-Set
test_set = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]]
)

# Validation Data-Set
validation_set = np.array([
    [0],
    [1],
    [1],
    [1]
])

# Weights
input_weights = np.random.rand(INPUT_LAYER, HIDDEN_LAYER)
output_weights = np.random.rand(HIDDEN_LAYER, OUTPUT_LAYER)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class Model:
    def __init__(self):
        self.input_layer = np.zeros(INPUT_LAYER)
        self.hidden_layer = np.zeros(HIDDEN_LAYER)
        self.output_layer = np.zeros(OUTPUT_LAYER)
        self.error = 0

    def forward(self, x):
        self.input_layer = x
        self.hidden_layer = sigmoid(np.dot(self.input_layer, input_weights))
        self.output_layer = sigmoid(np.dot(self.hidden_layer, output_weights))
        return self.output_layer

    def backward(self, y):
        self.error = y - self.output_layer
        output_delta = self.error * sigmoid_derivative(self.output_layer)
        hidden_error = output_delta.dot(output_weights.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer)

        global output_weights
        output_weights += self.hidden_layer.T.dot(output_delta) * L_RATE

        global input_weights
        input_weights += self.input_layer.T.dot(hidden_delta) * L_RATE

    def train_model(self, epochs=10000):
        for epoch in range(epochs):
            for i in range(len(test_set)):
                self.forward(test_set[i])
                self.backward(validation_set[i])

def main():
    perceptron = Model()
    perceptron.train_model(20000)

    # Testing the perceptron
    for i in range(len(test_set)):
        output = perceptron.forward(test_set[i])
        print(f"Input: {test_set[i]}, Predicted Output: {output}, Expected Output: {validation_set[i]}")

if __name__ == "__main__":
    main()
