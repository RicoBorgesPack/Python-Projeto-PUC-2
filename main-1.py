#importa biblioteca dados
import dados as data
#roda o codigo em loo´p
while True:
  #obtem palavra
  frase = input("Digite uma palavra: ")
  #Valida se é menor ou igual a dois
  if len(frase) <= 2:
    print("Digite novamente")
  else:
    #executa procedimento de contar quantos
    print("essa frase possui " + str(data.contaForaDoAlfabeto(frase)) + " algarismos que não são letras do alfabeto")
    #executa o procedimento de contar palavras
    print("Numero de palavras na frase é " + str(data.contaPalavras(frase)))
    #executa o procedimento que conta os espaços
    print("Numero de espaços na frase é " + str(data.contaEspacos(frase)))
    #executa o procedimento que conta vogais
    data.contaVogais(frase)
    #pergunta se deseja encerrar o programa
    resposta = input("deseja sair do programa?? Digite sair caso queira: ")
    #caso digitado "sair", o programa encerra
    if resposta == "sair":
      print("Muito obrigado por usar esse software")
      break
    
