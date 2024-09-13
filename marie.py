"""
Esse programa lê entradas de dados à partir do teclado.

O programa lê as entradas até que encontre a exceção de fim de arquivo (EOFError).
Quando encontrar o fim de arquivo, o programa não irá ler o último caractere que foi fornecido de entrada,
portanto este não poderá ser um caractere significativo para a interpretação do código binário.

Para entradas de dados que possuem quaisquer caracteres da parte de Latin Básico da tabela Unicode como 
ruído para a entrada (mas que não adicione mais bits binários em relação à entrada sem ruído), o programa
executará normalmente.

Para entradas onde haja somente caracteres binários, sem qualquer quebras de linha, espaços em branco ou 
caracteres de ruído, o programa executará normalmente.
"""


mnemonicos = ["JnS", "Load", "Store", "Add", "Subt", "Input", "Output", "Halt", "Skipcond", "Jump", "Clear", "AddI", "JumpI", "LoadI", "StoreI"]
instrucoes_requisitadas = []
enderecos_acessados = []
fim_de_leitura = False

entrada = ''  #Vai armazenar a entrada toda de dados
entrada_tratada = ''  #Vai armazenar somente os dígitos binários que vieram na entrada original

# Realiza a leitura de toda a entrada de dados
while not fim_de_leitura:
    try:
        entrada += input()
    except EOFError:
        fim_de_leitura = True

# Faz a seleção somente dos dígitos binários (0 e 1) que vieram na entrada
for i in entrada:
    if i == '0' or i == '1':
        entrada_tratada += i

# Separa as instruções dos endereços acessados
for i in range(0, len(entrada_tratada), 16):
    instrucao_bin = entrada_tratada[i:i+4]
    endereco_bin = entrada_tratada[i+4:i+16]

    x = len(endereco_bin)
    
    # Guarda a instrução requisitada e o endereço acessado por essa instrução
    if len(instrucao_bin) == 4 and len(endereco_bin) == 12 and int(instrucao_bin, 2) <= 14:
        instrucoes_requisitadas.append(mnemonicos[int(instrucao_bin, 2)])
        enderecos_acessados.append(int(endereco_bin, 2))

print("\nInstruções:\n")
for i in instrucoes_requisitadas:
    print(i)
print()

print("Endereços acessados:\n")
for i in enderecos_acessados:
    if i != 0:
        print(i)
        print()
