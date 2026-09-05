# Troubleshooting Load Balancer SSL Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_ssl.htm
- Fetched: 2026-09-05 01:40 CDT

# Troubleshooting Load Balancer SSL Issues

Learn about secure socket layer (SSL) issues associated with load balancers.

## SSL-Related Backend Server Health Check Failures

If the backend server health check fails because of the SSL error, it might be indicative of the backend server being is configured to accept SSL, but the health check protocol selected not matching that of the backend server.

If this behavior occurs, confirm that you're using non-TLS health check on a backend server that has TLS enabled.

See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/load_balancer_health_management.htm)for more information.

## SSL Handshake

If you experience SSL handshake failures in Oracle Cloud Infrastructure metrics, this might indicate an SSL handshake issue. Handshake issues can occur if the backend server isn't configured to accept SSL. See[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics.htm)for background information.

Possible solutions include:
- Confirming that the backend server certificate matches the certificate authority that's provided.
- Ensuring that all certificates in the chain are provided in the correct order in the Certificate field.
- Ensuring that you provide the correct certificate depth.

See the section on SSL handshake errors under[Common Load Balancer Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Troubleshooting/common_load_balancer_errors.htm)for more information.

## Backend Server SSL Handshake

If you receive a failure with a 502 Bad Gateway error, this might indicate a backend server SSL handshake issue. Possible causes for backend server SSL handshake issues can include:
- The backend server is not configured to accept SSL.
- The backend server certificate is invalid.

Possible solutions include:
- Confirming that the backend server certificate matches the certificate authority that is provided.
- Ensuring that all certificates in the chain are provided in the correct order in the Certificate field.
- Ensuring that you provide the correct certificate depth.

See the section on backend server SSL handshake errors under[Common Load Balancer Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Troubleshooting/common_load_balancer_errors.htm)for more information.

## SSL Certificate

If you experience an SSL handshake failure in Oracle Cloud Infrastructure metrics, it might be indicative of an SSL certificate issue. See[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics.htm)for background information.

Possible causes for SSL certificate issues can include:
- The client certificate is invalid.
- The client certificate isn't trusted.
- An invalid peer certification verify depth.

Possible solutions include:
- Ensuring that the client certificate is valid.
- Removing the Peer Cert Verify feature on the listener.

See the section on key pair mismatches under[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managingcertificates.htm)for more information.

## Client SSL Certificate

If you experience a 400 response error or no required SSL certificates appear in load balancer error logs, that might be indicative of a client SSL certificate issue. This error can result from the client not sending a client certificate.

Possible solutions include:
- Updating the client to send the correct client certificate.
- Removing the Peer Cert Verify feature on the listener.
- Adjusting the certificate verification depth.

See the section on configuring peer certificate verification under[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managingcertificates.htm)for more information.

## SSL Host Name Verification

If you receive a failure with a 502 Bad Gateway error, it might be indicative that the provided host name does not match what is expected.

Possible solutions include:
- Configuring the client to use the expected host name.
- Configuring the certificate to match the host name sent by the client.

See[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managingcertificates.htm)for more information.

## SSL Virtual Listener

If you can't create backend servers for an existing load balancer nor can you add new servers to the backend server created previously within the same load balancer, that is indicative of an SSL virtual listener issue.

A possible cause of SSL virtual listener issues is a mismatch of transport layer security (TLS) versions. If behavior occurs, match the TLS versions on the listeners.

See the section on virtual listener errors under[Common Load Balancer Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Troubleshooting/common_load_balancer_errors.htm)
