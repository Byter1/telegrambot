import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import numpy as np

n  = -3 # регулирует диапозон значений x для построения графика
func = 'tan(x)' # график функции
final_result_y = [] # конечные значения Y для передачи в конструктор графиков

x = sp.Symbol('x')
expr = parse_expr(func) # парсится функция для последующего eval-type использования
print('expr:', expr)
res = []
# построение значений y c zoo и комлексными значения
for i in np.arange(-n, n+1, 0.01):
    result = expr.subs({'x': i}).evalf()
    res += [result]

# Исключение zoo, комплексных значений и проч
for k in res:
    try: s = float(k)
    except TypeError:
        s = None
    final_result_y += [s]

# построение списка на основе переменной n, хранящей диапозон абсцисс для построение графика функции
final_result_x = [i for i in np.arange(-n, n+1, 0.01)]



fig, ax = plt.subplots()
# Координатные оси
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Построение графика по сгенерированным координатам, сохранение
ax.plot(final_result_x, final_result_y)
fig.savefig('graphic')
