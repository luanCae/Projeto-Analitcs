import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv('gasolina.csv')


plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda')
plt.title('Preço da Gasolina 10 primeiro dias de Julho de 2021')
plt.ylabel('preço')