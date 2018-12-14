# The following is a quick tutorial dealing with TensorFlow basic commands
# NOTE: Code was tested using Jupyter notebooks using TensorFlow 1.3.0
import tensorflow as tf

# Print version of TF
# Version 1.3.0 was used to run the following code
print(tf.__version__)

#___________________Performing "Hello World"___________________________

hello = tf.constant("Hello ")
world = tf.constant("World")

# The type is actually a tensor object 
# Tensors are n-dimensional arrays
type(hello)

# Parameters of the tensor are given by
print(hello)

# To print in bytes literal - b'
with tf.Session() as sess:
	result1 = sess.run(hello+world) # Concat

# Print Hello World
print(result1)

# __________________Performing simple addition_________________________

# Initialize two constant tensor types 
a = tf.constant(10)
b = tf.constant(20)

# Do the addition a + b and print the sum
with tf.Session() as sess:
	result2 = sess.run(a + b)

print(result2)

#___________________Matrix Operations__________________________________

const = tf.constant(10)

# Fill 4x4 matrix w/ 10s
fill_mat = tf.fill((4,4),10)

# Fill 4x4 matrix with 0s
myzeros = tf.zeros((4,4))

# Fill 4x4 matrix with 1s
myones = tf.ones((4,4))

# Random normal distribution of 4x4 
myrandn = tf.random_normal((4,4), mean = 0, stddev = 1.0)

# Random discrete uniform distribution of 4x4 
myrandu = tf.random_uniform((4,4), minval = 0, maxval = 1)

# Create list of previous operations
my_ops = [const, fill_mat, myzeros, myones, myrandn, myrandu]

# Declare session
sess = tf.InteractiveSession()

# Run session of operations
for op in my_ops:
	print(sess.run(op))
	print('\n')

# NOTE: All operations should be printed on the live Jupyter notebook

# MATRIX MULTIPLICATION:

# Create new 2x2 matrix through a nested list
a = tf.constant([ [1,2],
				  [3,4] ])

# Get demensions of a-matrix
a.get_shape()

# Create second 2x1 matrix
b = tf.constant([ [10], [100]])

# Get demensions of b-matrix
b.get_shape()

# Multiply matrices: Keep in mind the simple linear algebra rules:
result3 = tf.matmul(a,b)

# Get result
sess.run(result3)
