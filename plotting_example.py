from plotting_library import *
plt.plot( np.linspace(-10, 10, 1000),  (np.linspace(-10, 10, 1000)**3)/10)
plt.plot( np.linspace(-10, 10, 1000),  -1*(np.linspace(-10, 10, 1000)**3)/10)
plt.show()
