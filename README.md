# ARMA_generator
Generation and visualisation of ARMA processes
convenient for ARMA process classification - you can see how ACF and PACF look like for the given parameters
contains two functions 
```KF_ARMA_generator(a, b, n, mu = 0, sigm=0.5)``` - generates series with selected parameters
```KF_ARMA_visualisator(a, b, n, mu = 0, sigm=0.5)``` - plot series, ACF, PACF
where   a - list of AR coefficients
        b - list of MA coefficients
        n - the size of the sample generated
        mu and sigm - parameters of normal distribution