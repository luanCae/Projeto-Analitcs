
***IMPORTANDO PACOTES***

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


***Lendo arquivo e tranformando em DATAFRAME***

df = pd.read_csv('gasolina.csv')


***Desenvolvimento do grafico***

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda')
plt.title('Preço da Gasolina no Dia')
plt.xlabel('Dia')
plt.ylabel('Preço')

***salvando grafico em PNG***

plt.savefig('gasolina.png')


