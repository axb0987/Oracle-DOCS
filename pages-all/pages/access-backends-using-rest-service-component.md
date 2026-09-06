# Access Backends Using the REST Service Component
- Source: https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-rest-service-component.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-rest-service-component.html#dcoc-content-body)

# Access Backends Using the REST Service Component

If your skill needs to retrieve or update some data through a backend service, you can quickly implement this by adding a REST service configuration for the API's endpoint and calling that service from your skill using the Call REST Service component.

### Add a REST Service for an Endpoint

Oracle Digital Assistant provides a built-in Call REST Service component that you can use in Visual Dialog skills to send a request to a REST service's endpoint. Before you can make the request from a Call REST Service component, you must first configure the endpoint in the REST Services tab.

To add a REST Service:
- 

In Oracle Digital Assistant, click to open the side menu, select Settings , select API Services , and then click the REST Services tab.
- 

Provide this general information:

Field Description
Name A unique name that lets you easily identify the endpoint that you are configuring. For example, for an appointments API, you might name the REST services "appointmentsUser" and "appointmentsUserEntry".
Endpoint The endpoint to access the REST operation. Use curly braces to delineate path parameters. For example:`https://example.com/appointments/{userId}`.

For Oracle Cloud Infrastructure endpoints, ensure that you use the endpoint for your tenancy's region.

Note: Do not use query parameters in this field. If you want to specify a query parameter to test the API, you can use the Parameters property (as described in the table below) for each method you define for the endpoint.
Description An optional description that explains the purpose of the endpoint. For example: "Adds and retrieves a user's appointments."
Authentication Type

Select how to authenticate the REST call.
- 

No Authentication Required: Select this when the service doesn't require authentication.
- 

Basic Authentication: Select this when the service uses a Basic authentication. You’ll then need to provide a user name and a password..
- 

API Key: Select this when the service uses an API Key for authentication. You’ll then need to indicate whether the key must be passed as a path parameter or a query parameter, and you'll need to specify the key name and value.
- 

Bearer Token: Select this when the service uses a Bearer token for authentication. You’ll then need to specify the token.
- 

OCI Resource Principal: Select this when you are accessing an Oracle Cloud Infrastructure API.
Private Endpoint If you have a private endpoint set up for the service that you need to access, turn this switch to the On position and select the private endpoint you are using.

Note: You can set up private endpoints for services that are not exposed publicly on the internet. See[Private Endpoint](https://docs.oracle.com/iaas/digital-assistant/doc/service-administration.html#GUID-5042E5CE-6105-4C00-B4C6-BDFC632942E7).
- 

For each method that you want to configure for the endpoint, click + Add Method , select the method, and then provide this information:

Field Description
Content Type The type of the content that's included in the request body.`application/json`and`text/plain`are supported.
Body For POST, PUT, and PATCH requests, the request body to send with the request. You can override this value in the Call REST Service component.

For large request bodies, click Use Edit Dialog to open an editor.
Parameters You can add path and query parameters for testing the request. You also can add path and query parameters to configure default values. Note that the skill developers can override these parameter values from the Call REST Service component. That is, they can add parameters in the component to override the values configured in the REST service, and not add the parameters where they want to use the values set in the REST service configuration.

For the path parameters that are in the endpoint, add a parameter of type Path , set the key to match the path parameter, and set the desired value.

For query parameters that you want to pass in the REST request, add a parameter of type Query , set the key to match the query parameter, and set the desired value.

If the authentication type is API Key, and the key is passed in as a query parameter, don't add a query parameter for that key value here as it's already configured.

After you edit the parameter, click to add the parameter to the list.

Note: The query parameter value must be a string (Freemarker expressions are not supported). This value is only for testing the API. The real value that your skill uses needs to configured within the[Call REST Service](https://docs.oracle.com/iaas/digital-assistant/doc/component-templates.html#GUID-B232187B-5211-41B6-B43E-30AF62D71295)component.
Headers Add any headers that you want to pass in the request.

If the authentication type is API Key, and the key is passed in a header, don't add a header for that key value here as it's already configured.
Static Response You can use the static response configuration for cases where you need a fallback response whenever there's an error. You can also use it to set up mock data for development or testing purposes.

To configure a static response, select a return status code and then define the response body. Alternatively, set the desired parameters and headers, click Test Request , and then click Save as Static Response to save values for the static response.
- 

If you want to test the method, set the path and query parameters to use for the path, set any necessary headers, provide a request body if necessary, and click Test Request . A Response Status dialog appears with the response status and body.

Tip: You can click Save as Static Response to save the status code and body in the static response fields.

### Use the Call REST Service Component

When a skill needs to retrieve or update some data through a backend service, add a state that uses the Call REST Service component. Here's how to use that component.
Note  
  
The Call Service Component is supported in visual dialogs only, not in YAML dialogs.
- 

Configure the endpoint on the Settings &gt; API Services &gt; REST Services page as described in[Add a REST Service for an Endpoint](https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-rest-service-component.html#GUID-05DDA62D-E170-4E5A-8597-9136AB2F90F5). This is where you define the endpoint, authentication type, supported methods, request body, path and query parameters, headers, and an optional static response.
- 

In the desired flow in the skill's flow designer, add the state, choose Service Integration &gt; Call Rest Service , provide a name, and then click Insert .
- 

Select the REST service that you configured on the REST Services page.
- 

Select the method.
- For POST, PUT, and PATCH requests, you'll typically need to provide a request body.

Tip: If the body contains FreeMarker expressions, then you can switch Expression to On to see FreeMarker syntax coloring. However, if you do so, JSON syntax validation is turned off.
- 

In the Parameters section, configure the path and query parameters that you want to send with the request.

Parameters that you set in the component override the parameters that are set in the REST service configuration. Conversely, if you don't set a parameter in the component, then the request uses the parameter value from the REST service configuration.

For query parameters that are defined in the REST service configuration, if you don't want to pass that query parameter, set its value to`${r""}`.
- 

Set any headers that you want to send with the request.

Headers that you set in the component override the headers that are set in the REST service configuration. Conversely, if you don't set a header in the component, then the request uses the header value from the REST service configuration.
- 

Specify which response you want returned after the call completes:
- 

Use Actual REST API Response: This returns the actual response from the REST service.
- 

Always Use Static REST Response: This returns the static response that is configured on the REST Services tab. This response is helpful during development and test phases, among other uses.
- 

Fallback Using Static Response: If the REST request is successful, then the REST response is returned. Otherwise, the static response that's configured on the REST Services tab is returned.

Note that if the REST service configuration doesn't have a static response, then the only choice is Use Actual Response .
- 

For the result variable, select the map variable for storing the response data. If it doesn't exist yet, click Create to make one.

After the request completes, the map will contain a`responsePayload`property for the response body and a`statusCode`property for the status code. How the response body is stored in the variable depends on the whether the response is a JSON object, JSON Array, or plain text (string):
- 

JSON Object: The object is stored in the`responsePayload`property.
- 

JSON Array: The array is stored in the`responsePayload.responseItems`property.
- 

Plain Text: The text is stored in the`responsePayload.message`property.
- On the Transitions tab, specify the next transition and the transitions for the success and failure actions.

- 

The success action occurs when the`statusCode`is between 100 and 299.
- 

The failure action occurs when the`statusCode`is 300 and above.
Note  
  
By default, the result variable can only hold a payload of up to 15 KB. If you need a higher limit, file a service request (SR) with Oracle Support.

For more details about this component, see[Call REST Service](https://docs.oracle.com/iaas/digital-assistant/doc/component-templates.html#GUID-B232187B-5211-41B6-B43E-30AF62D71295).

- [Access Backends Using the REST Service Component](https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-rest-service-component.html#DACUA-GUID-1992F05A-0336-4AFE-B9DE-FDBE2AFFB377)
- [Add a REST Service for an Endpoint](https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-rest-service-component.html#DACUA-GUID-05DDA62D-E170-4E5A-8597-9136AB2F90F5)
- [Use the Call REST Service Component](https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-rest-service-component.html#DACUA-GUID-445C7128-9E85-48CD-8B2F-A9CB725DC413)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
