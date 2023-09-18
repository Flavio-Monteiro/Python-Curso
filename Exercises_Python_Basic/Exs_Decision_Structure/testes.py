# Exemplo de condição composta com condições aninhadas
idade = 25
tem_carteira_de_motorista = True

if idade >= 18:
    print("Você é maior de idade.")
    if tem_carteira_de_motorista:
        print("Você também tem uma carteira de motorista.")
    else:
        print("Você não tem uma carteira de motorista.")
else:
    print("Você é menor de idade.")

# Este é um exemplo simples. Você pode aninhar quantas condições desejar,
# dependendo da lógica do seu programa.
