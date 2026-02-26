import pandas as pd 
url ='https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url)
dados
dados.head(8)
dados.shape
dados.columns
dados.tail(8)
dados.describe()
dados.fillna(0)
#alice e carlos sairam da turma 
dados.drop([7,8],axis=0,inplace=True)
dados
aprovados = (dados['Aprovado']==True)
alunos_aprovados= dados[aprovados]
alunos_aprovados
alunos_aprovados.to_csv("alunos-aprovados",index=False,sep=",")
dados
dados["pontos_extras"] = dados['Notas'].apply(lambda x: x * 0.4)
dados.head()
dados["notas_finais"] = dados['Notas'] + dados['pontos_extras']
dados.head()
dados['situação final'] = dados['notas_finais'].apply(lambda x: True if x> 6 else False)
dados.head()

# Criando o filtro
selecao = (dados['Aprovado'] == False) & (dados['situação final'] == True)

# Aplicando o filtro e mostrando o resultado
alunos_que_subiram = dados[selecao]
alunos_que_subiram