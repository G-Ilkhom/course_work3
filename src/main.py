import json
import os
from config import ROOT_DIR
from src.utils import get_all_operations

OPERATIONS_PATH = os.path.join(ROOT_DIR, '', 'operations.json')
all_operations = get_all_operations(OPERATIONS_PATH)
all_operations = [operations for operations in all_operations if operations != {}]
filtered_operations = list(filter(lambda operation: operation["state"] == "EXECUTED", all_operations))
sorted_operations = sorted(filtered_operations[:5], key=lambda operation: operation['date'], reverse=True)