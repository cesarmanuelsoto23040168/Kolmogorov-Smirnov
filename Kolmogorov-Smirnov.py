import numpy as np
import scipy.stats as stats

# 1. Generar 100 números aleatorios en el rango [0, 1]
n = 100
random_numbers = np.random.random(n)

# Mostrar los números aleatorios
print("Números aleatorios generados (n = 100):")
print(random_numbers)

# 2. Prueba de Kolmogorov-Smirnov para una muestra (comparar con una distribución uniforme)
ks_statistic, p_value = stats.kstest(random_numbers, 'uniform')

# 3. Mostrar resultados
print("\nPrueba de Kolmogorov-Smirnov (KS)")
print("Estadístico KS:", ks_statistic)
print("Valor p:", p_value)

# 4. Interpretación del resultado
if p_value < 0.05:
    print("\nRechazamos la hipótesis nula: la distribución no es uniforme.")
else:
    print("\nNo podemos rechazar la hipótesis nula: la distribución parece uniforme.")
