import random
# '\U0001F4A3'
def iniciaMatriz():
  matriz = []
  for i in range(tamanho):
    linha = []
    for j in range(tamanho):
      linha.append('x')
    matriz.append(linha)
  return matriz

def escreveMatriz():
  for lista in matriz:
    print(lista)

def escolhePosicao():
  x = int(input('Escolha a linha: ')) - 1
  y = int(input('Escolha a coluna: ')) - 1
  return [x, y]

def geraBombas():
  bombas = []
  for bomba in range(tamanho):
    repetida = True
    while repetida:
      bomba = [random.randint(0, tamanho-1), random.randint(0, tamanho-1)]
      if bomba not in bombas:
        bombas.append(bomba)
        repetida = False
  return bombas

tamanho = 3
bombas = geraBombas()
print(bombas)

matriz = iniciaMatriz()
escreveMatriz()

escolha = []
contador = 0

O_JOGO = True
while O_JOGO:
  escolha = escolhePosicao()
  if escolha in bombas:
    print('PERDEU PREIBOI')
    O_JOGO = False
    # matriz[x][y] = '\U0001F4A3'
    matriz[escolha[0]][escolha[1]] = '\U0001F4A3'
  else:
    matriz[escolha[0]][escolha[1]] = 0
    contador += 1
    if contador >= (tamanho*tamanho)-tamanho:
      print('VOCE GANHOU!!')
      O_JOGO = False
  escreveMatriz()
