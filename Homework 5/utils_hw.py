# This is a set of utilities to run the NN excersis in ISTA 421, Introduction to ML
# By Leon F. Palafox, December, 2014

from __future__ import division
import numpy as np
import math


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


def initialize(hidden_size, visible_size):
    # choose weights uniformly from the interval [-r, r] following what we saw in class

    ### YOUR CODE HERE ###
    r = math.sqrt(6 / (hidden_size + visible_size + 1))
    w1 = np.random.rand(hidden_size, visible_size) * 2 * r - r
    w1 = np.reshape(w1, (1, hidden_size * visible_size))[0]

    w2 = np.random.rand(visible_size, hidden_size) * 2 * r - r
    w2 = np.reshape(w2, (1, hidden_size * visible_size))[0]

    b1 = np.zeros(hidden_size)
    b2 = np.zeros(visible_size)

    theta = np.concatenate((w1, w2, b1, b2))

    return theta


def sparse_autoencoder_cost(theta, visible_size, hidden_size,
                            lambda_, data):
    # The input theta is a vector (because minFunc expects the parameters to be a vector).
    # We first convert theta to the (W1, W2, b1, b2) matrix/vector format, so that this
    # follows the notation convention of the lecture notes.

    ### YOUR CODE HERE ###
    w1EndPoint = hidden_size * visible_size
    w2EndPoint = w1EndPoint * 2
    b1EndPoint = w2EndPoint + hidden_size

    w1 = theta[:w1EndPoint]
    w1 = np.reshape(w1, (hidden_size, visible_size))
    w2 = theta[w1EndPoint:w2EndPoint]
    w2 = np.reshape(w2, (visible_size, hidden_size))
    b1 = theta[w2EndPoint:b1EndPoint]
    b2 = theta[b1EndPoint:]

    z2 = np.dot(w1, data)
    b1ShapedLikez2 = np.reshape([b1] * z2.shape[1], (hidden_size, z2.shape[1]))
    z2 = z2 + b1ShapedLikez2

    a2 = sigmoid(z2)

    z3 = np.dot(w2, a2)
    b2ShapedLikez3 = np.reshape([b2] * z3.shape[1], (visible_size, z3.shape[1]))
    z3 = z3 + b2ShapedLikez3

    a3 = sigmoid(z3)
    yHat = a3

    y = what
    J = (1 / 2) * np.sum(np.power((y - a3), 2))

    # do gradients now
    w1gradient = np.zeros(w1)
    w2gradient = np.zeros(w2)
    b1gradient = np.zeros(b1)
    b2gradient = np.zeros(b2)

    delta3 = np.multiply(-(y - yHat), sigmoid_prime(z3))
    dJdw2 = np.dot(np.transpose(a2), delta3)

    # return cost, grad


# visible_size: the number of input units (probably 64)
# hidden_size: the number of hidden units (probably 25)
# lambda_: weight decay parameter
# sparsity_param: The desired average activation for the hidden units (denoted in the lecture
#                            notes by the greek alphabet rho, which looks like a lower-case "p").
# beta: weight of sparsity penalty term
# data: Our 64x10000 matrix containing the training data.  So, data(:,i) is the i-th training example.
#
# The input theta is a vector (because minFunc expects the parameters to be a vector).
# We first convert theta to the (W1, W2, b1, b2) matrix/vector format, so that this
# follows the notation convention of the lecture notes.
# Returns: (cost,gradient) tuple


def sparse_autoencoder(theta, hidden_size, visible_size, data):
    """
    :param theta: trained weights from the autoencoder
    :param hidden_size: the number of hidden units (probably 25)
    :param visible_size: the number of input units (probably 64)
    :param data: Our matrix containing the training data as columns.  So, data(:,i) is the i-th training example.
    """

    # We first convert theta to the (W1, W2, b1, b2) matrix/vector format, so that this
    # follows the notation convention of the lecture notes.
    W1 = theta[0:hidden_size * visible_size].reshape(hidden_size, visible_size)
    b1 = theta[2 * hidden_size * visible_size:2 * hidden_size * visible_size + hidden_size]

    # Number of training examples
    m = data.shape[1]

    # Forward propagation
    z2 = W1.dot(data) + np.tile(b1, (m, 1)).transpose()
    a2 = sigmoid(z2)
    return a2
