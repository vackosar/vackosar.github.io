<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


In case of a [linear regression, bias-variance tradeoff](http://www.dam.brown.edu/people/geman/Homepage/Essays%20and%20ideas%20about%20neurobiology/bias-variance.pdf) can be expressed via an equation.

\\( E_{x \in X_{test}} \lbrack (y - f(x, D))^2 |x, D \rbrack = \\)
\\( E[(y - E[y|x])^2 | x] + E[(f(x, D) - E[y|x])^2 | x, D] \\)

Where first element represents the variance and second the bias.


https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff

# Bias-Variance Trade-off for L2 Norm
- A prediction function \\( f \\) was fitted on the training data \\( D = \lbrace (x_1, y_1), (x_2, y_2), ..., (x_n, y_n) \rbrace \\) .
- The test sample has noisy label \\( y = Ey + \epsilon \\), but the mean label \\( Ey \\) represents the true value.
- Because the test label noise is independent of the training data, the fitted function has zero covariance with the test label noise: \\( E \epsilon f = 0 \\).

Then the  test error can be written as in following:
Then the expected L2 test error \\ (E(y-f)^2 \\) below conditioned on a test sample \\( x \\) over all draws of train samples D and label noise.

\\( E(y-f)^2 = E(y - Ey + Ey - f)^2 \\)
\\( = \sigma^2 + E (Ey - f)^2 + 2 E \epsilon (Ey - f) \\)
\\( = \sigma^2 + E (Ey - f)^2 \\)
\\( = (Ey - Ef)^2 + E(Ef - f)^2 \\).
