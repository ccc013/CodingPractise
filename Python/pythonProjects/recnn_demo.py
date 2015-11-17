import theano
import theano.tensor as T
import numpy as np

class LogisticRegression(object):
    def __init__(self, rng,input,n_in,n_out):
        """ Initialize the parameters of the logistic regression

        :type: rng:
        :param: rng: the random number generator

        :type input: theano.tensor.TensorType
        :param input: symbolic variable that describes the input of the
                      architecture (one minibatch)

        :type n_in: int
        :param n_in: number of input units, the dimension of the space in
                     which the datapoints lie

        :type n_out: int
        :param n_out: number of output units, the dimension of the space in
                      which the labels lie

        W and b: theano.tensor.TensorType
        """

        self.W = theano.shared(value = np.asarray(rng.normal(0, 0.05, (n_in, n_out)),
                                                  dtype = theano.config.floatX
                                              ),
                               name = 'logreg_W',
                               borrow = True
                           )
        self.b = theano.shared(value = np.asarray(
            np.zeros((n_out, )),
            dtype = theano.config.floatX
        ),
                               name = 'logreg_b',
                               borrow = True)

        # the probability of labels given the data
        self.p_y_given_x = T.nnet.softmax(T.dot(input, self.W) + self.b)

        self.params = [self.W, self.b]

    def nnl(self, y):
        """negative log-likelihood """
        return T.mean(
            -T.log(self.p_y_given_x[T.arange(y.shape[0]), y])
        )


x = T.imatrix('x')
y = T.ivector('y')
vocab_size = 100
embed_dim = 100
label_n = 5

parent_ids = x[:,0]
children_ids = x[:,1:]

rng = np.random.RandomState(1234)

embedding = theano.shared(
    value = rng.normal(0, 0.05, (vocab_size, embed_dim)),
    name = 'embedding',
    borrow = True,
)


def update_embedding(child_indices, my_index):

    assert child_indices.ndim == 1
    assert my_index.ndim == 0

    return T.set_subtensor(embedding[my_index],
                           T.switch(T.eq(child_indices[0], -1),
                                    embedding[my_index],
                                    (embedding[child_indices[0]] + embedding[child_indices[1]]) / 2
                                )
                       )

final_embedding, updates = theano.scan(
    fn = update_embedding,
    sequences = [children_ids, parent_ids],
)

final_embedding = final_embedding[-1]

update_embedding = theano.function(inputs = [x],
                                   updates = [(embedding, T.set_subtensor(embedding[parent_ids], final_embedding[parent_ids]))])


# the logistic regression layer that predicts the label
logreg_layer = LogisticRegression(rng,
                                  input = final_embedding[parent_ids],
                                  n_in = embed_dim,
                                  n_out = label_n
)

cost = logreg_layer.nnl(y)

params = logreg_layer.params + [embedding]

grads = [T.grad(cost = cost, wrt=p) for p in params]

updates = [(p, p - 0.01 * g)
           for p,g in zip(params, grads)]

train = theano.function(inputs = [x, y],
                        updates = updates)


x_input = np.asarray([[0, -1, -1], [1, -1, -1], [2, -1, -1], [3, 0, 1], [4, 1, 2], [5, 0, 2]], dtype = np.int32)
y_input = np.array([3,4,2,0,2,1], dtype = np.int32)

train(x_input, y_input)