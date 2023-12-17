from json import load


class transaction:
    def __init__(self, path):
        with open(path, encoding='UTF-8') as file:
            self.data = sorted([operation for operation in load(file) if len(operation) > 0 and operation['state'] == 'EXECUTED' and 'Перевод' in operation['description']], key=lambda x: x['date'], reverse=True)

    def get_date_and_description(self, number):
        date = self.data[number]["date"]
        description = self.data[number]['description']
        date = date.split('T')[0]
        date = '.'.join(date.split('-')[::-1])
        return f'{date} {description}'

    def get_payment_transfer(self, number):
        payer_info = self.data[number]['from'].split()
        to_ = self.data[number]['to'].split()
        payment_method_from = payer_info[-1]
        payment_method = ''
        for i in range(0, len(payment_method_from), 4):
            payment_method += payment_method_from[i:i + 4] + ' '
        payment_method = payment_method[:7] + '** **** ' + payment_method[-5:]
        recipients = '**' + to_[1][-4:]
        return f'{" ".join(payer_info[:-1])} {payment_method} -> {to_[0]} {recipients}'