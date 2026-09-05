# Response cache TLS handshake fails
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-response_cache_tls_handshake_fails.htm
- Fetched: 2026-09-05 01:39 CDT

# Response cache TLS handshake fails

Find out how to troubleshoot response cache TLS handshake failures when creating API deployments with the API Gateway service.

If response caching is enabled and API Gateway reports cache health problems with a TLS handshake failure, API Gateway can reach the cache connection path but cannot complete the TLS handshake with the cache store.

## Issue Symptoms

You might see one or more of the following symptoms:
- The API deployment is active, but responses are not stored in the cache.
- The response cache is reported as unhealthy.
- Execution logs include an SSL handshake timeout, a TLS handshake failure, or a cache connection failure.
- Cached responses stop working, but the API continues to serve traffic.

## Possible Causes

This issue can occur for one or more of the following reasons:
- The cache endpoint hostname or port is incorrect.
- The API deployment is configured to use TLS, but the cache listener is not configured for TLS on the specified port or does not present the expected certificate.
- The cache server presents an expired, incomplete, or invalid certificate chain.
- A firewall, proxy, route rule, network security group (NSG), or security list blocks or interrupts the TLS handshake.
- The gateway subnet cannot reliably reach the cache endpoint.
- The cache authentication credentials in the referenced secret are missing, expired, or incorrect.

## Review the Response Cache Configuration

Review the response cache configuration and confirm that the following settings match the cache endpoint that you expect API Gateway to use:
- `responseCaching.responseCache.servers[0].host`
- `responseCaching.responseCache.servers[0].port`
- `responseCaching.responseCache.isSslEnabled`
- `responseCaching.responseCache.isSslVerifyDisabled`
- `responseCaching.responseCache.authenticationSecretId`
- `responseCaching.responseCache.authenticationSecretVersionNumber`
- `responseCaching.responseCache.connectTimeoutInMs`

Confirm that the response cache configuration points to the intended cache server. API Gateway supports only a single cache server host for response caching.

## Check the Execution log

Check the execution log for response-cache TLS handshake failures or cache connection failures.

## Confirm the Cache TLS Endpoint

Confirm that the cache endpoint is ready to accept the TLS connection from the gateway:
- Confirm that the cache listener expects TLS on the configured port.
- Confirm that the certificate presented by the cache server chains to a certificate authority (CA) that API Gateway trusts when certificate verification is enabled.
- Confirm that the cache username and password in the referenced secret are valid.
- From a compute instance that uses the same network path as the gateway subnet, run`nc -vz <cache-host> <cache-port>`to confirm TCP reachability.
- Run`openssl s_client -connect <cache-host>:<cache-port> -servername <cache-host> -showcerts`to inspect the certificate chain and TLS handshake result.

## Fix Response Cache TLS Issues

Use the following actions to resolve the TLS handshake failure:
- If the cache endpoint is incorrect, update the configured cache host or port.
- If the cache server is not listening for TLS on the configured port, correct the listener configuration or disable TLS in the gateway configuration when plaintext cache traffic is acceptable for your environment.
- If the certificate chain is expired, incomplete, or untrusted, update the certificate chain or the trust configuration.
- If the cache credentials are incorrect, update the referenced secret version with the correct username and password.
- If the network path is blocked, update the route rule, NSG rule, security list rule, firewall, or proxy configuration that controls traffic between the gateway subnet and the cache endpoint.

## Verify Response Caching

After you update the configuration, verify that response caching works as expected:
- Retry a request that should use response caching.
- Confirm that the cache TLS handshake failure no longer appears in the execution log.
- Confirm that API Gateway no longer reports response-cache health problems for the request path.

## For More Information

For more information, see:
- [Caching Responses to Improve Performance](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm)
- [Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm)
- [HTTP-5xx errors when API deployment is created successfully but requests fail](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm)
