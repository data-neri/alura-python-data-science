#importando dados 
import pandas as pd
import matplotlib as plt
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)
#ajeitando a separação e nomeandoa
dados =pd.read_csv(url, sep=";")
dados
#leitura de cima para baixo
dados.head(11)
#leitura de baixo para cima 
dados.tail()
type(dados)
dados.shape
#ver todas as colunas dos dados presente
dados.columns
#mesma forma só que mais simplificada
dados.info()
#puxar apenas uma coluna pegando como exemplo a coluna tipo 
dados['Tipo']
#consigo tambem pegar duas colunas ou mais 
dados[['Quartos','Valor']]
dados.head(11)
#calcular a media de cada imovel
dados['Valor'].mean()
dados.groupby('Tipo').mean(numeric_only=True)
#selecionando apenas valor
dados.groupby('Tipo')["Valor"].mean()
#preço medio dos imoveis 
dados.groupby('Tipo')[["Valor"]].mean().sort_values("Valor")
#preço medio dos imoveis e com um gradico mostrando o mais caro ao mais barato
preço_tipo = dados.groupby('Tipo')[["Valor"]].mean().sort_values("Valor")
preço_tipo.plot(kind='barh', figsize=(14,10), color="purple");
#mostrando todos os tipos de imoveis 
dados.Tipo.unique()
imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']
                                            
#retirando todos os imoveis comerciais
ims_residenciais = dados.query("@imoveis_comerciais not in Tipo")
ims_residenciais.head()
#agora o mesmo grafico mas só com os residenciais 
preço_tipo = ims_residenciais.groupby('Tipo')[["Valor"]].mean().sort_values("Valor")
preço_tipo.plot(kind='barh', figsize=(14,10), color="purple");
ims_residenciais.Tipo.unique()
#percentual de cada tipo de imovel 
ims_residenciais.Tipo.value_counts(normalize=True)
ims_residenciais.Tipo.value_counts(normalize=True).to_frame("Tipo")
#grafico para ver a quantidade de imoveis de cada tipo
ims_percentual_tipo = ims_residenciais.Tipo.value_counts(normalize=True).to_frame("Tipo")
ims_percentual_tipo.plot(kind='bar', figsize=(14,10), color = 'red',
                         xlabel='Tipos', ylabel = 'Percentual'); 
#selecionando apenas apartamento para trabalhar com o maior tipo 
apartamentos = ims_residenciais.query('Tipo == "Apartamento" ')
apartamentos.head()
#começar a verificar os dados nulo
apartamentos.isnull()
#verificação dos valores nulos
apartamentos.isnull().sum()
#só os apartamentos que tem valores nulos abaixo fillna ira substituir o nulo por 0 
apartamentos.fillna(0)
#substituindo por 0
apartamentos = apartamentos.fillna(0)
#remover os registros em que valor é igual a 0 ou condominio seja igual 0 
apartamentos.query("Valor == 0 | Condominio == 0")
#o index vai mostrar os valores igual a 0 
registro_a_remover = apartamentos.query("Valor == 0 | Condominio == 0").index
#axis= para remover a linha e não aparecer eo inplace para alterações seja aplicadas no apartamentos
apartamentos.drop(registro_a_remover, axis=0, inplace=True)

#vazio agora pois não aparecera nenhum valor igual a 0
apartamentos.query("Valor == 0 | Condominio == 0")
apartamentos.head()
apartamentos.Tipo.unique()
#ja que só estamos trabalhando com apartamentos não faz sentico colocar a categoria tipo,agora no axis entra o igual a 1 para remover a coluna em especifico
apartamentos.drop("Tipo",axis=1, inplace=True)
#agora a coluna apartamentos não existe mais 
apartamentos.head()
#1ºfiltrar os quartos para os que possuem só um quarto e o alugel seja 1200
#2ºfiltrar para que com 2 ou mais quartos e seja menor que 3200 e tenha uma area maios que 70m²
apartamentos['Quartos'] == 1
#filtrando para apenas um quarto
seleção1 = apartamentos['Quartos'] == 1
apartamentos[seleção1]
#filtrando preços abaixo de 1200
seleção2 =apartamentos["Valor"]<= 1200
apartamentos[seleção2]
#juntando as duas seleções 
seleções_finais = (seleção1) & (seleção2)
apartamentos[seleções_finais]

#facilitando para escolher essa seleção 
apartamentos_01 = apartamentos[seleções_finais]
#agora de um metodo mais curto e mais pratico 
apt = apartamentos
seleção= (apt['Quartos'] >=2) & (apt['Valor'] <3200) & (apt['Area'] >70)
apt[seleção]
#salvando os dados com todas as mudanças realizadas
apt.to_csv("dados_apartamentos.csv")
pd.read_csv("dados_apartamentos.csv")
#correção da coluna dos dados e colocando o delimitador que foi dado antes que é o ;
apt.to_csv("dados_apartamentos.csv",index=False,sep=";")
#agora sai da maneira correta como foi data antes 
pd.read_csv("dados_apartamentos.csv",sep=";")
#criar gasto por mês e por ano dos dados originais
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados['Valor_por_ano'] = (dados['Valor_por_mes']*12) + dados['IPTU']
dados.head()
#criando uma discrição para os imoveis
'''
dados['descrição'] = dados['Tipo'] + " em " + dados['Bairro']
dados.head()
'''
#melhorando a descrição colocando o ".astype(str)" faz com que as colunas "Quarto" e "Vargas" se tornem str pois podem da conflito str e int
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
dados.head()
#criando descrição para suites
dados['possui_suite'] = dados['Suites'].apply(lambda x: 'sim' if x>0 else 'não')
dados.head()
dados.to_csv("dados_completos")