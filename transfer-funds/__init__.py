# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.

import re

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    output = []
    request_body = context.get_input()

    try:
        data = yield context.call_activity('get-funds-transfer-data', request_body)
        output.append('Get funds transfer data: DONE')

        yield context.call_activity('validate-input', data)
        output.append('Validate input: DONE')

        if data['sourceAccount']['bankId'] == data['targetAccount']['bankId']:
            yield context.call_activity('validate-internal-account', data)
            output.append('Validate internal account: DONE')

        yield context.call_activity('handle-funds-transfer', data)
        output.append('Handle funds transfer: DONE')

        return output
    except Exception as e:
        # Any exception that is raised by a function is re-raised by its enclosing activity task.
        # The original error message is part of the new exception message, formatted as
        # "Activity function '<function_name>' failed:  <exception_type>: <exception_message>",
        # so a regex is used to extract the original message and generate a friendlier output.
        function_name = None
        function_exception_type = None
        function_exception_msg = None
        activity_exception_msg = ''.join(e.args)
        activity_exception_matcher = re.search(
            r"Activity[\s]*function[\s]*'(?P<function_name>.+?)'[\s]*failed:"
            r"[\s]*(?P<exception_type>.+?):"
            r"[\s]*(?P<exception_message>.+?)[\s]*\n", activity_exception_msg)

        if activity_exception_matcher:
            function_name = activity_exception_matcher.group('function_name')
            function_exception_type = activity_exception_matcher.group('exception_type')
            function_exception_msg = activity_exception_matcher.group('exception_message')
            context.set_custom_status(function_exception_msg)

        orchestrator_msg = f"'{function_name}' raised {function_exception_type} >> " \
                           f" {function_exception_msg}'" \
                           if function_exception_msg else activity_exception_msg
        output.append(orchestrator_msg)
        raise Exception(output)


main = df.Orchestrator.create(orchestrator_function)
