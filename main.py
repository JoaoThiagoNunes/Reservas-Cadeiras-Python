import function

filasTeatro = 7
qtCadeiras = 7
teatro = function.geraMatriz(filasTeatro,qtCadeiras)

while True:
    function.opçoesDisponiveis()
    opçãoCliente = int(input('Qual opção deseja? '))

    if opçãoCliente == 1:
        function.imprimeMatriz(teatro)
        marcarFila = int(input('Informe a fila que deseja: '))
        marcarCadeira = int(input('Qual a cadeira? '))
        print('-='*11)

        #verificaMarcação recebe a função para saber se vai retornar false ou não
        verificaMarcação = function.marcarCadeira(teatro,marcarFila,marcarCadeira)
        if verificaMarcação == False:
            function.imprimeMatriz(teatro)
            print('ERRO, CADEIRA JÁ ESTÁ MARCADA!')
        else: 
            function.imprimeMatriz(teatro)
            print('Cadeira reservada com sucesso!')
            
    if opçãoCliente == 2:
        function.imprimeMatriz(teatro)

    if opçãoCliente == 3:
        function.listar_cadeiras_disponiveis(teatro)

    if opçãoCliente == 4:
        function.imprimeMatriz(teatro)
        desmarcarFila = int(input('Informe a fila que deseja desmarcar: '))
        desmarcarCadeira = int(input('Qual a cadeira? '))
        print('-='*11)

        #verificaDesmarcação recebe a função para saber se vai retornar false ou não
        verificaDesmarcação = function.desmarcarCadeira(teatro,desmarcarFila,desmarcarCadeira)
        if verificaDesmarcação == False:
            function.imprimeMatriz(teatro)
            print('ERRO, NÃO EXISTE NENHUMA RESERVA NESSA CADEIRA!')
        else:
            function.imprimeMatriz(teatro)
            print('Cadeira desmarcada com sucesso!')

            

