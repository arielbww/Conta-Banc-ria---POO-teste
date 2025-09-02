#classe-conta-bancaria-Ariel-Nascimento-Nunes

No meu código eu criei uma classe para simular uma Conta Bancária, o nome que dei para essa classe foi Conta_bancária.

```python
class Conta_bancária:
def init(self, titular, saldo):
self.titular = titular
self.saldo =  saldo #DEFINE O TITULAR E O SALDO DA CONTA!
```

PRIMEIRO, EU CRIEI o construtor __init__, que é responsável por criar a conta. Ele define as informações iniciais, que são o titular e o saldo.

DEPOIS, CRIEI DOIS MÉTODOS. O primeiro é o exibir_saldo, que serve para mostrar na tela as informações atuais da conta.

```python
def exibir_saldo(self):
print(f'TITULAR DA CONTA: {self.titular} \nSALDO BANCÁRIO ATUAL: R${self.saldo}')
```

O SEGUNDO MÉTODO QUE CRIEI FOI o saldo_atual. A ideia dele é funcionar como uma operação de depósito. Ele usa um input() para perguntar ao usuário um valor e depois exibe uma mensagem de confirmação do valor depositado.

```python
def saldo_atual(self):
self.saldo = float(input('QUANTO VOCÊ QUER DEPOSITAR? ')) #PERGUNTA O VALOR E ATUALIZA O SALDO
print(f'FOI DEPOSITADO O VALOR DE: {self.saldo}')
print(f'TITULAR DA CONTA: {self.titular} \nSALDO BANCÁRIO ATUAL: R${self.saldo}')
```

E POR ÚLTIMO, FORA DA CLASSE, eu crio o objeto titular_saldo a partir da classe Conta_bancária, definindo 'Ariel' como o titular e 0.0 como saldo inicial. A outra linha foi comentada pois era um teste.

```python
#OBJETO DA CLASSE
titular_saldo = Conta_bancária('Ariel', 0.0) #CRIA A CONTA PARA 'ARIEL' COM SALDO 0.0
```

LOGO EM SEGUIDA, EU CHAMO OS MÉTODOS para interagir com o usuário, primeiro mostrando o saldo inicial e depois pedindo o valor do depósito.

```python
#APRESENTA O TITULAR E O SALDO
titular_saldo.exibir_saldo()
titular_saldo.saldo_atual()
```
EXEMPLO DE COMO FICOU O RESULTADO LOGO ABAIXO:

TITULAR DA CONTA: Ariel 
SALDO BANCÁRIO ATUAL: R$0.0
QUANTO VOCÊ QUER DEPOSITAR? 789.47
FOI DEPOSITADO O VALOR DE: 789.47
TITULAR DA CONTA: Ariel 
SALDO BANCÁRIO ATUAL: R$789.47
