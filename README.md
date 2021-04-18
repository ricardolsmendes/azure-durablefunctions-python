# azure-durablefunctions-python

Companion repository for the **How to chain Azure Functions and leverage Durable Functions to
reduce the burden when managing long-living serverless workloads** blog post.

> Note: both the blog post and this repo are work in progress!

## Sample application

The dummy Funds Transfer App comprises 4 business steps, each of them implemented as an
Azure Function:

![N|Solid](.diagrams/workloads-funds-transfer.png
"The sample Funds Transfer App using Azure Durable Functions")

Main characteristics:
1. `get-funds-transfer-data` returns a value to the orchestrator; 

1. `get-funds-transfer-data`, `validate-input`, and `handle-funds-transfer` are mandatory and must
   run in this order;
   
1. `validate-internal-account` is optional can execute between `validate-input` and
   `handle-funds-transfer` under certain conditions.

## Quickstart guide

1. Create an Azure Function using the Azure Portal.

1. Clone this repo:
   ```shell
   git clone https://github.com/ricardolsmendes/azure-durablefunctions-python.git
   cd azure-durablefunctions-python
   ```

1. Publish the Azure Function:
   ```shell
   func azure functionapp publish <YOUR-FUNCTION-NAME>
   ```
   _The HTTP URI will be displayed at the end of the publishing logs._
   
1. Use [Postman](https://www.postman.com) or equivalent tool to make requests and see it in
   action. Please use the below content as a reference request body:
   ```json
    {
      "metadata": {
        "requestId": "6d79dbfb",
        "requestType": "fundsTransfer"
      },
      "data": {
        "sourceAccount": {
          "id": "123456",
          "bankId": "001"
        },
        "targetAccount": {
          "id": "456789",
          "bankId": "002"
        }
      }
    }
   ```
   This will result in successful execution. The validation errors and optional execution path
   can be activated by applying slight changes to it:
   - remove `data`, `data.sourceAccount`, or `data.targerAccount` to see the validation errors;
   - change `data.targetAccount.bankId` to `001` to run `validate-internal-account` in a given
     workflow.
