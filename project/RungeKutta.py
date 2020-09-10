import numpy as np
from subtool import SampleFunc


def runge(Efield, Bfield, q, m, t_repetition, x, v):
    for i in range(t_repetition):
        print(type(x[i]))
        E = Efield.VectorField(x[i])
        E = [E["x"],E["y"],E["z"]]
        #E = np.array(E)
        B = Bfield.VectorField(x[i])
        B = [B["x"],B["y"],B["z"]]
        #B = np.array(B)

        v1 = v[i]
        u1 = np.cross(v1,B)
        k1 = q*(E + u1)/m
        l1 = v[i]

        v2 = v1 + k1*dt/2
        u2 = np.cross(v2,B)
        k2 = q*(E + u2)/m
        l2 = v[i] + l1/2

        v3 = v1 + k2*dt/2
        u3 = np.cross(v3,B)
        k3 = q*(E + u3)/m
        l3 = v[i] + l2/2

        v4 = v1 + k3*dt
        u4 = np.cross(v4,B)
        k4 = q*(E + u4)/m
        l4 = v[i] + l3

        v_tem = v[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6
        v = np.append(v, np.array([v_tem]), axis=0)
        x_tem = x[i] + dt*(l1 + 2*l2 + 2*l3 + l4)/6
        x = np.append(x, np.array([x_tem]), axis=0)

    np.save('runge_posi',x)

    return x, v
