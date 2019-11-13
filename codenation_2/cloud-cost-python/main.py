from calendar import monthcalendar
import calendar

class CloudCost():

    def __init__(self):
        self.valor_mensagem = 0.00000040
        self.execucao_funcao = 0.0000002
        self.execucao_tempo = 0.0002080
        self.funcao_disparada = 2

    def lambda_execution(self, segundos_funcao = 3):
        valor_segundos = self.execucao_tempo * segundos_funcao 
        valor_total = valor_segundos + self.execucao_funcao
        return valor_total

    def app_execution(self, execution_times):
        valor_cada_funcao = self.lambda_execution()
        total_item = (valor_cada_funcao * self.funcao_disparada) + self.valor_mensagem
        return total_item * execution_times

    def month(self, execution_times, month_of_year):
        days = calendar.mdays[month_of_year]
        total = self.app_execution(execution_times) * days
        return total
    
    def year(self, execution_times):
        total = []
        for mes in range(1, 13):
            total.append(self.month(execution_times, mes))
        return total
