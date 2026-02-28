# Creado por: RGA (Ricardo Garcia Alvarez)
# Fecha: 27/02/2026
# Proyecto: Equipo 2 - Análisis de Datos Colaborativo

import pandas as pd

# BLOQUE 1: Carga de datos
# RGA - Leemos el archivo 'datos.csv' generado por la Colaboradora A (Odette))
# para integrarlo en nuestro flujo de trabajo.
# Fecha: 27/02/2026
df = pd.read_csv('datos.csv')

# BLOQUE 2: Inspección de estructura
# RGA - Mostramos las primeras filas para verificar que el CSV 
# tenga el formato correcto y las columnas esperadas.
# Fecha: 27/02/2026
print("--- Vista previa de los datos de Odette ---")
print(df.head())

# BLOQUE 3: Cálculo estadístico específico
# RGA - Obtenemos el promedio de la columna 'Monto'
# para dar un valor de análisis real al proyecto del equipo.
# Fecha: 27/02/2026
promedio_monto = df['Monto'].mean()
print(f"El promedio del monto gastado mensualmente en la tienda de abarrotes es: ${promedio_monto:,.2f}")

# BLOQUE 4: Resumen final
# RGA - Mensaje de confirmación de que el script de Ricardo G se ejecutó
# sin conflictos técnicos antes del push final.
# Fecha: 27/02/2026
print("\nAnálisis finalizado con éxito por Ricardo GA.")