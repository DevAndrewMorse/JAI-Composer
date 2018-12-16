# Tutorial 2: 
# Simple Graph Demo
# This is a simple graph demo to help explain the components of the TensorFlow framework
# Graph - A set of connected nodes
# NOTE: The following example will use two layers of nodes, an input layer and an output node
# Example: 
# 
# N1 ->  1  Some Operation (add)
#           N3 ->  Ouput (3)
# N2 ->  2


# Program was tested and run using Jupyter Notebooks a long w/ TensorFlow 1.3.0
# For accurate results run one class per line using Jupyter Notebooks and Anaconda Python 3

# Operation classes
class Operation():

	def __init__(self, input_nodes = []):

		self.input_nodes = input_nodes
		self.output_nodes = []

		# Move operation results to output nodes
		for node in input_nodes:
			node.output_nodes.append(self)

		_default_graph.operations.append(self)

	def compute(self):
		pass

# Subclass operations: Following TF naming convention w/ class names (lowercase).
class add(Operation):

	def __init__(self, x, y):

		super().__init__([x, y])

	def compute(self, x_var, y_var):
		self.inputs = [x_var, y_var]
		return x_var + y_var

class multiply(Operation):

	def __init__(self, x, y):

		super().__init__([x, y])

	def compute(self, x_var, y_var):
		self.inputs = [x_var, y_var]
		return x_var * y_var

# Matrix multiplication		
class matmul(Operation):

	def __init__(self, x, y):

		super().__init__([x, y])

	def compute(self, x_var, y_var):
		self.inputs = [x_var, y_var]
		return x_var.dot(y_var)
	

# Placeholder - An "empty" node that needs a value to be provided to compute output
class Placeholder():

	def __init__(self):

		self.output_nodes = []

		_default_graph.placeholders.append(self)

# Variable - Changeable parameters of the graph (e.g. the weights)
class Variable():

	def __init__(self, initial_value = None):

		self.value = initial_value
		self.output_nodes = []

		_default_graph.variables.append(self)

# Graph - Keeps track in the form of a list
class Graph():

	def __init__(self):

		self.operations = []
		self.placeholders = []
		self.variables = []

	def set_as_default(self):

		global _default_graph
		_default_graph = self


# Setup the following:
# F(x): z = Ax + b
# A = 10 
# b = 1 : Our bias input
# z = 10x + 1 : Where x becomes the placeholder

# Create graph object
g = Graph()

g.set_as_default()
A = Variable(10)
b = Variable(1) 

x = Placeholder()

# Carry out the f(x) operations:
y = multiply(A,x)
z = add(y,b)


# Postorder traversal is used to make sure the nodes are executed in the correct order
def traverse_postorder(operation):

	nodes_postorder = []
	def recurse(node):
		if isinstance(node, Operation):
			for input_node in node.input_nodes:
				recurse(input_node)
		nodes_postorder.append(node)

	recurse(operation)
	return nodes_postorder

# Session - Executes the graph + operations
class Session():

	# Feed dictionary - Dictionary that maps placeholders to input values (used in TensorFlow)
	def run(self, operation, feed_dict ={}):

		nodes_postorder = traverse_postorder(operation)

		for node in nodes_postorder:

			if type(node) == Placeholder:

				node.output = feed_dict[node]

			elif type(node) == Variable:

				node.output = node.value

			else:
				# OPERATION
				node.inputs = [input_node.output for input_node in node.input_nodes]

				# * - Used when we don't know the number of node inputs being passed through
				node.output = node.compute(*node.inputs)


			if type(node.output) == list:
				node.output = np.array(node.output)


		return operation.output

# TESTING OUTPUT(S):
# Execute example session for testing:
sess = Session()

# x = 10
test = sess.run(operation = z, feed_dict = {x : 10})

# F(x): z = 10x + 1 
print(test)

# Classification - Activation f(x)
class Sigmoid(Operation):

	def __init__(self, z):

		super().__init__([z])

	def compute(self, z_val):
		return 1 / (1 + np.exp(-z_val))

from sklearn.datasets import make_blobs

data = make_blobs(n_samples = 50, n_features = 2, centers = 2, random_state = 75)

# Features and it's labels printed out as tuple
print(data)
type(data)
# Labels output:
data[1]

features = data[0]
labels = data[1]

# Scatter plot ouput of features x-axis vs y-axis
plt.scatter(features[:, 0], features[:, 1], c = labels)

# Seperator line for features
# Line determines threshold for classification
x = np.linspace(0,11,10)
y = -x + 5
plt.scatter(features[:,0], features[:,1], c =labels)
plt.plot(x,y)

# Threshold for classifying features for the perceptron
# A = 1x1 matrix
# A * f - 5 = 0

# Testing classification outputs for perceptron using seperator line as threshold
np.array([1,1]).dot(np.array([[8], [10]])) - 5
np.array([1,1]).dot(np.array([[2], [-10]])) - 5

# Example session for classification using sigmoid f(x)
g = Graph()
g.set_as_default()
x = Placeholder()
w = Variable([1,1])
b = Variable(-5)
z = add(matmul(w,x), b)

a = Sigmoid(z)

sess = Session()
sess.run(operation = a, feed_dict = {x:[8,10]})
