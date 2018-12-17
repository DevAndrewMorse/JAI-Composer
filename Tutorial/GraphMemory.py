# Andrew Morse
# Tutorial 3:
# This is a brief tutorial on handling graphs and their respective memory addresses
# This is important for the sake of properly managing multiple graphs during implementation
# NOTE: Tested using Anaconda Python 3 and Jupyter Notebooks

import tensorflow as tf

# Create graph (TensorFlow will do this automatically by default)
n1 = tf.constant(1)
n2 = tf.constant(2)

n3 = n1 + n2

# Run the session 
with tf.Session() as sess:
	result = sess.run(n3)

# Prints expected byte literal result
print(result)

# Is still the type tensor, and prints it's parameters
print(n3)

# Prints the graph object's memory address 
print(tf.get_default_graph())

# How to create a new graph
g = tf.Graph()

# Print out address information of the newly created graph
print(g)

# Initalize the first graph for clarity
graph_one = tf.get_default_graph()

# Make sure address matches original default graph
print(graph_one)

# Initalize a second graph for clarity
graph_two = tf.Graph()

# Print out the address of the second graph for reference
print(graph_two)

# Create a boolean check to set the second graph as the default graph
with graph_two.as_default():
	print(graph_two is tf.get_default_graph())
# True

# However, because the original default is still global it reverts back
print(graph_two is tf.get_default_graph())
# False
