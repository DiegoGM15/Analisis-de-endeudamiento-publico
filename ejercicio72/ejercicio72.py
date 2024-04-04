import ejercicio72_funciones


fecha1 = '2000Q1'
pais1 = 'ARG'
deuda = 'Deuda externa'
cuatropaises = ['ARG','MEX','ESP','BRA']

resultado = ejercicio72_funciones.dict_pais(pais1,fecha1)

resultado1 = ejercicio72_funciones.deuda_paises(deuda,fecha1)

resultado2 = ejercicio72_funciones.diagrama_deuda(pais1,fecha1)

resultado3 = ejercicio72_funciones.diagrama_tipo_deuda(pais1,fecha1)

resultado4 = ejercicio72_funciones.diagrama_tipo_paises(cuatropaises,deuda)

resultado5 = ejercicio72_funciones.pais_deudas(['ARG'], ['Deuda interna','Deuda externa','Deuda a largo plazo'])

resultado6 = ejercicio72_funciones.diagrama_de_cajas(['ARG','RUS','AUS','USA'],['Deuda interna','Deuda externa','Deuda a largo plazo'])