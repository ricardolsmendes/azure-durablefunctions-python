# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    output = []

    transfer = yield context.call_activity('get-funds-transfer-data', context.get_input())
    output.append('Get funds transfer data: DONE')

    yield context.call_activity('validate-input', transfer)
    output.append('Validate input: DONE')

    if transfer['sourceAccount']['bankId'] == transfer['targetAccount']['bankId']:
        yield context.call_activity('validate-internal-account', transfer)
        output.append('Validate internal account: DONE')

    """    
    yield context.call_activity('handle-funds-transfer', transfer)
    output.append('Handle funds transfer: DONE')
    """

    return output


main = df.Orchestrator.create(orchestrator_function)
