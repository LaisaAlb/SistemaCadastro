# Criando um Sistema em Python utilizando funções
from time import sleep


def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('\033[31mERROR! Por favor, digite um número inteiro valido\033[m')
      continue
    except KeyboardInterrupt:
      print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
      return 0
    else:
      return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
  cabecalho('MENU PRINCIPAL')
  c = 1
  for item in lista:
    print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
    c += 1
  print(linha())
  opc = leiaInt('\033[33mSua Opção: \033[m')
  return opc

def arquivoExiste(nome):
  try: 
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else: 
    return True   
  
def criarArquivo(nome):
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print('Houve um ERRO na criação do arquivo!')
  else:
    print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
  try:
    a = open(nome, 'rt')
  except:
    print('Erro ao ler o arquivo!')
  else:
    cabecalho('PESSOAS CADASTRADAS')
    for linha in a:
      dado = linha.split(';')
      dado[1] = dado[1].replace('\n', '')
      print(f'{dado[0]:<30}{dado[1]:>3} anos')
  finally:
    a.close()

def cadastrar(arq, nome='desconhecido', sobrenome='desconhecido', idade=0):
  try:
    a = open(arq, 'at')
  except:
    print('Houve um ERRO na abertura de arquivo!')
  else:
    try:
      a.write(f'{nome} {sobrenome};{idade}\n')
    except:
      print('Houve um ERRO na hora de escrever os dados!')
    else: 
      print(f'Novo registro de {nome} adicionado')
    finally:
      a.close()


# Acima estão todas as funções. E em seguida, o programa principal do sistema  

arq = 'pessoascadastradas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
  if resposta == 1:
    # Opção de listar o conteúdo de um arquivo
    lerArquivo(arq)
  elif resposta == 2:
    # Opção de Cadastrar uma nova pessoa 
    while True:
      cabecalho('NOVO CADASTRO')
      nome = str(input('Nome: '))
      sobrenome = str(input('Sobrenome: '))
      idade = int(input('Idade: '))
      cadastrar(arq, nome, sobrenome,  idade )
      continuar = str(input("Deseja continuar cadastrando? [S/N] ")).strip().upper()[0]
      if continuar == 'N':
        break
        
  elif resposta == 3:
      cabecalho('Saindo do Sistema... Até logo!')
      break
  else: 
    print('\033[31mERROR! Digite uma opção válida\033[m')
  sleep(2)