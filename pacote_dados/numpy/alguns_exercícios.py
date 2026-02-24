# importando o numpy e testando 
import numpy as np
np.array(42)

# testando matrizes

np.array([[3, 2, 7],
          [4, 9, 1],
          [5, 6, 8]])


# %importando o matplot
import matplotlib.pyplot as plt

#aprendendo a importa os arquivos ja baixados 

# Como o arquivo está na mesma pasta, basta o nome
df = pd.read_csv('citrus.csv')

# Para o arquivo de séries temporais das maçãs 
df_apples = pd.read_csv('apples_ts.csv')

print(df.head())

# aprendendo a ler os dados e tetando deixa ele alinhados
dado =np.loadtxt('apples_ts.csv', delimiter=',',usecols=np.arange(1,88,1)) 
dado

# %alinhando os dados
dados_transposto = dado.T
dados_transposto

# colocando um grafico nos dados
plt.plot(dados_transposto)
plt.plot

# grafico para compara data e preços
datas = dados_transposto[:,0]
precos = dados_transposto[:,1:6]
datas = np.arange(1,88,1)
plt.plot(datas,precos[:,0])



# separação dos preço com a região
Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

# seperação dos anos para fica mais pratico
Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

# comparação em grafico da venda de maças de cada ano 
plt.plot(np.arange(0,12),Moscow_ano1)
plt.plot(np.arange(0,12),Moscow_ano2)
plt.plot(np.arange(0,12),Moscow_ano3)
plt.plot(np.arange(0,12),Moscow_ano4)
plt.legend(["Ano 1", "Ano 2", "Ano 3", "Ano 4"])       

# grafico incompleto de Kaliningrad
plt.plot(datas,Kaliningrad)

# error nan em Kaliningrad,como corrigir?
Kaliningrad

# soma para descobri a média aritmética que esta faltando ali 
Kaliningrad[4] = np.mean([Kaliningrad[3],Kaliningrad[5]])
plt.plot(datas,Kaliningrad)

#comparação de vendas de maças com a média aritmética

print ("Média de Moscou: ", np.mean(Moscow))
print ("Média de Kaliningrad: ", np.mean(Kaliningrad))

#grafico de vendas moscow
plt.plot(datas,Moscow)

# criando uma linha do grafico de vendas
x = datas
y= 2*x+80
plt.plot(datas,Moscow)
plt.plot(x,y)


# %%
np.sqrt(np.sum(np.power(Moscow-y,2))) 
plt.plot(datas,Moscow)
plt.plot(x,y)

# alinhando a linha com o grafico para mostra o índice de crescimento
y= 0.52*x+80
plt.plot(datas,Moscow)
plt.plot(x,y)



