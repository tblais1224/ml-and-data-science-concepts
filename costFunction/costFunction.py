import numpy as np


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1105
    n = len(x)
    learning_rate = 0.0670032  # tweak as you go to make cost better
    # m 2.000000000006345, b 2.9999999999770908, cost 1.0000080525120793e-22, iteration 1104

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))


# numpy array is good for marice multiplication and faster than normal list
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
