# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    output = []

    data = yield context.call_activity('get-funds-transfer-data', context.get_input())
    output.append('Get funds transfer data: DONE')

    yield context.call_activity('validate-input', data)
    output.append('Validate input: DONE')

    if data['sourceAccount']['bankId'] == data['targetAccount']['bankId']:
        yield context.call_activity('validate-internal-account', data)
        output.append('Validate internal account: DONE')

    yield context.call_activity('handle-funds-transfer', data)
    output.append('Handle funds transfer: DONE')

    return output


main = df.Orchestrator.create(orchestrator_function)
