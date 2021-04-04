import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


def KF_ARMA_generator(a, b, n, mu = 0, sigm=0.5):
    '''function for generation ARMA process'''
    # errors with normal distribution
    # Input:
    # a - list with coefs AR
    # b - list with coefs MA
    # n - out put range size
    # mu - expected value
    # sig - standard deviation of errors
    # Output data:
    # list size n with generated series

    # generate errors
    e = np.random.normal(mu, sigm, n)
    result = []

    for i in range(n):
        y = e[i]
        for j,ta in enumerate(a):
            if (j+1) <= len(result):
                y += result[i-(j+1)]*ta

        for j,tb in enumerate(b):
            if (j+1) <= len(result):
                y += e[i-(j+1)]*(-tb)
                
        result.append(y)

    return result

def KF_ARMA_visualisator(a, b, n, mu = 0, sigm=0.5, lags = 20):
    '''function for generation and representing ARMA process with ACF and PACF'''
    # errors with normal distribution
    # Input:
    # a - list with coefs AR
    # b - list with coefs MA
    # n - out put range size
    # mu - expected value
    # sig - standard deviation of errors
    # Output data:
    # figure with chart
    
    plt.figure(figsize=(15,7))

    y = KF_ARMA_generator(a,b,n,mu,sigm)
    ax = plt.subplot(311)
    plt.plot(list(range(n)), y)

    ax = plt.subplot(312)
    sm.graphics.tsa.plot_acf(y, lags=lags, ax=ax)

    ax = plt.subplot(313)
    sm.graphics.tsa.plot_pacf(y, lags=lags, ax=ax)

    plt.tight_layout()
    plt.show()

#KF_ARMA_visualisator([0.7], [-0.9], 200)