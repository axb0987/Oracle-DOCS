# Uploads Using POST with Amazon S3 Compatibility API for Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/s3-post-upload.htm
- Fetched: 2026-09-05 02:52 CDT

# Uploads Using POST with Amazon S3 Compatibility API for Object Storage

Upload objects from Object Storage using HTTPS POST with the Amazon S3 Compatibility API using an HTML form and a pre-signed POST policy.

You can upload objects directly from a browser using an HTML form and a pre-signed POST policy in Object Storage. This method provides fine-grained control over upload parameters, enforces security requirements, and supports key features like server-side encryption and checksum validation.

This topic describes the required elements for POST-based uploads, how to construct the necessary policy and signature, and how to specify advanced rules and custom fields.

[

[

## Setting Up the Workflow

The following steps describe the workflow to upload objects to Object Storage using a browser:
- You requests an HTML page using a web browser from your application's web server.
- The returned web page contains a form with the required parameters for object upload to Object Storage.
- You select a file and submits the form from their browser, uploading the object directly to Object Storage.

To perform these steps, the following elements must be established:
- A security policy: This defines the allowed bucket, object key prefix, metadata, and other conditions.
- A policy signature: This authenticates the policy and authorizes the upload.
- An HTML form: This presents fields for file selection and includes the policy and signature as hidden elements.

## Security Policy and HTML Form

The policy document is a transient JSON object only used for validating the upload request at the time of submission. This document is not stored in Object Storage and doesn't require an API call to create. Your server must create, sign, and embed the policy in the HTML form.

Here is an example policy JSON used to create the HTML form:
```

```

Here is the resulting HTML form:
```

```

## Policy Conditions and Matching Rules

The POST policy is used for the following purposes:
- Creating authentication signature.
- Specifying conditions that the request must meet.

The POST policy contains the`expiration`and`conditions`elements. The`expiration`element specifies the expiration date and time of the POST policy in ISO8601 UTC date format. Each form field (excluding`x-amz-signature`,`file`,`policy`, and fields beginning with`x-ignore-`) must have at least one condition in the policy JSON. The policy also supports complex rules, by specifying several conditions for a form field.

The conditions can have different match types internally. For example, to restrict the POST upload to a specific bucket, specify the condition as`{"bucket": "examplebucket"}`, which indicates Object Storage matches the incoming bucket name in the URL with the specific bucket specified in the policy. Another match type could be`starts-with`which specifies that the value starts with the string mentioned in the policy. For example if we want the object name/key to start with a specific prefix, we can mention the condition as`["starts-with", "$key", "user/user1/"]`. Here`$key`refers to the value provided in the`key`HTML form field.

Conditions support variables as shown with`$key`. Any word that begins with a`$`is treated as a variable. These variables are expanded to values incoming from the HTML form fields before validation of the POST policy. You can have custom fields in HTML form such as`customfield01`and the corresponding`$customfield01`in the policy condition for validation performed on Object Storage.

The following table contains the complete list of match types:

Match Types
Match Types Descriptions
Specifying Ranges Defines minimum and maximum values, such as file size limits for uploads.

For example:`["content-length-range", 2097152, 10485760]`allows content between 2 and 10 MiB.
Matching Any Content An empty string in a`starts-with`condition matches any value.

For example:`["starts-with", "$success_action_redirect", ""]`
Matching Content-Types in a Comma-Separated List For`starts-with`on Content-Type, all values in a comma-separated list must match.

For example:
Pass :`"image/jpg,image/png,image/gif"`for
```

```

Fail :`["image/jpg,text/plain"]`. Other fields are treated as simple strings.
Starts With The value must begin with a specified prefix.

For example:`["starts-with", "$key", "u/u1/"]`means object keys must start with`u/u1/`.
Exact Matches The field value must exactly match the policy value exactly.

For example:`{"bucket": "prod-bucket-01"}`

Form fields such as`bucket`,`content-length-range`, and REST-specific headers have special handling for conditions. For example,`bucket`supports only exact matching and doesn't support`starts-with`operation.

The following table shows the handling for matching for different elements that can be specified in the policy.

Matching for Different Elements
Element-Name Required Description
`success_action_status`No Status code returned to the client after a successful upload (if no redirect). Supports exact matching. Required only if the success action status code is overridden from the default which is 200.
`x-amz-date`Yes ISO8601 date for signature calculation (such as 20130728T000000Z). Supports exact matching.
`x-amz-credential`Yes Credential string (access key ID, date, region, service) used for signature calculation. Supports exact matching.
`x-amz-signature`Yes The signature computed based on the policy. This is present only as a form-field and isn't part of the policy.
`success_action_redirect`No URL to redirect the client after a successful upload. Supports exact matching and starts-with. Required only if a redirect must be done by the server upon successful POST upload.
`Cache-Control / Content-Type / Content-Disposition / Content-Encoding / Expires`No REST-specific headers. Support exact matching and starts-with.
`key`Yes Acceptable object key name or prefix. Supports exact matching and starts-with.
`bucket`Yes Acceptable bucket name. Supports exact matching.
`content-length-range`No Minimum and maximum size for uploaded content. Supports content-length-range matching. Required only if the object needs to be restricted to the specific range.
`x-amz-meta-*`No User-defined metadata fields. Support exact matching and starts-with. These are optional fields, which is stored as user metadata of the object.
`x-amz-storage-class`No The storage class to use for storing the object. Supports exact matching. Optional, defaults to Standard.
`x-amz-algorithm`Yes Specifies the required signing algorithm (such as AWS4-HMAC-SHA256). Supports exact matching.

A special field called`$filename`can be referenced in the policy document. This value is replaced by the name of the file that's being uploaded from the browser. For any other custom field that's present in the HTML form, a corresponding entry is present in the policy JSON. The`exact matches`and`starts-with`values are supported for custom fields. An example custom field called my-custom-field is shown in the following example:
```

```

### Special Character Handling in Policy

The following table shows some special characters that are expected to be escaped in the POST policy document.

Special Characters that are Escaped
Escape Sequence Description
`\n`New line
`\uxxxx`Represents any Unicode character
`\f`Form feed
`\v`Vertical tab
`\r`Carriage return
`\b`Backspace
`\`Backslash
`\t`Horizontal tab
`$`Dollar symbol

#### Summary of Condition Matching

The following list summarizes the condition matching:
- A value of`""`for`starts-with`indicates that anything is allowed.
- If a field in a condition is preceding with`$`, the value of the field is replaced before the condition evaluation.
- `$filename`is a special variable that's recognized by all form fields. This is replaced with the name of the file provided before the condition is evaluated. Only the filename is used, if the filename contains full path like`c:\test-folder\test-file.txt`or`/usr/home/test/test-folder/test-file.txt`, only`test-file.txt`is used for the value of`$filename`.`filename`is a header in the`file`form field, which typically gets automatically added by the browsers.
- For validating`content-length`, the available conditions are`exact-match`,`starts-with`,`content-match-in-list`,`any-match`, and`content-length-range`.
- `file`and`bucket`fields have special significance.`file`always refers to the attached object that's being uploaded. The bucket field refers to the bucket to which the object is to be uploaded.

### Signature Computation

Follow this workflow for getting the signature:
- Write the policy and encode it in UTF-8.
- Convert the UTF-8 bytes of the policy to a base64-encoded string—this becomes the`StringToSign`.
- Generate a signing key.
- Sign the`StringToSign`using the signing key and the HMAC-SHA256 algorithm.

## Other Feature Headers

This section describes the other feature headers available to you.

### Additional Checksum Form Fields

When uploading an object, you can provide more checksum headers to compute these checksums on Object Storage. Checksums are also available for data integrity checks.

The following table shows the list of headers to be supported for checksums.

Additional Checksum Form Fields
Name Required Description
`x-amz-checksum-algorithm`No Can have the value SHA256. One other checksum is computed along with MD5 which is the default.
`x-amz-checksum-sha256`No Base64-encoded, 256-bit SHA-256 digest of the object. Required if`x-amz-checksum-algorithm`is set as SHA256.

### SSE-C Form Fields

When customers manage their own encryption keys, include the following headers listed in the following table in the form fields when you manage your own encryption keys:

SSE-C Form Fields
Name Required Description
`x-amz-server-side-encryption-customer-algorithm`No Specifies the algorithm to use to when encrypting the object. Only supported value is AES256.
`x-amz-server-side-encryption-customer-key`Conditional Base64 encoded encryption key.
`x-amz-server-side-encryption-customer-key-MD5`Conditional Specifies the base64-encoded 128-bit MD5 digest of the encryption key according to[RFC 1321](http://tools.ietf.org/html/rfc1321).

### Response to POST Object Requests

Unlike`PutObject`where only a HTTP status code is returned after the put finishes, POST object return depends on certain fields defined in the policy.
- If there was an error on`PostObject`, the exact HTTP status code, for example, 429, 500, 503 and so on, is returned.
- If the`PostObject`was successful and if success_action_redirect is mentioned in the policy, a redirect to the URL specified in the`success_action_redirect`field is sent.
- If the`PostObject`was successful, but`success_action_redirect`isn't mentioned and`success_action_status`is defined, then return the exact status code defined in the`success_action_status`.
- If neither`success_action_redirect`nor`success_action_status`
