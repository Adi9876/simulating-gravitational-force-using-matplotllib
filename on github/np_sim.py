import numpy as np
import matplotlib.pyplot as plt

m = np.load('masses_5.npy')
s = np.load('positions_5.npy')
u = np.load('velocities_5.npy')

plt.ylim([-10., 10.])
plt.xlim([-10., 10.])
plt.scatter(s[:, 0], s[:, 1])
plt.savefig('0.png')
plt.clf()

t = 1e-4
G = 6.67e-11

# Gravitational Force experienced by particle at r1 due to particle at r2.
def force(r1, r2, m1, m2):
	return - G * m1 * m2 * (r1 - r2) / np.linalg.norm(r1 - r2) ** 3

for i in range(500):
	forces = np.zeros((5, 5, 2))
	for j in range(5):
		for k in range(j + 1, 5):
			forces[j, k] = force(s[j], s[k], m[j], m[k])
			forces[k, j] = -forces[j, k]

	a = np.zeros((5, 2))
	for j in range(5):
		a[j] = np.sum(forces[j], axis=0) / m[j]
	
	del_s = u * t + 0.5 * a * t ** 2
	u = u + a * t
	s = s + del_s

	plt.ylim([-10., 10.])
	plt.xlim([-10., 10.])
	plt.scatter(s[:, 0], s[:, 1])
	plt.savefig(str(i + 1)+'.png')
	plt.clf()
	print (i)
