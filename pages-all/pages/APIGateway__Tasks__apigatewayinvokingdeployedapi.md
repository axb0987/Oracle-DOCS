# Calling an API Deployed on an API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm
- Fetched: 2026-09-05 01:38 CDT

# Calling an API Deployed on an API Gateway

Find out how to call an API that you have previously deployed on an API gateway with the API Gateway service.

Having deployed an API on an API gateway, you can call the deployed API.
Tip  
  

When assembling the curl command described in this topic, you can quickly get the value of the`https://<gateway-hostname>/<deployment-path-prefix>`string as the API deployment's endpoint using:
- The Console, by going to the Details tab of the API deployment details page and selecting Copy beside the endpoint of the API deployment.
- The API, by using the[GetDeployments](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/GetDeployment)operation.

## Using curl

To call an API deployed on an API gateway:
- 

Open a terminal window and type a cURL command similar to the following that is appropriate for the deployed API:

```

```

where:
- `<method>`is a valid method for the deployed API (for example, GET, PUT).
- 

`<gateway-hostname>`is an automatically generated domain name in the format`<gateway-identifier>.apigateway.<region-identifier>.oci.customer-oci.com`, where:
- `<gateway-identifier>`is the string of characters that identifies the API gateway. For example,`lak...sjd`(abbreviated for readability).
- `<region-identifier>`is the identifier of the region in which the API gateway has been created. See[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayprerequisites.htm#regional-availability).

For example,`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`.

Use the Console or the API to find out the domain name to use as the value of`<gateway-hostname>`.
- 

`/<deployment-path-prefix>`is the prefix added to the path of every route in the API deployment. Note that the deployment path prefix in the request:
- can contain multiple forward slashes (provided they are not adjacent)
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- cannot include parameters and wildcards
- must match exactly the deployment path prefix defined for the API deployment (see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm))

Use the Console or the API to find out the path prefix to use as the value of`<deployment-path-prefix>`.
- 

`/<api-route-path>`is the path to a particular route defined in the API deployment specification. Note that the route path in the request:
- is relative to the deployment path prefix
- can be a single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- need not match exactly the route path defined in the API deployment specification, provided the route path in the API deployment specification includes a path parameter with or without a wildcard (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))

Use the Console or the API to find out the path to use as the value of`<api-route-path>`.

For example:

```

```

If the API gateway back end is a serverless function that accepts parameters, include those parameters in the call to the API. For example:

```

```
