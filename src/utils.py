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