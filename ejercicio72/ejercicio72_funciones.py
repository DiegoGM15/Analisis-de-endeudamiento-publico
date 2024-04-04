import pandas as pd
import matplotlib.pyplot as plt

tabla = pd.read_csv('c:/nueva/ejercicio72/listado_deudas_paises.csv', sep=';', decimal=',')

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
    argtabla = pd.DataFrame(dict_pais)
    argtabla.to_csv('c:/nueva/ejercicio72/argtabla.csv', sep=';', decimal=',', index=True)

    return dict_pais

#resultado = dict_pais(pais1,fecha1)

#argtabla = pd.DataFrame(resultado)

deuda = 'Deuda externa'

def deuda_paises(deuda,fecha):

    filtrado = (copiatabla['TipoId'] == deuda) & (copiatabla['Fecha'] == fecha)
    dictdeuda = copiatabla.loc[filtrado]
    dict_deuda = dictdeuda.to_dict()
    deuda_paises_tabla = pd.DataFrame(dict_deuda)
    deuda_paises_tabla.to_csv('c:/nueva/ejercicio72/deuda_paises.csv', sep=';', decimal=',', index=True)

    return dict_deuda

#resultado1 = deuda_paises(deuda,fecha1)

#deuda_paises_tabla = pd.DataFrame(resultado1)

def diagrama_deuda(pais,fecha):

    filtrado = (copiatabla['PaisId'] == pais) & (copiatabla['Fecha'] == fecha) & ((copiatabla['TipoId'] == 'Deuda interna') | (copiatabla['TipoId'] == 'Deuda externa'))
    argfiltrado = copiatabla.loc[filtrado]
    plt.pie(argfiltrado['Cantidad'], autopct='%1.1f%%')
    plt.title(f'Distribucion de deuda externa e interna de Argentina en el trimestre{fecha}')
    plt.tight_layout()
    plt.plot(argfiltrado['Cantidad'],label= 'Deuda Interna')
    plt.plot(argfiltrado['Cantidad'],label= 'Deuda Externa')
    plt.legend(title='Tipo de deuda', loc='best')
    plt.savefig("C:/nueva/ejercicio72/diagrama_deuda_arg.png")
    plt.show()

    #return argfiltrado

#resultado2 = diagrama_deuda(pais1,fecha1)

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
    plt.savefig("C:/nueva/ejercicio72/diagrama_tipodeuda_arg.png")
    plt.show()

#resultado3 = diagrama_tipo_deuda(pais1,fecha1)

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
    plt.savefig("C:/nueva/ejercicio72/diagrama_tipodeuda_paises.png")
    plt.show()

    #return linea_arg

#resultado4 = diagrama_tipo_paises(cuatropaises,deuda)

#print(resultado4)

def pais_deudas(pais,tipodeuda):

    filtradopais = copiatabla[copiatabla.PaisId.isin(pais)]
    
    #print(filtradopais['TipoId'])
    for tipo_deuda in tipodeuda:
        
        filtradotipo = filtradopais[filtradopais['TipoId'] == tipo_deuda]
        plt.plot(filtradotipo['Fecha'], filtradotipo['Cantidad'], label= tipo_deuda)
    
    plt.title('Evolucion de los tipos de deudas de Argentina')
    plt.legend(title='Tipos de deuda', loc='best')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("C:/nueva/ejercicio72/diagrama_tipodeuda_pais.png")
    plt.show()

#resultado5 = pais_deudas(['ARG'], ['Deuda interna','Deuda externa','Deuda a largo plazo'])

def diagrama_de_cajas(paises,tipodeuda):

    filtrado = copiatabla[copiatabla['PaisId'].isin(paises) & copiatabla['TipoId'].isin(tipodeuda)]
    filtrado.boxplot(column='Cantidad', by=['PaisId','TipoId'], figsize=(10,6))
    plt.xlabel("País y Tipo de Deuda")
    plt.ylabel("Deuda")
    plt.title("Diagrama de Cajas de Deudas por País y Tipo de Deuda")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("C:/nueva/ejercicio72/diagrama_cajas_paises.png")
    plt.show()

#resultado6 = diagrama_de_cajas(['ARG','RUS','AUS','USA'],['Deuda interna','Deuda externa','Deuda a largo plazo'])












