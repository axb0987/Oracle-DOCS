# Creating an API Deployment Specification
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm
- Fetched: 2026-09-05 01:37 CDT

# Creating an API Deployment Specification

Find out how to create an API specification (a machine-readable definition of an API in JSON format) for use with API Gateway.

Before you can deploy an API on an API gateway, you have to create an API deployment specification. Every API deployment has an API deployment specification.

Each API deployment specification describes a set of resources, and the methods (for example, GET, PUT) that can be performed on each resource.

You can use a single API gateway as the front end for multiple back-end services by:
- Creating a single API deployment on the API gateway, with an API deployment specification that defines multiple back-end services.
- Creating multiple API deployments on the same API gateway, each with an API deployment specification that defines one (or more) back-end services.

Typically, back-end services will be in the same VCN as the API gateway on which you deploy an API. However, they don't have to be. In the API deployment specification, you can describe back-end services that are on a private or public subnet in your tenancy, as well as services outside your tenancy (including on the public internet). Wherever they are located, the back-end services must be routable from the subnet containing the API gateway on which the API is deployed. For example, if the back-end service is on the public internet, the VCN must have an internet gateway to enable the API gateway to route requests to the back-end service.

You can create an API deployment specification:
- Using dialogs in the Console whilst creating an API deployment.
- Using your preferred JSON editor to create a separate JSON file. You can then specify the JSON file when using the Console, the CLI, or the API to create an API deployment.
- Using an API description file you upload for an API resource. The API description file provides some initial values for the API deployment specification, which you can modify and extend when deploying the API resource on an API gateway. See[Creating an API Resource with an API Description](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm).

The instructions in this topic show a basic API deployment specification with a single backend, only one route, and no request or response policies. See[Example API Deployment Specification with Multiple Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm#Example)for a more typical API deployment specification that includes multiple back ends, each with one or more routes.

In addition, you can add request and response policies that apply to routes in an API deployment specification (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).

## Using the Console to Create an API Deployment Specification

To create an API deployment specification whilst creating an API deployment using dialogs in the Console, see[Using the Console to Create an API Deployment from Scratch](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm#consolescratch).

## Using a JSON Editor to Create an API Deployment Specification in a Separate JSON File

To create an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, create the API deployment specification in a JSON file in the format:

```

```

where:
- `"requestPolicies"`specifies optional policies to control the behavior of an API deployment. If you want to apply policies to all routes in an API deployment specification, place the policies outside the`routes`section. If you want to apply the policies just to a particular route, place the policies inside the`routes`section. See[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm).
- 

`<api-route-path>`specifies a path for API calls using the listed methods to the back-end service. Note that the route path you specify:
- is relative to the deployment path prefix (see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm))
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- `<method-list>`specifies one or more methods accepted by the back-end service, separated by commas. For example,`"GET, PUT"`.
- `<backend-type>`specifies the type of the back-end service. Common values are`ORACLE_FUNCTIONS_BACKEND`,`HTTP_BACKEND`, and`STOCK_RESPONSE_BACKEND`. For OAuth 2.0 login and logout back ends, use`OAUTH2_LOGIN_BACKEND`and`OAUTH2_LOGOUT_BACKEND`.
- `<backend-target>`and`<identifier>`specify the back-end service. Valid values for`<backend-target>`and`<identifier>`depend on the value of`<backend-type>`, as follows:
- If you set`<backend-type>`to`ORACLE_FUNCTIONS_BACKEND`, then replace`<backend-target>`with`functionId`, and replace`<identifier>`with the OCID of the function. For example,`"functionId": "ocid1.fnfunc.oc1.phx.aaaaaaaaab5b..."`. See[Adding a Function in OCI Functions as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm).
- If you set`<backend-type>`to`HTTP_BACKEND`, then replace`<backend-target>`with`url`, and replace`<identifier>`with the URL of the back-end service. For example,`"url": "https://api.weather.gov"`. See[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm).
- If you set`<backend-type>`to`STOCK_RESPONSE_BACKEND`, then replace`<backend-target>`and`<identifier>`with appropriate key-value pairs. See[Adding Stock Responses as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingstockresponses.htm).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

For a more complex example that defines multiple back ends, see[Example API Deployment Specification with Multiple Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm#Example).
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).

## Using an API Description File to Create an API Deployment Specification

To create an API deployment specification based on an API description file you upload for an API resource, see[Creating an API Resource with an API Description](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm)

The API description file provides some initial values for the API deployment specification, which you can modify and extend when deploying the API resource on an API gateway.

## Example API Deployment Specification with Multiple Back Ends

You can create a single API deployment on an API gateway, with an API deployment specification that defines multiple back-end services.

For example, the following API deployment specification defines a simple Hello World serverless function in OCI Functions as one back end, and the National Weather Service API as a second back end.

```

```
