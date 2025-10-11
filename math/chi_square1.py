from matplotlib import pyplot as plt
from numpy import arange, array, linspace
from numpy.random import default_rng
from scipy.stats import binom, chi2

import stat1

binomial_params = {'n': 50, 'p': 0.9}
general = binom.rvs(size=10**7, **binomial_params)

sample_len = 500
sample = default_rng().choice(general, sample_len)

# >>> sample.min(), sample.max()
# (np.int64(39), np.int64(50))

x_intervals = [(39, 41), (41, 43), (43, 45), (45, 47), (47, 49), (49, 51)]

x_intervals_means = array([sum(interval)/2 for interval in x_intervals])
m_intervals = array(stat1.sample_to_interval(sample, x_intervals))
w_intervals = m_intervals / sample_len

# >>> print(array([x_intervals_means, m_intervals], dtype=int))
# [[40 42 44 46 48 50]
#  [ 4 28 54 74 35  5]]

p_intervals = array([
    binom.cdf(x2, **binomial_params) - binom.cdf(x1, **binomial_params)
    for x1, x2 in x_intervals
])

chi_square_obs = sum(
    sample_len * (w_intervals[i] - p_intervals[i])**2 / p_intervals[i]
    for i in range(len(x_intervals))
)

# число степеней свободы
ddof = len(x_intervals) - 0 - 1
# граница критической области
chi_square_crit = chi2.isf(0.01, df=ddof)


H0: bool = chi_square_obs < chi_square_crit
if H0:
    ...
else:
    ...


fig = plt.figure(figsize=(6, 6))
axs = fig.subplots()

axs.bar(x_intervals_means, w_intervals, width=2)

pmf_x = arange(sample.min(), sample.max()+1)
pmf_y = binom.pmf(pmf_x, **binomial_params)
axs.plot(pmf_x, pmf_y, color='#f21010')

fig.show()

