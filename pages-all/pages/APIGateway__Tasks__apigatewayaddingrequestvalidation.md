# Adding Request Validation to API deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestvalidation.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Request Validation to API deployments

Find out how to prevent invalid requests being sent to back-end services, by validating incoming requests against a validation request policy with API Gateway.

Typically, you want to avoid placing unnecessary load on back-end services by only sending valid requests to those services. To prevent invalid requests being sent to back-end services, you can use an API gateway to validate incoming requests against a validation request policy. If a request does not meet the validation policy requirements, you can configure the API gateway to reject the request instead of passing it through to the targeted back-end service. Instead, the API gateway sends a 4xx error code response to the API client that sent the request.

Using an API gateway, you can set up validation request policies to check that :
- the request includes specific headers
- the request includes specific query parameters
- the request body is of a specific content type

You can control how an API gateway applies a validation request policy by specifying a validation mode for the policy:
- In Enforcing mode, the API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service. The API gateway does not send requests that fail validation to the back-end service. The API gateway sends a 4xx error code response to an API client sending a request that fails validation. The API gateway includes entries in execution logs for validation errors.
- In Permissive mode, the API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation. Note that requests that fail validation are still sent to the back-end service. The API gateway includes entries in execution logs for validation errors. Use the Permissive mode to assess the likely impact of applying a validation request policy to a system already in production system, without affecting API clients currently sending requests.
- In Disabled mode, the API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

The API gateway applies validation request policies after CORS request policies, and after authentication and authorization request policies, but before transformation request policies.

You can add validation request policies to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Validation Request Policies

To add validation request policies to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

Select Next and specify authentication options on the Authentication page.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next and enter details for individual routes in the API deployment on the Routes page.
- On the Routes page, select the route for which you want to specify validation request policies.
- Select Show route request policies .
- To validate the headers included in a request to the API gateway for the current route by creating a header validation request policy:
- Select the Add button beside Header validations and specify details of the first header in the request to validate:
- Header name: The name of a header in the request to validate. For example,`X-Username`.
- Required: Whether the header you specified must be present in the request for the request to be considered valid.
- (Optional) Select Another header and specify additional headers in the request to validate.
- Select Show Advanced Options and select a Mode to specify how the header validation request policy is applied:
- Enforcing: The API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service.
- Permissive: The API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation.
- Disabled: The API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

Note that Enforcing is the default validation mode.
- Select Update .
- To validate the query parameters included in a request to the API gateway for the current route by creating a query parameter validation request policy:
- Select the Add button beside Query parameter validations and specify details of the first query parameter in the request to validate:
- Parameter Name: The name of a query parameter in the request to validate. For example,`state`.
- Required: Whether the query parameter you specified must be present in the request for the request to be considered valid.
- (Optional) Select Another parameter and specify additional query parameters in the request to validate.
- Select Advanced options and select a Mode to specify how the query parameter validation request policy is applied:
- Enforcing: The API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service.
- Permissive: The API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation.
- Disabled: The API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

Note that Enforcing is the default validation mode.
- Select Add Validations .
- To validate the content in the body of a request to the API gateway for the current route by creating a body validation request policy:
- Select the Add button beside Body Validation and specify:
- Required: Whether the body of a request must be one of the content types you specify for the request to be considered valid.
- Media Type: A valid content type for the body of a request. For example,`application/json`,`application/xml`.
- (Optional) Select Another Media Type and specify additional valid content types for the body of the request.

If you specify multiple content types, the request body must be one of the allowed content types that you specify for the request to be considered valid.
- Select Advanced options and select a Mode to specify how the body validation request policy is applied:
- Enforcing: The API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service.
- Permissive: The API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation.
- Disabled: The API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

Note that Enforcing is the default validation mode.
- Select Update .
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for individual routes.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Validation Request Policies

To add validation request policies to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add validation request policies, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

Insert a`requestPolicies`section after the`backend`section for the route to which you want the validation request policy to apply. For example:

```

```

- 

To validate the headers included in a request to the API gateway for the current route, specify a`headerValidations`validation request policy:

```

```

where:
- `"name":"<header-name>"`is a header in the request to validate. The name you specify is not case-sensitive. For example,`X-Username`.
- `"required": <true|false>`indicates whether the header specified by`"name":"<header-name>"`must be present in the request for the request to be considered valid.
- 

`"validationMode": "<ENFORCING|PERMISSIVE|DISABLED>"`indicates how the API gateway validates requests against the header validation request policy, as follows:
- `ENFORCING:`The API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service.
- `PERMISSIVE:`The API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation.
- `DISABLED:`The API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

For example,`"validationMode": "PERMISSIVE"`. Note that`ENFORCING`is used as the default validation mode if you don't include`"validationMode"`.

For example:

```

```

In this example, for the request to be considered valid, the request must include the`X-Username`header. The API gateway only sends requests that pass validation to the back-end service.
- 

To validate the query parameters included in a request to the API gateway for the current route, specify a`queryParameterValidations`validation request policy:

```

```

where:
- `"name":"<query-parameter-name>"`is a query parameter in the request to validate. The name you specify is not case-sensitive. For example,`state`.
- `"required": <true|false>`indicates whether the query parameter specified by`"name":"<query-parameter-name>"`must be present in the request for the request to be considered valid.
- 

`"validationMode": "<ENFORCING|PERMISSIVE|DISABLED>"`indicates how the API gateway validates requests against the query parameter validation request policy, as follows:
- `ENFORCING:`The API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service.
- `PERMISSIVE:`The API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation.
- `DISABLED:`The API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

For example,`"validationMode": "PERMISSIVE"`. Note that`ENFORCING`is used as the default validation mode if you don't include`"validationMode"`.

For example:

```

```

In this example, for the request to be considered valid, the request can optionally include the`state`query parameter. The API gateway only sends requests that pass validation to the back-end service.
- 

To validate the content in the body of a request to the API gateway for the current route, specify a`bodyValidation`validation request policy:

```

```

where:
- `"required": true`indicates that the content type of the request body must be one of the content types you specify.
- `"content": {"<media-type-1>": {"validationType": "NONE"}, "<media-type-2>": {"validationType": "NONE"}}`indicates one or more allowed content types for the request body. The request body must be one of the content types that you specify. For example`application/json`,`application/xml`. Only`NONE`is currently supported for`"validationType"`.
- 

`"validationMode": "<ENFORCING|PERMISSIVE|DISABLED>"`indicates how the API gateway validates requests against the body validation request policy, as follows:
- `ENFORCING:`The API gateway validates all requests against the validation request policy. The API gateway only sends requests that pass validation to the back-end service.
- `PERMISSIVE:`The API gateway validates all requests against the validation request policy. The API gateway sends all requests to the back-end service, regardless of whether they pass or fail validation.
- `DISABLED:`The API gateway does not validate any requests against the validation request policy. The API gateway sends all requests to the back-end service.

For example,`"validationMode": "PERMISSIVE"`. Note that`ENFORCING`is used as the default validation mode if you don't include`"validationMode"`.

For example:

```

```

In this example, for the request to be considered valid, the content type of the request body must be application/json or application/xml. The API gateway only sends requests that pass validation to the back-end service.
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
