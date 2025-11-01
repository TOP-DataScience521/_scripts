from pandas import DataFrame

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

groupped_means_diffs = DataFrame({
    'mean_0': mean_0,
    'mean_1': mean_1,
    'diff': abs(mean_0 - mean_1)
}).sort_values(by='diff', ascending=False)

# >>> groupped_means_diffs
#                            mean_0    mean_1      diff
# worst concave points     1.028886 -0.610991  1.639877
# worst perimeter          1.015076 -0.602790  1.617865
# mean concave points      1.006907 -0.597939  1.604846
# worst radius             1.006699 -0.597816  1.604515
# mean perimeter           0.962853 -0.571778  1.534631
# worst area               0.951430 -0.564995  1.516424
# mean radius              0.946507 -0.562072  1.508579
# mean area                0.919222 -0.545869  1.465091
# mean concavity           0.902855 -0.536149  1.439004
# worst concavity          0.855208 -0.507854  1.363062
# mean compactness         0.773427 -0.459290  1.232717
# worst compactness        0.766250 -0.455028  1.221278
# radius error             0.735309 -0.436654  1.171963
# perimeter error          0.721056 -0.428190  1.149246
# area error               0.710807 -0.422104  1.132911
# worst texture            0.592390 -0.351784  0.944174
# worst smoothness         0.546444 -0.324499  0.870943
# worst symmetry           0.539740 -0.320518  0.860258
# mean texture             0.538302 -0.319664  0.857966
# concave points error     0.529041 -0.314164  0.843206
# mean smoothness          0.464886 -0.276066  0.740952
# mean symmetry            0.428503 -0.254461  0.682964
# worst fractal dimension  0.419912 -0.249359  0.669271
# compactness error        0.379884 -0.225589  0.605473
# concavity error          0.328969 -0.195354  0.524324
# fractal dimension error  0.101094 -0.060033  0.161127
# smoothness error        -0.086889  0.051598  0.138486
# mean fractal dimension  -0.016644  0.009884  0.026528
# texture error           -0.010766  0.006393  0.017159
# symmetry error          -0.008456  0.005021  0.013477

