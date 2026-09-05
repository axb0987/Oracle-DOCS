# Deploying an API on an API Gateway by Creating an API Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm
- Fetched: 2026-09-05 01:37 CDT

# Deploying an API on an API Gateway by Creating an API Deployment

Find out how to deploy an API on an API gateway by creating an API deployment with the API Gateway service.

Having created an API gateway, you deploy an API on the API gateway by creating an API deployment. When you create an API deployment, you include an API deployment specification that defines the API. The API Gateway service inspects the API deployment specification to confirm that it is valid.

You can use a single API gateway as the front end for multiple back-end services by:
- Creating a single API deployment on the API gateway, with an API deployment specification that defines multiple back-end services.
- Creating multiple API deployments on the same API gateway, each with an API deployment specification that defines one (or more) back-end services.

## Using the Console to Create an API Deployment from Scratch

To use the Console to create an API deployment, entering the API deployment specification in dialogs in the Console as you go:
- On the Gateways list page, select the API gateway on which you want to deploy the API. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- 

On the Deployments tab, select Create deployment and in the Basic information section, specify:
- Name: The name of the new API deployment. Avoid entering confidential information.
- 

Path prefix: A path on which to deploy all routes contained in the API deployment specification. For example:
- `/v1`
- `/v2`
- `/test/20191122`

Note that the deployment path prefix you specify:
- must be preceded by a forward slash (`/`), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), but must not end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- cannot include parameters and wildcards

Also note that if an API deployment has a single forward slash as its deployment path prefix, then that is the only API deployment allowed on a given API gateway. You cannot create an API deployment with a single forward slash as its deployment path prefix if there's already another API deployment on the same API gateway.
- Compartment: The compartment in which to create the new API deployment.
- 

(Optional) In the API request policies section, optionally specify request policy details to provide support for:
- Mutual-TLS: Select Enable mTLS and enter details for an mTLS request policy (see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm)).
- CORS: Select Add and enter details for a CORS request policy (see[Adding CORS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm)).
- Rate limiting: Select Add and enter details for a rate limiting request policy (see[Limiting the Number of Requests to API Gateway Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylimitingbackendaccess.htm)).
- Usage plans: Select Add and enter details for a usage plan request policy (see[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm)).
- 

(Optional) In the API logging policies section, optionally specify an execution log level to record information about processing within the API gateway. See[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm).
- 

(Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next to display the Authentication page and enter details for an authentication request policy:
- No Authentication: Select to give unauthenticated access to all routes in the API deployment.
- Single Authentication: Select to route all authentication requests to a single authentication server. The authentication server can be an identity provider that validates JSON Web Tokens (JWTs), or an authorizer function that validates multi-argument or single-argument access tokens. For more information, see:
- [Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)
- [Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)
- Multi-Authentication: Select to route authentication requests to different authentication servers, according to the context variable and rules you enter. For more information, see[Adding Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm).

For more information, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- Select Next to enter details of the routes in the API deployment.
- 

In the Routes section, select Add route and specify the first route in the API deployment that maps a path and one or more methods to a back-end service:
- 

Path: A path for API calls using the listed methods to the back-end service. Note that the route path you specify:
- is relative to the deployment path prefix
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- Methods: One or more methods accepted by the back-end service, separated by commas. For example,`GET, PUT`.
- 

Add a single backend or Add multiple backends : Whether to route all requests to the same back end, or to route requests to different back ends according to the context variable and rules you enter.

These instructions assume you want to use a single back end, so select Add a single backend . Alternatively, if you want to use different back ends, select Add multiple backends and follow the instructions in[Using the Console to Add Dynamic Back End Selection to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm#apigatewaydynamicroutingbasedonrequest_topic-Using_the_Console_to_Add_Dynamic_Backend_Selection_to_an_API_Deployment_Specification).
- Backend Type: The type of the back-end service, as one of:
- HTTP: For an HTTP back end, you also need to specify a URL, timeout details, and whether to disable SSL verification (see[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)).
- Oracle Functions: For an OCI Functions back end, you also need to specify the application and function (see[Adding a Function in OCI Functions as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm)).
- Stock response: For a stock response back end, you also need to specify the HTTP status code, the content in the body of the response, and one or more HTTP header fields (see[Adding Stock Responses as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingstockresponses.htm)).
- Logout : For a logout back end, you also need to specify a list of allowed URLs to which a request can be redirected to revoke tokens, and optionally data to pass to the logout URL (see[Adding Logout as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogoutbackends.htm)).
- Login: For a login back end, you define a static route to which the identity provider redirects API clients as part of the authentication flow. The route path must match the login path specified in the OAuth 2.0 validation failure policy (see[Adding Login as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingloginbackends.htm)).
- Show route request policies: Request policies to apply to the route (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).
- Show route response policies: Response policies to apply to the route (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).
- Show response caching policies: Response caching policies to apply to the route (see[Caching Responses to Improve Performance](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm)).
- Show route logging policies: Logging policies to apply to the route (see[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)).
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the new API deployment.
- 

Select Create to create the new API deployment.

Note that it can take a few minutes to create the new API deployment. While it is being created, the API deployment is shown with a state of Creating on the Deployments tab of the API gateway details page. When it has been created successfully, the new API deployment is shown with a state of Active.

Also note that rather than creating the new API deployment immediately, you can create it later using Resource Manager and Terraform, by selecting Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

If you have waited more than a few minutes for the API deployment to be shown with an Active state (or if the API deployment creation operation has failed):
- Select the name of the API deployment on the Deployments tab of the API gateway details page, and select Work requests to see an overview of the API deployment creation operation.
- Select the Create Deployment operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the API deployment creation operation has failed and you cannot diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Using the Console to Create an API Deployment from a JSON File

To use the Console to create an API deployment, uploading the API deployment specification from a JSON file:
- On the Gateways list page, select the API gateway on which you want to deploy the API. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- 

On the Deployments tab, select Upload an existing deployment API and in the Basic information section, specify:
- Name: The name of the new API deployment. Avoid entering confidential information.
- 

Path prefix: A path on which to deploy all routes contained in the API deployment specification. For example:
- `/v1`
- `/v2`
- `/test/20191122`

Note that the deployment path prefix you specify:
- must be preceded by a forward slash (`/`), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), but must not end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- cannot include parameters and wildcards
- Compartment: The compartment in which to create the new API deployment.
- Specification: The JSON file containing the API deployment specification, either by dragging and dropping the file, or by selecting select one . See[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm).

Also note that if an API deployment has a single forward slash as its deployment path prefix, then that is the only API deployment allowed on a given API gateway. You cannot create an API deployment with a single forward slash as its deployment path prefix if there's already another API deployment on the same API gateway.
- 

(Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next to review the details you entered for the new API deployment.
- 

Select Create to create the new API deployment.

Note that it can take a few minutes to create the new API deployment. While it is being created, the API deployment is shown with a state of Creating on the Deployments tab of the API gateway details page page. When it has been created successfully, the new API deployment is shown with a state of Active.

Also note that rather than creating the new API deployment immediately, you can create it later using Resource Manager and Terraform, by selecting Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

If you have waited more than a few minutes for the API deployment to be shown with an Active state (or if the API deployment creation operation has failed):
- Select the name of the API deployment, and select Work requests to see an overview of the API deployment creation operation.
- Select the Create Deployment operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the API deployment creation operation has failed and you cannot diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Using the Console to Create an API Deployment from an API Resource

You can create an API deployment from an existing API resource, using the API resource's API description. In this case, the API description is based on an API description file you've uploaded for the API resource (see[Creating an API Resource with an API Description](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm)). The API description file provides some initial values for the API deployment specification, which you can modify and extend when creating the API deployment. In particular, a default route is created for each path and associated method in the API description.

To use the Console to create an API deployment from an existing API resource, using an API deployment specification derived from an API description file:
- On the APIs list page, select the name of the API resource that you want to deploy. If you need help finding the list page, see[Listing API Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm).
- (Optional) On the Details tab, confirm that a valid API deployment specification has been created for the API resource from an uploaded API description file. If no API deployment specification is available, see[Creating an API Resource with an API Description](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm).
- Select Deploy to use the Console dialogs for creating an API deployment.

Some of the initial values for the API deployment specification properties shown in the Console dialogs are derived from the API description file.
- In the Gateway section, select the API gateway on which to create the API deployment.
- 

In the Basic information section, specify:
- Name: The name of the new API deployment. Avoid entering confidential information.
- 

Path prefix: A path on which to deploy all routes contained in the API deployment specification.

For example:
- `/v1`
- `/v2`
- `/test/20191122`

Note that the deployment path prefix you specify:
- must be preceded by a forward slash (`/`), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), but must not end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- cannot include parameters and wildcards

Also note that if an API deployment has a single forward slash as its deployment path prefix, then that is the only API deployment allowed on a given API gateway. You cannot create an API deployment with a single forward slash as its deployment path prefix if there's already another API deployment on the same API gateway.
- Compartment: The compartment in which to create the new API deployment.
- 

(Optional) In the API request policies section, optionally specify request policy details to provide support for:
- Mutual-TLS: Select Enable mTLS and enter details for an mTLS request policy (see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm)).
- CORS: Select Add and enter details for a CORS request policy (see[Adding CORS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm)).
- Rate limiting: Select Add and enter details for a rate limiting request policy (see[Limiting the Number of Requests to API Gateway Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylimitingbackendaccess.htm)).
- Usage plans: Select Add and enter details for a usage plan request policy (see[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm)).
- 

(Optional) In the API logging policies section, optionally specify an execution log level to record information about processing within the API gateway. See[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm).
- 

(Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next to display the Authentication page and enter details for an authentication request policy:
- No Authentication: Select to give unauthenticated access to all routes in the API deployment.
- Single Authentication: Select to route all authentication requests to a single authentication server. The authentication server can be an identity provider that validates JSON Web Tokens (JWTs), or an authorizer function that validates multi-argument or single-argument access tokens. For more information, see:
- [Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)
- [Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)
- Multi-Authentication: Select to route authentication requests to different authentication servers, according to the context variable and rules you enter. For more information, see[Adding Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm). For more information, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to display the Routes page and review and enter details of the routes in the API deployment.

By default, a route is created for every path and associated method that is present in the API description. Initially, each of these default routes is created with a stock response back end. The HTTP status code, the content in the body of the response body content, and the header are obtained from the details in the API description. If the API description does not include response information for a particular path and associated method, a default stock response back end is created for that route with 501 as the HTTP status code.
- 

Review each default route in turn, optionally editing its configuration if necessary to meet your requirements, including:
- Whether to route all requests to the same back end, or to route requests to different back ends according to the context variable and rules you enter (see[Adding API Gateway Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingbackendstoapigateways.htm)).
- Updating request, response, caching, and logging policies (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).
- (Optional) Select Add route to enter details of more routes, in addition to those created by default from the API description.
- Select Next to review the details you entered for the new API deployment.
- 

Select Create to create the new API deployment.

Note that it can take a few minutes to create the new API deployment. While it is being created, the API deployment is shown with a state of Creating on the Deployments tab of the API gateway details page. When it has been created successfully, the new API deployment is shown with a state of Active.
- 

If you have waited more than a few minutes for the API deployment to be shown with an Active state (or if the API deployment creation operation has failed):
- Select the name of the API deployment on the Deployments tab of the API gateway details page, and select the Work requests tab to see an overview of the API deployment creation operation.
- Select the Create deployment operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the API deployment creation operation has failed and you cannot diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Using the CLI

To create a new API deployment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

Open a command prompt and run`oci api-gateway deployment create`to create the deployment:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment in which to create the new API deployment.
- `<api-name>`is the name of the new API deployment. Avoid entering confidential information.
- `<gateway-ocid>`is the OCID of the existing gateway on which to deploy the API. To find out the API gateway's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- 

`/<deployment-path-prefix>`is a path on which to deploy all routes contained in the API deployment specification.

Note that the deployment path prefix you specify:
- must be preceded by a forward slash (`/`) in the JSON file, and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), but must not end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- cannot include parameters and wildcards

Also note that if an API deployment has a single forward slash as its deployment path prefix, then that is the only API deployment allowed on a given API gateway. You cannot create an API deployment with a single forward slash as its deployment path prefix if there's already another API deployment on the same API gateway.
- `<filename>`is the API deployment specification, including a path, one or more methods, and a back end definition. See[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm).

For example:

```

```

The response to the command includes:
- The API deployment's OCID.
- 

The host name on which the API deployment has been created, as a domain name in the format`<gateway-identifier>.apigateway.<region-identifier>.oci.customer-oci.com`, where:
- `<gateway-identifier>`is the string of characters that identifies the API gateway. For example,`lak...sjd`(abbreviated for readability).
- `<region-identifier>`is the identifier of the region in which the API deployment has been created. See[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayprerequisites.htm#regional-availability).

For example,`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`.

The host name will be the domain name to use when calling an API deployed on the API gateway.
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to create the API deployment (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API deployment is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

Note that you cannot use the API deployment until the work request has successfully created it and the API deployment is active.
- 

(Optional) To see the status of the API deployment, enter:

```

```

- 

(Optional) To see the status of the work request that is creating the API deployment, enter:

```

```

- 

(Optional) To view the logs of the work request that is creating the API deployment, enter:

```

```

- 

(Optional) If the work request that is creating the API deployment fails and you want to review the error logs, enter:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateDeployment](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/CreateDeployment)
