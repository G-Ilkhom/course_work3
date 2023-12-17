from json import load


class transaction:
    def __init__(self, path):
        with open(path, encoding='UTF-8') as file:
            self.data = sorted([operation for operation in load(file) if
                                len(operation) > 0 and operation['state'] == 'CANCELED' and '' in operation['description']], key=lambda x: x['date'], reverse=True)

    def get_date_and_description(self, number):
        date = self.data[number]["date"]
        description = self.data[number]['description']
        date = date.split('T')[0]
        date = '.'.join(date.split('-')[::-1])
        return f'{date} {description}'

    def get_payment_transfer(self, number):
        if 'from' not in self.data[number]:
            to_ = self.data[number]['to'].split()
            recipients = '**' + to_[1][-4:]
            return f'{to_[0]} {recipients}'
        else:
            payer_info = self.data[number]['from'].split()
            to_ = self.data[number]['to'].split()
            if to_[0] in "Счет":
                payment_method_from = payer_info[-1]
                payment_method = ''
                for i in range(0, len(payment_method_from), 4):
                    payment_method += payment_method_from[i:i + 4] + ' '
                payment_method = payment_method[:7] + '** **** ' + payment_method[-5:]
                recipients = '**' + to_[1][-4:]
                return f'{" ".join(payer_info[:-1])} {payment_method} -> {to_[0]} {recipients}'
            else:
                payment_method_from = payer_info[-1]
                payment_method_to = to_[-1]
                payment_method = ''
                recipients = ''
                for i in range(0, len(payment_method_from), 4):
                    payment_method += payment_method_from[i:i + 4] + ' '
                payment_method = payment_method[:7] + '** **** ' + payment_method[-5:]
                for i in range(0, len(payment_method_to), 4):
                    recipients += payment_method_to[i:i + 4] + ' '
                recipients = recipients[:7] + '** **** ' + recipients[-5:]
                return f'{" ".join(payer_info[:-1])} {payment_method} -> {" ".join(to_[:-1])} {recipients}'

    def get_operation_amount(self, number):
        amount = self.data[number]['operationAmount']["amount"]
        currency = self.data[number]['operationAmount']["currency"]["name"]
        return f'{amount} {currency}'

    def results(self, operation):
        return f'{self.get_date_and_description(operation)}\n{self.get_payment_transfer(operation)}\n{self.get_operation_amount(operation)}\n'