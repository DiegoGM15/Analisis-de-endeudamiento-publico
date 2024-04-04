import pandas as pd
import matplotlib.pyplot as plt

tabla = pd.read_csv('c:/nueva/ejercicio72/listado_deudas_paises1.csv', sep=';', decimal=',')

copiatabla = tabla.drop(columns=['Pais','Tipo'])
copiatabla['PaisId'] = copiatabla['PaisId'].astype(str)
copiatabla['Fecha'] = copiatabla['Fecha'].astype(str)
fecha1 = '2000Q1'
pais1 = 'ARG'

listapaises = copiatabla['PaisId'].unique().tolist()

def dict_pais (pais,fecha):

    filtradopais = (copiatabla['PaisId'] == pais) & (copiatabla['Fecha'] == fecha) & ((copiatabla['TipoId'] == 'Deuda interna') | (copiatabla['TipoId'] == 'Deuda externa') | (copiatabla['TipoId'] == 'Deuda en moneda local') | (copiatabla['TipoId'] == 'Deuda en moneda extranjera') | (copiatabla['TipoId'] == 'Deuda a largo plazo') | (copiatabla['TipoId'] == 'Deuda a corto plazo'))
    dictpais = copiatabla.loc[filtradopais]
    dict_pais = dictpais.to_dict()

    return dict_pais

resultado = dict_pais(pais1,fecha1)

argtabla = pd.DataFrame(resultado)

deuda = 'Deuda externa'

def deuda_paises(deuda,fecha):

    filtrado = (copiatabla['TipoId'] == deuda) & (copiatabla['Fecha'] == fecha)
    dictdeuda = copiatabla.loc[filtrado]
    dict_deuda = dictdeuda.to_dict()

    return dict_deuda

resultado1 = deuda_paises(deuda,fecha1)

deuda_paises_tabla = pd.DataFrame(resultado1)

def diagrama_deuda(pais,fecha):

    filtrado = (copiatabla['PaisId'] == pais) & (copiatabla['Fecha'] == fecha) & ((copiatabla['TipoId'] == 'Deuda interna') | (copiatabla['TipoId'] == 'Deuda externa'))
    argfiltrado = copiatabla.loc[filtrado]
    plt.pie(argfiltrado['Cantidad'], autopct='%1.1f%%')
    plt.title(f'Distribucion de deuda externa e interna de Argentina en el trimestre{fecha}')
    plt.tight_layout()
    plt.plot(argfiltrado['Cantidad'],label= 'Deuda Interna')
    plt.plot(argfiltrado['Cantidad'],label= 'Deuda Externa')
    plt.legend(title='Tipo de deuda', loc='best')
    plt.show()

    #return argfiltrado

resultado2 = diagrama_deuda(pais1,fecha1)

def diagrama_tipo_deuda(pais,fecha):

    filtrado = (copiatabla['PaisId'] == pais) & (copiatabla['Fecha'] == fecha)  & ((copiatabla['TipoId'] == 'Deuda interna') | (copiatabla['TipoId'] == 'Deuda externa') | (copiatabla['TipoId'] == 'Deuda en moneda local') | (copiatabla['TipoId'] == 'Deuda en moneda extranjera') | (copiatabla['TipoId'] == 'Deuda a largo plazo') | (copiatabla['TipoId'] == 'Deuda a corto plazo'))
    tipos_deudas_arg = copiatabla.loc[filtrado]
    #tipos_deudas_arg.plot(kind='bar', color='skyblue')
    plt.bar(tipos_deudas_arg['TipoId'],tipos_deudas_arg['Cantidad'], color='skyblue')
    plt.title(f'Tipos de deuda de Argentina en el trimestre {fecha}')
    plt.xlabel('Tipo de deuda')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

resultado3 = diagrama_tipo_deuda(pais1,fecha1)

#copiatabla['PaisId'] = copiatabla['PaisId'].astype(str)
filtro = (copiatabla['PaisId'] == 'ARG') | (copiatabla['PaisId'] == 'BRA') | (copiatabla['PaisId'] == 'MEX') | (copiatabla['PaisId'] == 'ESP')
cuatropaises = copiatabla.loc[filtro, 'PaisId'].unique().tolist()

filtrodeudas =  ((copiatabla['TipoId'] == 'Deuda interna') | (copiatabla['TipoId'] == 'Deuda externa') | (copiatabla['TipoId'] == 'Deuda en moneda local') | (copiatabla['TipoId'] == 'Deuda en moneda extranjera') | (copiatabla['TipoId'] == 'Deuda a largo plazo') | (copiatabla['TipoId'] == 'Deuda a corto plazo'))
listadeudas = copiatabla.loc[filtrodeudas, 'TipoId'].unique().tolist()
#print(listadeudas)

#filtroanios = ((copiatabla['Fecha'] == '1995Q1') | (copiatabla['Fecha'] == '2000Q1') | (copiatabla['Fecha'] == '2005Q1') | (copiatabla['Fecha'] == '2010Q1') | (copiatabla['Fecha'] == '2015Q1') | (copiatabla['Fecha'] == '2019Q1'))
#listaanios = copiatabla.loc[filtroanios, 'Fecha'].unique().tolist()



def diagrama_tipo_paises(lista,tipo):

    filtrado_arg = (copiatabla['TipoId'] == tipo) & (copiatabla['PaisId'] == 'ARG') 
    linea_arg = copiatabla.loc[filtrado_arg]
    filtrado_bra = (copiatabla['TipoId'] == tipo) & (copiatabla['PaisId'] == 'BRA')
    linea_bra = copiatabla.loc[filtrado_bra]
    filtrado_mex = (copiatabla['TipoId'] == tipo) & (copiatabla['PaisId'] == 'MEX')
    linea_mex = copiatabla.loc[filtrado_mex]
    filtrado_esp = (copiatabla['TipoId'] == tipo) & (copiatabla['PaisId'] == 'ESP')
    linea_esp = copiatabla.loc[filtrado_esp]
    plt.plot(linea_arg['Fecha'],linea_arg['Cantidad'], label='Argentina')
    plt.plot(linea_bra['Fecha'],linea_bra['Cantidad'], label='Brasil')
    plt.plot(linea_mex['Fecha'],linea_mex['Cantidad'], label='Mexico')
    plt.plot(linea_esp['Fecha'],linea_esp['Cantidad'], label='España')
    plt.title('Evolucion de deuda externa en España, Argentina, Brasil, Mexico')
    plt.xlabel('Deuda Externa')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.legend(title='Paises', loc='best')
    plt.tight_layout()
    plt.show()

    #return linea_arg

resultado4 = diagrama_tipo_paises(cuatropaises,deuda)

#print(resultado4)

def pais_deudas(pais,tipodeuda):

    filtradopais = copiatabla[copiatabla.PaisId.isin(pais) & copiatabla.TipoId.isin(tipodeuda)]

    for tipo_deuda in tipodeuda:

        plt.plot(filtradopais.index, filtradopais[tipo_deuda], label='tipo_de_deuda')
    #deuda_interna = filtrado.loc[filtrado['TipoId'] == 'Deuda interna', 'Cantidad']
    #plt.plot(filtrado['Fecha'], (filtrado.loc[filtrado['TipoId'] == 'Deuda externa','Cantidad']),label='Deuda externa')
    #plt.plot(filtrado['Fecha'], (filtrado.loc[filtrado['TipoId'] == 'Deuda interna','Cantidad']), label='Deuda interna')
    #plt.plot(filtrado['Fecha'], (filtrado.loc[filtrado['TipoId'] == 'Deuda a largo plazo','Cantidad']), label='Deuda a largo plazo')
    plt.title('Evolucion de los tipos de deudas de Argentina')
    plt.legend(title='Tipos de deuda', loc='best')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    #return deuda_interna

resultado5 = pais_deudas(['ARG'], ['Deuda interna','Deuda externa','Deuda a largo plazo'])

#print(resultado5)












