# Adding Path Parameters and Wildcards to Route Paths
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Path Parameters and Wildcards to Route Paths

Find out how to add path parameters and wildcards to route paths in API deployment specifications with API Gateway.

You might want different API requests routed to the same backend, even when the request URLs vary to a greater or lesser extent from the route path definition in the API deployment specification.

When defining a route path in an API deployment specification, you can include a path parameter to exactly replace an individual segment of the path. If necessary, you can include multiple path parameters in the route path. You can also append the asterisk (*) wildcard to a path parameter in the route path to provide even more flexibility when identifying requests to send to the same backend.

The examples in this topic assume you are adding route paths to an API deployment specification in a JSON file. Note the examples also apply when you're defining an API deployment specification using dialogs in the Console.

## Example: Adding Path Parameters to Match Similar URLs

You might have a requirement to route requests with similar URLs to the same backend. For example:
- https://&lt;gateway-hostname&gt;/marketing/hello/us/index.html
- https://&lt;gateway-hostname&gt;/marketing/hello/apac/index.html
- https://&lt;gateway-hostname&gt;/marketing/hello/emea/index.html

To enable calls to these similar URLs to resolve to the same backend, add a path parameter name enclosed within curly brackets as the segment of the route path that will vary between API calls. For example,`{region}`as shown below:

```

```

Note that path parameter names:
- Can include alphanumeric uppercase and lowercase characters.
- Can include the underscore`_`special character.
- Cannot include other special characters. In particular, note that you cannot include spaces, forward slashes, and curly brackets in path parameter names.

## Example: Adding Path Parameters with a Wildcard to Match Dissimilar URLs

You might have a requirement to route requests to the same backend, even though the request URLs are significantly different. For example:
- https://&lt;gateway-hostname&gt;/marketing/hello/us/index.html
- https://&lt;gateway-hostname&gt;/marketing/hello/apac/introduction/
- https://&lt;gateway-hostname&gt;/marketing/hello/emea/welcome.html
- https://&lt;gateway-hostname&gt;/marketing/hello/introduction
- https://&lt;gateway-hostname&gt;/marketing/hello/top.html
- https://&lt;gateway-hostname&gt;/marketing/hello/

To enable calls to these significantly different URLs to resolve to the same backend:
- add a path parameter name enclosed within curly brackets as the first segment of the route path that will differ between the various API calls
- add the asterisk (*) wildcard to the end of the path parameter name

For example,`{generic_welcome*}`as shown below:

```

```

Note that a path parameter name with an asterisk wildcard will match:
- no path segment
- a single path segment
-
