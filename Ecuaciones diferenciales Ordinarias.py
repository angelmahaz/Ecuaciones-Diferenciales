import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def edo(x, y):
    return -2 * y + np.exp(-x)


x_min, x_max = 0, 5


y0 = [1]

sol = solve_ivp(edo, (x_min, x_max), y0, t_eval=np.linspace(x_min, x_max, 100))

plt.plot(sol.t, sol.y[0], label="Solución numérica")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Solución de la ecuación diferencial")
plt.legend()
plt.grid()
plt.show()
