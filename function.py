from pickle import FALSE
def opçoesDisponiveis():
    print('-='*17)
    print('1 - Cadastrar reserva \n2 - Consultar reserva \n3 - Listar cadeiras disponíveis \n4 - Excluir reserva \n0 - Sair')
    print('-='*17)

def geraMatriz(x,y):
    matrizCadeiras = list()
    for i in range(x):
        marcarFilas = list()
        for j in range(y):
            marcarFilas.append(0)
        matrizCadeiras.append(marcarFilas)
    return matrizCadeiras

def imprimeMatriz(x):
    for c,i in enumerate(x):
        print(c+1,i)
    print('   1  2  3  4  5  6  7')

def marcarCadeira(x,y,z):
    teatro = x
    if teatro[y-1][z-1] == 0:
        teatro[y-1][z-1] = 1    
        return teatro
    if teatro[y-1][z-1] == 1:
        return False
        
def listar_cadeiras_disponiveis(matriz):
    disponiveis = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == False:
                disponiveis.append(j+1)
        print(f'Fila {i+1}: {disponiveis}')
        disponiveis = []       

def desmarcarCadeira(x,y,z):
    teatro2 = x
    if teatro2[y-1][z-1] == 1:
        teatro2[y-1][z-1] = 0 
        return teatro2
    if teatro2[y-1][z-1] == 0:
        return False

        
