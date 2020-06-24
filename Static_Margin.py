print('##### Static Margin Calculator #####')
c = 0.17        # Aerodynamic medium wing rope
xca = 0.050     # Aerodynamic center position
n = 0.85        # Efficiency
clasa = 0.050   # Derivative of Cl x Alfa of the wing 
arasa = 4.00    # Ar of the wing
clpro = 0.050   # Derivate of Cl x Alfa of the elevator
s = 0.3500      # Wing area
sht = 0.1100    # Elevator area
lht = 0.45      # Distance from the CG to the CA of the elevator 
xcg = 0.06      # CG position

clasa = clasa*(1/0.01745) 
clpro = clpro*(1/0.01745)
vh = (lht*sht)/(c*s)
de = (2*clasa)/(3.1415*arasa)
hpn = (xca/c) + (vh*n*clpro)/(clasa)*(1-de)
hpg = xcg/c

me = hpn-hpg

print('Static Margin Value %f' % me)

