# Adding an HTTP or HTTPS URL as an API Gateway Back End
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm
- Fetched: 2026-09-05 01:39 CDT

# Adding an HTTP or HTTPS URL as an API Gateway Back End

Find out how to create an API deployment to access HTTP and HTTPS URLs with API Gateway.

A common requirement is to build an API with the HTTP or HTTPS URL of a back-end service, and an API gateway providing front-end access to the back-end URL.

Having used the API Gateway service to create an API gateway, you can create an API deployment to access HTTP and HTTPS URLs.

The HTTP or HTTPS URL that you specify for the back-end service can be:
- The URL of a service that is publicly available on the internet.
- The URL of an Oracle Cloud Infrastructure service (for example, OCI Functions).
- The URL of a service on your own private or internal network (for example, connected to the VCN by FastConnect).

The URL you provide in the API deployment specification to identify the HTTP or HTTPS back-end service can include the host name or the host IP address. If you provide the host name, use the DHCP Options property of the API gateway's subnet to control how host names included in the API deployment specification are resolved to IP addresses at runtime:
- If the host name for a back-end service is publicly published on the internet, or if the host name belongs to an instance in the same VCN, select a DHCP options set for the API gateway's subnet that has the Oracle-provided Internet and VCN Resolver as the DNS Type . This is the default if you do not explicitly select a DHCP options set.
- If the host name is for a back-end service on your own private or internal network, select a DHCP options set for the API gateway's subnet that has Custom Resolver as the DNS Type , and has the URL of a suitable DNS server that can resolve the host name to an IP address.

Note that you can change the DNS server details in the DHCP options set specified for an API gateway's subnet. The API gateway will be reconfigured to use the updated DNS server details within two hours. For more information about resolving host names to IP addresses, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)and[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).

You can add HTTP and HTTPS back ends to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add HTTP or HTTPS Back Ends to an API Deployment Specification

To add an HTTP or HTTPS back end to an API deployment specification using the Console:
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
- Backend Type: The type of the back-end service as`HTTP`.
- 

URL: The URL you want to use as the back-end service, in the format`<protocol>://<host>:<port>/<path>`where:
- `<protocol>`is either`http`or`https`.
- `<host>`is the host name or the host IP address of the back-end service. For example,`api.weather.gov`. If you provide a host name, use the DHCP Options property of the API gateway's subnet to control how host names are resolved to IP addresses at runtime.
- `<port>`is optionally a port number.
- 

`<path>`is optionally a subdirectory or file at the host where the back-end service is located.

Note that`<path>`must not contain parameters directly, but can contain context variables. For more information and examples showing how to use context variables to substitute path, query, and header parameters into the path, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

For example,`"url": "https://api.weather.gov"`.
- Connection establishment timeout in seconds: Optionally, a floating point value indicating how long (in seconds) to allow when establishing a connection with the back-end service. The minimum is 1.0, the maximum is 75.0. If not specified, the default of 60.0 seconds is used.
- Request transmit timeout in seconds: Optionally, a floating point value indicating how long (in seconds) to allow when transmitting a request to the back-end service. The minimum is 1.0, the maximum is 300.0. If not specified, the default of 10.0 seconds is used.
- Reading response timeout in seconds: Optionally, a floating point value indicating how long (in seconds) to allow when reading a response from the back-end service. The minimum is 1.0, the maximum is 300.0. If not specified, the default of 10.0 seconds is used.
- Disable SSL verification: Whether to disable SSL verification when communicating with the back-end service. By default, this option is not selected.

In this example, the route defines a weather service as an HTTP back end.

Field: Enter:
Path:`/weather`
Methods:`GET`
Backend Type:`HTTP`
URL:`https://api.weather.gov`
Connection establishment timeout in seconds:`45`
Request transmit timeout in seconds:`15`
Reading response timeout in seconds:`15`
Disable SSL verification: (Not selected)
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add HTTP or HTTPS Back Ends to an API Deployment Specification

To add an HTTP or HTTPS back end to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)) in the format:

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
- `"type": "HTTP_BACKEND"`specifies the API gateway back end is an HTTP or HTTPS URL.
- 

`"url: "<identifier>"`specifies the URL you want to use as the back-end service, in the format`<protocol>://<host>:<port>/<path>`where:
- `<protocol>`is either`http`or`https`.
- `<host>`is the host name or the host IP address of the back-end service. For example,`api.weather.gov`. If you provide a host name, use the DHCP Options property of the API gateway's subnet to control how host names are resolved to IP addresses at runtime.
- `<port>`is optionally a port number.
- 

`<path>`is optionally a subdirectory or file at the host where the back-end service is located.

Note that`<path>`must not contain parameters directly, but can contain context variables. For more information and examples showing how to use context variables to substitute path, query, and header parameters into the path, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

For example,`"url": "https://api.weather.gov"`.
- `"connectTimeoutInSeconds": <seconds>`is an optional floating point value indicating how long (in seconds) to allow when establishing a connection with the back-end service. The minimum is 0.0, the maximum is 75.0. If not specified, the default of 60.0 seconds is used.
- `"readTimeoutInSeconds": <seconds>`is an optional floating point value indicating how long (in seconds) to allow when reading a response from the back-end service. The minimum is 0.0, the maximum is 300.0. If not specified, the default of 10.0 seconds is used.
- `"sendTimeoutInSeconds": <seconds>`is an optional floating point value indicating how long (in seconds) to allow when transmitting a request to the back-end service. The minimum is 0.0, the maximum is 300.0. If not specified, the default of 10.0 seconds is used.
- `"isSSLVerifyDisabled": <true|false>`is an optional boolean value (either`true`or`false`) indicating whether to disable SSL verification when communicating with the back-end service. If not specified, the default of`false`is used.

For example, the following basic API deployment specification defines a weather service as an HTTP back end:

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
- 

(Optional) Confirm the API has been deployed by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
