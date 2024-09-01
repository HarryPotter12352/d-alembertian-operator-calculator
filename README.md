# d'Alembertian operator calculator

In this repository, I provide Python code to compute the d'Alembertian operator and give the $\LaTeX$ code for it, which is the generalised version of the Laplacian $\nabla$.
It is denoted by $\Box$ and given by
$$\Box\psi = \frac{1}{\sqrt{-g}}\partial_{\mu}\left(\sqrt{-g} g^{\mu\nu}\partial_{\nu}\psi\right)$$
where $g^{\mu\nu}$ are the elements of the inverse of the metric tensor, and $g$ is the determinant of the same.
The d'Alembertian operator is usually used in equations such as the Klein-Gordon equation
$$(\Box + m^2)\psi  = 0$$
and the linearised Einstein field equation
$$\Box h_{\mu\nu} = -16\pi T_{\mu\nu}$$
All the equations above are in natural units.

In my example, I use the FLRW metric, given by
$$ds^2 = -dt^2 + a^2(t) \left[\frac{dr^2}{1-k^2} + r^2(d\theta^2 + \sin^2 \theta d\phi^2)\right] $$