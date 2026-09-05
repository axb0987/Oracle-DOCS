# Transformation Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-transformexamples.htm
- Fetched: 2026-09-05 01:38 CDT

# Transformation Examples

Use examples to learn how to modify incoming requests and outgoing responses being sent to and from back-end services with API Gateway.

The examples in this section assume the following API deployment definition and basic API deployment specification in a JSON file:

```

```

Note the examples also apply when you're defining an API deployment specification using dialogs in the Console.

## Example 1: Transforming header parameters to query parameters

In this example, assume an existing HTTP back end only handles requests containing query parameters, not header parameters. However, you want the HTTP back end to handle requests that include header parameters. To achieve this, you create an API deployment specification that includes a query parameter transformation request policy to pass the value obtained from a request header to the HTTP back end as a query parameter.

```

```

In this example, a request like`curl -H "region: west" https://<gateway-hostname>/marketing/weather`resolves to`https://api.weather.gov?region=west`.

## Example 2: Transforming one header to a different header

In this example, assume an existing HTTP back end only handles requests containing a particular header. However, you want the HTTP back end to handle requests that include a different header. To achieve this, you create an API deployment specification that includes a header transformation request policy to take the value obtained from one request header and pass it to the HTTP back end as a different request header.

```

```

In this example, a request like`curl -H "locale: west" https://<gateway-hostname>/marketing/weather`resolves to the request`curl -H "region: west" https://api.weather.gov`.

## Example 3: Adding an authentication parameter obtained from a JWT as a request header

In this example, assume an existing HTTP back end requires the value of the`sub`claim in a validated JSON Web Token (JWT) to be included in a request as a header with the name JWT_SUBJECT. The API Gateway service has saved the value of the`sub`claim included in the JWT as an authentication parameter in the`request.auth`table.

To include the value of`sub`in a header named JWT_SUBJECT, you create an API deployment specification that includes a header transformation request policy. The request policy obtains the`sub`value from the`request.auth`table and passes it to the HTTP back end as the value of the JWT_SUBJECT header.

```

```

In this example, when a request has been successfully validated, the JWT_SUBJECT header is added to the request passed to the HTTP back end.

## Example 4: Adding a key obtained from an authorizer function as a query parameter

In this example, assume an existing HTTP back end requires requests to include a query parameter named`access_key`for authentication purposes. You want the`access_key`query parameter to have the value of a key named`apiKey`that has been returned by an authorizer function that has successfully validated the request. The API Gateway service has saved the`apiKey`value as an authentication parameter in the`request.auth`table.

To include the`access_key`query parameter in the request, you create an API deployment specification that includes a query parameter transformation request policy. The request policy obtains the`apiKey`value from the`request.auth`table and passes it to the HTTP back end as the value of the`access_key`query parameter.

```

```

In this example, the`access_key`query parameter is added to the request passed to the HTTP back end, with the`apiKey`value from the`request.auth`table. A request like`https://<gateway-hostname>/marketing/weather`resolves to a request like`https://api.weather.gov?access_key=fw5n9abi0ep`

## Example 5: Adding a default value for an optional query parameter

In this example, assume an existing HTTP back end requires requests to include a query parameter named`country`. However, the`country`query parameter is optional, and it's not included by some of the API clients sending requests. If a request already includes a`country`query parameter and a value, you want both passed as-is to the HTTP back end. However, if a request doesn't already include a`country`query parameter, you want the`country`query parameter and a default value added to the request.

To make sure every request includes a`country`query parameter, you create an API deployment specification that includes a query parameter transformation request policy. The request policy adds the`country`query parameter and a default value to any requests that do not already include the`country`query parameter.

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather`resolves to`https://api.weather.gov?country=usa`. A request like`https://<gateway-hostname>/marketing/weather?country=canada`resolves to`https://api.weather.gov?country=canada`
