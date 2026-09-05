# Transforming Incoming Requests and Outgoing Responses
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests.htm
- Fetched: 2026-09-05 01:38 CDT

# Transforming Incoming Requests and Outgoing Responses

Find out how to modify incoming requests and outgoing responses being sent to and from back-end services with API Gateway.

There are often situations when you'll want an API gateway to modify incoming requests before sending them to back-end services. Similarly, you might want the API gateway to modify responses returned by back-end services. For example:
- Back-end services might require requests to include a particular set of HTTP headers (for example, Accept-Language and Accept-Encoding). To hide this implementation detail from API consumers and API clients, you can use your API gateway to add the required headers.
- Web servers often include full version information in response headers. For security reasons, you might want to prevent API consumers and API clients knowing about the underlying technology stack. You can use your API gateway to remove server headers from responses.
- Back-end services might include sensitive information in a response. You can use your API gateway to remove such information.

Using an API gateway, you can:
- Add, remove, and modify headers in requests and responses.
- Add, remove, and modify query parameters in requests.
- Rewrite request URLs from a public format to an internal format, perhaps to support legacy applications and migrations.

You use request and response policies to transform the headers and query parameters of incoming requests, and the headers of outgoing responses (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).

You can include context variables in header and query parameter transformation request and response policies. Including context variables enables you to modify headers and query parameters with the values of other headers, query parameters, path parameters, and authentication parameters. Note that values of context variable values are extracted from the original request or response, and are not subsequently updated as an API gateway uses a transformation policy to evaluate a request or response. For more information about context variables, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

If a header or query parameter transformation request or response policy will result in an invalid header or query parameter, the transformation policy is ignored.

Note that you cannot use header transformation policies to transform certain protected request and response headers. See[Protected Request Headers and Response Headers](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-protectedrequestresponseheaders.htm).

You can add header and query parameter transformation request and response policies to an API deployment specification by:
- using the Console
- editing a JSON file

Contents:
- [Adding Header Transformation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingheadertransformrequestpolicies.htm)
- [Adding Query Parameter Transformation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingqueryparamtransformrequestpolicies.htm)
- [Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm)
- [Transformation Examples](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-transformexamples.htm)
- [Protected Request Headers and Response Headers](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-protectedrequestresponseheaders.htm)
