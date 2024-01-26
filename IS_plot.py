import matplotlib.pyplot as plt
import numpy as np
   

Ns = (1021, 2053, 4099, 8191, 16381, 32771, 65537, 131071, 262147,
	524287, 1048573)
MC_std = np.load('./MC_std.npy')
RQMC_std = np.load('./RQMC_std.npy')
print(RQMC_std,MC_std)
Ns = Ns[:6] + Ns[7:]
MC_std1 = np.zeros(len(Ns))
MC_std1[:6] = MC_std[:6]
MC_std1[6:] = MC_std[7:]
RQMC_std1 = np.zeros(len(Ns))
RQMC_std1[:6] = RQMC_std[:6]
RQMC_std1[6:] = RQMC_std[7:]

fig, ax = plt.subplots()

ax.plot(np.log2(Ns), np.log10(MC_std1), label='MC')
ax.plot(np.log2(Ns), np.log10(RQMC_std1), label='RQMC')

# MC reference line
k = - np.log10(2) / 2
b = np.log10(MC_std1[0]) - k*np.log2(Ns[0])
ax.plot(np.log2(Ns), k*np.log2(Ns)+b, label='-1/2')

# RQMC reference line
k = - np.log10(2)
b = np.log10(RQMC_std1[0]) - k*np.log2(Ns[0])
ax.plot(np.log2(Ns), k*np.log2(Ns)+b, label='-1')

ax.legend()

fig.savefig('IS_std_plot.png')

plt.close(fig)
