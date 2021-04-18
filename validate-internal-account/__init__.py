# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.

import time
from typing import Any, Dict


# Using `transfer` as the parameter name because `data` causes a
# `Microsoft.Azure.WebJobs.Host: Can't bind parameter 'data' to type 'System.String'.` error.
# https://github.com/Azure/Azure-Functions/issues/1281 for reference.
def main(transfer: Dict[str, Any]) -> Dict[str, Any]:
    time.sleep(2)
    # Internal Accounts validation logic should be added here.
    return transfer
