# Generative AI Inference Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#dcoc-content-body)

## Generative AI Inference Common Types

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_SERVING_MODE_T Type

The model's serving mode, which could be on-demand serving or dedicated serving.

Syntax
```

```

Fields

Field Description

`serving_type`

(required) The serving mode type, which could be on-demand serving or dedicated serving.

Allowed values are: 'ON_DEMAND', 'DEDICATED'

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_DEDICATED_SERVING_MODE_T Type

The model's serving mode is dedicated serving and has an endpoint on a dedicated AI cluster.

Syntax
```

```

`dbms_cloud_oci_generative_ai_inference_dedicated_serving_mode_t`is a subtype of the`dbms_cloud_oci_generative_ai_inference_serving_mode_t`type.

Fields

Field Description

`endpoint_id`

(required) The OCID of the endpoint to use.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_EMBED_TEXT_DETAILS_T Type

Details for the request to embed texts.

Syntax
```

```

Fields

Field Description

`inputs`

(required) The list of strings for embeddings.

`serving_mode`

(required)

`compartment_id`

(required) The OCID of compartment that the user is authorized to use to call into the Generative AI service.

`is_echo`

(optional) Whether or not to include the original inputs in the response. Results are index-based.

`truncate`

(optional) For an input that's longer than the maximum token length, specifies which part of the input text will be truncated.

Allowed values are: 'NONE', 'START', 'END'

`input_type`

(optional) Specifies the input type.

Allowed values are: 'SEARCH_DOCUMENT', 'SEARCH_QUERY', 'CLASSIFICATION', 'CLUSTERING'

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_EMBED_TEXT_RESULT_T Type

The generated embedded result to return.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the generated result.

`inputs`

(optional) The original inputs. Only present if \"isEcho\" is set to true.

`embeddings`

(required) The embeddings corresponding to inputs.

`model_id`

(optional) The OCID of the model used in this inference request.

`model_version`

(optional) The version of the model.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_GENERATE_TEXT_DETAILS_T Type

Details for the request to generate text.

Syntax
```

```

Fields

Field Description

`prompts`

(required) Represents the prompt to be completed. Trailing whitespaces will be trimmed.

`serving_mode`

(required)

`compartment_id`

(required) The OCID of compartment that the user is authorized to use to call into the Generative AI service.

`is_stream`

(optional) Whether to stream back partial progress. If set, tokens are sent as data-only server-sent events as they become available.

`is_echo`

(optional) Whether to include the user prompt in the response. Applies only to non-stream results.

`num_generations`

(optional) The number of of generated texts that will be returned.

`max_tokens`

(optional) The maximum number of tokens to predict for each response. Includes input plus output tokens.

`temperature`

(optional) A number that sets the randomness of the generated output. A lower temperature means a less random generations. Use lower numbers for tasks with a correct answer such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.

`top_k`

(optional) An integer that sets up the model to generate outputs that include only the top k most likely tokens. A higher k introduces more randomness into the output making the output text sound more natural. Default value is 0 which means that this method is disabled and all tokens are considered. To set a number for the likely tokens, choose an integer between 1 and 500. If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20, but the probabilities of the top 10 add up to .75, then only the top 10 tokens are chosen.

`top_p`

(optional) If set to a probability 0.0 &lt; p &lt; 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step. To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1.0 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.

`frequency_penalty`

(optional) To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Greater numbers encourage the model to use new tokens and lower numbers encourage the model to repeat the tokens. Set to 0 to disable.

`presence_penalty`

(optional) To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens. Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.

`stop_sequences`

(optional) The generated text is cut at the end of the earliest occurrence of this stop sequence. The generated text will include this stop sequence.

`return_likelihoods`

(optional) Specifies how and if the token likelihoods are returned with the response.

Allowed values are: 'NONE', 'ALL', 'GENERATION'

`truncate`

(optional) For an input that's longer than the maximum token length, specifies which part of the input text will be truncated.

Allowed values are: 'NONE', 'START', 'END'

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_GENERATE_TEXT_RESULT_T Type

The generated text to return.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for this GenerateTextResult.

`generated_texts`

(required) Each prompt in input array has an array of GeneratedText, controlled by numGenerations parameter in request.

`time_created`

(required) The date and time that the model was created in an RFC3339 formatted datetime string.

`prompts`

(optional) The original prompt. Only applicable for non-stream response.

`model_id`

(optional) The OCID of the model used in this inference request.

`model_version`

(optional) The version of the model.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_TOKEN_LIKELIHOOD_T Type

An object that contains the returned token and its corresponding likelihood.

Syntax
```

```

Fields

Field Description

`token`

(optional) A word, part of a word, or a punctuation. For example, apple is a token and friendship is made up of two tokens, friend and ship. When you run a model, you can set the maximum number of output tokens. Estimate three tokens per word.

`likelihood`

(optional) The likelihood of this token during generation.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_TOKEN_LIKELIHOOD_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_inference_token_likelihood_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_GENERATED_TEXT_T Type

The text generated during each run.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for this text generation.

`text`

(required) The generated text.

`likelihood`

(required) The overall likelihood of the generated text. When a large language model generates a new token for the output text, a likelihood is assigned to all tokens, where tokens with higher likelihoods are more likely to follow the current token. For example, it's more likely that the word favorite is followed by the word food or book rather than the word zebra. A lower likelihood means that it's less likely that token follows the current token.

`finish_reason`

(optional) The reason why the model stopped generating tokens. A model stops generating tokens if the model hits a natural stop point or reaches a provided stop sequence.

`token_likelihoods`

(optional) A collection of generated tokens and their corresponding likelihoods.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_ON_DEMAND_SERVING_MODE_T Type

The model's serving mode is on-demand serving on a shared infrastructure.

Syntax
```

```

`dbms_cloud_oci_generative_ai_inference_on_demand_serving_mode_t`is a subtype of the`dbms_cloud_oci_generative_ai_inference_serving_mode_t`type.

Fields

Field Description

`model_id`

(required) The unique ID of a model to use. Can use list Models API to list available models.

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_SUMMARIZE_TEXT_DETAILS_T Type

Details for the request to summarize text.

Syntax
```

```

Fields

Field Description

`input`

(required) The input string to be summarized.

`serving_mode`

(required)

`compartment_id`

(required) The OCID of compartment that the user is authorized to use to call into the Generative AI service.

`is_echo`

(optional) Whether or not to include the original inputs in the response.

`temperature`

(optional) A number that sets the randomness of the generated output. Lower temperatures mean less random generations. Use lower numbers for tasks with a correct answer such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0, and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.

`additional_command`

(optional) A free-form instruction for modifying how the summaries get generated. Should complete the sentence \"Generate a summary _\". For example, \"focusing on the next steps\" or \"written by Yoda\".

`length`

(optional) Indicates the approximate length of the summary. If \"AUTO\" is selected, the best option will be picked based on the input text.

Allowed values are: 'SHORT', 'MEDIUM', 'LONG', 'AUTO'

`format`

(optional) Indicates the style in which the summary will be delivered - in a free form paragraph or in bullet points. If \"AUTO\" is selected, the best option will be picked based on the input text.

Allowed values are: 'PARAGRAPH', 'BULLETS', 'AUTO'

`extractiveness`

(optional) Controls how close to the original text the summary is. High extractiveness summaries will lean towards reusing sentences verbatim, while low extractiveness summaries will tend to paraphrase more.

Allowed values are: 'LOW', 'MEDIUM', 'HIGH', 'AUTO'

### DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_SUMMARIZE_TEXT_RESULT_T Type

Summarize text result to return to caller.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for this SummarizeTextResult.

`input`

(optional) The original input. Only included if \"isEcho\" set to true.

`summary`

(required) Summary result corresponding to input.

`model_id`

(optional) The OCID of the model used in this inference request.

`model_version`

(optional) The version of the model.

- [Generative AI Inference Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-7970B902-26AF-4B6C-A5BE-63ADDF53D5CA)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-9D1ECE35-5347-45B1-BEDE-C132A73198F1)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_SERVING_MODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-DAECE8A3-BB5C-48F1-9CA9-4CD270137980)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_DEDICATED_SERVING_MODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-0FA26338-12FE-4AE4-8416-51A2B2CA76C5)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_EMBED_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-8CCCCB70-531D-4A6F-BDB8-14AD8C94795D)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_EMBED_TEXT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-9074F004-921C-4620-8ABB-36CBD4B3CE94)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-7564A20C-DA4E-4351-989B-D14DAAD2F8DE)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_GENERATE_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-4F024B34-F325-4382-A0DC-D6A2AB8921CA)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_GENERATE_TEXT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-8AD6163F-77B8-4BD0-BB26-0037A9A8FCAE)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_TOKEN_LIKELIHOOD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-8D7232DC-4B9D-4B49-AFCC-742A7D8030E9)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_TOKEN_LIKELIHOOD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-21B43D92-40EE-402C-A308-4EFE2607F777)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_GENERATED_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-72DB73E9-D242-4F94-B15F-7EC7F37508E0)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_ON_DEMAND_SERVING_MODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-73F4473C-FD46-4977-89A3-177F93DC0D79)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_SUMMARIZE_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-AA441FC1-FACE-4ABF-88F2-7A622B56788B)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_INFERENCE_SUMMARIZE_TEXT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_inference_t.html#ADSDK-GUID-A8971765-37A8-430E-A314-90BD482A3A09)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
