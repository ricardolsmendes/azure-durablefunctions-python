# This function an HTTP starter function for Durable Functions.

import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new(
        orchestration_function_name=req.route_params['functionName'],
        client_input=req.get_json())

    logging.info(f'Started orchestration with ID = "{instance_id}".')

    return client.create_check_status_response(req, instance_id)
