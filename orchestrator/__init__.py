# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    result1 = yield context.call_activity('Hello', "Tokyo")
    result2 = yield context.call_activity('Hello', "Seattle")
    result3 = yield context.call_activity('Hello', "London")
    return [result1, result2, result3]


main = df.Orchestrator.create(orchestrator_function)
