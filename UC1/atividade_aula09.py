#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.

class SomaImparError(Exception):
    """Exceção personalizada para soma ímpar."""
    pass

def obter_numero_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def main():
    for i in range(3)
        print(f"\nGrupo {i + 1}:")
        a = obter_numero_inteiro("Digite o primeiro número inteiro: ")
        b = obter_numero_inteiro("Digite o segundo número inteiro: ")
        soma = a + b
        
        try:
            if soma % 2 != 0:
                raise SomaImparError("A soma dos números é ímpar.")
            print(f"A soma do grupo {i + 1} é: {soma}")
        except SomaImparError as e:
            print(e)

if __name__ == "__main__":
    main()