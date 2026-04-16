# Azure Configuration for AI-103 Practice Apps

## Prerequisites

1. **Azure Subscription**: Active subscription with AI resources
2. **Azure CLI**: Install from https://aka.ms/azure-cli
3. **Python 3.10+**: Already confirmed in workspace

## Setup Steps

### 1. Create `.env` File

Copy the template below to `.env` in the project root:

```
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_KEY=<your-api-key>
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4  # or gpt-35-turbo

# Azure AI Language
AZURE_LANGUAGE_ENDPOINT=https://<your-region>.api.cognitive.microsoft.com/
AZURE_LANGUAGE_KEY=<your-api-key>

# Optional: Azure AI Search for RAG
AZURE_SEARCH_ENDPOINT=https://<your-search>.search.windows.net/
AZURE_SEARCH_KEY=<your-api-key>
AZURE_SEARCH_INDEX_NAME=ai103-practice
```

### 2. Retrieve Your Keys

#### Azure OpenAI:
```bash
az cognitiveservices account keys list \
  --resource-group <your-rg> \
  --name <your-openai-resource>
```

#### Azure AI Language:
```bash
az cognitiveservices account keys list \
  --resource-group <your-rg> \
  --name <your-language-resource>
```

### 3. Install Azure Python SDK

```bash
pip install -r requirements-azure.txt
```

### 4. Run Cloud-Connected Apps

```bash
python apps/text-analysis-cli-azure/main.py --input data/sample-inputs/customer-feedback.txt

python apps/prompt-eval-trainer-azure/main.py
```

## Cost Estimates

- **Azure OpenAI**: ~$0.01-0.05 per 1K tokens (depends on model)
- **Azure AI Language**: $2/1K requests (Sentiment/Entities)
- **Azure AI Search**: $0.25-4/day for S0-S3 tiers

## Security Best Practices

- Never commit `.env` files; add to `.gitignore`
- Use Managed Identity in production (not API keys)
- Rotate keys quarterly
- Use Key Vault for secret storage in production
- Audit all API calls with Application Insights

## Troubleshooting

- **401 Unauthorized**: Check API key and endpoint URL
- **Rate Limit Exceeded**: Implement retry logic with exponential backoff
- **Model Not Found**: Verify deployment name matches resource
