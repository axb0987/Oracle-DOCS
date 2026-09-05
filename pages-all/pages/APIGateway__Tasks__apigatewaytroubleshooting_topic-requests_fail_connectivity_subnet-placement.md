# Requests fail between a load balancer and API Gateway because of connectivity or subnet-placement issues
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-requests_fail_connectivity_subnet-placement.htm
- Fetched: 2026-09-05 01:39 CDT

# Requests fail between a load balancer and API Gateway because of connectivity or subnet-placement issues

Find out how to troubleshoot problems with the network path between a load balancer and an API gateway created with the API Gateway service.

When you place a load balancer URL in front of API Gateway and requests return`504 Gateway Timeout`, the failure is often in the network path between the load balancer and API Gateway. The back-end application might be working correctly, but the request might not reach API Gateway or the back-end service through the new path.

## Issue Symptoms

You might see one or more of the following symptoms:
- The new load balancer URL returns`504 Gateway Timeout`.
- Authentication completes, but the application is not reached.
- API Gateway access logs and execution logs do not show the expected request.
- The same back-end service works through one path, but fails through the new load balancer URL.

## Possible Causes

This issue can have one or more of the following causes:
- The load balancer backend set points to the wrong API Gateway endpoint.
- The load balancer and API Gateway use subnets that do not allow the required traffic path.
- Network security groups (NSGs) or security lists do not allow traffic between the load balancer and API Gateway.
- Route tables do not support the network path between the load balancer and API Gateway.
- The request times out before API Gateway can process it.

## Map the Request Path

Review each part of the request path before you update network rules or back-end targets:
- Client to load balancer.
- Load balancer to API Gateway.
- API Gateway to the back-end service.

In the Console, verify the following resources:
- The load balancer frontend listener.
- The load balancer backend set.
- The back-end target that is defined for API Gateway.
- The load balancer subnet.
- The API Gateway subnet.
- The API Gateway OCID.
- The API deployment OCID.

Verify that the load balancer backend set targets the intended API Gateway address or endpoint, not an outdated or unreachable path.

## Check Whether the Request Reaches API Gateway

Send the request through the load balancer URL and capture the response:
```

```

Review the API Gateway logs for the request:
- Open the API Gateway access log.
- Open the API Gateway execution log.
- Search the time window for the failing request.
- If the value is available, search for the`opc-request-id`value.

Use the log results to identify where the request failed:
- If API Gateway logs do not show the request, troubleshoot the load balancer or the network path before API Gateway.
- If API Gateway logs show the request, troubleshoot the path from API Gateway to the back-end service.

## Review Subnet Placement and Network Rules

For the load balancer subnet and the API Gateway subnet, review the following network resources:
- Route tables.
- NSGs.
- Security lists.

Verify the following network requirements:
- The load balancer subnet can send traffic to the API Gateway subnet.
- The API Gateway subnet can receive the required traffic from the load balancer path.
- No rule blocks the protocol or port that the load balancer uses to connect to API Gateway.

If the load balancer and API Gateway were created in different subnets for the new path, compare those subnets with the known-working path.

## Fix the Connectivity Issue

Apply the resolution that matches the problem that you found:
- If the load balancer backend set points to the wrong API Gateway target, update the backend set.
- If the load balancer subnet and API Gateway subnet do not support the intended path, update the subnet placement or routing configuration.
- If NSGs or security lists block the path, update the ingress or egress rules.
- If route tables do not allow traffic between the load balancer and API Gateway, update the route rules.
- If API Gateway never receives the request, fix the load balancer-to-API Gateway path before you troubleshoot the back-end service.

## Verify Connectivity

After you update the back-end target, subnet placement, or network rules, verify the connectivity again:
- Send the same request through the load balancer URL.
- Confirm that the request appears in API Gateway logs.
- Confirm that the`504 Gateway Timeout`response no longer occurs on the load balancer-to-API Gateway path.
- Confirm that the application is reachable through the intended external URL.

## For More Information

For more information, see:
- [Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm)
- [Configuring Your Tenancy for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringtenancies.htm)
- [Load Balancer Types](https://docs.oracle.com/iaas/Content/Balance/Concepts/load_balancer_types.htm)
- [HTTP-5xx errors when API deployment is created successfully but requests fail](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm)
