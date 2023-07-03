import requests


class BankRequest():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20200302&json'

    def __init__(self, yy, mm, dd):
        self.year = yy
        self.month = mm
        self.day = dd
        self.str = f'{yy}{0}{mm}{0}{dd}'
        self.new_url = self.url.replace('20200302', self.str)

    @property
    def get_request(self):
        try:
            res = requests.get(self.new_url, timeout=0.5)
        except:
            return 'Error, time limit exceeded'
        else:
            if 199 < res.status_code < 300:
                if res.headers.get('Content-Type') == 'application/json; charset=utf-8':
                    res_json = res.json()
                    with open('ExchangeRates.txt', 'wt') as file:
                        file.write(f'Current date is: {self.year}/{self.month:0>2d}/{self.day:0>2d}\n')
                        for dct in res_json:
                            file.write(f"{dct['cc']} to UAH: {dct['rate']}\n")
                    return res

    def __repr__(self):
        return f'{self.get_request}'


bank = BankRequest(2011, 5, 5)
print(bank)


