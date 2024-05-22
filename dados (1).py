#vetor com vogais
vogal = ["A","E","I","O","U"]
#procedimento para contar palavras
def contaPalavras(frase):
  #separa as palavras da frase e conta as mesmas
  palavras = len(frase.split())
  return palavras
#procedimento para contar espaços
def contaEspacos(frase):
  #instancia os espaços iguais a zero
  espacos = 0
  #método de repetição para buscar espaços
  for x in frase:
    #caso seja encontrado um espaço, adiciona um na variavél
    if x == " ":
      espacos+= 1
  return espacos
#procecimento para contar algarismos que não estão no alfabeto
def contaForaDoAlfabeto(frase):
  #instancia variavel com zero
  algarismo = 0
  #método de repetição para buscar algarismos
  for x in frase:
    #caso não seja alfanumérico e diferente que espaço, adiciona um a variavél
    if x.isalpha() == False and x != " ":
      algarismo += 1
  return algarismo
  
#procedimento para contar vogais
def contaVogais(frase):
  #instancia as variaveis das vogais
  A = E = I = O = U =0
  #Valida se os algarismos são iguais as vogais, caso correto adiciona um a variavél correspondente
  for x in frase:
    if x.upper() == vogal[0]:
      A += 1
    elif x.upper() == vogal[1]:
      E += 1
    elif x.upper() == vogal[2]:
      I += 1
    elif x.upper() == vogal[3]:
      O += 1
    elif x.upper() == vogal[4]:
      U += 1
  #Printa os valores de cada valor
  print("Total de vogais A: " + str(A))
  print("Total de vogais E: " + str(E))
  print("Total de vogais I: " + str(I))
  print("Total de vogais O: " + str(O))
  print("Total de vogais U: " + str(U))