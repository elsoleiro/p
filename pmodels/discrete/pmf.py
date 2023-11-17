class Bernoulli:
    def __init__(self, index: float):
        if (index < 0) | (index > 1):
            raise ValueError('Index must be real number between 0 and 1')
        self.index = index

    def __repr__(self):
        return f'Bernoulli({self.likelihood.index})'

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
    def __init__(self, n: int, likelihood: float):
        self.n = n
        self.likelihood = Bernoulli(likelihood)

    def __repr__(self):
        return f'B({self.n}, {self.likelihood.index})'

    def bang(self, x: int) -> int:
        res = 1
        for i in range(1, x + 1, 1):
            res *= i
        return int(res)
    
    def combination(self, n: int, x: int) -> int:
        return int(self.bang(n) / (self.bang(x)*self.bang(n - x)))

    def p(self, x: int) -> float:
        if x > self.n:
            raise ValueError('x not satisfy x ∈ {0, 1, 2, ... , n}')

        n_x = self.combination(self.n, x)

        successes = 1
        for i in range(1, (x + 1), 1):
            successes *= self.likelihood.p(1)

        failures = 1
        for i in range(1, ((self.n - x) + 1), 1):
            failures *= self.likelihood.p(0)
        
        likelihood = n_x * successes * failures
        
        '''The total number of successes: {x} \n
        In total number of trials: {self.n} \n
        With with probability: {self.likelihood.index} \n
        Gives likelihood: {likelihood}
        '''
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
    def __init__(self, likelihood: float):
        print(f'Constructing Geometric distribution G({likelihood})')
        self.likelihood = Bernoulli(likelihood)
    
    def __repr__(self):
        return f'G({self.likelihood.index})'

    def p(self, x: int) -> float:

        failures = 1
        for i in range(1, (x + 1) - 1, 1):
            failures *= self.likelihood.p(0)

        success = self.likelihood.index
        
        likelihood = failures * success
        
        '''
        The probability p = {self.likelihood.index} is constant from trial to trial. \n
        The likelihood of success trial {x} is {likelihood}.
        '''
        print(likelihood)
        return likelihood

    def F(self, x: int) -> float:
        
        failures = 1
        for i in range(1, (x + 1), 1):
            failures *= self.likelihood.p(0)
        
        likelihood = 1 - failures
        
        '''
        The probability that we will see at most {x} trials is {result}.
        '''
        return likelihood
