# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    output = []

    funds_transfer_data = yield context.call_activity('get-funds-transfer-data')
    output.append('Get funds transfer data: DONE')

    """    
    yield context.call_activity('validate-input', funds_transfer_data)
    output.append('Validate input: DONE')

    yield context.call_activity('validate-internal-account', funds_transfer_data)
    output.append('Validate internal account: DONE')

    yield context.call_activity('handle-funds-transfer', funds_transfer_data)
    output.append('Handle funds transfer: DONE')
    """

    return output


main = df.Orchestrator.create(orchestrator_function)
