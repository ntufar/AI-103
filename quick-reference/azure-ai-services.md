# Azure AI Services Quick Reference

## Service Selection Cheatsheet

- Azure OpenAI: text generation, chat, summarization, extraction with prompts
- Azure AI Language: sentiment, entities, key phrases, classification
- Azure AI Vision: image analysis, OCR, captions, visual tags
- Azure AI Speech: speech-to-text, text-to-speech, translation
- Azure AI Search: indexing and retrieval, semantic and vector search
- Azure AI Document Intelligence: form/document field extraction

## Decision Hints

- Need conversational generation with instructions? Use Azure OpenAI.
- Need deterministic NLP labels? Use Azure AI Language.
- Need search over enterprise docs? Use AI Search (often with OpenAI for answers).
- Need text from scanned content? Use Vision OCR or Document Intelligence.

## Common Trade-offs

- Cost vs quality: larger models usually improve quality but cost more.
- Latency vs complexity: multi-step pipelines may improve quality but increase response time.
- Recall vs precision in retrieval: larger chunks increase recall, smaller chunks improve precision.

## Security and Governance Checklist

- [ ] Principle of least privilege
- [ ] Managed identities where possible
- [ ] Data residency requirements checked
- [ ] Content filtering/moderation enabled where needed
- [ ] Logs and monitoring enabled
