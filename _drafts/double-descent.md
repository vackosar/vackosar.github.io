<script src="/javascript/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="/javascript/tex-mml-chtml.js"></script>


In case of a [linear regression, bias-variance tradeoff](http://www.dam.brown.edu/people/geman/Homepage/Essays%20and%20ideas%20about%20neurobiology/bias-variance.pdf) can be expressed via an equation.

\\( E_{x \in X_{test}} \lbrack (y - f(x, D))^2 |x, D \rbrack = \\)
\\( E[(y - E[y|x])^2 | x] + E[(f(x, D) - E[y|x])^2 | x, D] \\)

Where first element represents the variance and second the bias.


https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff

