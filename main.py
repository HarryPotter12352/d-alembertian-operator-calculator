import sympy as sp

def compute_d_alembertian_flrw(a, k, x_coords):
    t, r, theta, phi = x_coords
    a_t = sp.Function('a')(t)
    g = sp.Matrix([
        [-1, 0, 0, 0],
        [0, a_t**2 / (1 - k * r**2), 0, 0],
        [0, 0, a_t**2 * r**2, 0],
        [0, 0, 0, a_t**2 * r**2 * sp.sin(theta)**2]
    ])
    det = g.det()
    inv = g.inv()
    psi = sp.Function('psi')(*x_coords)
    d_alembertian = 0
    for mu in range(4):
        for nu in range(4):
            term = inv[mu, nu] * sp.diff(psi, x_coords[nu])            
            partial_term_mu = sp.diff(term, x_coords[mu])            
            d_alembertian += partial_term_mu    
    d_alembertian /= sp.sqrt(-det)    
    return d_alembertian


t, r, theta, phi = sp.symbols('t r theta phi')
x_coords = [t, r, theta, phi]
a = sp.Function('a')(t)
k = sp.Symbol('k', real=True)

d_alembertian_operator = compute_d_alembertian_flrw(a, k, x_coords)

print("Symbolic d'Alembertian operator:")
print(d_alembertian_operator)

latex_code = sp.latex(d_alembertian_operator)
print("\nLaTeX code:")
print(latex_code)
