#CLASSE CONTA BANCARIA E CONSTRUTOR INIT, RESPONSAVEL POR CRIAR A CONTA
class Conta_bancária:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo =  saldo

   #PRIMEIRO METODO: EXIBIR TITULAR E SALDO ATUAL        
    def exibir_saldo(self):
        print(f'TITULAR DA CONTA: {self.titular} \nSALDO BANCÁRIO ATUAL: R${self.saldo}')

    #SEGUNDO METODO: EXIBIR TITULAR E VALOR DEPOSITADO NA CONTA.
    def saldo_atual(self):
        self.saldo = float(input('QUANTO VOCÊ QUER DEPOSITAR? ')) #PERGUNTA O VALOR E ATUALIZA O SALDO
        print(f'FOI DEPOSITADO O VALOR DE: {self.saldo}')
        print(f'TITULAR DA CONTA: {self.titular} \nSALDO BANCÁRIO ATUAL: R${self.saldo}')

#OBJETO DA CLASSE 
titular_saldo = Conta_bancária('Ariel', 0.0)

#APRESENTA O TITULAR E O SALDO ATUAL
titular_saldo.exibir_saldo()
titular_saldo.saldo_atual()