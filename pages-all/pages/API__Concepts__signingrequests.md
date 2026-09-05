# Request Signatures
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm
- Fetched: 2026-09-05 01:35 CDT

# Request Signatures

This topic describes how to sign Oracle Cloud Infrastructure API requests.

Signing samples are included for the following:
- [Java](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__Java)
- [Python](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__Python)
- [TypeScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__TypeScript)
- [JavaScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__JavaScript)
- [Ruby](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__RubySigningSample)
- [Go](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__Go)
- [Bash](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__Bash)
- [C#](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm#seven__CSharp)

## Signature Version 1

The signature described here is version 1 of the Oracle Cloud Infrastructure API signature. In the future, if Oracle modifies the method for signing requests, the version number will be incremented and your company will be notified.

## Required Credentials and OCIDs

You need an API signing key in the correct format. See[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm).
Caution  
  

Client Clock Skew

If the client's clock is skewed more than 5 minutes, a 401 (NotAuthenticated) HTTP status code is returned. This will affect your API requests. For more information, see[Maximum Allowed Client Clock Skew](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm#clock).

You also need the OCIDs for your tenancy and user. See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#five).

## Summary of Signing Steps

In general, these are the steps required to sign a request:
- Form the HTTPS request (SSL protocol TLS 1.2 is required).
- Create the signing string, which is based on parts of the request.
- Create the signature from the signing string, using your private key and the RSA-SHA256 algorithm.
- Add the resulting signature and other required information to the`Authorization`header in the request.

See the remaining sections in this topic for details about these steps.

## Specification You Need to Be Familiar With

To learn how to perform steps 2-4 in the process above, refer to[draft-cavage-http-signatures-08](https://tools.ietf.org/html/draft-cavage-http-signatures-08). It's a draft specification that forms the basis for how Oracle handles request signatures. It describes generally how to form the signing string, how to create the signature, and how to add the signature and required information to the request. The remaining sections in this topic assume you're familiar with it. Important details of the Oracle Cloud Infrastructure implementation of the reference are listed in the next section.

## Special Implementation Details

The following sections describe important items to note about the Oracle Cloud Infrastructure implementation of the spec.

### Authorization Header

The Oracle Cloud Infrastructure signature uses the`Signature`Authentication scheme (with an`Authorization`header), and not the Signature HTTP header.

### Required Headers

This section describes the headers that must be included in the signing string.
Note  
  

Error if Required Header is Missing

If a required header is missing, your client will receive a 401 "Unauthorized" response.

For GET and DELETE requests (when there's no content in the request body), the signing string must include at least these headers:
- `(request-target)`(as described in[draft-cavage-http-signatures-08](https://tools.ietf.org/html/draft-cavage-http-signatures-08))
- `host`
- `date`or`x-date`(if both are included, Oracle uses`x-date`)

For PUT and POST requests (when there's content in the request body), the signing string must include at least these headers:
- `(request-target)`
- `host`
- `date`or`x-date`(if both are included, Oracle uses`x-date`)
- `x-content-sha256`(except for Object Storage PUT requests; see the next section)
- `content-type`
- `content-length`
Caution  
  

For PUT and POST requests, your client must compute the`x-content-sha256`and include it in the request and signing string, even if the body is an empty string. Also, the`content-length`is always required in the request and signing string, even if the body is empty. Some HTTP clients will not send the`content-length`if the body is empty, so you must explicitly ensure your client sends it. If`date`and`x-date`are both included, Oracle uses`x-date`. The`x-date`is used to protect against the reuse of the signed portion of the request (replay attacks).

The one exception is for Object Storage PUT requests on objects (see the next section).

### Special Instructions for Object Storage PUT

For Object Storage[PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject)and[UploadPart](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/UploadPart)PUT requests, the signing string must include at least these headers:
- `(request-target)`
- `host`
- `date`or`x-date`(if both are included, Oracle uses`x-date`)

If the request also includes any of the other headers that are normally required for PUT requests (see the list above), then those headers must also be included in the signing string.

### Case and Order of Headers

The headers must be all lowercase in the signing string.

The order of the headers in the signing string does not matter. Just make sure to specify the order in the`headers`parameter in the`Authorization`header, as described in the[draft-cavage-http-signatures-05](https://tools.ietf.org/html/draft-cavage-http-signatures-05).
Caution  
  
The`(request-target)`includes the path and query string from the request. Oracle expects that you will create the signing string with the query parameters in the same order as they appear in the request. If the request query parameters change order after signing occurs, authentication will fail.

### URL Encoding of Path and Query String

When forming the signing string, you must URL encode all parameters in the path and query string (but not the headers) according to[RFC 3986](https://www.ietf.org/rfc/rfc3986.txt).

### Key Identifier

You must set`keyId="<TENANCY OCID>/<USER OCID>/<KEY FINGERPRINT>"`in the`Authorization`header that you add to the request. To get those values, see[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#five). An example`keyId`looks like this (wrapped to better fit the page):
```

```

### Signing Algorithm

The signing algorithm must be RSA-SHA256, and you must set`algorithm="rsa-sha256"`in the`Authorization`header (notice the quotation marks).

### Signature Version

You should include`version="1"`in the`Authorization`header (notice the quotation marks). If you do not, it's assumed that you're using whatever the current version is (which is version 1 at this time).

### Example Header

Here's an example of the general syntax of the`Authorization`header (for a request with content in the body):
```

```

## Test Values

Here's an example key pair, two example requests, and the resulting`Authorization`header for each.
Caution  
  
The example signatures use the RSA 2048-bit keys below. Use these keys only for testing your signing code, not for sending production requests.

```

```

## Sample Code

This section shows the basic code for signing API requests.

### Java

```

```

### Python
Important  
  
This Python sample code requires TLS 1.2, which is not included with the default Python on Mac OS X.

```

```

### TypeScript

```

```

### JavaScript

```

```

### Ruby

```

```

### Go

The following example shows how to create a default signer.
Note  
  
The SDK for Go exposes a stand-alone signer that you can use to sign custom requests. You can find related code at[http_signer.go](https://github.com/oracle/oci-go-sdk/blob/master/common/http_signer.go).

```

```

### Bash

[View the Bash sample in full screen for easier reading](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../../Resources/Assets/signing_sample_bash.txt).

```

```

### C#

```

```
