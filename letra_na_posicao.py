palavra = '' #variável que armazenerá a palavra a ser processada.
option = '2' #opção de comando, será setada pelo usuário no fim do programa.

def nova_palavra(): #função executada quando uma nova palavra deve ser declarada para ser processada.
    global palavra #resgata na função a variável de escopo global.
    palavra = input('Palavra a ser repetida: ') #atualiza a variável "palavra" conforme entrada do usuário.
    valid = False #variável que valida a entrada do usuário.
    while valid != True: #validação de entrada do usuário.
        try:
            posicao = int(input('Posição a ser buscada: '))
            valid = True
        except:
            print('Entrada inválida! Digite um número inteiro.')
    print(f'Letra na posição {posicao}: {palavra[(posicao%len(palavra))-1]}') #resultado do processamento.
    
def nova_consulta(): #função executada quando não se precisa declarar uma nova palavra a ser processada, a função aproveita o conteúdo atual da variável "palavra".
    global palavra #resgata na função a variável de escopo global.
    valid = False #variável que valida a entrada do usuário.
    while valid != True: #validação de entrada do usuário.
        try:
            posicao = int(input('Posição a ser buscada: '))
            valid = True
        except:
            print('Entrada inválida! Digite um número inteiro.')
    print(f'Letra na posição {posicao} : {palavra[(posicao%len(palavra))-1]}') #resultado do processamento.

while option != '0': #loop que mantém o programa funcionando após a primeira consulta.
    if option == '1':
        nova_consulta()
    if option == '2':
        nova_palavra()
    option = input('Digite 1 para nova busca, 2 para trocar a palavra ou 0 para encerrar o programa\n')