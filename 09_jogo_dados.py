# -*- coding: utf-8 -*-
"""09_jogo_dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k-RP8PDXVZ1CKpdMbHy35HlQraNr2f93
"""

import random
min = 1 # Valor mínimo que um dado pode mostrar
max = 6 # Valor máximo que um dado pode mostrar

jogar_novamente = 'sim'
while jogar_novamente == 'sim' or jogar_novamente == 's':
    print('Jogando os dados...')
    print('Os valores são...')
    print(random.randint(min,max))
    print(random.randint(min,max))
    
    jogar_novamente = input('Jogar os dados mais uma vez?')