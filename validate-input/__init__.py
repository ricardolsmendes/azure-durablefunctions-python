# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.

import time
from typing import Any, Dict


def main(data: Dict[str, Any]) -> Dict[str, Any]:
    time.sleep(2)

    if not data:
        raise Exception('The funds transfer data is mandatory')

    if not data.get('sourceAccount'):
        raise Exception('The Source Account is mandatory')

    if not data.get('targetAccount'):
        raise Exception('The Target Account is mandatory')

    return data
