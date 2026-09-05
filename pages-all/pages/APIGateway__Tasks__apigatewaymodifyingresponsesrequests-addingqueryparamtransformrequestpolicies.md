# Adding Query Parameter Transformation Request Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingqueryparamtransformrequestpolicies.htm
- Fetched: 2026-09-05 01:38 CDT

# Adding Query Parameter Transformation Request Policies

You can add query parameter transformation request policies to API deployment specifications using the Console or by editing a JSON file.

## Using the Console to Add Query Parameter Transformation Request Policies

To add query parameter transformation request policies to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

Select Next and specify authentication options on the Authentication page.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to enter details for individual routes in the API deployment on the Routes page.
- On the Routes page, select the route for which you want to specify query parameter transformation request policies.
- Select Show route request policies .
- Select the Add button beside Query parameter transformations to update the query parameters included in a request to the API gateway for the current route.
- 

To limit the query parameters included in a request, specify:
- Action: Filter.
- Type: Either Block to remove from the request the query parameters you explicitly list, or Allow to only allow in the request the query parameters you explicitly list (any other query parameters are removed from the request).
- Query parameter names: The list of query parameters to remove from the request or allow in the request (depending on the setting of Type ). The names you specify are case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items you filter as allowed).. For example,`User-Agent`.
- 

To change the name of a query parameter included in a request (whilst keeping its original value), specify:
- Action: Rename.
- Query parameter name: The original name of the query parameter that you are renaming. The name you specify is case-sensitive, and must not be included in any other transformation request policies for the route. For example,`X-Username`.
- New query parameter name: The new name of the query parameter you are renaming. The name you specify is case-sensitive (capitalization is respected), and must not be included in any other transformation request policies for the route (with the exception of items you filter as allowed). For example,`X-User-ID`.
- 

To add a new query parameter to a request (or to change or retain the values of an existing query parameter already included in a request), specify:
- Action: Set.
- 

Behavior: If the query parameter already exists, specify what to do with the query parameter's existing value:
- Overwrite , to replace the query parameter's existing value with the value you specify.
- Append , to append the value you specify to the query parameter's existing value.
- Skip , to keep the query parameter's existing value.
- Query parameter name: The name of the query parameter to add to the request (or to change the value of). The name you specify is case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items you filter as allowed). For example,`X-Api-Key`.
- Values: The value of the new query parameter (or the value to replace or append to an existing query parameter's value, depending on the setting of Behavior ). The value you specify can be a simple string, or can include context variables enclosed within`${...}`delimiters. For example,`"value": "zyx987wvu654tsu321"`,`"value": "${request.path[region]}"`,`"value": "${request.headers[opc-request-id]}"`. You can specify multiple values.
- Select Update .
- Select Update , and then select Next to review the details you entered for individual routes.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Query Parameter Transformation Request Policies

To add query parameter transformation request policies to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add query parameter transformation request policies, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

Insert a`requestPolicies`section after the`backend`section for the route to which you want the query parameter transformation request policy to apply. For example:

```

```

- 

Add a`queryParameterTransformations`section to the`requestPolicies`section.

```

```

- 

To limit the query parameters included in a request, specify a`filterQueryParameters`query parameters transformation request policy:

```

```

where:
- `"type": "<BLOCK|ALLOW>"`indicates what to do with the query parameters specified by`"items":[{"name":"<query-parameter-name>"}]`:
- Use`BLOCK`to remove from the request the query parameters you explicitly list.
- Use`ALLOW`to only allow in the request the query parameters you explicitly list (any other query parameters are removed from the request).
- `"name":"<query-parameter-name>`is a query parameter to remove from the request or allow in the request (depending on the setting of`"type": "<BLOCK|ALLOW>"`). The name you specify is case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items in`ALLOW`lists). For example,`User-Agent`.

You can remove and allow up to 50 query parameters in a`filterQueryParameters`query parameter transformation request policy.

For example:

```

```

In this example, the API gateway removes the`User-Agent`query parameter from all incoming requests.
- 

To change the name of a query parameter included in a request (whilst keeping its original value), specify a`renameQueryParameters`query parameter transformation request policy:

```

```

where:
- `"from": "<original-name>"`is the original name of the query parameter that you are renaming. The name you specify is case-sensitive, and must not be included in any other transformation request policies for the route. For example,`X-Username`.
- `"to": "<new-name>"`is the new name of the query parameter you are renaming. The name you specify is case-sensitive (capitalization is respected), and must not be included in any other transformation request policies for the route (with the exception of items in`ALLOW`lists). For example,`X-User-ID`.

You can rename up to 20 query parameters in a`renameQueryParameters`query parameter transformation request policy.

For example:

```

```

In this example, the API gateway renames any`X-Username`query parameter to`X-User-ID`, whilst keeping the query parameter's original value.
- 

To add a new query parameter to a request (or to change or retain the values of an existing query parameter already included in a request), specify a`setQueryParameters`query parameter transformation request policy:

```

```

where:
- `"name": "<query-parameter-name>"`is the name of the query parameter to add to the request (or to change the value of). The name you specify is case-sensitive, and must not be included in any other transformation request policies for the route (with the exception of items in`ALLOW`lists). For example,`X-Api-Key`.
- `"values": ["<query-parameter-value>"]`is the value of the new query parameter (or the value to replace or append to an existing query parameter's value, depending on the setting of`"ifExists": "<OVERWRITE|APPEND|SKIP>"`). The value you specify can be a simple string, or can include context variables enclosed within`${...}`delimiters. For example,`"values": "zyx987wvu654tsu321"`,`"values": "${request.path[region]}"`,`"values": "${request.headers[opc-request-id]}"`.

You can specify up to 10 values. If you specify multiple values, the API gateway adds a query parameter for each value.
- 

`"ifExists": "<OVERWRITE|APPEND|SKIP>"`indicates what to do with the query parameter's existing value if the query parameter specified by`<query-parameter-name>`already exists:
- Use`OVERWRITE`to replace the query parameter's existing value with the value you specify.
- Use`APPEND`to append the value you specify to the query parameter's existing value.
- Use`SKIP`to keep the query parameter's existing value.

If not specified, the default is`OVERWRITE`.

You can add (or change the values of) up to 20 query parameters in a`setQueryParameters`query parameter transformation request policy.

For example:

```

```

In this example, the API gateway adds the`X-Api-Key:zyx987wvu654tsu321`query parameter to all incoming requests. If an incoming request already has an`X-Api-Key`query parameter set to a different value, the API gateway replaces the existing value with`zyx987wvu654tsu321`.
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
