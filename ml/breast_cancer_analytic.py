from pandas import DataFrame, Series

from breast_cancer_init import data, target


# >>> data.describe().round(2).transpose()
#                          count    mean     std     min     25%     50%      75%      max
# mean radius              569.0   14.13    3.52    6.98   11.70   13.37    15.78    28.11
# mean texture             569.0   19.29    4.30    9.71   16.17   18.84    21.80    39.28
# mean perimeter           569.0   91.97   24.30   43.79   75.17   86.24   104.10   188.50
# mean area                569.0  654.89  351.91  143.50  420.30  551.10   782.70  2501.00
# mean smoothness          569.0    0.10    0.01    0.05    0.09    0.10     0.11     0.16
# mean compactness         569.0    0.10    0.05    0.02    0.06    0.09     0.13     0.35
# mean concavity           569.0    0.09    0.08    0.00    0.03    0.06     0.13     0.43
# mean concave points      569.0    0.05    0.04    0.00    0.02    0.03     0.07     0.20
# mean symmetry            569.0    0.18    0.03    0.11    0.16    0.18     0.20     0.30
# mean fractal dimension   569.0    0.06    0.01    0.05    0.06    0.06     0.07     0.10
# radius error             569.0    0.41    0.28    0.11    0.23    0.32     0.48     2.87
# texture error            569.0    1.22    0.55    0.36    0.83    1.11     1.47     4.88
# perimeter error          569.0    2.87    2.02    0.76    1.61    2.29     3.36    21.98
# area error               569.0   40.34   45.49    6.80   17.85   24.53    45.19   542.20
# smoothness error         569.0    0.01    0.00    0.00    0.01    0.01     0.01     0.03
# compactness error        569.0    0.03    0.02    0.00    0.01    0.02     0.03     0.14
# concavity error          569.0    0.03    0.03    0.00    0.02    0.03     0.04     0.40
# concave points error     569.0    0.01    0.01    0.00    0.01    0.01     0.01     0.05
# symmetry error           569.0    0.02    0.01    0.01    0.02    0.02     0.02     0.08
# fractal dimension error  569.0    0.00    0.00    0.00    0.00    0.00     0.00     0.03
# worst radius             569.0   16.27    4.83    7.93   13.01   14.97    18.79    36.04
# worst texture            569.0   25.68    6.15   12.02   21.08   25.41    29.72    49.54
# worst perimeter          569.0  107.26   33.60   50.41   84.11   97.66   125.40   251.20
# worst area               569.0  880.58  569.36  185.20  515.30  686.50  1084.00  4254.00
# worst smoothness         569.0    0.13    0.02    0.07    0.12    0.13     0.15     0.22
# worst compactness        569.0    0.25    0.16    0.03    0.15    0.21     0.34     1.06
# worst concavity          569.0    0.27    0.21    0.00    0.11    0.23     0.38     1.25
# worst concave points     569.0    0.11    0.07    0.00    0.06    0.10     0.16     0.29
# worst symmetry           569.0    0.29    0.06    0.16    0.25    0.28     0.32     0.66
# worst fractal dimension  569.0    0.08    0.02    0.06    0.07    0.08     0.09     0.21


data_norm = (data - data.describe().loc['mean', :]) / data.describe().loc['std', :]

mean_0 = data_norm[target == 0].mean()
mean_1 = data_norm[target == 1].mean()

corr_kendall = Series([
    target.corr(data[var], method='kendall')
    for var in data.columns
], name='tau_corr', index=data.columns)

vars_by_effect_on_target = DataFrame({
    # 'mean_0': mean_0,
    # 'mean_1': mean_1,
    'diff': abs(mean_0 - mean_1).round(2),
    'tau_corr': abs(corr_kendall).round(3),
})

# >>> vars_by_effect_on_target.sort_values(by='diff', ascending=False)
#                          diff  tau_corr
# worst concave points     1.64     0.639
# worst perimeter          1.62     0.651
# mean concave points      1.60     0.636
# worst radius             1.60     0.644
# mean perimeter           1.53     0.612
# worst area               1.52     0.643
# mean radius              1.51     0.599
# mean area                1.47     0.600
# mean concavity           1.44     0.599
# worst concavity          1.36     0.577
# mean compactness         1.23     0.498
# worst compactness        1.22     0.496
# radius error             1.17     0.504
# perimeter error          1.15     0.515
# area error               1.13     0.584
# worst texture            0.94     0.390
# worst smoothness         0.87     0.348
# worst symmetry           0.86     0.324
# mean texture             0.86     0.378
# concave points error     0.84     0.400
# mean smoothness          0.74     0.304
# mean symmetry            0.68     0.272
# worst fractal dimension  0.67     0.255
# compactness error        0.61     0.311
# concavity error          0.52     0.384
# fractal dimension error  0.16     0.165
# smoothness error         0.14     0.043
# mean fractal dimension   0.03     0.021
# texture error            0.02     0.016
# symmetry error           0.01     0.075

# >>> vars_by_effect_on_target.sort_values(by='tau_corr', ascending=False)
#                          diff  tau_corr
# worst perimeter          1.62     0.651
# worst radius             1.60     0.644
# worst area               1.52     0.643
# worst concave points     1.64     0.639
# mean concave points      1.60     0.636
# mean perimeter           1.53     0.612
# mean area                1.47     0.600
# mean radius              1.51     0.599
# mean concavity           1.44     0.599
# area error               1.13     0.584
# worst concavity          1.36     0.577
# perimeter error          1.15     0.515
# radius error             1.17     0.504
# mean compactness         1.23     0.498
# worst compactness        1.22     0.496
# concave points error     0.84     0.400
# worst texture            0.94     0.390
# concavity error          0.52     0.384
# mean texture             0.86     0.378
# worst smoothness         0.87     0.348
# worst symmetry           0.86     0.324
# compactness error        0.61     0.311
# mean smoothness          0.74     0.304
# mean symmetry            0.68     0.272
# worst fractal dimension  0.67     0.255
# fractal dimension error  0.16     0.165
# symmetry error           0.01     0.075
# smoothness error         0.14     0.043
# mean fractal dimension   0.03     0.021
# texture error            0.02     0.016

