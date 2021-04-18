# azure-durablefunctions-python

Companion repository for the **How to chain Azure Functions and leverage Durable Functions to
reduce the burden when managing long-living serverless workloads** blog post.

> Note: both the blog post and this repo are work in progress!

## Quickstart guide

1. Create an Azure Function using the Azure Portal.

1. Clone this repo:
   ```shell
   git clone https://github.com/ricardolsmendes/azure-durablefunctions-python.git
   cd azure-durablefunctions-python
   ```

1. Publish the Durable Functions:
   ```shell
   func azure functionapp publish <YOUR-FUNCTION-NAME>
   ```
   The HTTP URI will be displayed at the end of the publishing logs.
   
1. Use [Postman](https://www.postman.com) or equivalent tool to make requests and see it in
   action. Please use the below content as a reference request body:
   ```json
    {
      "metadata": {
        "requestId": "6d79dbfb-0e37-4fc4-981f-442c9ca65760",
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
   The validation errors and optional execution path can be activated by suppressing and/or
   changing the `data` content.
