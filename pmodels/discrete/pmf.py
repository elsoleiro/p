from pmodels.utils.math import (
    e,
    bang, 
    combination
)

class Bernoulli:
    def __init__(self, index: float) -> None:
        if (index < 0) | (index > 1):
            raise ValueError('Index must be real number between 0 and 1')
        self.index: float = index

    def __repr__(self) -> str:
        return f'Bernoulli({self.index})'

    def p(self, x: int) -> float:
        match x:
            case 0:
                return 1 - self.index
            case 1:
                return self.index
        raise ValueError(
            'does not satisfy x ∈ {0, 1}'
        )

class Binomial:
    def __init__(self, n: int, likelihood: float) -> None:
        self.n: int            = n
        self.likelihood: float = Bernoulli(likelihood)

    def __repr__(self):
        return f'B({self.n}, {self.likelihood.index})'

    def p(self, x: int) -> float:
        if x > self.n:
            raise ValueError('x not satisfy x ∈ {0, 1, 2, ... , n}')

        n_x: int = combination(self.n, x)

        successes: float = 1.0
        for i in range(1, (x + 1), 1):
            successes *= self.likelihood.p(1)

        failures: float = 1.0
        for i in range(1, ((self.n - x) + 1), 1):
            failures *= self.likelihood.p(0)
        
        likelihood: float = n_x * successes * failures
        
        return likelihood

class Geometric:
    '''
    The number of trials from the start of a sequence of independent Bernoulli
    trials up to and _including_ the first success. Let the number of trials
    up to and including the first success be denoted by X. Then:
        X = 1 if the first trial is a success,
        X = 2 if the second trial is a success,
        and so on.

    So,
        P(X=1) = p,
        P(X=2) = (1-p) * p,
        P(X=3) = (1-p) * (1-p) * p,
        and so on.
    
    The probability that first x-1 trials are failures is
        (1-p) * (1-p) * ... * (1-p) = (1-p)^{x-1}

    Hence the probability that that xth trial is the first success is
        P(X=x) = (1-p)^{x-1} * p
    '''
    def __init__(self, likelihood: float) -> None:
        self.likelihood: float = Bernoulli(likelihood)
    
    def __repr__(self) -> str:
        return f'G({self.likelihood.index})'

    def p(self, x: int) -> float:
        failures: int = 1
        for i in range(1, (x + 1) - 1, 1):
            failures *= self.likelihood.p(0)

        success: float    = self.likelihood.index
        likelihood: float = failures * success
        
        return likelihood

    def F(self, x: int) -> float:
        failures = 1
        for i in range(1, (x + 1), 1):
            failures *= self.likelihood.p(0)
        
        likelihood: float = 1 - failures
        
        return likelihood

class Poisson:
    def __init__(self, λ: float) -> None:
        self.λ = λ

    def __repr__(self) -> str:
        return f'Poisson({self.λ})'

    def p(self, x: int) -> float:
        numerator: float = e(self.λ * (-1)) * self.λ**x
        denominator: int = bang(x)

        return numerator/denominator

class Uniform:
    def __init__(self, n: int, m: int) -> None:
        '''
        The range of the random variable X is m, m+1, ... , n-1, n.
        Where m = 1, p(x) = 1/n.
        Where m = 0, p(x) = 1/n+1
        '''
        match m:
            case 1: self.n, self.m = n, m
            case 0: self.n, self.m = n, m
            case _: raise ValueError('m must be 0 or 1')

    def __repr__(self) -> str:
        return f'Uniform({self.n}, {self.m})'

    def p(self, x: int) -> float:
        if x > self.n:
            raise ValueError('x does not satisfy x = m, m+1, ..., n.')
        return 1/(self.n - self.m + 1)
