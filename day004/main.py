# "\033[(valor da cor)m"

#  Day 004 - 100 Days of Code [17 Janeiro, 2024]

print("=== \033[33m Seu Simulador de Aventura \033[0m ===")
print("""
Olá, jovem herói! 
Você será questionado algumas vezes
e então criaremos para você uma\033[32m história incrível \033[0m
com VOCÊ como a ESTRELA! 🤩
""")
print()
hero = input("Seu nome: ")
enemy = input("Nome do seu pior inimigo: ")
power = input("Seu super poder: ")
print()
print(f"""A história começa quando {hero} se aproxima de um castelo ameaçador. De repente, um raio atinge o chão aos pés de {hero}.\n\033[31m"- Nossa batalha final começa agora, seu verme insolente!"\033[0m grita o malvado {enemy}, claramente sem perceber que {hero} possui o poder de {power}, o que significa que seu inimigo tá perdido.""")
print()
print(f"""As particulas do poder de {hero} o envolvem, formando uma aura grandiosa. {enemy}, apesar de sua bravura, começa a recuar ao ver o poder impressionante de {hero}. O herói avança, lançado ataques de {power} em direção ao inimigo.""")
print()
print(f"""{hero} e {enemy} estão agora envolvidos em uma batalha épica, onde raios de {power} e sombras se entrelaçaram. {hero}, com sua habilidade única, cria uma escudo de {power} que o protege dos ataques de {enemy}.""")
print()
print(f"""{hero} emerge triunfante, tendo derrotado seu pior inimigo. A gisgantesca aura de {power} que antes eram ameaçadoras agora se acalmam, revelando um novo dia para o reino. {hero}, o herói com o poder de {power}, é aclamado como salvador da terra e sua coragem é cantada em canções por gerações.""")


# Color     / Valor

# Default   /   0
# Black     /  30
# Red       /  31
# Green     /  32
# Yellow    /  33
# Blue      /  34
# Purple    /  35
# Cyan      /  36
# White     /  37

# "\033[(valor da cor)m"

# "O homem forte se defende sozinho, o homem MAIS FORTE defende os outros