from config import OPERATIONS_PATH
from src.utils import transaction


def test_date_and_description():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.get_date_and_description(1) == '19.11.2019 Перевод организации'
    assert test_data.get_date_and_description(0) == '07.12.2019 Перевод организации'


def test_payment_transfer():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.get_payment_transfer(0) == 'Visa Classic 2842 87** **** 9012  -> Счет **3655'
    assert test_data.get_payment_transfer(1) == 'Maestro 7810 84** **** 5568  -> Счет **2869'


def test_operation_amount():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.get_operation_amount(0) == '48150.39 USD'
    assert test_data.get_operation_amount(1) == '30153.72 руб.'


def test_results():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.results(0) == ('07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012  -> Счет **3655\n48150.39 USD\n')
    assert test_data.results(1) == ('19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568  -> Счет **2869\n30153.72 руб.\n')


