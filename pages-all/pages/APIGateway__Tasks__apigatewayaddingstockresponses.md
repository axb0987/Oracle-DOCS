# Adding Stock Responses as an API Gateway Back End
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingstockresponses.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Stock Responses as an API Gateway Back End

Find out how to define a path to a stock response back end with API Gateway.

You'll often want to verify that an API has been successfully deployed on an API gateway without having to set up an actual back-end service. One approach is to define a route in the API deployment specification that has a path to a 'dummy' back end. On receiving a request to that path, the API gateway itself acts as the back end and returns a stock response you've specified.

Equally, there are some situations in a production deployment where you'll want a particular path for a route to consistently return the same stock response without sending a request to a back end. For example, when you want a call to a path to always return a specific HTTP status code in the response.

Using the API Gateway service, you can define a path to a stock response back end that always returns the same:
- HTTP status code
- HTTP header fields (name-value pairs)
- content in the body of the response

Note the following restrictions when defining stock responses and stock response back ends:
- each header name must not exceed 1KB in length
- each header value must not exceed 4KB in length
- each body response must not exceed 5KB in length (including any encoding)
- a stock response back end definition must not include more than 50 header fields

You can add stock response back ends to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Stock Responses to an API Deployment Specification

To add stock responses to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

On the Authentication page, specify authentication options.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

On the Routes page, create a new route and specify:
- 

Path: A path for API calls using the listed methods to the back-end service. Note that the route path you specify:
- is relative to the deployment path prefix (see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm))
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- Methods: One or more methods accepted by the back-end service. For example,`GET, PUT`.
- 

Add a single backend or Add multiple backends : Whether to route all requests to the same back end, or to route requests to different back ends according to the context variable and rules you enter.

These instructions assume you want to use a single back end, so select Add a single backend . Alternatively, if you want to use different back ends, select Add multiple backends and follow the instructions in[Using the Console to Add Dynamic Back End Selection to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm#apigatewaydynamicroutingbasedonrequest_topic-Using_the_Console_to_Add_Dynamic_Backend_Selection_to_an_API_Deployment_Specification).
- Backend Type: The type of the back-end service as`Stock response`.
- Status code: Any valid HTTP response code. For example,`200`
- 

Body: Optionally specifies the content of the response body, in an appropriate format. For example:
- If you specify a Header name and Header value of`Content-Type`and`text/plain`respectively, the response body might be`"Hello world"`.
- If you specify a Header name and Header value of`Content-Type`and`application/json`respectively, the response body might be`{"username": "john.doe"}`.

Note that the response body must not exceed 5KB in length (including any encoding).
- 

Header name and Header value : Optionally, you can specify the name of an HTTP response header and its value. For example, a name of`Content-Type`and a value of`application/json`. You can specify multiple header name and value pairs (up to a maximum of 50). Note that in each case:
- the header name must not exceed 1KB in length
- the header value must not exceed 4KB in length

In this example, a request to the`/test`path returns a 200 status code and a JSON payload in the body of the response.

Field: Enter:
Path:`/test`
Methods:`GET`
Backend Type:`Stock response`
Status code:`200`
Body:`{"username": "john.doe"}`
Header name:`Content-Type`
Header value:`application/json`

In this example, a request to the`/test-redirect`path returns a 302 status code and a temporary url in the`Location`header of the response.

Field: Enter:
Path:`/test-redirect`
Methods:`GET`
Backend Type:`Stock response`
Status code:`302`
Body: n/a
Header name:`Location`
Header value:`http://www.example.com`
- (Optional) Select Another header to enter details of additional headers.
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Stock Responses to an API Deployment Specification

To add stock responses to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add a stock response back end, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

In the`routes`section, include a new`path`section for a stock response back end:

```

```

where:
- 

`<api-route-path>`specifies a path for API calls using the listed methods to the stock response back end. Note that the route path you specify:
- is relative to the deployment path prefix (see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm))
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- 

can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- `<method-list>`specifies one or more methods accepted by the stock response back end, separated by commas. For example,`"GET, PUT"`.
- `"type": "STOCK_RESPONSE_BACKEND"`indicates that the API gateway itself will act as the back end and return the stock response you define (the status code, the header fields and the body content).
- `<http-response-code>`is any valid HTTP response code. For example,`200`
- `"name": "<header-name>", "value": "<header-value>"`optionally specifies the name of an HTTP response header and its value. For example,`"name": "Content-Type", "value":"application/json"`. You can specify multiple`"name": "<header-name>", "value": "<header-value>"`pairs in the`headers:`section (up to a maximum of 50). Note that in each case:
- `<header-name>`must not exceed 1KB in length
- `<header-value>`must not exceed 4KB in length
- `"body": "<body-content>"`optionally specifies the content of the response body, in an appropriate format. For example:
- If the`Content-Type`header is`text/plain`, the response body might be`"body": "Hello world"`.
- If the`Content-Type`header is`application/json`, the response body might be`"body": "{\"username\": \"john.doe\"}"`. In the case of a JSON response, note that quotation marks in the response have to be escaped with a backslash (`\`) character.

Note that`<body-content>`must not exceed 5KB in length (including any encoding).

In this example, a request to the`/test`path returns a 200 status code and a JSON payload in the body of the response.

```

```

In this example, a request to the`/test-redirect`path returns a 302 status code and a temporary url in the`Location`header of the response. This example also demonstrates that you can create an API deployment specification with just one route to a back end of type STOCK_RESPONSE_BACKEND.

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
