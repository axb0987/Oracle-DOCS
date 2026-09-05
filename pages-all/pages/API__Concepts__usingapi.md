# REST APIs
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm
- Fetched: 2026-09-05 01:35 CDT

# REST APIs

The Oracle Cloud Infrastructure APIs are typical REST APIs that use HTTPS requests and responses. This topic describes basic information about using the APIs.

## API Reference and Endpoints

For links to the Oracle Cloud Infrastructure API reference and a list of the regional API endpoints, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

## API Version

The base path of the endpoint includes the desired API version (for example, 20160918). Here's an example for a POST request to create a new VCN in the Ashburn region:
```

```

## API Breaking Changes Policy

Oracle Cloud Infrastructure provides 12 months advance notice before the date of removing or changing an existing API of a Cloud Service that you have deployed which would require you to update the code.

## Request Signing Required

All Oracle Cloud Infrastructure API requests must be signed for authentication purposes. For information about the required credentials and how to sign the requests, see[Request Signatures](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm).

## HTTPS and TLS 1.2 Required

All Oracle Cloud Infrastructure API requests must support HTTPS and SSL protocol TLS 1.2.

## Maximum Allowed Client Clock Skew

HTTP status code 401 (NotAuthenticated) is returned if the client's clock is skewed more than 5 minutes from the server's. To determine the server's clock time, use this curl command with the API endpoint:
```

```

For example:

```

```

## Request and Response Format

The Oracle Cloud Infrastructure APIs use standard HTTP requests and responses. Each may contain Oracle-specific headers for pagination, entity tags (ETags), and so on as described elsewhere in this topic and in the API documentation.

Each response includes a unique Oracle-assigned request ID (for example, bb3f3275-f356-462a-93c4-bf40fb82bb02) in the`opc-request-id`response header. If you need to contact Oracle about a particular request, please provide this request ID.

Many of the API operations require JSON in the request body or return JSON in the response body. The specific contents of the JSON are described in the API documentation for the individual operation. Notice that the JSON is not wrapped or labeled according to the operation's name or the object's name or type.
Note  
  

Make sure to set the`Content-Type`header to`application/json`in your POST and PUT requests that contain JSON in the body.

### Example CreateVcn Request
```

```

### Example CreateVcn Response
```

```

## Error Format

If a request results in an error, the response contains a standard HTTP response code with 4xx for client errors and 5xx for server errors. The body also includes JSON with an error code and a description of the error. For example:
```

```

For a list of common errors across all services, see[API Errors](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../References/apierrors.htm).

## Request Throttling

Oracle Cloud Infrastructure applies throttling to many API requests to prevent accidental or abusive use of resources. If you make too many requests too quickly, you might see some succeed and others fail. Oracle recommends that you implement an exponential back-off, starting from a few seconds to a maximum of 60 seconds. When a request fails due to throttling, the system returns response code 429 and the following error code and description:
```

```

## Polling for Resource Status

Most Oracle Cloud Infrastructure resources, such as compute instances, have lifecycles. In many cases, you want your code to wait until a resource or work request reaches a specific state, or a timeout is exceeded, before taking further action.

You can poll a resource to determine its state. For example, when you call[GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance), the response body contains an[instance resource](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/)that includes the`lifecycleState`attribute. You might want your code to wait until the instance's`lifecycleState`is RUNNING before proceeding.

Different resources take different amounts of time to transition between states. Therefore, the optimal frequency and duration parameters for a polling strategy can vary among resources. The Oracle Cloud Infrastructure SDK waiters use the following default strategy:
- Use an exponential back-off, starting from a few seconds to a maximum of 30 seconds between poll attempts.
- Poll up to 20 minutes, and then stop.

Or more information on waiters, see:
- [SDK for Java waiters documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/javasdkconcepts.htm#waiters)
- [SDK for Ruby waiters documentation](https://docs.oracle.com/iaas/tools/ruby/latest/OCI/Response.html)

## Where to Find Your Tenancy's OCID

If you use the API, you'll need your tenancy 's OCID in order to sign the requests (see[Request Signatures](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm)). You'll also need it for some of the IAM API operations. An OCID is an Oracle Cloud ID (see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

Get the tenancy OCID from the Oracle Cloud Console on the Tenancy Details page:
- 

In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- 

The tenancy OCID is shown under Tenancy Information . Select Show to display the entire ID or select Copy to copy it to your clipboard.

[

The tenancy OCID looks something like this (notice the word "tenancy" in it):`ocid1.tenancy.oc1.. <unique_ID>`.

## List Pagination

Most List operations paginate results. For example, results are paginated for the[ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances)operation in the Core Services API. When you call a paginated List operation, the response indicates more pages of results by including the`opc-next-page`header.
Note  
  
A page can be empty even when more results remain. Anytime the`opc-next-page`header appears, there are more list items to get. For more information about resource list control, see[Overview of Search](https://docs.oracle.com/iaas/Content/Search/Concepts/queryoverview.htm).

List pagination for Object Storage[ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects)works differently because the pagination controls are also used for object name filtering.[ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects)returns`nextStartWith`instead of`opc-next-page`in the response body. To paginate through more objects, use the returned`nextStartWith`value with the`start`parameter. To filter which objects ListObjects returns, use the`start`and`end`parameters.

[To get the next page of results](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm#)

Make a new GET request against the same URL, modified by setting the page query parameter to the value from the`opc-next-page`header. Repeat this process until you get a response without an`opc-next-page`header. The absence of this header indicates that you have reached the last page of the list.
Note  
  
For an alternative to writing pagination code, see the functions in the[pagination module](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/pagination.html)provided with the SDK for Python.

[To get the previous page of results](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm#)

(Available with some APIs.) Make a new GET request against the same URL, modified by setting the page query parameter to the value from the`opc-prev-page`header. Repeat this process until you get a response without an`opc-prev-page`header. The absence of this header indicates that you have reached the first page of the list.
Note  
  
For an alternative to writing pagination code, see the functions in the[pagination module](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/pagination.html)provided with the SDK for Python.

[To change the maximum number of results per page](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm#)

In the GET request, set the`limit`to the number of items you want returned in the response.
Note  
  
The service will return no more than the number specified as`limit`, but might not return that exact number.

## Retry Token

For some operations you can provide a unique retry token (`opc-retry-token`) so the request can be retried in case of a timeout or server error without the risk of executing that same action again. The token expires after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

## ETags for Optimistic Concurrency Control

The API supports etags for the purposes of optimistic concurrency control. The GET and POST calls return an`etag`response header with a value you should store. When you later want to update or delete the resource, set the`if-match`header to the ETag you received for the resource. The resource will then be updated or deleted only if the ETag you provide matches the current value of that resource's ETag.

## Null vs. Empty Strings for Optional Parameters

If you send an empty string ("") as the value of an optional parameter, the API validates the value as normal (for example, checks against minimum and maximum allowed length, and so on). Often the minimum allowed length is 1, so an error would be returned. If you don't set the value (it's null), the API performs no validation, and some other action may occur. For example: if you don't set a value for the`displayName`
