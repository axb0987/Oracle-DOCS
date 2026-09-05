# Resending Email Verifications When The Email Address Is Already Verified
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm
- Fetched: 2026-09-05 02:18 CDT

# Resending Email Verifications When The Email Address Is Already Verified

After a user creates an account in an identity domain using the self-registration process, an email notification is sent to the user to verify the user's email address. After users verify their email addresses, they can no longer verify their email addresses after that.

However, identity domains also allow custom clients to reinitiate the change email flow for the same email address as many times as needed. To support this capability, you must set the`triggerEmailVerificationFlowIfEmailAlreadyVerified`attribute to`true`in the`MeEmailVerifier`request payload.

Use the following steps to trigger the email verification flow, if an email address is already verified:
- 

[Step 1: Create a User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_e52_wkl_5jb)
- 

[Step 2: Get a User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_zgz_tll_5jb)
- 

[Step 3: Initiate Self-Service Email Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_avt_xml_5jb)
- 

[Step 4: Obtain a User Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_cr3_jql_5jb)
- 

[Step 5: Self-Verify Email Address](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm#concept_nhv_nkl_5jb__section_nff_drl_5jb)

## Step 1: Create a User

This step shows how to create a user by submitting a POST request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).
```

```

Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the identity domain URL, and the resource path represents the identity domain API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.

Example of Request Body

The following shows an example of a request body in JSON format:
```

```

Example of Response Body

The following shows an example of the response body:
```

```

## Step 2: Get a User

This step shows how to retrieve a user by the user's ID by submitting a GET request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).
```

```

Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.

Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Step 3: Initiate Self-Service Email Verification

This step shows how to initiate email validation of either the user's primary or recovery email address by submitting a PUT request on the REST resource using cURL. For more information about cURL, see[Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).
```

```

Example of Request Body

The following shows an example of a request body in JSON format:
```

```

Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Step 4: Obtain a User Token

This step shows how to retrieve a user token using its ID by submitting a GET request on the REST resource using cURL. For more information about cURL, see[Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).
```

```

Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Step 5: Self-Verify Email Address

This step shows how to verify a new email address by submitting a POST request on the REST resource using cURL. This endpoint validates the token, and then marks the email address as verified. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).
```

```

Example of Request Body

The following shows an example of a request body in JSON format:
```

```

Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```
