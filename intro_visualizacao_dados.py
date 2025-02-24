import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.show()  # Comando para mostrar o gráfico

# Histograma - Parâmetros
plt.figure(figsize=(10,6))  # Escolhe o tamanho do gráfico 10x6
plt.hist(df["salario"], bins=100, color = 'green', alpha = 0.8)  # bins = tamanho da divisão do gráfico, alpha = transparência
plt.title('Histograma - Distribuição de Salários')  # Título
plt.xlabel('Salários')  # Nome do eixo X
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))  # Seleciona o intervalo do gráfico, do 0 até o máximo + 2000
plt.ylabel('Frequência')  # Nome do eixo Y
plt.grid(True)  # Cria a divisão do grid
plt.show()

# Múltiplos Gráficos
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)  # Número de linhas, colunas e posição do gráfico (2 linhas, 2 colunas, 1º Gráfico)
# Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão Salário - Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1,2,2)  # 1 Linha, 2 Colunas, 2º Gráfico
plt.scatter(df['salario'], df['anos_experiencia'], color = '#327da8', alpha = 0.6, s=30)  # Cor Hexadecimal, Alpha = Transparência, s = tamanho da bolinha
plt.title("Dispersão - Salário X Anos de experiência")
plt.xlabel('Salários')
plt.ylabel('Anos de Experiência')

# Mapa de Calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3)  # 2 Linhas, 2 Colunas, 3º Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário X Idade')

plt.tight_layout()  # Ajustar o espaçamento entre os gráficos
plt.show()

