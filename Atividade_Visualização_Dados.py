import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())

# Histograma
print(df['Preço'].describe())
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=100, alpha= 0.8, color = 'green')
plt.title('Histograma - Preços de Venda')
plt.xlabel('Preços')
plt.xticks(ticks=range(0, int(df['Preço'].max())+100, 50))
plt.ylabel('Frequência')
plt.grid (True)
plt.show()

# Dispersão
plt.figure(figsize = (10,6))
plt.scatter(df['Preço'], df['Desconto'], color = 'Blue', alpha = 1.0, s = 15)
plt.xticks(ticks=range(0, int(df['Preço'].max())+100, 50))
plt.title('Dispersão - Desconto X Preço')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.grid(True)
plt.show()

# Mapa de Calor
plt.figure(figsize = (10,6))
corr = df[['Qtd_Vendidos_Cod', 'N_Avaliações', 'Nota',]].corr()
sns.heatmap(corr, annot = True, cmap = 'coolwarm')
plt.title('Correlação - Qtd. Vendidos X Núm. Avaliações X Nota')
plt.show()

# Gráfico de Barra
x1 = df['Desconto'].value_counts().index
y1 = df['Desconto'].value_counts().values

plt.figure(figsize = (10,6))
plt.bar(x1, y1, color = 'red')
plt.xticks(rotation = 0)
plt.xlabel('Desconto')
plt.ylabel('Quantidade')
plt.title('Frequência - Descontos')
plt.grid(True)
plt.show()

# Gráfico de Pizza
print(df['Temporada'].value_counts())
df['Temporada'] = df['Temporada'].apply(lambda x: None if x not in  ['primavera/verão', 'outono/inverno', 'não definido'] else x)
df['Temporada'] = df['Temporada'].str.title()
x2 = df['Temporada'].value_counts().index
y2 = df['Temporada'].value_counts().values
plt.figure(figsize = (10,6))
plt.pie(y2, labels = x2, autopct = '%1.1f%%', startangle = 90)
plt.title('Gráfico de Pizza - Temporada')
plt.show()

# Gráfico de Densidade
plt.figure(figsize = (10,6))
sns.kdeplot(df['Preço'],fill = True, color ='#15ff00')
plt.xticks(ticks=range(0, int(df['Preço'].max())+100, 50))
plt.title('Densidade - Preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.grid(True)
plt.show()

# Gráfico de Regressão
plt.figure(figsize = (10,6))
sns.regplot(x = 'Preço', y = 'Desconto', data = df, color = 'red', scatter_kws = {'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão - Preço X Desconto')
plt.grid(True)
plt.show()
