import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')  # Importar biblioteca

# Gráfico de Barras 1ª forma de criar
plt.figure(figsize = (10, 6))
df['nivel_educacao'].value_counts().plot(kind ='bar', color ='blue')  # Outra forma de se fazer esse gráfico
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Escolaridade')
plt.ylabel('Quantidade')
plt.xticks(rotation = 0)  # Seleciona a rotação
plt.show()

# Gráfico de Barras 2ª forma de criar

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize = (10,6))
plt.bar(x, y, color = 'green')
plt.xticks(rotation = 0)
plt.xlabel('Escolaridade')
plt.ylabel('Quantidade')
plt.title('Divisão de Escolaridade - 2')
plt.show()

# Gráfico de pizza
plt.figure(figsize = (10,6))
plt.pie(y, labels = x, autopct = '%1.1f%%', startangle = 90)  # Divise Y pela quantidade de X/ autopct = quantas casas décimais mostra na %/ strangle = o ponto que o gráfico começa, ex: 90º
plt.title('Gráfico de Pizza Escolaridade')
plt.show()

# Gráfico de Dispersão
plt.hexbin(df['idade'], df['salario'], gridsize =  40, cmap= 'Blues')
plt.colorbar(label = 'Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salários')
plt.title('Dispersão de Idade X Salário')
plt.show()
