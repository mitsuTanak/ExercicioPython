# Intro
print("==-APROVADOR(usando media)-==")

# Var
nota1 = int(input("Informe a 1° nota: "))
nota2 = int(input("Informe a 2° nota: "))

# Calcula media
media = (nota1 + nota2)/2

# uso if ternario
alerta = "Deu uma de ESTHER!" if media<50 else "APROVADO!"

# Alerta
print(alerta)