
# coding: utf-8

# In[38]:


import json
from pprint import pprint

with open(r'D:\Hacker Civics\Proyecto Migrador\Importacion - Productos\Scripts\Python\Scrapeo\Tutorial\tutorial\json_codigo_nc_categoria.json') as json_data:
    d = json.load(json_data)
    json_data.close()
    pprint(d)

dicct={}
for items in d:
    dicct.update(items)

archivo = open(r'D:\Hacker Civics\Proyecto Migrador\Importacion - Productos\Scripts\Python\Scrapeo\Tutorial\tutorial\diccionario_python_sin_reemplazo.json','w')
dicct = str (dicct)
archivo.write(dicct)
archivo.close()

