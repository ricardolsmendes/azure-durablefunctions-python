# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.

import time
from typing import Dict, Optional


def main(body: Dict[str, object]) -> Optional[object]:
    time.sleep(2)
    return body.get('fundsTransfer') if body else {}
