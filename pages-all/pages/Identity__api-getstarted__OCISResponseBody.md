# Response Body
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISResponseBody.htm
- Fetched: 2026-09-05 02:17 CDT

# Response Body

The identity domains REST API requests return a JSON response body. The status code indicates success or failure.

## Supported Response Codes

Note  
  
See[Response Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/StatusCodes.htm)for more information on the supported response codes.

## Response Body on Success

The response format for all REST API requests is a JSON object. The exact contents of the response depends on the contents and type of request, whether the request succeeded or failed, and any query filtering that was performed.
Note  
  
See the Examples tab on each endpoint page for specific response body examples.

## Successful POST Response Body

The following is an example response indicating successful creation of a`User`resource with a`POST`request:
```

```

## Successful GET Response Body

`GET`requests typically return a`ListResponse`object, which might contain multiple records. This example shows the results of a`GET`search on Users, with the query parameter:`filter=userName sw "d"`, that is, users whose usernames begin with`d`.
```

```

## Simple Response Body on Error

On error, and on success, the response body is JSON. The format for all identity domains REST API error responses is similar. This example is a simple exception detailing the status code and exception message for an invalid request.
```

```

## Validation Exception Response Example

This example is a validation exception where some required attributes are missing.
```

```

## Functional Exception Response Example

This example is a functional exception with additional details.
```

```

## Dynamic Monitoring Using the ECID and RID HTTP Headers

Dynamic monitoring is the mechanism by which HTTP requests can be uniquely identified and thus tracked as they flow through the system.

It also provides a means by which context information can be communicated between cooperating identity domain components involved in fulfilling requests. The Execution Context ID (ECID) and the Relationship ID (RID) are useful in tracking the sequence of events between services.
- 

The ECID: A unique identifier. The ECID is unique for each new root task. This number remains the same as it's shared across the tree of tasks associated with the root task.
- 

The RID: A relationship identifier. The RID is an ordered set of numbers that describes the location of each task in the tree of tasks. The leading number is typically a zero, and then the numbers increase for each additional subtask.

The`X-ORACLE-DMS-ECID`and the`X-ORACLE-DMS-RID`HTTP headers are returned as part of the REST response from the identity domain. These HTTP headers correspond to the ECID and the RID of the request. The values for these headers are set by the identity domain when returning the response. The caller can use the ECID and the RID to track and correlate requests that originate with events that arise from the identity domain.

For example, the client may include these values as part of an error message, because it's important to correlate events on the client side with errors on the server side. The Oracle standard format for logging involves a field dedicated to the ECID. After the ECID is known, when it's read from an error level log message, for example, it's possible to find all other log messages associated with that task by querying the log files for messages that contain that ECID.

Use the identity domains Diagnostic Data reports to view logging data captured for diagnostic purposes. You can find the ECID and the RID in the report, and then correlate those identifiers to the ECID and the RID that are returned by the identity domains REST calls that your applications make. See[Running the Diagnostic Data Report](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../reports/run-diagnostic.htm).

### Dynamic Monitoring Examples
This section contains examples that show the following:
- 

A POST request on the`/Users`endpoint.
- 

The cURL command headers that are a result of executing the POST on the`/Users`endpoint.
- 

A return response of a GET on the`/AuditEvents`endpoint that shows that the ECID is the same as what was used by the server to create the user.
- 

A section of the diagnostic report that was generated when the POST request on the`/Users`endpoint was run.

POST Request to /Users
```

```

cURL Command Headers in the Response
```

```

Response to the GET Request to /AuditEvents

Note: This example shows that the ECID is the same as what was used by the server to create the user. Request
```

```

Response
```

```

Diagnostic Report Sample
