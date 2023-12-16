import json
import os
from config import ROOT_DIR
from src.utils import get_all_operations

OPERATIONS_PATH = os.path.join(ROOT_DIR, '', 'operations.json')
all_operations = get_all_operations(OPERATIONS_PATH)
all_operations = [operations for operations in all_operations if operations != {}]