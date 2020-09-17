<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


In case of a [linear regression, bias-variance tradeoff](http://www.dam.brown.edu/people/geman/Homepage/Essays%20and%20ideas%20about%20neurobiology/bias-variance.pdf) can be expressed via an equation.

\\( E_{x \in X_{test}} \lbrack (y - f(x, D))^2 |x, D \rbrack = \\)
\\( E[(y - E[y|x])^2 | x] + E[(f(x, D) - E[y|x])^2 | x, D] \\)

Where first element represents the variance and second the bias.


https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff


- Expectation below is conditioned on given samples \\( x \\). Later we can do calculate expectation over samples.
- Noisy labels (but Ey is the true value): \\( y = Ey + \epsilon \\)
- Function that was fitted on the training data: \\( f \\)
- Label noise in given training set is independent of the fitted function \\( Cov(\epsilon, f) = 0 \\).
   - When it is correlated when not?
   

\\(

E(y-f)^2 = E(y-Ey + Ey - f)^2 = \sigma^2 + E (Ey - f)^2 + 2 E \epsilon (Ey - f) =
\sigma^2 + E (Ey - f)^2 = (Ey - Ef)^2 + E(Ef - f)^2

\\)