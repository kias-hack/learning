import math
import code
import random

class Perceptron:
	# Веса [[1,2,3...], [2,3,4...], ...]
	weights = []
	# Смещение bias=0-нету смещения
	bias = 0.01
	# Состояние сети перед активацией нейронов слоя
	state = []
	# Состояние каждого нейрона слоя
	activation_state = []
	# Функция активации [sigmoid|tanh|ReLu|...]
	function_activation = False

	input_values = []

	def tune(self, delta, learning_rate):
		x = self.input_values
		weights = self.weights
		self.weights = [ [ weight - x[i] * learning_rate * delta for weight in weights[i] ] for i in range(len(weights)) ]


	def addMatrix(self, x, y):
		gen_y = range(len(y))
		bias = self.bias

		return [sum([(weight[i] * y[i]) + bias for i in gen_y]) for weight in x]

	def getResult(self, x):
		self.input_values = x

		self.state = self.addMatrix(self.weights, x)
		self.activation_state = [self.function_activation(i) for i in self.state]

		return self.activation_state

	def sigmoid(x):
		return 1/(1+math.pow(math.e, -x))

	def tanh(x):
		return 2/(1+math.pow(math.e, -2*x))

	def ReLu(x):
		return max(0, x)

	def __init__(self, input_shape = 10, output_shape = 5, weight_init_func = random.random, bias = 0.01, function_activation = self.sigmoid):
		self.initWeights(input_shape, output_shape)

		self.bias = bias


	def initWeights(self, size_x, size_y):
		#настраиваем веса
		for i in range(size_x):
			self.weights.push([weight_init_func() for e  in range(size_y)])
	
			

class Sequence:
	layers = []

	def addLayer(self, x):
		self.layers.push(x)

	def train(self, x, y, learning_rate = 0.01, bias = 0.01):
		for i in range(x):


	def predict(self, x):
		prev = self.layers[0].calc(x)

		for layer in range(1, self.layers):
			prev = layer.calc(prev)

		return prev

def sigmoid(x):
	return 1/(1 + math.pow(math.e, -x))

def quad(x):
	return 1 if x >= 0.5 else 0

def dx(x):
	s = sigmoid(x)
	return s * (1 - s)

def calc_err(actual, expected):
	return actual - expected


weight = [0.5, 0.5]
x = [
	[1, 1],
	[0, 1],
	[1, 0],
	[0, 0]
]

y = [0, 1, 1, 0]

def train(input, weight, expected, learning_rate = 0.5):
	output = predict(input, weight, activation = quad)

	w_d = calc_err(output, expected) * dx(output)

	for i in range(len(input)):
		weight[i] = weight[i] - input[i] * w_d * learning_rate

def predict(x, weight, bias = 0.01, activation = sigmoid):
	neuron_var = 0
	for i in range(len(x)):
		neuron_var = neuron_var + weight[i] * x[i] + bias

	return activation(neuron_var)

def epoch(count, x, y, weight, learning_rate = 0.1):
	for i in range(count):
		for i in range(len(x)):
			train(x[i], weight, y[i], learning_rate)

code.interact(local=locals())