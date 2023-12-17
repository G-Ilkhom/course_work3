from config import OPERATIONS_PATH
from src.utils import transaction


def test_date_and_description():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.get_date_and_description(1) == '17.05.2019 Перевод с карты на карту'
    assert test_data.get_date_and_description(0) == '03.12.2019 Перевод с карты на карту'
    assert test_data.get_date_and_description(2) == '18.04.2019 Открытие вклада'
    assert test_data.get_date_and_description(3) == '14.02.2019 Перевод организации'


def test_payment_transfer():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.get_payment_transfer(0) == 'MasterCard 1796 81** **** 9527  -> Visa Classic 7699 85** **** 9288 '
    assert test_data.get_payment_transfer(1) == 'МИР 8021 88** **** 6544  -> Visa Gold 8702 71** **** 3248 '
    assert test_data.get_payment_transfer(2) == 'Счет **4865'
    assert test_data.get_payment_transfer(3) == 'Visa Classic 4610 24** **** 6784  -> Счет **2700'
    assert test_data.get_payment_transfer(4) == 'Visa Platinum 2241 65** **** 8487  -> Счет **8486'



def test_operation_amount():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.get_operation_amount(0) == '17628.50 USD'
    assert test_data.get_operation_amount(1) == '74604.56 USD'
    assert test_data.get_operation_amount(2) == '73778.48 руб.'


def test_results():
    test_data = transaction(OPERATIONS_PATH)
    assert test_data.results(0) == ('03.12.2019 Перевод с карты на карту\nMasterCard 1796 81** **** 9527  -> Visa Classic 7699 85** **** 9288 \n17628.50 USD\n')
    assert test_data.results(1) == ('17.05.2019 Перевод с карты на карту\nМИР 8021 88** **** 6544  -> Visa Gold 8702 71** **** 3248 \n74604.56 USD\n')


