import numpy as np
from datetime import datetime, date


class ManagerDates:

    def date_is_valid(self, date):

        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except:
            return False

    def date_weekday(self, date):

        dias_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        numero_dia = date.weekday()
        dia = dias_semana[numero_dia]
        return dia

    def convert_string_to_date(self, date_str):
     
        data = ''
        retorno = ''
        try:
            data = datetime.strptime(date_str, "%d/%m/%Y")
        except:
            retorno = 'erro'

        try:
            data = datetime.strptime(date_str, "%d%m%Y")
        except:
            retorno = 'erro'

        try:
            data = datetime.strptime(date_str, "%d-%m-%Y")
        except:
            retorno = 'erro'

        if data != '':
            return data
        else:
            return False

    def get_all_dates(self, month, year):
        start = year + '-' + month
        month = int(month) + 1
        end = year + '-0' + str(month)
        days = np.arange(start, end, dtype='datetime64[D]')

        return days

    def count_days_mounth(self, month, year):
        start = year + '-' + month
        month = int(month) + 1
        end = year + '-0' + str(month)
        days = np.busday_count(start, end)
        return days

    def get_first_monday(self, year):
        start = year + '-05'
        days = np.busday_offset(start, 0, roll='forward', weekmask='Mon')
        days = days.astype(datetime)
        days_format = days.strftime('%d/%m/%Y')

        return days_format
