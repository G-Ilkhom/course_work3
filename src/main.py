from config import OPERATIONS_PATH
from utils import transaction

for operation in range(5):
    transfer = transaction(OPERATIONS_PATH)
    print(transfer.results(operation))