# Adding Header Transformation Request Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingheadertransformrequestpolicies.htm
- Fetched: 2026-09-05 01:38 CDT

# Adding Header Transformation Request Policies

You can add header transformation request policies to API deployment specifications using the Console or by editing a JSON file.

Note that you cannot use header transformation policies to transform certain protected request headers. See[Protected Request Headers and Response Headers](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-protectedrequestresponseheaders.htm).

## Using the Console to Add Header Transformation Request Policies

To add header transformation request policies to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

Select Next and specify authentication options on the Authentication page.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to enter details for individual routes in the API deployment on the Routes page.
- On the Routes page, select the route for which you want to specify header transformation request policies.
- Select Show route request policies .
- Select the Add button beside Header transformations to update the headers included in a request to the API gateway for the current route.
- 

To limit the headers included in a request, specify:
- Action: Filter.
- Type: Either Block to remove from the request the headers you explicitly list, or Allow to only allow in the request the headers you explicitly list (any other headers are removed from the request).
- Header names: The list of headers to remove from the request or allow in the request (depending on the setting of Type ). The names you specify are not case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items you filter as allowed). For example,`User-Agent`.
- 

To change the name of a header included in a request (whilst keeping its original value), specify:
- Action: Rename.
- Header name: The original name of the header that you are renaming. The name you specify is not case-sensitive, and must not be included in any other transformation request policies for the route. For example,`X-Username`.
- New header name: The new name of the header you are renaming. The name you specify is not case-sensitive (capitalization might be ignored), and must not be included in any other transformation request policies for the route (with the exception of items you filter as allowed). For example,`X-User-ID`.
- 

To add a new header to a request (or to change or retain the values of an existing header already included in a request), specify:
- Action: Set.
- 

Behavior: If the header already exists, specify what to do with the header's existing value:
- Overwrite , to replace the header's existing value with the value you specify.
- Append , to append the value you specify to the header's existing value.
- Skip , to keep the header's existing value.
- Header name: The name of the header to add to the request (or to change the value of). The name you specify is not case-sensitive (capitalization might be ignored), and must not be included in any other transformation request policies for the route (with the exception of items you filter as allowed). For example,`X-Api-Key`.
- Values: The value of the new header (or the value to replace or append to an existing header's value, depending on the setting of Behavior ). You can specify multiple values. The value you specify can be a simple string, or can include context variables (except for`request.body`) enclosed within`${...}`delimiters. For example,`"value": "zyx987wvu654tsu321"`,`"value": "${request.path[region]}"`,`"value": "${request.headers[opc-request-id]}"`.
- Select Update .
- Select Update , and then select Next to review the details you entered for individual routes.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Header Transformation Request Policies

To add header transformation request policies to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add header transformation request policies, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

Insert a`requestPolicies`section after the`backend`section for the route to which you want the header transformation request policy to apply. For example:

```

```

- 

Add a`headerTransformations`section to the`requestPolicies`section.

```

```

- 

To limit the headers included in a request, specify a`filterHeaders`header transformation request policy:

```

```

where:
- `"type": "<BLOCK|ALLOW>"`indicates what to do with the headers specified by`"items":[{"name":"<header-name>"}]`:
- Use`BLOCK`to remove from the request the headers you explicitly list.
- Use`ALLOW`to only allow in the request the headers you explicitly list (any other headers are removed from the request).
- `"name":"<header-name>`is a header to remove from the request or allow in the request (depending on the setting of`"type": "<BLOCK|ALLOW>"`). The name you specify is not case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items in`ALLOW`lists). For example,`User-Agent`.

You can remove and allow up to 50 headers in a`filterHeaders`header transformation request policy.

For example:

```

```

In this example, the API gateway removes the`User-Agent`header from all incoming requests.
- 

To change the name of a header included in a request (whilst keeping its original value), specify a`renameHeaders`header transformation request policy:

```

```

where:
- `"from": "<original-name>"`is the original name of the header that you are renaming. The name you specify is not case-sensitive, and must not be included in any other transformation request policies for the route. For example,`X-Username`.
- `"to": "<new-name>"`is the new name of the header you are renaming. The name you specify is not case-sensitive (capitalization might be ignored), and must not be included in any other transformation request policies for the route (with the exception of items in`ALLOW`lists). For example,`X-User-ID`.

You can rename up to 20 headers in a`renameHeaders`header transformation request policy.

For example:

```

```

In this example, the API gateway renames any`X-Username`header to`X-User-ID`, whilst keeping the header's original value.
- 

To add a new header to a request (or to change or retain the values of an existing header already included in a request), specify a`setHeaders`header transformation request policy:

```

```

where:
- `"name":"<header-name>`is the name of the header to add to the request (or to change the value of). The name you specify is not case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items in`ALLOW`lists). For example,`X-Api-Key`.
- `"values": ["<header-value>"]`is the value of the new header (or the value to replace or append to an existing header's value, depending on the setting of`"ifExists": "<OVERWRITE|APPEND|SKIP>"`). The value you specify can be a simple string, or can include context variables (except for`request.body`) enclosed within`${...}`delimiters. For example,`"values": "zyx987wvu654tsu321"`,`"values": "${request.path[region]}"`,`"values": "${request.headers[opc-request-id]}"`.

You can specify up to 10 values. If you specify multiple values, the API gateway adds a header for each value.
- 

`"ifExists": "<OVERWRITE|APPEND|SKIP>"`indicates what to do with the header's existing value if the header specified by`<header-name>`already exists:
- Use`OVERWRITE`to replace the header's existing value with the value you specify.
- Use`APPEND`to append the value you specify to the header's existing value.
- Use`SKIP`to keep the header's existing value.

If not specified, the default is`OVERWRITE`.

You can add (or change the values of) up to 20 headers in a`setHeaders`header transformation request policy.

For example:

```

```

In this example, the API gateway adds the`X-Api-Key:zyx987wvu654tsu321`header to all incoming requests. If an incoming request already has an`X-Api-Key`header set to a different value, the API gateway replaces the existing value with`zyx987wvu654tsu321`.
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
