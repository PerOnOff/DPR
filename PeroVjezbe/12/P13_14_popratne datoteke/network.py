# network.py
from __future__ import annotations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid
T = TypeVar('T') # oznaka izlaznog tipa (output type) koji predstavlja NN
class Network:
    def __init__(self,
                 layer_structure: List[int],
                 learning_rate: float,
                 activation_function: Callable[[float], float] = sigmoid,
                 derivative_activation_function: Callable[[float], float] = derivative_sigmoid
                 ) -> None:
        if len(layer_structure) < 3:
            raise ValueError("Error: Mreža treba imati najmanje 3 sloja (1 input, 1 hidden, 1 output)")
        self.layers: List[Layer] = []
        # input layer
        input_layer: Layer = Layer(None, layer_structure[0], learning_rate, activation_function, derivative_activation_function)
        self.layers.append(input_layer)
        # hidden layers and output layer
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate, activation_function, derivative_activation_function)
            self.layers.append(next_layer)
    # Input podatke procesiramo u prvi sloj, potom output iz prvog sloja
    # kao input u drugi sloj, iz drugog u treći itd.
    def outputs(self,
                input: List[float]
                ) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)
    # Promjena u neuronu je bazirana na greški outputa i očekivane vrijednosti
    def backpropagate(self,
                      expected: List[float]
                      ) -> None:
        # izračunamo delta vrijednost za output layer neurone
        last_layer: int = len(self.layers) - 1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        # izračunamo delta za hidden layer u reverse/obratnom slijedu
        for l in range(last_layer - 1, 0, -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])
    # backpropagate() ne mijenja težine
    # ova funkcija koristi delte iz backpropagate() za
    # promjene težina
    def update_weights(self) -> None:
        for layer in self.layers[1:]: # skip input layer
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + (neuron.learning_rate * (layer.previous_layer.output_cache[w]) * neuron.delta)

    # train() koristi rezultate iz outputs() run nad više inputa i usporedbi
    # u odnosu na očekivane za feed backpropagate() i update_weights()
    def train(self,
              inputs: List[List[float]],
              expecteds: List[List[float]]
              ) -> None:
        for location, xs in enumerate(inputs):
            ys: List[float] = expecteds[location]
            outs: List[float] = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()

    # za opći rezultat koji zahtijeva klasifikacija ova funkcija vraća
    # broj ispravnih pokušaja i postotak u odnosu na ukupan broj
    def validate(self,
                 inputs: List[List[float]],
                 expecteds: List[T],
                 interpret_output: Callable[[List[float]], T]
                 ) -> Tuple[int, int, float]:
        correct: int = 0
        for input, expected in zip(inputs, expecteds):
            result: T = interpret_output(self.outputs(input))
            if result == expected:
                correct += 1
        percentage: float = correct / len(inputs)
        return correct, len(inputs), percentage

