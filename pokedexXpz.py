## CODE BY: xpz

try:
    with open("pokedex.txt", "r") as arquivo:
        pokedex = [linha.strip() for linha in arquivo]
except FileNotFoundError:
    pokedex = []

def salvar_pokedex():
    with open("pokedex.txt", "w") as arquivo:
        for pokemon in pokedex:
            arquivo.write(pokemon + "\n")

def listar_poke():
    print("\n" + "-" * 30)
    print("=== SUA POKEDEX ===")

    if pokedex:
        print(f"Você possui {len(pokedex)} pokémon(s):\n")

        for pokemon in sorted(pokedex):
            print(f"• {pokemon.title()}")
    else:
        print("Pokedex vazia.")

    print("-" * 30)
    input("\nPressione ENTER para voltar ao menu...")

def add_poke():
    nome = input("\nAdicione o pokémon desejado: ").strip().lower()

    if nome == "":
        print("\nNome inválido.")
    elif nome in pokedex:
        print("\nEste pokémon já está na sua pokedex!")
    else:
      pokedex.append(nome)
    salvar_pokedex()
    print(f"\n{nome.title()} adicionado.")

def remover_poke():
    nome = input("\nDigite o pokémon que deseja remover: ").strip().lower()

    if nome in pokedex:
        pokedex.remove(nome)
        salvar_pokedex()
        print(f"\n{nome.title()} removido da pokedex.")

    else:
        print("\nEsse pokémon não está na sua pokedex.")
        
def sair_poke():
    print("\nSaindo...")

print("Olá, este é meu sistema de Pokédex Pokémon em Python. by: xpz".upper())
user = input("Por favor, digite seu nickname: ").strip()

print(f"\nBem-vindo à sua Pokedex, {user}!")

senha = input("Digite a senha para acessar a Pokedex: ")
tentativas = 3

while senha.strip().lower() != "s12" and tentativas > 1:
    tentativas -= 1
    print(f"\nSenha incorreta. Você ainda tem {tentativas} tentativa(s).")
    senha = input("Digite a senha para acessar a Pokedex: ")

if senha.strip().lower() != "s12":
    print("\nNúmero máximo de tentativas excedido. Acesso negado.")
else:
    print(f"\n== BEM-VINDO(A) À SUA POKEDEX, {user.upper()}! ==")

    while True:
        print("\n" + "=" * 30)
        print("        MENU POKEDEX")
        print("=" * 30)
        print("1 - Ver Pokédex")
        print("2 - Adicionar Pokémon")
        print("3 - Remover Pokémon")
        print("4 - Sair")
        print("=" * 30)

        option = input("👉 Digite qual opção deseja: ").strip()

        if option == "1":
            listar_poke()
        elif option == "2":
            add_poke()
        elif option == "3":
            remover_poke()
        elif option == "4":
            sair_poke()
            break
        else:
            print("\nOpção inválida! Escolha 1, 2, 3 ou 4.")