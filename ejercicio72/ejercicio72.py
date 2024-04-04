import pandas as pd
import matplotlib.pyplot as plt

tabla = pd.read_csv('c:/nueva/ejercicio72/listado_deudas_paises.csv', sep=';', decimal=',')

print(tabla.tail(10)) #Mostrar las ultimas 10 filas del dataframe

copiatabla = tabla.drop(columns=['Pais','Tipo'])

print(copiatabla.tail(10))
