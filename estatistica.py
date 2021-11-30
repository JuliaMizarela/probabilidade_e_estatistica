import numpy as np
import matplotlib.pyplot as plt


def modelo_uniforme_discreto(k):
    # Variáveis discretas com chances iguais de ocorrências
    # Sair qualquer face de um dado honesto, onde k é o número de faces, 
    # Sorteado qualquer bilhete de uma rifa, onde k é o número de bilhetes
    pX = (1/k)
    return pX

def modelo_binomial(k):
    # Variável discreta com uma chance fixa de ocorrência/sucesso
    # A vairável só pode ter valores de sucesso ou fracasso
    # A pessoa examinada está doente, o jovem concluiu o segundo grau
    pSucesso = 1/k
    pFracasso = 1 - pSucesso
    return pSucesso

def realizar_ensaios_de_Bernoulli(pSucesso: float, sucessosDesejados: int, repeticoes: int) -> float:
    fatorial = np.math.factorial
    binomio = fatorial(repeticoes)/(fatorial(sucessosDesejados)*fatorial(repeticoes-sucessosDesejados))
    pX = binomio * (pSucesso**sucessosDesejados) * ((1-pSucesso)**(repeticoes-sucessosDesejados))
    print(f"{repeticoes}!/({sucessosDesejados}!{repeticoes-sucessosDesejados}!) . {pSucesso : .4f}^{sucessosDesejados} . {1- pSucesso : .4f}^{repeticoes -sucessosDesejados} = {pX : .4f}")
    return pX

def usar_ensaios_de_Bernoulli(pSucesso: float, sucessosDesejados: int, repeticoes: int) -> float:
    fatorial = np.math.factorial
    binomio = fatorial(repeticoes)/(fatorial(sucessosDesejados)*fatorial(repeticoes-sucessosDesejados))
    pX = binomio * (pSucesso**sucessosDesejados) * ((1-pSucesso)**(repeticoes-sucessosDesejados))
    return pX

exemplo_Bernoulli_1 = f"\nUm dado é lançado 50 vezes e quer se saber qual a probabilidade de 8 lançamentos darem a face 6"
print(exemplo_Bernoulli_1)
print(f"{realizar_ensaios_de_Bernoulli(1/6, 8, 50): .4f}")
exemplo_Bernoulli_2 = f"\nAs estacas para a fundação de um préidio devem atigir 15m de profundidade. A cada 5m os operários verificam se será necessário tomar medidas em função do solo, cuja probabilidade é de 0,1, que aumentam o valor final da obra em 50 UPCs(unidade padrão de construção). Como se comportará a variável aumento do custo final da obra"
print(exemplo_Bernoulli_2)
print("sem custo adicional\n", f"{realizar_ensaios_de_Bernoulli(0.9, 3, 3) : .4f}")
print("custo adicional de 50\n", f"{realizar_ensaios_de_Bernoulli(0.1, 1, 3)  : .4f}")
print("custo adicional de 100\n", f"{realizar_ensaios_de_Bernoulli(0.1, 2, 3)  : .4f}")
print("custo adicional de 150\n", f"{realizar_ensaios_de_Bernoulli(0.1, 3, 3)  : .4f}")
exemplo_Bernoulli_3 = "\nUma prova de 20 questões independentes, cada uma de V ou F. Se um aluno responder a esmo, qual a probabilidade de tirar 5?"
print(exemplo_Bernoulli_3)
print(f"{realizar_ensaios_de_Bernoulli(0.5, 10, 20): .4f}")

def usar_ensaios_de_Bernoulli(pSucesso: float, sucessosDesejados: int, repeticoes: int) -> float:
    fatorial = np.math.factorial
    binomio = fatorial(repeticoes)/(fatorial(sucessosDesejados)*fatorial(repeticoes-sucessosDesejados))
    pX = binomio * (pSucesso**sucessosDesejados) * ((1-pSucesso)**(repeticoes-sucessosDesejados))
    return pX

exemplo_Bernoulli_3a = "\nPara uma prova de 20 questões independentes, cada uma de V ou F, qual o gráfico de probabilidades gerado com ensaios de Bernoulli?"
print(exemplo_Bernoulli_3a)
plt.bar(range(0, 20), [usar_ensaios_de_Bernoulli(0.5, x, 20) for x in range(0, 20)])
plt.show()
exemplo_Bernoulli_4 = "\nPara uma prova de 20 questões independentes, cada uma com cinco opções de resposta, qual o gráfico de probabilidades gerado com ensaios de Bernoulli?"
print(exemplo_Bernoulli_4)
plt.bar(range(0, 20), [usar_ensaios_de_Bernoulli(0.2, x, 20) for x in range(0, 20)])
plt.show()



# Probabilidade de tirar 4 caras muitos lançamentos de em 4 moedas 
np.random.seed(44)
random_numbers = np.random.random(size=4)
print(random_numbers)

coroas = random_numbers < 0.5
print(coroas)
print(np.sum(coroas))

# Simualções com "hacker-statistics"
total_quatro_caras = 0
lancamentos = 100000
for _ in range(lancamentos): # para cada lançamento
    caras = np.random.random(size=4)<0.5 # obtenho quatro numeros aleatórios
    n_caras_no_lancamento = np.sum(caras) # conto menores que 0.5
    if n_caras_no_lancamento == 4: # se eu contar os quatro menores que 0.5
        total_quatro_caras += 1  # aumento meu total de 4 caras em 4 
print(total_quatro_caras/lancamentos) 


def simular_ensaios_de_bernoulli(pSucesso: float, kEnsaios: int) -> float:
    n_sucessos = 0
    for _ in range (kEnsaios):
        if np.random.random() < pSucesso:
            n_sucessos += 1
    return n_sucessos


print(simular_ensaios_de_bernoulli(0.5**4, 100000)/100000)
print(simular_ensaios_de_bernoulli(0.5**2, 100000)/100000)
print(simular_ensaios_de_bernoulli((1/6)**1, 100000)/100000)


def usar_modelo_geometrico(pSucesso, kEnsaiosPrecedemSucesso):
    pX = pSucesso*((1-pSucesso)**kEnsaiosPrecedemSucesso)
    return pX 


def realizar_modelo_geometrico(pSucesso, kEnsaiosPrecedemSucesso):
    print(f"Px = {pSucesso  : .4f}(1-{pSucesso : .4f})^{kEnsaiosPrecedemSucesso} = {pSucesso*((1-pSucesso)**kEnsaiosPrecedemSucesso) : .4f} ")


exemplo_modelo_geometrico1 = "\nQuando você percorre uma avenida, a probabilidade de encontrar o sinal aberto é de 25%. Qual a probabilidade de encontrar o sinal aberto apenas na quinta vez que você passar?"
print(exemplo_modelo_geometrico1)
realizar_modelo_geometrico(0.25, 4)
exemplo_modelo_geometrico2 = "\nFaça um estudo da probabildade do número de lançamentos de um dados para obter pela primeira vez a face com o número 1"
print(exemplo_modelo_geometrico2)
plt.bar(range(36), [usar_modelo_geometrico(1/6, x) for x in range(36)])
plt.show()


def usar_modelo_poisson(lambdaTaxaOcorrencias, kOcorrencias):
    # A taxa é constante, os eventos são independentes e não-concomitantes
    # Unidade de medida contínua, variável aleatória discreta
    # Número de defeitos por cm², número de chamadas telefôncias por minuto
    fatorial = np.math.factorial
    e = np.math.e
    return ((e**(-lambdaTaxaOcorrencias))*lambdaTaxaOcorrencias**kOcorrencias)/fatorial(kOcorrencias)


def realizar_modelo_poisson(lambdaTaxaOcorrencias, kOcorrencias):
    # Unidade de medida contínua, variável aleatória discreta
    # Número de defeitos por cm², número de chamadas telefôncias por minuto
    fatorial = np.math.factorial
    e = np.math.e
    pX = ((e**(-lambdaTaxaOcorrencias))*lambdaTaxaOcorrencias**kOcorrencias)/fatorial(kOcorrencias)
    print(f"(e^{-lambdaTaxaOcorrencias} . {lambdaTaxaOcorrencias}^{kOcorrencias})/{kOcorrencias}!  = {pX : .4f}")


exemplo_modelo_poisson1 = "\nEm um posto de saúde chegam 4 pessoas por hora, e essa taxa é bem aproximada pela distribuição de Poisson. Determine a probabilidade não chegar ninguém em meia hora e a probabilidade de chegarem 5 pessoas em meia hora"
print(exemplo_modelo_poisson1)
realizar_modelo_poisson(2, 0)
realizar_modelo_poisson(2, 5)

exemplo_modelo_poisson2a = "\nEm um posto de saúde chegam 4 pessoas por hora, e essa taxa é bem aproximada pela distribuição de Poisson. Qual o gráfico de probabilidade para a chegada de x pessoas em uma hora?"
print(exemplo_modelo_poisson2a)
plt.bar(range(12), [usar_modelo_poisson(4, x) for x in range(12)] )
plt.show()
exemplo_modelo_poisson2b = "\nEm um posto de saúde chegam 4 pessoas por hora, e essa taxa é bem aproximada pela distribuição de Poisson. Qual o gráfico de probabilidade para a chegada de x pessoas em meia?"
print(exemplo_modelo_poisson2b)
plt.bar(range(12), [usar_modelo_poisson(2, x) for x in range(12)] )
plt.show()

exemplo_modelo_poisson3 = "\nUm tecido apresenta defeitos que podem ser aproximados pelo modelo de Poisson com uma media de 0,2 defeitos por m². Determine a probabilidade de que em 6m² existam menos que 2 defeitos"
# A amostra tem 6m². A taxa (lambda) seria de 6 . 0,2 = 1,2 defeitos / 6m² 
# Já o k é < 2, então queremos k = 0 e k = 1
print(exemplo_modelo_poisson3)
realizar_modelo_poisson(1.2, 0)
realizar_modelo_poisson(1.2, 1)
print (f"{usar_modelo_poisson(1.2, 0) : .4f} + {usar_modelo_poisson(1.2, 1) : .4f} =  {(usar_modelo_poisson(1.2, 0) + usar_modelo_poisson(1.2, 1)) : .4f}")

exemplo_modelo_poisson4 = "\nUma molécula emite partículas radioativas seguindo o modelo de Poisson, a uma taxa média de ocorrência de 5 partículas por minuto. Calcule a probabilidade de haver mais de 2 emissões por minuto"
# Podemos calcular k = 0, 1 e 2 e somar, depois subtrair de 1.
print(exemplo_modelo_poisson4)
realizar_modelo_poisson(5, 0)
realizar_modelo_poisson(5, 1)
realizar_modelo_poisson(5, 2)
print (f"1 - ({usar_modelo_poisson(5, 0) : .4f} + {usar_modelo_poisson(5, 1) : .4f} + {usar_modelo_poisson(5, 2) : .4f}) = {(1 - (usar_modelo_poisson(5, 0) + usar_modelo_poisson(5, 1)  + usar_modelo_poisson(5, 2))) : .4f}")


def combinacao(n, k):
    fatorial = np.math.factorial
    return fatorial(n)/(fatorial(k)*fatorial(n-k))


def stringfy_combinacao(n, k):
    s = f" {n}!/{k}!({n}-{k})! "
    return s


def usar_modelo_hipergeometrico(populacao, sucessoPopulacao, amostra, sucessoAmostra):
    n = populacao # Todos os objetos
    m = sucessoPopulacao # Objetos do tipo indesejado na pop
    # m - n seriam os objetos do tipo desejad que existem na pop
    r = amostra # Tamanho da amostra
    k = sucessoAmostra # Objetos do tipo indesejado na amostra
    # r - k seriam os objetos do tipo desejado que existem na amostra
    fatorial = np.math.factorial
    pX = ( (fatorial(m)/(fatorial(k)*(fatorial(m-k))) * (fatorial(n-m)/(fatorial(r-k)*fatorial((n-m)-(r-k))) )) / (fatorial(n)/(fatorial(r)*fatorial(n-r))))
    return pX


def realizar_modelo_hipergeometrico(pop, sucessoPop, amostra, sucessoAmostra):
    resultado = (combinacao(sucessoPop, sucessoAmostra) * combinacao(pop - sucessoPop, amostra - sucessoAmostra)) / combinacao(pop, amostra)
    s1 = ""+stringfy_combinacao(sucessoPop, sucessoAmostra)+f" . "+stringfy_combinacao(pop - sucessoPop, amostra - sucessoAmostra)+f"  / "+stringfy_combinacao(pop, amostra)
    s2 = f"{combinacao(sucessoPop, sucessoAmostra) : .4f} . {combinacao(pop - sucessoPop, amostra - sucessoAmostra) : .4f}  / {combinacao(pop, amostra) : .4f} = {resultado : .4f}"
    print(s1+"\n"+s2)


exemplo_modelo_hipergeometrico1a = "\nNuma caixa de 10 lâmpadas, 2 são defeituosas. Extraída uma amostra de 4 lâmpadas, determine a probabilidade de nenhuma ter feito"
print(exemplo_modelo_hipergeometrico1a)
realizar_modelo_hipergeometrico(10, 2, 4, 0)

exemplo_modelo_hipergeometrico1b = "\nNuma caixa de 10 lâmpadas, 2 são defeituosas. Extraída uma amostra de 4 lâmpadas, determine a probabilidade de haver pelo menos duas defeituosas"
print(exemplo_modelo_hipergeometrico1b)
realizar_modelo_hipergeometrico(10, 2, 4, 0) # nenhuma defeituosa
realizar_modelo_hipergeometrico(10, 2, 4, 1) # uma defeituosa
print(f"{usar_modelo_hipergeometrico(10, 2, 4, 0) : .4f} + {usar_modelo_hipergeometrico(10, 2, 4, 1) : .4f} {(usar_modelo_hipergeometrico(10, 2, 4, 0) + usar_modelo_hipergeometrico(10, 2, 4, 1)): .4f}")