# API Errors
- Source: https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm
- Fetched: 2026-09-05 01:35 CDT

# API Errors

## Common Errors Returned by All Services

The following table lists the common errors returned by all the services for Oracle Cloud Infrastructure.

HTTP Status Code Error Code Description Retry
[400](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400__400_cannotparserequest)CannotParseRequest`The request is incorrectly formatted. No.
[400](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400__400_invalidparameter)InvalidParameter`A parameter is invalid or incorrectly formatted. No.
[400](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400__400_limitexceeded)LimitExceeded`Fulfilling this request exceeds the Oracle-defined limit for this tenancy for this resource type. No.
[400](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400__400_missingparameter)MissingParameter`A required parameter is missing. No.
[400](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400__400_quotaexceeded)QuotaExceeded`Fulfilling this request exceeds the administrator-defined quota for this compartment for this resource. No.
[400](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_400__400_relatedresourcenotauthorizedornotfound)RelatedResourceNot AuthorizedOrNotFound`

A resource specified in the body of the request was not found, or you do not have authorization to access that resource. No.
[401](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_401)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_401__401_notauthenticated)NotAuthenticated`

The required authentication information was not provided or was incorrect. No.
[403](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_403)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_403__403_notallowed)NotAllowed`This operation must be directed at the home region. No.
[403](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_403)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_403__403_notauthorized)NotAuthorized`You do not have authorization to update one or more of the fields included in this request. No.
[403](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_403)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_403__403_signuprequired)SignUpRequired`This operation requires opt-in before it may be called. No.
[404](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404__404_invalidparameter)InvalidParameter`A dynamic path component is invalid or is syntactically valid but is not allowed. No.
[404](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404__404_notauthorizedornotfound)NotAuthorizedOrNotFound`A resource specified via the URI (path or query parameters) of the request was not found, or you do not have authorization to access that resource. For more information, see[HTML Status Code 404](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5). No.
[404](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404__404_notfound)NotFound`There is no operation supported at the URI path and HTTP method you specified in the request. No.
[404](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_404__404_namespacenotfound)NamespaceNotFound`You do not have authorization to perform this request, or the requested resource could not be found. No.
[405](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_405)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_405__405_methodnotallowed)MethodNotAllowed`The target resource does not support the HTTP method. No.
[409](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409__409_conflict)Conflict`The requested state for the resource conflicts with its current state. This state is not transient. No.
[409](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409__409_externalserverincorrectstate)ExternalServerIncorrectState`The server is in an incorrect state, and has timed out, returned an invalid response, or is unreachable. Yes, with backoff. Refer to the error description for any required actions before you retry.
[409](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409__409_incorrectstate)IncorrectState`The requested state for the resource conflicts with its current state but given some amount of time it will be in the correct state. Yes, with backoff. Refer to the error description for any required actions before you retry.
[409](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409__409_invalidatedretrytoken)InvalidatedRetryToken`The provided retry token was used in an earlier request that resulted in a system update, but a subsequent operation invalidated the token. This can happen, for example, in cases where an entity created with the same token has since been deleted. If the system state change that is associated with this request should be performed again, retry it using a different token. No.
[409](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409__409_resourcelocked)ResourceLocked`The requested resource is locked. This is usually because the resource is in active use, or because modifying the resource will cause another resource to stop functioning. No.
[409](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_409__409_notauthorizedorresourcealreadyexists)NotAuthorizedOrResourceAlreadyExists`You do not have authorization to perform this request, or the resource you are attempting to create already exists. This error code is returned only from`create`operations, where it is returned instead of the more general`NotAuthorizedOrNotFound`error code. No.
[412](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_412)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_412__412_noetagmatch)NoEtagMatch`The ETag specified in the request does not match the ETag for the resource. No.
[413](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_413)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_413__413_payloadtoolarge)PayloadTooLarge`The request entity is larger than limits defined by server. No.
[422](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_422)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_422__422_unprocessableentity)UnprocessableEntity`Payload is syntactically correct but semantically invalid. No.
[429](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_429)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_429__429_toomanyrequests)TooManyRequests`You have issued too many requests to the Oracle Cloud Infrastructure APIs in too short of an amount of time. Yes, with backoff.
[431](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_431)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_431__431_requestheaderfieldstoolarge)RequestHeaderFieldsTooLarge`The request's HTTP headers are too long. The request may be resubmitted after reducing the size of the request headers. No.
[500](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_500)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_500__500_internalservererror)InternalServerError`An internal server error occurred. Yes, with backoff.
[501](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_501)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_501__501_methodnotimplemented)MethodNotImplemented`The HTTP request target does not recognize the HTTP method. No.
[503](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503__503_serviceunavailable)ExternalServerUnreachable`A connection with an external system needed to fulfill the request could not be established. Yes, with backoff.
[503](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503__503_serviceunavailable)ExternalServerTimeout`A connection with an external system needed to fulfill the request timed out before a response was received. Yes, with backoff.
[503](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503__503_serviceunavailable)ExternalServerInvalidResponse`A connection with an external system needed to fulfill the request resulted in an unacceptable response. Yes, with backoff.
[503](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503)`[](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#apierrors_503__503_serviceunavailable)ServiceUnavailable`The service is currently unavailable. Yes, with backoff.

## API Error Details and Troubleshooting

This section contains detailed information and troubleshooting suggestions for HTTP Status error codes.

### HTTP Status 400 Error Codes

#### RelatedResourceNotAuthorizedOrNotFound

Description

A resource specified in the body of the request was not found, or you do not have authorization to access that resource.

Troubleshooting
- Authorization error: Verify that the user making the request is in a group that has the permissions to work with resources in a compartment. To understand more about permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).
- Compartment or resource not found: Verify that the compartment or resource exists and is referenced correctly.

#### InvalidParameter

Description

A parameter value is invalid or incorrectly formatted.

Troubleshooting
- Refer to the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation and check parameters in the request for typos or incorrect formats and correct the request.

#### MissingParameter

Description

A required parameter is missing

Troubleshooting
- The request is missing a required parameter for this API. Refer to the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation and correct the request.

#### QuotaExceeded

Description

Fulfilling this request exceeds the administrator-defined quota for this compartment for this resource.

Troubleshooting
- The administrator-defined quota for this compartment for this resource would be exceeded by fulfilling this request. Check the resource quota and request an increase for the quota or clean up unused resources if necessary. To understand more about quotas, see:[Overview of Compartment Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

#### LimitExceeded

Description

Fulfilling this request exceeds the Oracle-defined limit for this tenancy for this resource type.

Troubleshooting The Oracle-defined limit for this tenancy for this resource type would be exceeded by fulfilling this request. Check the tenancy level limit for this resource and[request a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)on the tenancy or clean up unused resources and re-send the request. To understand more about your OCI service limits and how to request a limit increase, see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).

#### CannotParseRequest

Description

The request is incorrectly formatted.

Troubleshooting The request for most operations that take a body should be formatted as[JSON](https://www.json.org/). See the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation to confirm if the operation takes JSON, and if so confirm you are passing valid JSON in the request body.

#### InvalidStorageTier

Description

The request is using an invalid Storage Tier.

Troubleshooting The storageTier parameter provided is not correct. Refer to the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation and correct the request.

### HTTP Status 401 Error Codes

#### NotAuthenticated

Description

The required authentication information was not provided or was incorrect.

Troubleshooting

There are several things that can trigger this error code:
- Missing or incorrect authentication information.
- Verify that all of the required information (tenant OCID, user OCID, fingerprint, and private key) is provided and accurate
- Verify your`private_key_path`is pointing to your private key and not the corresponding public key
- Verify the public/private key pairs you are using are in the correct format
- Verify the user account is part of a group with the appropriate permissions to perform the actions in the plan you are executing
- Verify your tenancy has been subscribed to the region you are targeting in your plan
- Verify that the public key corresponding to the fingerprint has been uploaded for the user you are making the request as. For more information, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs).
- Clock skew. This status code is returned if the client's clock is skewed more than five (5) minutes from the server's clock. For more information, see[Maximum Allowed Client Clock Skew](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#clock).
- API request signature error. This status code is returned if a required piece of information is missing or is malformed in the Authorization header. For more information, see[Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm#Request_Signatures).

### HTTP Status 403 Error Codes

#### SignUpRequired

Description

This operation requires opt-in before it can be called.

Troubleshooting Make sure that the user is signed up for this feature. If not, please contact support and sign up for this service.

#### NotAllowed

Description

This operation must be directed at the home region.

Troubleshooting This operation must be directed at the home region. Update the source code to provide the correct region information.

#### NotAuthorized

Description

You do not have authorization to update one or more of the fields included in this request.

Troubleshooting Check the request and remove any unauthorized fields. To understand more about permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

### HTTP Status 404 Error Codes

#### NamespaceNotFound

Description

A resource specified via the URI (path or query parameters) of the request was not found, or you do not have authorization to access that resource.

Troubleshooting The resource is not found or the caller is not authorized to perform requested operation on the resource, for a resource specified via the request URI for GET (list or single entity get), UPDATE, and DELETE operations. Check that the requested resource actually exists and that you have access to it. To understand more about permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

#### NotFound

Description

There is no operation supported at the URI path and HTTP method you specified in the request.

Troubleshooting Either the static path components do not exist or you are unauthorized to access them. Check the request and update the static path component.

#### NotAuthorizedOrNotFound

Description

A resource specified via the URI (path or query parameters) of the request was not found, or you do not have authorization to access that resource.

Troubleshooting The resource is not found or the caller is not authorized to perform requested operation on the resource, for a resource specified via the request URI for GET (list or single entity get), UPDATE, and DELETE operations. Check that the requested resource actually exists and that you have access to it. To understand more about permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

#### InvalidParameter

Description

A parameter specified in the path is invalid or is syntactically valid but is not allowed.

Troubleshooting Check the parameters in the request for typos or incorrect formats. Refer to the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation and correct the request.

### HTTP Status 405 Error Codes

#### MethodNotAllowed

Description

The target resource does not support the HTTP method used.

Troubleshooting The HTTP method in the request (for example, PUT, POST, DELETE, or GET) is not allowed by the target resource. Check if the intended HTTP method is specified correctly, and check the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation to confirm you are using the correct HTTP method.

### HTTP Status 409 Error Codes

#### NotAuthorizedOrResourceAlreadyExists

Description

You do not have authorization to perform this request, or the resource you are attempting to create already exists. This error code is returned only from create operations, where it is returned instead of the more general`NotAuthorizedOrNotFound`error code.

Troubleshooting
- If the request is to create a resource, check that the resource does not already exist and that the calling user is authorized to create this type of resource in this compartment.
- Verify that the user is in a group that has the permissions to work with resources in a compartment. To understand more about permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

#### InvalidatedRetryToken

Description

The provided retry token was used in an earlier request that resulted in a system update, but a subsequent operation invalidated the token. This can happen in cases where an entity created with the same token has since been deleted. If the system state change that is associated with this request needs to be performed again, use a different token.

Troubleshooting Check the source code and verify that the retry token is used correctly.

#### ExternalServerIncorrectState

Description

The server is in an incorrect state, and has timed out, returned an invalid response, or is unreachable.

Troubleshooting

Try the following:
- Check the error message for more details. You may have to retart your server and make sure it is accessible by Oracle services.
- Check the error logs on your server for useful information.
- Your server may have experienced a temporary problem. Wait a moment, and then retry the request.
- If the request still fails, contact OCI technical support and include the opc-request-id from the HTTP request or response which failed.

#### IncorrectState

Description

The requested state for the resource conflicts with its current state but given some amount of time it will be in the correct state.

Troubleshooting

Try the following:
- Check resource dependencies. A resource cannot be deleted if it is still used by other resources.
- Try the request again later or update the code to wait for the right state to be reached before performing this action. Some operations require the resource to be in a certain state (for example, running).

#### Conflict

Description

The requested state for the resource conflicts with its current state. This state is not transient.

Troubleshooting Check the requested resource state and try again.

#### ResourceLocked

Description

The requested resource is locked. This is usually because the resource is in active use, or because modifying the resource will cause another resource to stop functioning.

Troubleshooting

Check the resource for details on the lock. You may be able to call an API to remove the lock on the resource, or you may be able to pass a parameter to the API to ignore the lock and perform the requested operation.

If the lock was placed on the resource by an external service, you may not be able to remove the lock at all. For example, administrators in parent tenancies can create locked quotas in a child tenancy, and administrators in the child tenancy cannot change the quotas.

Some locks specify a related resource where you must delete the related resource in order to remove the lock on this resource.

### HTTP Status 412 Error Codes

#### NoEtagMatch

Description

The ETag specified in the if-match field of the request does not match the ETag for the resource.

Troubleshooting

Correct ETag in the request if this is not expected. For more information on ETags, see the[Etag documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag).

### HTTP Status 413 Error Codes

#### PayloadTooLarge

Description

The request entity is larger than limits defined by server.

Troubleshooting

Try sending a smaller request.

### HTTP Status 422 Error Codes

#### UnprocessableEntity

Description

The payload is syntactically correct but semantically invalid.

Troubleshooting

The service is unable to process the request. Check the request and reformat if necessary.

### HTTP Status 429 Error Codes

#### TooManyRequests

Description

You have issued too many requests to the Oracle Cloud Infrastructure APIs too quickly.

Troubleshooting

This is caused by too many requests within a small amount of time. If the service has throttling mechanisms, too many requests within a short period of time will result in some requests being rejected. Try adding some delays between requests to avoid this error.

### HTTP Status 431 Error Codes

#### RequestHeaderFieldsTooLarge

Description

The HTTP headers in the request are too long.

Troubleshooting

The request may be resubmitted after reducing the size of the request headers.

### HTTP Status 500 Error Codes

#### InternalServerError

Description

An internal server error occurred.

Troubleshooting

The service failed to process the request for unknown reasons. This is usually an issue on the service side, possibly due to a temporary service outage or a bug. Retry sending the same request. If the retry still fails, contact[OCI technical support](https://www.oracle.com/support/cloud.html#infrastructure-tab)and include the`opc-request-id`from the HTTP request or response that failed in your message.

### HTTP Status 501 Error Codes

#### MethodNotImplemented

Description

The HTTP request target does not recognize the HTTP method.

Troubleshooting

The HTTP method in the request is not implemented on the service. Refer to the[REST API documentation](https://docs.oracle.com/iaas/api/)for the operation and update the request to use the right HTTP method for the operation.

### HTTP Status 503 Error Codes

#### ServiceUnavailable, ExternalServerUnreachable, ExternalServerTimeout, ExternalServerInvalidResponse

Description

The service timed out, is unreachable, is currently unavailable, or returned an invalid response.

Troubleshooting

Retry sending the same request after some time. If the retry still fails,[contact OCI technical support](https://www.oracle.com/support/cloud.html#infrastructure-tab)
