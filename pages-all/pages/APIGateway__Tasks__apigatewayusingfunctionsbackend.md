# Adding a Function in OCI Functions as an API Gateway Back End
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm
- Fetched: 2026-09-05 01:39 CDT

# Adding a Function in OCI Functions as an API Gateway Back End

Find out how to create an API deployment with API Gateway that exposes serverless functions defined in OCI Functions.

A common requirement is to build an API with serverless functions as a back end, and an API gateway providing front-end access to those functions.

OCI Functions enables you to create serverless functions that are built as Docker images and pushed to a specified Docker registry. A definition of each function is stored as metadata in the OCI Functions server. When a function is invoked for the first time, OCI Functions pulls the function's Docker image from the specified Docker registry, runs it as a Docker container, and executes the function. If there are subsequent requests to the same function, OCI Functions directs those requests to the same running container. After a period being idle, the Docker container is stopped.

Having used the API Gateway service to create an API gateway, you can create an API deployment that invokes serverless functions defined in OCI Functions.

Before you can use serverless functions in OCI Functions as the back end for an API:
- Serverless functions referenced in the API deployment specification must have already been created and deployed in OCI Functions. The functions must be routable from the VCN specified for the API gateway, either through an internet gateway (in the case of a public API gateway) or through a service gateway (in the case of a private API gateway). The functions must use RFC-compliant HTTP status codes to communicate status. See[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm). For a related Developer Tutorial, see[Functions: Call a Function using API Gateway](https://docs.oracle.com/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#setup-functions-dev).
- 

Appropriate policies must already exist that give access to serverless functions defined in OCI Functions to:
- a group to which your user account belongs (see[Create a Policy to Give API Gateway Users Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersfunctionspolicy))
- API gateways (see[Create a Policy to Give API Gateways Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy))

You can add serverless function back ends to an API deployment specification by:
- using the Console
- editing a JSON file

## Creating and Deploying a Serverless Function in OCI Functions for Use as an API Gateway Back End

To create a serverless function in OCI Functions that can be invoked from an API gateway, follow the instructions in the OCI Functions documentation to:
- Confirm that you have completed the prerequisite steps for using OCI Functions, as described in[Preparing for Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsprerequisites.htm).
- Create and deploy the function in a compartment to which API gateways have been granted access, as described in[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm).

## Using the Console to Add Serverless Function Back Ends to an API Deployment Specification

To add an OCI Functions function back end to an API deployment specification using the Console:
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
- Backend Type: The type of the back-end service as`Oracle Functions`.
- Oracle Functions application: The name of the application in OCI Functions that contains the function. You can select an application from a different compartment.
- Function name: The name of the function in OCI Functions.

In this example, the route defines a simple Hello World serverless function in OCI Functions as a single back end.

Field: Enter:
Path:`/hello`
Methods:`GET`
Backend Type:`Oracle Functions`
Oracle Functions application:`acmeapp`
Function name:`acme-func`
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- 

(Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

If the serverless function accepts parameters, include those in the call to the API. For example:

```

```

## Editing a JSON File to Add Serverless Function Back Ends to an API Deployment Specification

To add an OCI Functions function back end to an API deployment specification in a JSON file:
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
- `<identifier>`specifies the OCID of the function you want to use as the back-end service. For example,`"functionId": "ocid1.fnfunc.oc1.phx.aaaaaaaaab______xmq"`.

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
- 

(Optional) Confirm the API has been deployed and that the serverless function in OCI Functions can be invoked successfully by calling the API (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

If the serverless function accepts parameters, include those in the call to the API. For example:

```

```
