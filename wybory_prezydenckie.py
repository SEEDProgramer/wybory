# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 02:55:51 2020

@author: marci
"""
import pandas as pn
# %%
df = pn.read_excel('wyniki_gl_na_kand_po_obwodach_utf8.xlsx')

# %%
s =df.describe()