#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cleaning_first(dafr):
    dafr['season']=dafr['category'].astype(str).str.split('/').str[5]
    dafr['teams']=dafr['category'].astype(str).str.split('/').str[4]
    dafr['mob']=dafr['dob1'].astype(str).str.split('/').str[1]
    dafr['yob']=dafr['dob1'].astype(str).str.split('/').str[2].str.split(' ').str[0]
    dafr['dayob']=dafr['dob1'].astype(str).str.split('/').str[0].str.split(' ').str[2]
    dafr['fn']=dafr['name'].str.split(' ').str[0].str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dafr['ln']=dafr['name'].str.split(' ').str[-1].str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dafr.loc[dafr['season'].astype(int)==2,'seasonord']=1
    dafr.loc[dafr['season'].astype(int)==6,'seasonord']=2
    dafr.loc[dafr['season'].astype(int)==4,'seasonord']=3
    dafr.loc[dafr['season'].astype(int)==1,'seasonord']=4
    dafr.loc[dafr['season'].astype(int)==5,'seasonord']=5
    dafr.loc[dafr['season'].astype(int)==3,'seasonord']=6
    dafr.loc[dafr['season'].astype(int)==7,'seasonord']=7
    dafr.loc[dafr['season'].astype(int)==8,'seasonord']=8
    dafr.loc[dafr['season'].astype(int)==9,'seasonord']=9
    dafr.loc[dafr['season'].astype(int)==0,'seasonord']=9
    dafr.loc[dafr['link']=='U14 Woman','catord']=1
    dafr.loc[dafr['link']=='U16','catord']=2
    dafr.loc[dafr['link']=='U19','catord']=3
    dafr.loc[dafr['link']=='Mayores','catord']=4
    dafr.loc[dafr['link']=='Sub 14','catord']=1
    dafr.loc[dafr['link']=='Sub 15','catord']=2
    dafr.loc[dafr['link']=='Sub 16','catord']=3
    dafr.loc[dafr['link']=='Sub 17','catord']=4
    dafr.loc[dafr['link']=='Sub 19','catord']=5
    dafr.loc[dafr['link']=='3A','catord']=6
    dafr.loc[dafr['link']=='1A','catord']=7
    return dafr
    
def cleaning_second(dafr):
    dictio={
    "Nacional": 81,
    "River Plate": 4463,
    "D. Maldonado":240,
    "Danubio": 284,
    "Liverpool": 205,
    "Def. Sporting": 190,
    "Peñarol": 139,
    "Cerro Largo": 92,
    "Boston River": 20,
    "Fénix": 25,
    "Albion": 150,
    "Wanderers": 231,
    "Plaza Colonia": 137,
    "M.C. Torque": 105,
    "Rentistas": 156,
    "Cerrito": 59,
    "Racing": 4471,
    "Uruguay Montevideo": 280,
    "Cerro": 226,
    "La Luz": 79,
    "Miramar Misiones": 91,
    "Sud América": 127,
    "Atenas de San Carlos": 187,
    "Rampla Juniors": 4462,
    "Villa Española": 65,
    "Progreso": 89,
    "Juventud": 202,
    "Central Español": 265,
    "Nacional (F)": 273,
    "Peñarol (F)": 68,
    "Defensor Sporting (F)": 236,
    "Wanderers (F)": 243,
    "Liverpool (F)": 61,
    "Fénix (F)": 72,
    "River Plate (F)": 229,
    "Náutico (F)": 304,
    "Atenas (F)": 73,
    "M.C. Torque (F)": 4694,
    "Danubio  (F)": 174,
    "S.J. Rentistas (F)": 99,
    "Boston River (F)": 256,
    "Racing (F)": 83,
    "Canadian (F)": 222,
    "Juventud (F)": 122,
    "Rampla Juniors (F)": 257,
    "Plaza Colonia (F)": 307
    }
    fem=list(dictio.values())[28:]
    first=[]
    first=list(dictio.values())[:17]+list(dictio.values())[28:37]
    dafr['fem']=0
    dafr.loc[dafr['teams'].astype(int).isin(fem),'fem']=1
    dafr['id']=dafr.groupby(['fn','ln','dayob','mob','yob','fem']).ngroup()
    minseason=dafr.groupby('id')['seasonord'].min()
    maxseason=dafr.groupby('id')['seasonord'].max()
    maxcat=dafr.groupby('id')['catord'].max()
    mincat=dafr.groupby('id')['catord'].min()
    dafr=dafr.merge(minseason, on=['id'])
    dafr=dafr.rename(columns={"seasonord_y": "minseason"})
    dafr=dafr.rename(columns={"seasonord_x": "seasonord"})
    dafr=dafr.merge(maxseason, on=['id'])
    dafr=dafr.rename(columns={"seasonord_y": "maxseason"})
    dafr=dafr.rename(columns={"seasonord_x": "seasonord"})
    dafr=dafr.merge(maxcat, on=['id'])
    dafr=dafr.rename(columns={"catord_y": "maxcat"})
    dafr=dafr.rename(columns={"catord_x": "catord"})
    dafr=dafr.merge(mincat, on=['id'])
    dafr=dafr.rename(columns={"catord_y": "mincat"})
    dafr=dafr.rename(columns={"catord_x": "catord"})
    dafr=dafr[dafr['link']!='Copa AUF Uruguay']
    dafr=dafr.drop_duplicates(subset=['seasonord','id'])
    first_p=dafr[(dafr['teams'].astype(int).isin(first)) & (dafr['catord']==dafr['mincat'])].index.tolist()
    dafr['first']=0
    dafr.loc[dafr.index.isin(first_p),'first']=1
    return dafr
    
def gen_freqs(dafr):    
    gl=dafr.groupby(['mob', 'link', 'fem']).count()['name'].to_frame()
    gl.reset_index(inplace=True)
    rp=dafr.groupby([ 'link', 'fem']).count()['name'].to_frame()
    rp.reset_index(inplace=True)
    merged=gl.merge(rp, on=['link', 'fem'])
    merged['freq']=merged['name_x']/merged['name_y']*100
    return merged
    
def cleaning_third(dafr):
    import pandas as pd
    idx = pd.MultiIndex.from_product([dafr.id.unique(), dafr.seasonord.unique()], names=["id", "seasonord"])
    dafr3 = dafr.set_index(["id", "seasonord"]).reindex(idx).reset_index()
    dafr3['present']=1
    dafr3.loc[dafr3['Unnamed: 0'].isna(),'present']=0
    dafr3['new_id']=dafr3['id']
    dafr3=dafr3.sort_values(by=['new_id', 'seasonord'])
    dafr3=dafr3.groupby(['id']).ffill().reset_index()
    dafr33=dafr3[dafr3['seasonord']>=dafr3['minseason']]
    return dafr33

