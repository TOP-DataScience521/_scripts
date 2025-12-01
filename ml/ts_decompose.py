from matplotlib import pyplot as plt
from pandas import Series
from statsmodels.tsa.seasonal import seasonal_decompose, STL

from ts_init import births, passengers, online, script_dir


# time_series = trend + seasonal + residuals


def ts_decompose(time_series: Series, period: int):
    # вычисление тренда скользящим средним
    trend = Series([], name=f'{time_series.name or "ts"}_trend_ma_{period}')
    for i in range(0, len(time_series)-period+1):
        dt_index = time_series.index[i+period//2]
        trend.loc[dt_index] = time_series.iloc[i:i+period].mean()
    # вычисление сезонности посредством вычитания тренда и усреднения по периодам
    seasonal = time_series - trend
    for i in range(len(time_series.index)-period):
        subgroup = seasonal[i::period]
        seasonal.iloc[i] = subgroup.mean()
    seasonal.name = f'{time_series.name or "ts"}_seasonal_{period}'
    # вычисление остатков посредством вычитания тренда и сезонгости
    residuals = time_series - trend - seasonal
    residuals.name = f'{time_series.name or "ts"}_residuals'
    
    return trend, seasonal, residuals


data = (
    (births.iloc[:, 0], {'period': 30}),
    (passengers.iloc[:, 0], {'period': 12}),
    (online.iloc[:, 0], {'period': 24}),
)
for ts, options in data:
    # самостоятельное разложение на компоненты на основе скользящего среднего
    trend, seasonal, residuals = ts_decompose(ts, **options)
    
    fig = plt.figure(figsize=(10, 15))
    axs = fig.subplots(4, 1, sharex=True)
    
    axs[0].plot(ts.index, ts.values)
    axs[1].plot(trend.index, trend.values)
    axs[2].plot(seasonal.index, seasonal.values)
    axs[3].scatter(residuals.index, residuals.values)
    
    bottom, top = axs[0].get_ylim()
    ylim_delta = top - bottom
    for i in range(1, 4):
        bottom = axs[i].get_ylim()[0]
        axs[i].set(ylim=(bottom, bottom+ylim_delta))
    
    fig.savefig(script_dir / f'ts_{ts.name}_decompose.png')
    
    
    # разложение на компоненты на основе скользящего среднего с уточнением сезонности
    decomposed = seasonal_decompose(ts, **options)
    fig = decomposed.plot()
    fig.savefig(script_dir / f'ts_{ts.name}_decompose_statsmodels.png')
    
    
    # разложение на компоненты на основе регрессии
    decomposed = STL(ts, **options).fit()
    fig = decomposed.plot()
    fig.savefig(script_dir / f'ts_{ts.name}_decompose_STL.png')
    
