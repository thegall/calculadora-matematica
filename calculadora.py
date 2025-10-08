import math
import sys

class Calculadora:
    def __init__(self):
        self.historico = []
    
    def adicionar_ao_historico(self, operacao, resultado):
        """Adiciona operação ao histórico"""
        self.historico.append(f"{operacao} = {resultado}")
    
    def somar(self, a, b):
        """Soma dois números"""
        resultado = a + b
        self.adicionar_ao_historico(f"{a} + {b}", resultado)
        return resultado
    
    def subtrair(self, a, b):
        """Subtrai dois números"""
        resultado = a - b
        self.adicionar_ao_historico(f"{a} - {b}", resultado)
        return resultado
    
    def multiplicar(self, a, b):
        """Multiplica dois números"""
        resultado = a * b
        self.adicionar_ao_historico(f"{a} * {b}", resultado)
        return resultado
    
    def dividir(self, a, b):
        """Divide dois números"""
        if b == 0:
            raise ValueError("Erro: Divisão por zero!")
        resultado = a / b
        self.adicionar_ao_historico(f"{a} / {b}", resultado)
        return resultado
    
    def potencia(self, base, expoente):
        """Calcula a potência"""
        resultado = base ** expoente
        self.adicionar_ao_historico(f"{base} ^ {expoente}", resultado)
        return resultado
    
    def raiz_quadrada(self, numero):
        """Calcula a raiz quadrada"""
        if numero < 0:
            raise ValueError("Erro: Não é possível calcular raiz quadrada de número negativo!")
        resultado = math.sqrt(numero)
        self.adicionar_ao_historico(f"√{numero}", resultado)
        return resultado
    
    def raiz_n(self, numero, indice):
        """Calcula a raiz n-ésima"""
        if numero < 0 and indice % 2 == 0:
            raise ValueError("Erro: Não é possível calcular raiz par de número negativo!")
        if indice == 0:
            raise ValueError("Erro: Índice da raiz não pode ser zero!")
        resultado = numero ** (1/indice)
        self.adicionar_ao_historico(f"^{indice}√{numero}", resultado)
        return resultado
    
    def logaritmo(self, numero, base=10):
        """Calcula o logaritmo"""
        if numero <= 0:
            raise ValueError("Erro: Logaritmo de número negativo ou zero!")
        if base <= 0 or base == 1:
            raise ValueError("Erro: Base do logaritmo deve ser positiva e diferente de 1!")
        if base == 10:
            resultado = math.log10(numero)
            self.adicionar_ao_historico(f"log({numero})", resultado)
        elif base == math.e:
            resultado = math.log(numero)
            self.adicionar_ao_historico(f"ln({numero})", resultado)
        else:
            resultado = math.log(numero, base)
            self.adicionar_ao_historico(f"log_{base}({numero})", resultado)
        return resultado
    
    def seno(self, angulo_graus):
        """Calcula o seno de um ângulo em graus"""
        angulo_radianos = math.radians(angulo_graus)
        resultado = math.sin(angulo_radianos)
        self.adicionar_ao_historico(f"sin({angulo_graus}°)", resultado)
        return resultado
    
    def cosseno(self, angulo_graus):
        """Calcula o cosseno de um ângulo em graus"""
        angulo_radianos = math.radians(angulo_graus)
        resultado = math.cos(angulo_radianos)
        self.adicionar_ao_historico(f"cos({angulo_graus}°)", resultado)
        return resultado
    
    def tangente(self, angulo_graus):
        """Calcula a tangente de um ângulo em graus"""
        angulo_radianos = math.radians(angulo_graus)
        resultado = math.tan(angulo_radianos)
        self.adicionar_ao_historico(f"tan({angulo_graus}°)", resultado)
        return resultado
    
    def fatorial(self, numero):
        """Calcula o fatorial de um número"""
        if numero < 0:
            raise ValueError("Erro: Fatorial de número negativo!")
        if numero != int(numero):
            raise ValueError("Erro: Fatorial apenas para números inteiros!")
        resultado = math.factorial(int(numero))
        self.adicionar_ao_historico(f"{int(numero)}!", resultado)
        return resultado
    
    def porcentagem(self, valor, percentual):
        """Calcula porcentagem"""
        resultado = (valor * percentual) / 100
        self.adicionar_ao_historico(f"{percentual}% de {valor}", resultado)
        return resultado
    
    def modulo(self, a, b):
        """Calcula o resto da divisão (módulo)"""
        if b == 0:
            raise ValueError("Erro: Divisão por zero!")
        resultado = a % b
        self.adicionar_ao_historico(f"{a} mod {b}", resultado)
        return resultado
    
    def mostrar_historico(self):
        """Mostra o histórico de operações"""
        if not self.historico:
            print("Histórico vazio.")
            return
        print("\n=== HISTÓRICO DE OPERAÇÕES ===")
        for i, operacao in enumerate(self.historico, 1):
            print(f"{i}. {operacao}")
    
    def limpar_historico(self):
        """Limpa o histórico"""
        self.historico.clear()
        print("Histórico limpo!")

def obter_numero(mensagem):
    """Obtém um número válido do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido!")

def obter_numero_inteiro(mensagem):
    """Obtém um número inteiro válido do usuário"""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número inteiro válido!")

def menu_principal():
    """Exibe o menu principal da calculadora"""
    print("\n" + "="*50)
    print("           CALCULADORA MATEMÁTICA")
    print("="*50)
    print("1.  Operações Básicas")
    print("2.  Potenciação e Radiciação")
    print("3.  Logaritmos")
    print("4.  Funções Trigonométricas")
    print("5.  Fatorial")
    print("6.  Porcentagem")
    print("7.  Módulo")
    print("8.  Ver Histórico")
    print("9.  Limpar Histórico")
    print("0.  Sair")
    print("="*50)

def menu_operacoes_basicas():
    """Menu para operações básicas"""
    print("\n--- OPERAÇÕES BÁSICAS ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Voltar")

def executar_operacoes_basicas(calc):
    """Executa operações básicas"""
    while True:
        menu_operacoes_basicas()
        opcao = input("\nEscolha uma operação: ")
        
        if opcao == "0":
            break
        elif opcao in ["1", "2", "3", "4"]:
            try:
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                
                if opcao == "1":
                    resultado = calc.somar(a, b)
                    print(f"Resultado: {resultado}")
                elif opcao == "2":
                    resultado = calc.subtrair(a, b)
                    print(f"Resultado: {resultado}")
                elif opcao == "3":
                    resultado = calc.multiplicar(a, b)
                    print(f"Resultado: {resultado}")
                elif opcao == "4":
                    resultado = calc.dividir(a, b)
                    print(f"Resultado: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")
        else:
            print("Opção inválida!")

def executar_potenciacao_radiciacao(calc):
    """Executa operações de potenciação e radiciação"""
    print("\n--- POTENCIAÇÃO E RADICIAÇÃO ---")
    print("1. Potenciação (a^b)")
    print("2. Raiz quadrada")
    print("3. Raiz n-ésima")
    print("0. Voltar")
    
    opcao = input("\nEscolha uma operação: ")
    
    try:
        if opcao == "1":
            base = obter_numero("Digite a base: ")
            expoente = obter_numero("Digite o expoente: ")
            resultado = calc.potencia(base, expoente)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            numero = obter_numero("Digite o número: ")
            resultado = calc.raiz_quadrada(numero)
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            numero = obter_numero("Digite o número: ")
            indice = obter_numero("Digite o índice da raiz: ")
            resultado = calc.raiz_n(numero, indice)
            print(f"Resultado: {resultado}")
        elif opcao == "0":
            return
        else:
            print("Opção inválida!")
    except ValueError as e:
        print(f"Erro: {e}")

def executar_logaritmos(calc):
    """Executa operações de logaritmo"""
    print("\n--- LOGARITMOS ---")
    print("1. Logaritmo base 10")
    print("2. Logaritmo natural (ln)")
    print("3. Logaritmo base personalizada")
    print("0. Voltar")
    
    opcao = input("\nEscolha uma operação: ")
    
    try:
        if opcao == "1":
            numero = obter_numero("Digite o número: ")
            resultado = calc.logaritmo(numero, 10)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            numero = obter_numero("Digite o número: ")
            resultado = calc.logaritmo(numero, math.e)
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            numero = obter_numero("Digite o número: ")
            base = obter_numero("Digite a base: ")
            resultado = calc.logaritmo(numero, base)
            print(f"Resultado: {resultado}")
        elif opcao == "0":
            return
        else:
            print("Opção inválida!")
    except ValueError as e:
        print(f"Erro: {e}")

def executar_trigonometria(calc):
    """Executa operações trigonométricas"""
    print("\n--- FUNÇÕES TRIGONOMÉTRICAS ---")
    print("1. Seno")
    print("2. Cosseno")
    print("3. Tangente")
    print("0. Voltar")
    
    opcao = input("\nEscolha uma operação: ")
    
    try:
        if opcao in ["1", "2", "3"]:
            angulo = obter_numero("Digite o ângulo em graus: ")
            
            if opcao == "1":
                resultado = calc.seno(angulo)
                print(f"Resultado: {resultado}")
            elif opcao == "2":
                resultado = calc.cosseno(angulo)
                print(f"Resultado: {resultado}")
            elif opcao == "3":
                resultado = calc.tangente(angulo)
                print(f"Resultado: {resultado}")
        elif opcao == "0":
            return
        else:
            print("Opção inválida!")
    except ValueError as e:
        print(f"Erro: {e}")

def main():
    """Função principal"""
    calc = Calculadora()
    
    print("Bem-vindo à Calculadora Matemática!")
    print("Esta calculadora suporta todas as operações matemáticas básicas e avançadas.")
    
    while True:
        menu_principal()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            print("Obrigado por usar a calculadora!")
            sys.exit(0)
        elif opcao == "1":
            executar_operacoes_basicas(calc)
        elif opcao == "2":
            executar_potenciacao_radiciacao(calc)
        elif opcao == "3":
            executar_logaritmos(calc)
        elif opcao == "4":
            executar_trigonometria(calc)
        elif opcao == "5":
            try:
                numero = obter_numero_inteiro("Digite o número para calcular o fatorial: ")
                resultado = calc.fatorial(numero)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "6":
            try:
                valor = obter_numero("Digite o valor: ")
                percentual = obter_numero("Digite o percentual: ")
                resultado = calc.porcentagem(valor, percentual)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "7":
            try:
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.modulo(a, b)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "8":
            calc.mostrar_historico()
        elif opcao == "9":
            calc.limpar_historico()
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
