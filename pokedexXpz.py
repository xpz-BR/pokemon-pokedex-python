## code by: xpzz

## Login Menu

print("Olá, este é meu sistema de pokédex pokémon em python. by: xpz")
user = input("Por favor, digite seu nickname: ")
print(f"Bem-vindo a sua Pokedex, {user}!")

senha = input("Digite a senha para acessar a Pokedex: ")
tentativas = 3
while senha.strip().lower() != "squirtle12" and tentativas > 0:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha para acessar a Pokedex: ")
    tentativas -= 1

if tentativas == 0:
    print("Número máximo de tentativas excedido. Acesso negado.")
else:
    print(f" == BEM-VINDO(A) À SUA POKEDEX, {user.upper()}! ")

################ Menu Pokedex #################

## funcões
def listar_poke():
    if pokedex:
        print("=== SUA POKEDEX ===")
        print(f"Você possui {len(pokedex)} pokémon(s) em sua pokedex!")

        for pokemon in pokedex:
            print(pokemon)

    else:
        print("Pokedex vazia.")

def add_poke():
    nome = input("Adicione o pokémon desejado: ").strip().lower()

    if nome in pokedex:
        print("Este pokemon ja está em sua pokedex!")

    else:
        pokedex.append(nome)
        print(f"{nome} adicionado.")

def sair_poke():
    print("Saindo...")

## lista
pokedex = []

## opções
while True:
    print("1 - Ver Pokédex\n2 - Adicionar Pokémon\n3 - Sair")

    option = input("Digite qual opção deseja: ")
    if option == "1":
        listar_poke()

    elif option == "2":
        add_poke()

    elif option == "3":
        sair_poke()
        break
