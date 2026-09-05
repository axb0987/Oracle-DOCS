# Common Load Balancer Errors
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/common_load_balancer_errors.htm
- Fetched: 2026-09-05 01:42 CDT

# Common Load Balancer Errors

Learn about common load balancer errors associated with the load balancers.

Common load balancer errors include, series 500 and series 400 errors, health check errors, client errors, and SSL errors. The subsequent topics in this section describe these common errors and detail troubleshooting procedures for each, where applicable.

## Server Errors (500-599)

### 504

Error messages :
- `lbStatusCode: "504"`
- `backendStatusCode: ""`

Oracle Cloud Infrastructure log category : Access log

Symptoms :

The client fails with a`504`error.

Possible causes :

The load balancer is not able to establish connections with any of the backends, even though the health check is marking the backends as available.

Possible solutions :

Configure the health check correctly.

Troubleshooting documentation :[Editing a Load Balancer's Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)

### 502, 502
Error messages :
- `lbStatusCode: "502"`
- `backendStatusCode: "502"`

Oracle Cloud Infrastructure log category : Access log and error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- The backend health check succeeds.
- The backend returns a`502`error.
Possible causes :
- An application on the backend is returning a`502`error.
- The backend is configured incorrectly.
- The backend is likely another reverse proxy or load balancer.

Possible solutions :

Examine the backend application logs to determine why a`502`error is returned.

Troubleshooting documentation :[HTTP 502 Bad Gateway Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_http.htm#HTTP502)and[Testing TCP and HTTP Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_backend.htm#TestTCPHTTPBackendServers).

### 502
Error messages :
- `lbStatusCode: "502"`
- `backendStatusCode: ""`
- `No healthy backends available in associated backend set`

Oracle Cloud Infrastructure log category : Access log and error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- The backend health check fails.
- No traffic observed to a specific backend or all backends.
Possible causes :
- A backend application is not responding to the health check with the expected response.
- If no error occurs from the backend, then a TCP health check is configured.
- A single backend or all backends are configured in drain mode.
Possible solutions :
- Determine why TCP health check is failing.
- Convert to HTTP health check.
- Change the drain mode to false ( undrain ) for a given backend or all backends.

Troubleshooting documentation :[HTTP 502 Bad Gateway Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_http.htm#HTTP502)and[Testing TCP and HTTP Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_backend.htm#TestTCPHTTPBackendServers).

### Session Persistence Issue
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- Session persistence is failing.
Possible causes
- Backend set is configured with session persistence and the expected backend is not available because the connection failed or timed out.
- Fallback option is disabled.
Possible solutions :
- Determine why backend application isn't reachable.
- Enable fallback option in case the selected server is unavailable.

Troubleshooting documentation :[Fallback](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/sessionpersistence.htm#fallback)

For all other 5 nn errors, the most likely causes are issues with the backend server.

## Client Errors (400-499)

### 400
Error messages :
- `lbStatusCode: "400"`
- `backendStatusCode: ""`
- `400 bad request header or cookie too large`

Oracle Cloud Infrastructure log category : Access log
Symptoms :
- The load balancer returns a status code`400`.
- The backend server doesn't return a status code.

Possible causes :

The client is sending a request that exceeds the configured buffer size.

Possible solutions :

Increase the HTTP request header size on the load balancer. By default, the size limit is 8 KB but raising it to 64 KB resolves the issue.

Troubleshooting documentation :[HTTP Header Rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingrulesets.htm#HTTPHeaderRules)

### 404, 404
Error messages :
- `lbStatusCode: "404"`
- `backendStatusCode: "404"`

Oracle Cloud Infrastructure log category : Access log
Symptoms :
- The load balancer returns a`404`status code.
- The backend server returns a`404`status code.

Possible causes :

The expected page does not exist on the backend.
Possible solutions :
- Create the missing page.
- Configure the client to call the correct page.

### 403, 403
Error messages :
- `lbStatusCode: "403"`
- `backendStatusCode: "403"`

Oracle Cloud Infrastructure log category : Access log
Symptoms :
- The load balancer returns a`403`status code.
- The backend server returns a`403`status code.
Possible causes :
- Expected page doesn't have enough permission on the backend.
- Expected authentication token is missing or not being forwarded.

Possible solutions :
- Create missing permissions on backend.
- Adjust client configuration to ensure that tokens are sent properly.
- Ensure that all tokens being sent are arriving at the backend.
- If the header is missing:
- Adjust header size on the load balancer or the client.
- Allow headers with special characters.

Troubleshooting documentation :[HTTP Header Rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingrulesets.htm#HTTPHeaderRules)

## Health Check Errors

### No Healthy Backend Servers
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log

Symptoms :

The client fails with a`502 Bad Gateway`error.
Possible causes :
- No backend servers in the backend set.
- No backend servers responding to health check.
Possible solutions :
- Determine why backend servers aren't responding to health check.
- Check and adjust any health check settings, including status code, regular expressions, interval timeout, port, and protocol.

Troubleshooting documentation :[Editing a Load Balancer's Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)

### Status Code Issues

Backend health status failure reason: Status code mismatch

Oracle Cloud Infrastructure category: Backend Health Status
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The backend server fails the health check.
- The client fails with a`502 Bad Gateway`error.
- `invalid statusCode`appears in the error logs.
Possible causes :
- The backend server is responding with an incorrect response code.
- The backend server health check fails because of response code mismatch.
- The health check failures are because of an unexpected status code in the regular expression body.
Possible solutions :
- Determine why the backend server is sending the incorrect response code.
- Adjust the path or status code of the health check to match the backend server.

Troubleshooting documentation :[Editing a Load Balancer's Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)

### Response Match Failed

Backend Health Status Failure Reason: Regular expression mismatch

Oracle Cloud Infrastructure category: Backend Health Status
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The backend server fails the health check.
- The client fails with a`502 Bad Gateway`error.
- `"response match result: failed"`appears in the error logs.

Possible causes :

The backend server health check fails because of regular expression mismatch, incorrect value returned, or incorrect value provided to the health check.
Possible solutions :
- Determine why the backend server is sending the incorrect body.
- Adjust the path or regular expression pattern of the health check to match the backend server.

Troubleshooting documentation :[Editing a Load Balancer's Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)

### Unreachable Host

Backend Health Status Failure Reason: Connection failed

Oracle Cloud Infrastructure category: Backend Health Status
Error messages :
```

```

```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The backend server fails the health check.
- The client fails with a`502 Bad Gateway`error.
- `"EHOSTUNREACH"`appears in error logs.
Possible causes :
- The backend server health check fails because of an unreachable host.
- The backend server health check fails because of a connection reset.
- An application or firewall is actively refusing the connection.
Possible solutions :
- Check the local instance firewall to confirm that traffic is being allowed.
- Check the local instance to confirm that the application is running.
- Check the network security group and security lists to confirm that traffic is allowed.

Troubleshooting documentation :[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm)

### Health Status Issues
Error messages :
```

```

```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client behaves as expected but fails periodically.
- The backend server switches between passing and failing the health check.
- `"Unhealthy to Healthy"`or`"Healthy to Unhealthy"`appears in error logs.
Possible causes :
- An unhealthy backend server becomes healthy.
- If the health status of the backend server changes often, it can indicate a chronic problem.
Possible solutions :
- Ensure that the instance isn't changing health status abnormally.
- Check application logs on the backend server for any application-specific issues.

### Connection Issues

Backend Health Status Failure Reason: Timed out

Oracle Cloud Infrastructure category: Backend Health Status
Error messages :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- The backend server is periodically or chronically failing health checks.
- `"connect timed out"`appears in the error logs.
Possible causes :
- The backend server isn't responding to health checks in the expected time period.
- Slow upstream dependency including, database, application service or API, or slow storage services, such as Oracle Cloud Infrastructure File Storage service, Elastic Block Store, or Object Storage.
Possible solutions :
- Perform a local test to the backend server to eliminate the load balancer as a cause.
- Check the performance of all upstream dependencies.
- Check application logs on the backend server for any dependencies reporting any sort of timeout.

Troubleshooting documentation :[Testing TCP and HTTP Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_backend.htm#TestTCPHTTPBackendServers).

## SSL Errors

### SSL Virtual Listener Issues
Error message :
```

```

Symptoms :

You can't create backend servers for an existing load balancer nor can you add new servers to the backend server created previously within the same load balancer.

Possible causes :

Mismatch of transport layer security (TLS) versions.

Possible solutions :

Match TLS versions on the listeners.

Troubleshooting documentation :[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm)

### SSL Handshake Issues
Error message :
```

```

Oracle Cloud Infrastructure log category : Client log

Symptoms :

The client experiences SSL handshake failures in Load Balancer metrics (see[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/loadbalancermetrics.htm)).

Possible causes :

The backend server isn't configured to accept SSL.
Possible solutions :
- Confirm that the backend server certificate matches the certificate authority that's provided.
- Ensure that all certificates in the chain are provided in the correct order in the Certificate field.
- Ensure that you provide the correct certificate depth.

Troubleshooting documentation :[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm)

### Backend SSL Handshake Issues
Error messages :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- The client experiences SSL handshake failures in Oracle Cloud Infrastructure metrics (see[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/loadbalancermetrics.htm)).
Possible causes :
- The backend server isn't configured to accept SSL.
- The backend server certificate is invalid.
Possible solutions :
- Confirm that the backend server certificate matches the certificate authority that's provided.
- Ensure that all certificates in the chain are provided in the correct order in the Certificate field.
- Ensure that you provide the correct certificate depth.

Troubleshooting documentation :[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm)

### SSL Certificate Issues

Error :

Client`backend_ip_address`has SSL certificate verify error.

Oracle Cloud Infrastructure log category : Error log

Symptoms :

The client experiences SSL handshake failures in Oracle Cloud Infrastructure metrics (see[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/loadbalancermetrics.htm)).
Possible causes :
- The client certificate is invalid.
- The client certificate isn't trusted.
- Invalid peer certification verify depth.
Possible solutions :
- Ensure that the client certificate is valid.
- Remove Peer Cert Verify feature on the listener.

Troubleshooting documentation :[Key Pair Mismatch](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm#key-pair-mismatch)and[Private Key Consistency](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm#private-key-consistency).

### Client SSL Certificate Issues
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client experiences a`400 Response`error.
- `no required SSL certificate`appears in error logs.

Possible causes :

The client isn't sending a client certificate.
Possible solutions :
- Update the client to send the correct client certificate.
- Remove Peer Cert Verify feature on the listener.
- Adjust the certificate verification depth.

Troubleshooting documentation :[Configuring Peer Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm#configure-peer-certificate-verification).

### SSL Error Causes Backend Server Health Check Failure
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log

Symptoms :

The backend server health check fails because of the SSL error.

Possible causes :

The backend server is configured to accept SSL but the health check protocol selected doesn't match that of the backend server.

Possible solutions :

Confirm that you're using non-TLS health check on a backend server that has TLS enabled.

Troubleshooting documentation :[Editing a Load Balancer's Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)

### SSL Host Name Verification Fails
Error message :
```

```

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- Error message contains`SSL host name verification failed`.

Possible causes :

Host name provided doesn't match what is expected.
Possible solutions :
- Configure client to use the expected host name.
- Configure certificate to match the host name sent by the client.

Troubleshooting documentation :[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingcertificates.htm)

## Client-Side Errors

### Client Access Denied

Error :

Access for`client_ip_address`denied by HTTP ACL rule.

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- The backend server doesn't pass health check.
- `forbidden by HTTP ACL rule`appears in the error log.

Possible causes :

Access control rule set is enabled bud doesn't include the source IP address.

Possible solutions :

Check and apply respective rule set to include the source IP address.

Troubleshooting documentation :[Access Control Rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingrulesets.htm#AccessControlRules)

### Client Timeout Issue

Error :

Client`client_name`timed out

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a`502 Bad Gateway`error.
- The client experiences SSL handshake failures in Oracle Cloud Infrastructure metrics (see[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/loadbalancermetrics.htm)).

Possible causes :

The client terminated the connection sooner than the configured timeout for the load balancer.
Possible solutions :
- Configure client timeout to match expected application configuration.
- Determine why the backend server didn't respond in the configured amount of time.

Troubleshooting documentation :[Testing TCP and HTTP Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_backend.htm#TestTCPHTTPBackendServers).

### Client Connection Closed Abruptly

Error :

Connection to`address`was abruptly closed by

Oracle Cloud Infrastructure log category : Error log

Symptoms :

The client fails with a 502 Bad Gateway error.

Possible causes :

The listener has an Max listener connection rule and an IP tried to make more connections to the listener than allowed by the rule.

Possible solutions
- Increase the allowed number of connections an IP can make to the listener.
- Reduce the number of connections the IP is making to the listener.

Troubleshooting documentation :[Max Listener Connection Rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Tasks/managingrulesets.htm#max-listener-connection-rules).

## Backend Server Errors

### Backend Server Connection Issue

Error :

Backend server`ip_address`abruptly closes connection.

Oracle Cloud Infrastructure log category : Error log
Symptoms :
- The client fails with a 502 Bad Gateway error.
- The client reports IO error in load balancer metrics.
- The backend server set uses HTTPS and the cipher suites or TLS versions aren't compatible.

Possible causes :
- The backend server connection timeout is configured incorrectly, with a lower timeout value than the load balancer.
- The backend server or its containing backend set has`maxConnections`set and the number of connections to the backend server has reached the specified limit.

Possible solutions :
- Determine why the backend server application is timing out.
- If the backend server timeout value needs to be adjusted, then adjust it to be greater than the load balancer timeout value.
- Add more backend servers to handle the load.
- Increase the`maxConnections`setting.

### No Healthy Backend Servers

Error :

No healthy backends available in associated`backendSet`

Oracle Cloud Infrastructure log category : Error log

Symptoms :

The client fails with a 502 Bad Gateway error.

Possible causes :
- No backend servers in the backend set.
- No backend servers responding to health check.
- All health backend servers in the backend set have reached their`maxConnections`limit.

Possible solutions :
- Determine why backend servers aren't responding to health check.
- Check and adjust any health check settings, including status code, regular expressions, interval timeout, port, and protocol.
- Check if backend servers have a`maxConnections`limit set. If so, add more backend servers to handle the load or increase the`maxConnections`limit.

Troubleshooting documentation :[Testing TCP and HTTP Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Troubleshooting/../Reference/troubleshooting_backend.htm#TestTCPHTTPBackendServers)
