# AI-103 Mock Exam Question Bank

## Domain 1: Plan and Manage Azure AI Solutions (25 questions)

### Service Selection & Architecture

1. A startup needs to build a chatbot for FAQ automation. Which service is the primary choice?
   - A) Azure AI Language
   - B) Azure OpenAI Service
   - C) Azure AI Vision
   - D) Azure AI Speech
   Answer: B

2. Your company processes 10 million customer support tickets monthly with unstructured text. Which indexing strategy minimizes latency while maintaining recall?
   - A) Full-text search only
   - B) Vector embeddings with semantic ranking
   - C) Keyword search with BM25
   - D) Regex pattern matching
   Answer: B

3. A manufacturing plant requires OCR on equipment photos daily. Latency must be <100ms per image. What is the best deployment model?
   - A) Batch processing in a Logic App
   - B) Real-time synchronous calls to Azure AI Vision
   - C) Edge deployment using Azure AI Vision as a Docker container
   - D) Store images and process weekly
   Answer: C

4. You must choose between Azure Cognitive Search and Pinecone vector DB. Which factor favors Azure Cognitive Search for an enterprise?
   - A) Lower cost per query
   - B) Integrated AAD security and compliance audit trails
   - C) Superior vector recall accuracy
   - D) Smaller learning curve
   Answer: B

5. A regulated healthcare firm stores patient records in Azure Cosmos DB. Which responsible AI principle should guide OCR and NLP model selection?
   - A) Maximize prediction accuracy at any cost
   - B) Privacy-first: minimize data retention and enable differential privacy
   - C) Only use models trained on in-house data
   - D) Disable all monitoring
   Answer: B

### Pricing & Quotas

6. Azure OpenAI tokens are counted as input + output. A 5,000-token context and 1,000-token response with GPT-3.5-turbo costs $0.0015 per 1K input, $0.002 per 1K output. Total cost?
   - A) $0.007500
   - B) $0.009000
   - C) $0.010500
   - D) $0.012000
   Answer: C

7. You provision Azure AI Language resource in East US at S1 tier. Monthly quota is 300K text records. If you process 1M records per month, what is the next step?
   - A) Upgrade to S2 tier
   - B) Use multiple S1 instances in different regions
   - C) Both A and B are valid
   - D) Cannot exceed quota without rebuilding
   Answer: C

8. Azure AI Search has a 100MB per document limit. Your PDFs average 150MB. What is the recommended approach?
   - A) Use Azure AI Document Intelligence to chunk, then index chunks
   - B) Compress PDFs
   - C) Use a third-party indexing service
   - D) Store blobs and index metadata only
   Answer: A

### Security & Compliance

9. You store OpenAI API keys in an Azure Web App. What is the most secure approach?
   - A) Hardcode in web.config
   - B) Store in environment variables during deployment
   - C) Use Azure Key Vault with Managed Identity
   - D) Email the key to developers
   Answer: C

10. A payment processor must ensure no customer PII is logged when using Azure OpenAI for analysis. Which safeguard is MOST effective?
    - A) Enable Application Insights logging only
    - B) Implement input/output filtering at the application layer and disable OpenAI logging
    - C) Use row-level security in the database
    - D) Encrypt all logs with a customer-owned key
    Answer: B

11. Your firm uses Azure AI Language to detect sentiment in 10 million customer comments per month. GDPR compliance requires data deletion on request. What must you implement?
    - A) Soft-delete flags in the database
    - B) A request pipeline to delete source data, search indices, and any cached model outputs
    - C) Anonymize data with SHA-256 hashing
    - D) Disable API logging
    Answer: B

12. Azure AI services in region X are compromised. You must failover to region Y with zero downtime. What architecture supports this?
    - A) Single-region deployment with backup storage
    - B) Active-active geo-redundant deployment with Azure Front Door routing
    - C) Manual failover via export/import
    - D) Replicate data only, not services
    Answer: B

### Monitoring & Governance

13. You deploy an Azure OpenAI chatbot and notice the model produces inappropriate responses 2% of the time. Which metric should you track weekly?
    - A) Query latency
    - B) Safety incident rate and human review feedback
    - C) Token consumption only
    - D) Model update frequency
    Answer: B

14. A data science team fine-tunes models weekly. How should you version and track model performance?
    - A) Use Model Registry in Azure Machine Learning with evaluations and promotion workflows
    - B) Store models in OneDrive
    - C) Overwrite the latest model each time
    - D) Keep a spreadsheet of accuracy numbers
    Answer: A

15. You must prove to auditors that all Azure AI outputs are reviewed before publication. Which tool provides audit trails?
    - A) Azure Monitor logs with custom queries
    - B) Application Insights events
    - C) Combination of Activity Log, Diagnostic Logs, and custom application logging
    - D) Azure Policy only
    Answer: C

---

## Domain 2: Implement Generative AI Solutions (30 questions)

### Prompt Engineering

16. You need a model to extract action items from meeting notes. Which prompt structure is most effective?
    - A) "Extract action items."
    - B) "You are an AI assistant. Extract action items from meeting notes. Return JSON with {person, task, deadline}. Notes: [input]"
    - C) "Extract action items from meeting notes. Ignore unclear items. Return only confirmed tasks."
    - D) B and C combined
    Answer: D

17. A prompt consistently produces verbose 2000+ token responses when you need <200 tokens. Which fix is most direct?
    - A) Use a cheaper model
    - B) Add to the prompt: "Response must be under 200 tokens. If you cannot fit the answer, say 'Too complex.'"
    - C) Fine-tune the model
    - D) Truncate responses after 200 tokens
    Answer: B

18. You use few-shot prompting with 3 examples. Model quality plateaus at 70% accuracy. Next best step?
    - A) Add 10 more examples
    - B) Analyze failure cases, add targeted examples of hard cases, and use chain-of-thought reasoning
    - C) Switch to a larger model
    - D) Use random sampling of examples
    Answer: B

19. A safety filter blocks 15% of legitimate user requests (false positives). What is the primary risk mitigation?
    - A) Remove the filter entirely
    - B) Adjust filter threshold and add explicit prompt guidance to reduce policy violations
    - C) Log false positives and ignore them
    - D) Use a second model to validate
    Answer: B

20. You must ground responses in a knowledge base to avoid hallucinations. What is the recommended pattern?
    - A) Include the entire knowledge base in the prompt
    - B) RAG: retrieve top-K relevant documents, then compose response from only those
    - C) Fine-tune the model on the knowledge base
    - D) Ask the model to cite sources
    Answer: B

### Evaluation & Refinement

21. You evaluate a summarization model with BLEU and ROUGE scores at 0.65. What does this NOT tell you?
    - A) Token-level overlap with reference summaries
    - B) Whether the summary is factually correct
    - C) Grammatical quality
    - D) Vocabulary overlap precision
    Answer: B

22. A prompt produces correct facts but confusing wording 30% of the time. How should you measure improvement?
    - A) Deploy to production and measure user satisfaction
    - B) Use an evaluation rubric with 5+ criteria, score 50+ samples before and after, test for statistical significance
    - C) Run once manually and compare
    - D) Ask colleagues if it looks better
    Answer: B

23. You A/B test two prompts. Prompt A: 68% success, N=200. Prompt B: 72% success, N=200. Can you declare Prompt B superior?
    - A) Yes, 72 > 68
    - B) No; this difference is within noise. Run N=5000+ to establish significance
    - C) Yes, run production immediately
    - D) No valid conclusion
    Answer: B

24. Your model is evaluated on fairness across demographic groups. One group has 8% error rate, another 14%. What is your remediation?
    - A) Use the model as-is
    - B) Add bias mitigation: balanced training data, fairness constraints, and alert users of lower reliability for the affected group
    - C) Remove the affected group from scope
    - D) Fine-tune only on the lower-performing group
    Answer: B

### RAG & Knowledge Grounding

25. You implement RAG with a vector database. Retrieved documents are often off-topic. What is the first debugging step?
    - A) Replace the entire vector database
    - B) Evaluate retrieval: is embedding quality high? Is chunk size appropriate? Is semantic search threshold too loose?
    - C) Use full-text search instead
    - D) Increase the number of retrieved documents to 100
    Answer: B

26. Your RAG pipeline returns 5 relevant documents, but the model ignores them and hallucinates. What is the likely cause?
    - A) Documents are too long
    - B) System prompt does not enforce grounding; model is not instructed to use ONLY the provided context
    - C) Vector database is broken
    - D) Model is hallucinating by design
    Answer: B

27. Knowledge base updates twice per day. Users see stale answers <1% of the time. What is the trade-off?
    - A) Use real-time indexing; eliminates staleness
    - B) Accept minor staleness or pay for continuous indexing; depends on business requirements
    - C) Disable caching
    - D) Use pull-based instead of push-based updates
    Answer: B

28. You chunk documents by paragraph, but paragraphs vary from 50 to 5000 words. Expected problem?
    - A) No problem
    - B) Variable chunk sizes degrade retrieval quality; use fixed-size overlapping chunks
    - C) Compression will fail
    - D) Embeddings will be incorrect
    Answer: B

29. Your retrieval returns high-scoring matches, but composition prompt ignores them. How do you enforce grounding?
    - A) Increase chunk size
    - B) Add explicit constraint: "Use ONLY information from the provided context. If context does not cover the question, respond: 'I don't have that information.'"
    - C) Use a retrieval threshold
    - D) Add more documents
    Answer: B

30. You must decide: retrieve top-5 or top-20 documents for a QA task. What factors matter?
    - A) Only query latency
    - B) Context window size, token cost, hallucination risk (more context = more noise), and relevance of tail documents
    - C) Model size
    - D) Number of users
    Answer: B

---

## Domain 3: Implement Natural Language Processing Solutions (25 questions)

### Sentiment & Opinion Mining

31. You analyze 50,000 customer reviews. 60% positive, 20% negative, 20% neutral. Which metric tells you confidence?
    - A) Raw percentages
    - B) Confidence scores per document; some predictions are <60% certain
    - C) Average star rating
    - D) Review length
    Answer: B

32. A sentiment model trained on product reviews is applied to political speeches. Expected problem?
    - A) No problem; sentiment is universal
    - B) Domain shift: sarcasm, formal language, and context are different; retraining on target domain is needed
    - C) Use a larger model
    - D) Add more data from product reviews
    Answer: B

33. You detect 10% of reviews as "mixed sentiment" (both positive and negative). How to handle operationally?
    - A) Treat as neutral
    - B) Split into positive and negative separately
    - C) Flag for manual review; decide business rule (e.g., weight positive 60%, negative 40%)
    - D) Discard them
    Answer: C

### Key Phrases & Entity Recognition

34. A Named Entity Recognition model extracts "New York" as a LOCATION from "New York style pizza." Is this correct?
    - A) Yes, New York is a location
    - B) No; it's a food descriptor; context matters; consider sequence labeling confidence
    - C) Both are valid
    - D) Impossible to determine
    Answer: B

35. You extract entities from clinical notes. Model misses "Type 2 diabetes" but detects "diabetes." Root cause?
    - A) Model is broken
    - B) Model trained on short entity spans; fine-tune on multi-word clinical entities with longer context windows
    - C) Use a rule-based system instead
    - D) Increase model size
    Answer: B

### Summarization

36. You summarize 100-page legal contracts to 500 words. Expected challenge?
    - A) No challenge; models handle this naturally
    - B) Long documents exceed token limits; split into sections, summarize each, then meta-summarize
    - C) Just use extractive summarization
    - D) Hire a lawyer to summarize
    Answer: B

37. A summary is shorter but misses critical dates and numbers. How to improve?
    - A) Increase summary length
    - B) Add to prompt: "Include all dates, amounts, and deadlines. Use exact numbers from the source."
    - C) Use a fine-tuned model
    - D) Switch to extractive summarization
    Answer: B

### Language Detection & Translation

38. You receive text "Bonjour, comment allez-vous?" Language detection returns 95% confidence French. Is this actionable?
    - A) Yes, treat as French immediately
    - B) No; consider context, script, and downstream use; 95% confidence is solid but verify with metadata if available
    - C) Always re-translate after detection
    - D) 95% is too low to use
    Answer: B

---

## Domain 4: Implement Computer Vision Solutions (20 questions)

### Image Analysis & Tagging

39. An image analysis API returns tags: "dog (0.98), animal (0.95), pet (0.88), cat (0.45)." A user photo contains a cat, not a dog. What happened?
    - A) Model is broken
    - B) Model trained on more dog data; cat confidence is lower; threshold at 0.50+ would correctly filter the false "dog" tag
    - C) Use vision-language models instead
    - D) Increase confidence threshold to 0.99
    Answer: B

40. You analyze 100,000 product images. 5% are blurry, causing low tag confidence. Mitigation?
    - A) Ignore blurry images
    - B) Preprocess: filter blurry images, flag for manual review, or use image enhancement
    - C) Train a blurriness detector
    - D) Use a more expensive API
    Answer: B

### OCR & Document Processing

41. You run OCR on a scanned historical document. Accuracy is 70% on blurry text. Next step?
    - A) Use the output as-is
    - B) Evaluate OCR confidence scores, manually review low-confidence words, apply spell-check
    - C) Re-scan the document
    - D) Use a different OCR tool
    Answer: B

42. A document image is rotated 90 degrees. OCR fails. Root cause?
    - A) OCR cannot handle rotated images
    - B) Most OCR requires upright text; preprocess with image rotation detection and correction
    - C) Use Azure Document Intelligence instead
    - D) Manually rotate before upload
    Answer: B

### Visual Understanding

43. You classify product images as "high-quality" vs "defective." Model achieves 92% accuracy on test data but 45% on production images. What is the issue?
    - A) Model is broken
    - B) Distribution shift: production images differ in lighting, angle, background; retest on representative production samples
    - C) Use a larger model
    - D) Data leakage
    Answer: B

---

## Domain 5: Implement Knowledge Mining & Document Intelligence (20 questions)

### Indexing & Retrieval

44. You index 10,000 documents averaging 5KB each. Search latency is 500ms per query. Expected improvement from switching to vector search with semantic ranking?
    - A) No improvement
    - B) 20-30% latency improvement; allows semantic relevance ranking
    - C) 10x improvement guaranteed
    - D) Latency increases
    Answer: B

45. A search index has 100 documents, 10,000 queries/day. You add a vector field. Indexing time increases 3x but retrieval improves. Trade-off decision?
    - A) Remove vector field
    - B) Evaluate: does improved relevance justify slower indexing? If most queries need semantic ranking, yes; schedule indexing off-peak
    - C) Use two indices
    - D) No decision needed
    Answer: B

### Document Intelligence (Form Processing)

46. Azure Document Intelligence extracts fields from invoices. It returns confidence 0.85 for "invoice date." Is this field reliable?
    - A) Yes, always
    - B) Not necessarily; <0.90 confidence warrants manual review; check field type (dates require high confidence)
    - C) No, too low
    - D) Confidence does not matter
    Answer: B

47. A custom Document Intelligence model is trained on 50 invoices. Performance on 10 test invoices is 95%. On 1000 new invoices from a different vendor format, accuracy drops to 60%. Why?
    - A) Model is broken
    - B) Overfitting to training domain; requires retraining with diverse vendor samples
    - C) Use a pretrained model instead
    - D) Increase training data by repeating samples
    Answer: B

### Skillsets & Enrichment

48. A search indexer has a skillset: split text -> language detection -> sentiment analysis -> index. A document fails at language detection. What happens to the pipeline?
    - A) Continue with default language
    - B) The downstream skills (sentiment) are skipped; document is partially indexed; error is logged
    - C) Entire pipeline fails
    - D) Retry automatically
    Answer: B

49. You enrich documents with both Azure AI Language (sentiment) and Azure OpenAI (summarization) skills. Processing time is 10 seconds per document. Optimization?
    - A) Remove one skill
    - B) Run skills in parallel where possible; evaluate if all skills are necessary; cache results for similar documents
    - C) Use cheaper models
    - D) Index without enrichment
    Answer: B

### Chunking Strategy

50. You index medical literature: 1000 papers, each 30 pages. Chunk size options: A) 1 paragraph, B) 5 paragraphs, C) 1 page, D) entire paper. Which minimizes hallucination in QA?
    - A) A
    - B) B or C; small chunks reduce irrelevant context, medium chunks preserve coherence
    - C) C
    - D) D
    Answer: B

---

## Bonus Scenario Questions (15 questions)

### End-to-End Scenarios

51. A retail company wants real-time product recommendations. They have 500,000 products with descriptions. Proposed stack: Azure OpenAI for embedding + vector search + composition. Evaluation?
    - A) Not viable
    - B) Viable but consider: embedding cost (500K × N tokens), latency, RAG quality, A/B testing against rule-based baseline
    - C) Always the best approach
    - D) Only for small catalogs
    Answer: B

52. A research firm needs to process 50,000 research papers for trend analysis. Batch processing (overnight) vs real-time. Decision driver?
    - A) Always batch
    - B) Batch is cheaper and sufficient if turnaround <24h; real-time needed only for live alerts
    - C) Always real-time
    - D) Use both simultaneously
    Answer: B

53. You build a multi-language customer support chatbot. Supported languages: 25. Proposed approach: detect language, route to language-specific model. Issue?
    - A) No issue
    - B) Maintenance burden: 25 language-specific models; consider multilingual models or single model with language prompting
    - C) Use machine translation instead
    - D) Pick one language
    Answer: B

54. A healthcare provider uses Azure AI Language for clinical note analysis. Regulatory requirement: full audit trail of all model decisions. Implementation?
    - A) Not possible
    - B) Log every inference: input text, model version, output entities, confidence scores, user action, timestamp
    - C) Only log errors
    - D) Disabled logging per HIPAA
    Answer: B

55. You deploy a content moderation system. False positive rate (incorrectly flagged safe content) is 8%. Business impact?
    - A) Acceptable
    - B) Operational cost: manual review workload; evaluate: is 8% manageable? Consider threshold tuning or human-in-the-loop
    - C) Unacceptable, disable system
    - D) No impact
    Answer: B

---

## Scoring Guide

- 40-50 correct: 80%+ - Exam ready
- 35-39 correct: 70-79% - Strong foundation, review weak domains
- 30-34 correct: 60-69% - Solid base, need targeted prep
- <30 correct: <60% - Focus on fundamentals before retesting

