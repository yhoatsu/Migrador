
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


tabla=pd.read_csv(r'D:\GoogleDrive\Hacker Civics\GibHub\Proyecto Migrador\Preparación datos balanza comercial\Tablas generadas\tabla_por_grupos.csv',sep=',',dtype={'Product category':str},engine="python", encoding="latin_1")
tabla_nc=pd.read_csv(r'D:\GoogleDrive\Hacker Civics\GibHub\Proyecto Migrador\Preparación datos balanza comercial\Tablas generadas\diccionario_codigo_nc_valenciano.csv',sep=';',dtype={'Code':str},engine="python", encoding="latin_1")
tabla_flow=pd.read_csv(r'D:\GoogleDrive\Hacker Civics\GibHub\Proyecto Migrador\Preparación datos balanza comercial\Tablas de reemplazo\Code_import_val.csv',sep=';',engine="python", encoding="latin_1")
tabla_contry=pd.read_csv(r'D:\GoogleDrive\Hacker Civics\GibHub\Proyecto Migrador\Preparación datos balanza comercial\Tablas de reemplazo\cod_paises_iso_val.csv',sep=';',engine="python", encoding="latin_1")
tabla_region=pd.read_csv(r'D:\GoogleDrive\Hacker Civics\GibHub\Proyecto Migrador\Preparación datos balanza comercial\Tablas de reemplazo\cod_paises_region.csv',sep=';',engine="python", encoding="latin_1")


# In[3]:


def crear_dic(table):
    dicc={}
    for nrow in range(0,(table.shape[0])):
        dicc[table.ix[nrow,1]]=table.ix[nrow,0]
    return dicc

def crear_dic2(table):
    dicc={}
    for nrow in range(0,(table.shape[0])):
        dicc[table.ix[nrow,0]]=table.ix[nrow,1]
    return dicc


# In[4]:


dicc_nc=crear_dic2(tabla_nc)


# In[5]:


dicc_flow=crear_dic2(tabla_flow)


# In[6]:


dicc_country=crear_dic(tabla_contry)


# In[8]:


dicc_region=crear_dic2(tabla_region)


# In[11]:


tabla.ix[:,'Value Cents Euro']=tabla.ix[:,'Value Cents Euro']/100


# In[12]:


tabla.rename(columns={'Value Cents Euro':'Value Euro'}, inplace=True)


# In[14]:


tabla.replace({'Product category': dicc_nc},  inplace = True)


# In[14]:


tabla.replace({'Country': dicc_country},  inplace = True)


# In[16]:


tabla.insert(3,'Region',tabla['Country'])


# In[30]:


tabla.replace({'Flow': dicc_flow},  inplace = True)


# In[17]:


tabla.replace({'Region': dicc_region},  inplace = True)



# In[32]:


tabla.to_csv(r'D:\GoogleDrive\Hacker Civics\GibHub\Proyecto Migrador\Preparación datos balanza comercial\Tablas generadas\Tabla_I_E_por_grupos_completa.csv')

