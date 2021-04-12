cd azure-durablefunctions-python || exit

# Create the Durable Functions
# ============================

# Create the Orchestrator
func new --name transfer-funds --template "Durable Functions orchestrator"

# Create the Activities
func new --name read-request-data --template "Durable Functions activity"
func new --name validate-input --template "Durable Functions activity"
func new --name validate-internal-account --template "Durable Functions activity"
func new --name handle-funds-transfer --template "Durable Functions activity"

# Create the HTTP starter
func new --name start-from-http --template "Durable Functions HTTP starter" \
  --authlevel "anonymous"
