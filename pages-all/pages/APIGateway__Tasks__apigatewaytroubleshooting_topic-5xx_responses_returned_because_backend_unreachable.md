# API Gateway returns 5xx responses because it cannot reach the backend
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-5xx_responses_returned_because_backend_unreachable.htm
- Fetched: 2026-09-05 01:38 CDT

# API Gateway returns 5xx responses because it cannot reach the backend

Find out how to troubleshoot gateway-generated 5xx responses caused by backend reachability problems when calling APIs, having successfully created API gateways and API deployments with the API Gateway service.

Use this topic after you confirm that the`5xx`response did not come from your back-end service. If API Gateway cannot connect to the back-end service or receive a usable response, it can return`502`or`504`on the back-end call path.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

The client receives a`502`or`504`response through API Gateway.
- 

The back-end service does not show a matching successful request.
- The back-end hostname does not resolve from the gateway path.
- 

The back-end service is reachable from some networks but not from the gateway subnet.

## Possible Causes

This issue can have one or more of the following causes:
- 

API Gateway cannot resolve the back-end hostname.
- 

The route table, network security group (NSG), security list, or cross-virtual cloud network (VCN) configuration blocks the network path to the back-end service.
- 

The back-end service rejects the connection or does not listen on the expected port.
- 

API Gateway connects to the back-end service, but the service takes too long to send a response.
- 

API Gateway times out while sending the request body to the back-end service.

## Review the Back-End Configuration

Review the API deployment configuration and confirm the following settings:
- 

The`backend.url`value uses the hostname, scheme, and port that must be reachable from the gateway subnet.
- 

The`gateway.endpointType`value matches the gateway network model.
- 

The`connectTimeoutInSeconds`,`readTimeoutInSeconds`, and`sendTimeoutInSeconds`values match the expected behavior of the back-end service.

For HTTP back-end services, the default timeout values are:
- 

`connectTimeoutInSeconds = 60`.
- 

`readTimeoutInSeconds = 10`.
- 

`sendTimeoutInSeconds = 10`.

## Review Log Messages

Review the execution log for messages that identify DNS, connectivity, or timeout failures. The log can include messages such as the following examples:
- 

`Upstream address resolution failure while resolving <backend-hostname>`.
- 

`An error occurred whilst sending request to <backend-url>: DNS_NXDOMAIN`.
- 

`An error occurred whilst sending request to <backend-url>: CONNECTION_REFUSED`.
- 

`An error occurred whilst sending request to <backend-url>: CONNECTION_TIMEOUT`.
- 

`An error occurred whilst sending request to <backend-url>: TIMEOUT`.
- 

`no route to host`.
- 

`connection timed out`.

Use these messages to determine whether the failure is caused by DNS resolution, a blocked network path, a refused connection, or a delayed back-end response.

## Test DNS and Network Reachability

From a compute instance that uses the same route tables, NSGs, and security lists as the gateway subnet, run tests that match the back-end hostname and port.

Use commands such as the following examples:
- 

`nslookup <backend-hostname>`.
- 

`curl -vk https://<backend-hostname>:<backend-port>/<path>`.

If the DNS lookup fails, fix the hostname or DNS configuration before changing timeout values. If DNS resolves but the connection fails, review routing, security rules, and the back-end listener configuration.

## Adjust Timeout Settings

Adjust only the timeout setting that matches the observed failure:
- 

Increase`connectTimeoutInSeconds`when API Gateway cannot establish the TCP connection to the back-end service quickly enough.
- 

Increase`readTimeoutInSeconds`when the back-end service accepts the connection but takes too long to send the response.
- 

Increase`sendTimeoutInSeconds`when API Gateway takes too long to send the request body to the back-end service.

Before you increase a timeout value, confirm that the DNS configuration, network path, and back-end service behavior are otherwise correct.

## Fix Back-End Reachability

Apply the resolution that matches your findings:
- 

If the back-end hostname does not resolve, fix the DNS or hostname configuration.
- 

If DNS resolves but the connection test fails with`no route to host`or`CONNECTION_REFUSED`, review subnet route tables, NSGs, security lists, local peering gateway (LPG) routing, dynamic routing gateway (DRG) routing, NAT gateway configuration, and service gateway assumptions.
- 

If the execution log shows`CONNECTION_TIMEOUT`, fix the network path before increasing`connectTimeoutInSeconds`.
- 

If the execution log shows`TIMEOUT`, check whether the back-end service takes too long to respond before increasing`readTimeoutInSeconds`.
- 

If the failure occurs while the client uploads a large request body, evaluate the request size and increase`sendTimeoutInSeconds`when the upload requires more time.

## Verify Back-End Connectivity

After you fix DNS, network path, back-end availability, or timeout configuration issues, verify the same API route again.
- 

Send the same request to the API deployment.
- 

Confirm that the gateway no longer returns`502`or`504`for the back-end path.
- 

Confirm that the execution log no longer shows back-end reachability or timeout errors.
- 

Confirm that the back-end service logs show the expected matching request and response.

## For More Information

For more information, see:
- 

[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)
- 

[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)
- 

[HTTP-5xx errors when API deployment is created successfully but requests fail](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm)
- 

[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)
