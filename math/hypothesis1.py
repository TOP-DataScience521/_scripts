from numpy import array, sort


class RCrit:
    """
    Класс для проверки принадлежности элементов ряда к нормально распределённой генеральной совокупности.
    """
    def __init__(self, data, significance, outliers=1, crit_source='std'):
        self.data = array(data)
        self.n = len(data)
        self.significance = significance
        self._iterations = outliers
        if crit_source == 'std':
            self.crit = float(input('граница крититческой области r-критерия: '))
        else:
            ...
        self.H0: dict[float, bool] = {}
    
    def __bool__(self):
        return bool(self.H0)
    
    def __repr__(self):
        try:
            el1, el2, el3 = self.data[:3]
        except ValueError:
            el1, el2, el3 = '', '', ''
        return f'<RCrit: [{el1} {el2} {el3} ...], significance={self.significance:.3f}>'
    
    def _observed_criteria(self, element):
        return abs(self.data.mean() - element) / (self.data.var() * ((self.n-1)/self.n)**0.5)
    
    def check(self, element):
        r_obs = self._observed_criteria(element)
        H0 = r_obs < self.crit
        self.H0[element] = H0
        return H0, r_obs
    
    def check_all_outliers(self):
        print(
            f'\nпроверка гипотезы о приндлежности значений из ряда N к генеральной совокупности',
            f'уровень значимости: {self.significance:.2f}',
            f'число степеней свободы: {self.n - 2}',
            sep='\n'
        )
        data = sort(self.data)
        for _ in range(self._iterations):
            for i in (0, -1):
                element = data[i]
                H0, r_obs = self.check(element)
                print(
                    f'\nзначение: {element}',
                    f'{r_obs:.3f} {"<" if H0 else ">="} {self.crit:.3f}',
                    f'{element} {"" if H0 else "не "}принадлежит генеральной совокупности ({"не " if H0 else ""}является промахом)',
                    sep='\n'
                )
            data = data[1:-1]
        return self.H0


if __name__ == '__main__':
    
    α = 0.05
    
    N = RCrit([227, 258, 271, 288, 292, 301, 322, 331, 372, 413], α)
    R = RCrit([371, 379, 388, 396, 395, 406, 460, 408, 409, 411, 419, 424, 441, 397], α, 2)

