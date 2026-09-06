# Generative AI Inference Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gai_generative_ai_inference.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gai_generative_ai_inference.html#dcoc-content-body)

## Generative AI Inference Functions

Package: DBMS_CLOUD_OCI_GAI_GENERATIVE_AI_INFERENCE

### EMBED_TEXT Function

Produces embeddings for the inputs. An embedding is numeric representation of a piece of text. This text can be a phrase, a sentence, or one or more paragraphs. The Generative AI embedding model transforms each phrase, sentence, or paragraph that you input, into an array with 1024 numbers. You can use these embeddings for finding similarity in your input text such as finding phrases that are similar in context or category. Embeddings are mostly used for semantic searches where the search function focuses on the meaning of the text that it's searching through rather than finding results based on keywords.

Syntax
```

```

Parameters

Parameter Description

`embed_text_details`

(required) Details for generating the embed response.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://inference.generativeai.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_TEXT Function

Generates a text response based on the user prompt.

Syntax
```

```

Parameters

Parameter Description

`generate_text_details`

(required) Details for generating the text response.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://inference.generativeai.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_TEXT Function

Summarizes the input text.

Syntax
```

```

Parameters

Parameter Description

`summarize_text_details`

(required) Details for summarizing the text.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://inference.generativeai.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Generative AI Inference Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gai_generative_ai_inference.html#ADSDK-GUID-DCF1BDEC-C870-46AF-AB08-2146806EAB5A)
- [EMBED_TEXT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gai_generative_ai_inference.html#ADSDK-GUID-938DB3C8-2DFB-48FE-B220-66C13B674488)
- [GENERATE_TEXT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gai_generative_ai_inference.html#ADSDK-GUID-B3CF219F-B153-4234-9C2C-91B23CAFD9BF)
- [SUMMARIZE_TEXT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gai_generative_ai_inference.html#ADSDK-GUID-2CBE0C54-2334-4081-B6FC-79F7A4787346)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
