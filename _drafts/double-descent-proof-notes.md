{% include mathjax.html %}


In case of a [linear regression, bias-variance tradeoff](http://www.dam.brown.edu/people/geman/Homepage/Essays%20and%20ideas%20about%20neurobiology/bias-variance.pdf) can be expressed via an equation.

\\( E_{x \in X_{test}} \lbrack (y - f(x, D))^2 |x, D \rbrack = \\)
\\( E[(y - E[y|x])^2 | x] + E[(f(x, D) - E[y|x])^2 | x, D] \\)

Where first element represents the variance and second the bias.


https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff












You can calculate variance term for the linear model for a special case of linear regression, for which the bias term is zero.
Let's assume

- training data \\( D = \lbrace (x_1, y_1), ..., (x_n, y_n) \rbrace \\),
- an dimension of the training data: \\( p \\),
- identity matrix of dimension \\( p \\): \\( I_p \\),
- train set \\( x \\) is normally distributed without covariance: \\( x \in N(0, I_p \sigma_{x-train}}) \\),
- train set \\( y \\) is normally distributed, single dimensional: \\( y(x) \in N(Ey, \sigma_y) \\).
- test set \\( x_t \in N(0, I_p \sigma_{x-test}) \\),\\)

Then if, one follows ["Deriving the final identity" in "Linear Regression and the  Bias Variance Tradeoff"](https://people.eecs.berkeley.edu/~jegonzal/assets/slides/linear_regression.pdf), without making an mistake at the end, I hope, one gets variance term:

\\(
E(Ef - f)^2 \approx \frac{ \sigma_y^2 (1 + p \sigma_{x-test}^2) }{ \sigma_{x-train} n}
\\).

So, we increase variance if we:
- increase the problem dimension \\( p \\)
- increase the training label variance \\( \sigma_y \\)
- decrease the training sample variance \\( \sigma_{x_{train}} \\) - poor training sample
- increase the test sample variance \\( \sigma_{x_{test}} \\) - unfamiliar test data

