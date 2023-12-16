import json
import datetime

def get_all_operations(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)

def get_formatted_operation(operations: list) -> list:
    formatted_operation = []
    for operation in operations:
        if isinstance(operation, dict):
            date = datetime.datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%y")
            description = operation["description"]
            payer_info = ""
            payment_method = ""
            if "from" in operation:
                payer = operation["from"].split()
                payment_method = payer.pop(-1)
                if payer[0].lower() == "счет":
                    payment_method_from = f"**{payment_method[-4:]}"
                else:
                    payment_method_from = f"{payment_method[:4]} {payment_method[4:6]}** **** {payment_method[-4:]}"
                payer_info = " ".join(payer)
            recipients = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
            operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
            formatted_operation.append(f"""{date} {description}
{payer_info} {payment_method_from}->{recipients}
{operation_amount}""")
    return formatted_operation