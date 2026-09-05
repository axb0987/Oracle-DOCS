# Dynamically Selecting API Gateway Back Ends Based on Request Elements
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm
- Fetched: 2026-09-05 01:38 CDT

# Dynamically Selecting API Gateway Back Ends Based on Request Elements

Find out how to route requests sent to the same API gateway to different back ends based on elements in the request with API Gateway.

A common requirement is to route requests sent to the same API gateway to different back ends based on elements in the request. For example, to route requests to different back ends based on:
- The host and/or domain and/or subdomain to which a request was sent. For example, to route incoming requests from cars.example.com and trucks.example.com that have been sent to the same API gateway to two completely different backends.
- The usage plan to which the API client sending a request is subscribed. For example, to route incoming requests either to a standard host for API clients subscribed to a`Free Tier`usage plan, or to a high performance host for API clients subscribed to the`Premium Tier`usage plan.
- Headers and header values in a request. For example, to route a request that includes an`Accept`header with a value of`application/xml`to an appropriate back end that returns a response of that content type.

Dynamically selecting a back end enables you to present a single facade to API consumers and shield them from the complexity of multiple back-end systems.

You can dynamically route requests to:
- HTTP back ends
- serverless function back ends
- stock response back ends

When defining multiple back ends for the same API deployment, you create rules to enable the API gateway to dynamically select the back end to which to route a request, based on an element in the original request.

To enable the API gateway to dynamically select the correct back end, you use the following context variables to capture elements of the request:
- `request.auth[<key>]`where`<key>`is the name of a claim returned by an authorizer function or contained in a JWT token.
- `request.headers[<key>]`where`<key>`is the name of a header included in the request to the API.
- `request.host`as the name of the host to which the original request was sent.
- `request.path[<key>]`where`<key>`is the name of a path parameter defined in the API deployment specification.
- `request.query[<key>]`where`<key>`is the name of a query parameter included in the request to the API.
- `request.subdomain[<key>]`where`<key>`is the trailing part of the host name to ignore when capturing the leading part of the host name to which the original request was sent.
- `request.usage_plan[id]`where`id`is the OCID of a usage plan to which the API client is subscribed.

Note that if a context variable has multiple values, only the first value is used when selecting the back end. For more information about context variables, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

You define the critiria to dynamically select back ends in an API deployment specification by:
- using the Console
- editing a JSON file

## Notes about back end rule matching

When creating the rules to determine which back end to use, you can specify how closely the context variable value must match a given value for the request to be routed to a particular back end. You can require an exact match, or you can specify a value starting with, or ending with, a wildcard. The API gateway evaluates the rules in the order you specify (exact match rules first, followed by wildcard rules), and uses the first matching rule. You can also specify a default rule to use if the context variable value does not match any back end rules. If no rule is specified as the default and the context variable value in an incoming request does not match any back end rules, the request returns an error. The order of precedence for determining which back end rule (and hence which back end) to use can be summarized as:
- If the context variable value exactly matches a rule's value, use that rule.
- Otherwise, if the context variable value matches a rule's value that starts or ends with a wildcard, use the first rule containing a wildcard that matches.
- Otherwise, if a rule is specified as the default rule, use that rule.
- Otherwise, return an error.

## Using the Console to Add Dynamic Back End Selection to an API Deployment Specification

To add dynamic back end selection to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- On the Authentication page, specify how to authenticate requests made to routes in the API deployment.

For more information, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
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
- Select Add multiple backends to specify that you want requests routed to different back ends, according to the context variable and rules you enter.
- From the Selector list, select the context table (containing the context variable) to use when determining the back end to which to send the request, as follows:
- Auth: Use the value of a claim returned by an authorizer function or contained in a JWT (and saved in the`request.auth`context table) to determine the back end.
- Headers: Use the value of a header from the original request (and saved in the`request.headers`context table) to determine the back end.
- Host: Use the name of the host to which the original request was sent (extracted from the host field of the Host header in the request, and saved in the`request.host`context table) to determine the back end.
- Path: Use a path parameter from the original request (and saved in the`request.path`context table) to determine the back end.
- Query parameters: Use the value of a query parameter from the original request (and saved in the`request.query`context table) to determine the back end.
- Subdomain: Use the leading part of the host name to which the original request was sent (just that part of the host name not specified as the key, and saved in the`request.subdomain`context table) to determine the back end. Note that the key is the trailing part of the host name to not use.
- Usage plan OCID: Use the OCID of a usage plan to which the API client is subscribed (identified from a client token in the original request, and saved in the`request.usage_plan`context table) to determine the back end.
- Depending on the context table you select, enter the name of the key to use when determining the back end to which to send the request.
- Select Add backend to enter a rule for the context variable that, if met, routes the request to the back end you define.
- Enter details for the rule as follows:
- Name: Enter a name for the rule. Use the name you enter to identify the back end when referring to logs and metrics.
- Match type: Specify how closely the context variable value must match a value you enter in order for the request to routed to this backend. Select Any of if you want the context variable to exactly match the value in the Values field. Select Wildcard if the context variable must match a value in the Expression field that contains wildcards. Value-matching is case-insensitive if you select Any of , and case-sensitive if you select Wildcard .
- Values: (Displayed if you selected Any of in the Match type field.) Specify a value (or multiple values in a comma-separated list) that the context variable must exactly match. Note that the match is case-insensitive if you selected Any of . Also note that values must be unique within a single back end rule, and across all back end rules defined for the API deployment.
- Expression: (Displayed if you selected Wildcard in the Match type field) Specify a value starting with, or ending with, a wildcard that the context variable must match. Use the`*`(asterisk) wildcard to indicate zero or more characters, and/or the`+`(plus sign) wildcard to indicate one or more characters. Note that the match is case-sensitive if you selected Wildcard . Note that you cannot include more than one wildcard in a value, and you cannot include a wildcard in the middle of a value. Also note that incorrect wildcard configuration could lead to requests being routed to unintended back ends.
- Make default: Specify whether to use the back end defined for this rule if no back end rules match.
- Enter details for the back end as follows:
- In the Backend Type field, select HTTP , Oracle Functions , or Stock response as the back end to which to route the request if the rule you entered is met.
- Enter details for the back end you selected. The details to enter will depend on the back end type you selected, and are fully described in:
- [Using the Console to Add HTTP or HTTPS Back Ends to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm#usingconsole)
- [Using the Console to Add Serverless Function Back Ends to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm#usingconsole)
- [Using the Console to Add Stock Responses to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingstockresponses.htm#usingconsole)
- Select Create to create the back end and associated rule.
- (Optional) Select Add backend again to define additional back ends and associated rules.
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Dynamic Back End Selection to an API Deployment Specification

To add dynamic back end selection to an API deployment specification in a JSON file:
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
- `"type": "DYNAMIC_ROUTING_BACKEND"`specifies that you want to dynamically select the back end based on elements in the request.
- `"type": "SINGLE"`specifies that you want to use a single context variable to dynamically select the back end.
- `"selector": "<context-table-key>"`specifies the context table (and key, if appropriate) from which to obtain the context variable value that determines the back end to send the request to, as follows:
- `request.auth[<key>]`Use the value of a claim returned by an authorizer function or contained in a JSON Web Token (JWT) to determine the back end.`<key>`is the name of the claim. For example,`request.auth[tenant]`
- `request.headers[<key>]`Use the value of a header from the original request to determine the back end.`<key>`is the header name. For example,`request.headers[Accept]`
- `request.host`Use the name of the host to which the original request was sent (extracted from the host field of the Host header in the request) to determine the back end.
- `request.path[<key>]`Use a path parameter from the original request to determine the back end.`<key>`is the path parameter name. For example,`request.path[region]`
- `request.query[<key>]`Use the value of a query parameter from the original request to determine the back end.`<key>`is the query parameter name. For example,`request.query[state]`
- `request.subdomain[<key>]`Use the leading part of the host name to which the original request was sent (just that part of the host name not specified as the key) to determine the back end. Note that`<key>`is the trailing part of the host name to not use. For example,`request.subdomain[example.com]`
- `request.usage_plan[id]`Use the OCID of a usage plan to which the API client is subscribed (identified from a client token in the original request) to determine the back end.
- `"key": {...}`specifies the rule that must be met to send a request to the back end specified by`"backend": {…}`.
- `"type": "<ANY_OF|WILDCARD>"`specifies how closely the value of the context variable identified by`<context-table-key>`must match the value you enter for`<context-variable-value>`in order for the request to be sent to the back end specified by`"backend": {…}`. Specify`ANY_OF`if the value of the context variable identified by`<context-table-key>`must exactly match the value you specify for`<context-variable-value>`. Specify`WILDCARD`if the value of the context variable identified by`<context-table-key>`must match a value containing wildcards that you specify for`<context-variable-value>`. Value-matching is case-insensitive if you specify`ANY_OF`, and case-sensitive if you specify`WILDCARD`.
- `<context-variable-value>`is a value that possibly matches the value of the context variable identified by`<context-table-key>`. You can include multiple`"<context-variable-value>"`entries in the`values:[...]`array, separated by commas. The request is sent to the back end specified by`"backend": {…}`if the values match, as follows:
- If you specified`"type": "ANY_OF"`, the values must match exactly. Note that values must be unique within a single back end rule, and across all back end rules defined for an API deployment. Value-matching is case-insensitive if you specified`ANY_OF`.
- If you specified`"type": "WILDCARD"`, you can specify a value for`<context-variable-value>`that starts with, or ends with, a wildcard. Use the`*`(asterisk) wildcard to indicate zero or more characters, and/or the`+`(plus sign) wildcard to indicate one or more characters. Note that you cannot include more than one wildcard in a value, and you cannot include a wildcard in the middle of a value. Value-matching is case-sensitive if you specified`WILDCARD`. Also note that incorrect wildcard configuration could lead to requests being routed to unintended back ends. For example, if you want a request from an API client that can accept an xml response (as indicated in the Accept header of the request) to be routed to a back end that returns xml, you might specify:
- `"selector": "request.headers[Accept]"`
- `"type": "ANY_OF"`
- `"values": ["application/xml"]`
- `"isDefault": "<true|false>"`is an optional boolean value (either`true`or`false`) indicating whether to use the back end for this rule if no back end rules match. If not specified, the default of`false`is used.
- `"name": "<rule-name>"`specifies a name for the rule. Use this name to identify the back end when referring to logs and metrics.
- `<backend-type>`specifies the type of the back-end service. Valid values are`ORACLE_FUNCTIONS_BACKEND`,`HTTP_BACKEND`, and`STOCK_RESPONSE_BACKEND`.
- `<backend-target>`and`<identifier>`specify the back-end service. Valid values for`<backend-target>`and`<identifier>`depend on the value of`<backend-type>`, as follows:
- If you set`<backend-type>`to`ORACLE_FUNCTIONS_BACKEND`, then replace`<backend-target>`with`functionId`, and replace`<identifier>`with the OCID of the function. For example,`"functionId": "ocid1.fnfunc.oc1.phx.aaaaaaaaab5b..."`. See[Adding a Function in OCI Functions as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm).
- If you set`<backend-type>`to`HTTP_BACKEND`, then replace`<backend-target>`with`url`, and replace`<identifier>`with the URL of the back-end service. For example,`"url": "https://api.weather.gov"`. See[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm).
- If you set`<backend-type>`to`STOCK_RESPONSE_BACKEND`, then replace`<backend-target>`and`<identifier>`with appropriate key-value pairs. See[Adding Stock Responses as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingstockresponses.htm).

For example, the following basic API deployment specification includes dynamic back end selection that routes requests based on the value of the`vehicle-type`query parameter passed in the request. If the`vehicle-type`query parameter has the value`car`, the request is routed to`cars-api.example.com`. If the`vehicle-type`query parameter has a value of`truck`or`minivan`, the request is routed to a serverless function in OCI Functions for processing. If the`vehicle-type`query parameter value is neither`car`, nor`truck`nor`minivan`, the request is routed to`cars-api.example.com`by default:

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
- 

(Optional) Confirm the API has been deployed by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Examples of Dynamic Selection of API Gateway Back Ends

The examples in this section assume the following API deployment definition and incomplete API deployment specification in a JSON file:

```

```

Note the examples also apply when you're defining an API deployment specification using dialogs in the Console.

### Example 1: Select back end by Host

You can configure an API deployment to dynamically select a back end based on the host to which the original request was sent (extracted from the host field of the Host header in the request). This design enables you to define an API gateway that supports different tenants.

```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the host to which the original request was sent (extracted from the host field of the Host header in the request), as follows:
- If the request was sent to`cars.example.com`, the request is routed to`http://cars-api.example.com`.
- If the request was sent to`minivans.examplecloud.com`or`trucks.example.com`, the request is routed to a serverless function back end in OCI Functions.
- If the request was sent to a different host, the request is routed to`http://cars-api.example.com`by default.

### Example 2: Select back end by Host Subdomain

You can configure an API deployment to dynamically select a back end based on a subdomain in the host string to which the original request was sent. The host string is extracted from the Host header in the request, and masked by a string you specify, leaving the subdomain that is used to route the request. This design enables you to define an API gateway that supports different tenants.
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the host subdomain to which the original request was sent, as follows:
- if the request was sent to`cars.example.com`, the request is routed to`http://cars-api.example.com`
- if the request was sent to`minivans.example.com`or`trucks.example.com`, the request is routed to a serverless function back end in OCI Functions
- if the request was sent to a different subdomain of`example.com`(such as`car.example.com`or`sedan.example.com`) the request is routed to`http://cars-api.example.com`by default

### Example 3a: Select back end by Host Subdomain (modifying the host name in the back end URL, and using a match type of ANY_OF)

You can configure an API deployment to dynamically select a back end based on a subdomain in the host string to which the original request was sent. The host string is extracted from the Host header in the request, and masked by a string you specify, leaving the subdomain that is used to route the request. For additional validation, you can include the subdomain mask as a context variable in the back end url to ensure that requests are only routed to back ends you intend to expose. If you specify`ANY_OF`as the match type, the value of the context variable cannot include wildcards, and must match exactly one of the`routes.routingBackends.key`values in order for the request to be sent to the back end.
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the host subdomain to which the original request was sent, as follows:
- if the request was sent to`cars.example.com`or`hatchbacks.example.com`, the request is routed to`http://cars-api.example.com`or`http://hatchbacks-api.example.com`
- if the request was sent to a different subdomain of`example.com`(such as`suvs.example.com`or`sedans.example.com`), the request fails.

If you are considering modifying the host name in the back end URL by including a context variable as shown in this example, note the following:
- You can only modify the back end url using the context variable specified for`selector`.
- To enforce the list of allowed back ends, do not set`"isDefault: "true"`for any rule.

### Example 3b: Select back end by Host Subdomain (modifying the host name in the back end URL, and using a match type of WILDCARD)

You can configure an API deployment to dynamically select a back end based on a subdomain in the host string to which the original request was sent. The host string is extracted from the Host header in the request, and masked by a string you specify, leaving the subdomain that is used to route the request. For additional validation, you can include the subdomain mask as a context variable in the back end url to ensure that requests are only routed to back ends you intend to expose. If you specify`WILDCARD`as the match type, the value of the context variable can include wildcards, and must match one of the`routes.routingBackends.key`values in order for the request to be sent to the back end.
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on whether the host subdomain to which the original request was sent matches the`routes.routingBackends.key`value including the wildcard. In this case, whether the original request was sent to a host subdomain that ends in the letter 's', as follows:
- If the request was sent to a subdomain that ends in the letter 's', the request is routed appropriately. For example, requests sent to`cars.example.com`,`hatchbacks.example.com`,`suvs.example.com`, or`sedans.example.com`, are routed to`http://cars-api.example.com`,`http://hatchbacks-api.example.com`,`http://suvs-api.example.com`or`http://sedans-api.example.com`respectively.
- If the request was sent to a subdomain that does not end in the letter 's', the request fails. For example, requests sent to`truck.example.com`or`tractor.example.com`fail.

If you are considering modifying the host name in the back end URL by including a context variable as shown in this example, note the following:
- You can only modify the back end url using the context variable specified for`selector`.
- When using wildcards, configure the wildcard carefully. Incorrect wildcard configuration could lead to requests being routed to unintended back ends. For instance, in the example, requests sent to`buses.example.com`are correctly routed to`http://buses-api.example.com`as expected. However, this configuration also routes requests originally sent to`bus.example.com`and`s.example.com`to`http://bus-api.example.com`and`http://s-api.example.com`respectively, neither of which was intended.

### Example 4: Select back end by Usage Plan

You can configure an API deployment to dynamically select a back end based on the OCID of a usage plan to which the API client is subscribed (identified from a client token in the original request). The OCID of the usage plan is stored in the`request.usage_plan[id]`context variable.
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the usage plan to which the API client is subscribed. Two usage plans have been defined, as follows:
- `Free Tier`, which has the OCID`ocid1.usageplan.oc1..aaaaaaaaab______gap`. When this OCID is the value of the`request.usage_plan[id]`context variable, the request is routed to`http://dev.example.com/`. The`Free Tier`usage plan is also used as the default if the request did not include a client token.
- `Premium Tier`, which has the OCID`ocid1.usageplan.oc1..aaaaaaaaay______lcf`. When this OCID is the value of the`request.usage_plan[id]`context variable, the request is routed to`http://api.example.com`

### Example 5: Select back end by Header Parameter

You can configure an API deployment to dynamically select a back end based on a parameter passed in the header of the original request.
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the value of the`Accept`header in the original request, as follows:
- if the`Accept`header requests a response in`application/json`format, the request is routed to`http://api.example.com`
- if the`Accept`header requests a response in`application/xml`format, the request is routed to`http://xml.example.com`

### Example 6: Select back end by Authentication Parameter

You can configure an API deployment to dynamically select a back end based on an authentication parameter (also known as a 'claim') returned by an authorizer function or contained in a JSON Web Token (JWT).
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the value of the`tenant`claim returned by an authorizer function, as follows:
- if the`request.auth[tenant]`context variable is set to`tenant-cars`, the request is routed to`http://cars-api.example.com`
- if the`request.auth[tenant]`context variable is set to`tenant-trucks`, the request is routed to`http://trucks-api.example.com`

### Example 7: Select back end by Query Parameter

You can configure an API deployment to dynamically select a back end based on a query parameter passed in by the original request.
```

```

In this example, how the API gateway resolves a request to`https://<gateway-hostname>/marketing/sales`depends on the value of the`vehicle-type`query parameter passed in by the original request., as follows:
- If the`vehicle-type`query parameter has the value`car`, the request is routed to`cars-api.example.com`.
- If the`vehicle-type`query parameter has a value of`truck`or`minivan`, the request is routed to a serverless function in OCI Functions for processing.
- If the`vehicle-type`query parameter value is neither`car`, nor`truck`nor`minivan`, the request is routed to`cars-api.example.com`
