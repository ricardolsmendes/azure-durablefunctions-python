cd azure-durablefunctions-python || exit

func new --name transfer-funds --template "Durable Functions orchestrator"

func new --name read-request-data --template "Durable Functions activity"
func new --name validate-input --template "Durable Functions activity"
func new --name handle-funds-transfer --template "Durable Functions activity"

func new --name start-from-http --template "Durable Functions HTTP starter" --authlevel "anonymous"
