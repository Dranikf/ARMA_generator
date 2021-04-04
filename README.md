# ARMA_generator
Generation and visualisation of ARMA processes
of the kind 

y(t) = a1*y(t-1) + a2*y(t-2) + ... + am(t-m) + e(t) - b1*e(t-1) - b2*e(t-2) - ... - bq*e(t)

convenient for ARMA process classification - you can see how ACF and PACF look like for the given parameters

contains two functions 

```KF_ARMA_generator(a, b, n, mu = 0, sigm=0.5)``` - generates series with selected parameters
```KF_ARMA_visualisator(a, b, n, mu = 0, sigm=0.5, lags = 20)``` - plot series, ACF, PACF

where   a - list of AR coefficients;
        b - list of MA coefficients;
        n - the size of the sample generated;
        mu and sigm - parameters of normal distribution;
        lags - number of lags for ACF and PACF

# Example
For ARMA(2,3) process you can use

```KF_ARMA_visualisator([0.7], [-0.9], 200)```

The result will be like this

<img src = "https://github.com/Dranikf/ARMA_generator/blob/main/examples/Figure_1.png" height = "600">