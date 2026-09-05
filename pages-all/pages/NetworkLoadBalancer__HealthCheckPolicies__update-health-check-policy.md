# Editing Network Load Balancer Health Check Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/update-health-check-policy.htm
- Fetched: 2026-09-05 02:48 CDT

# Editing Network Load Balancer Health Check Policies

Update the health check policy for a network load balancer and backend set.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/update-health-check-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/update-health-check-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/update-health-check-policy.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- From the Actions menu for the backend set you want, select Update health check .
- Update any of the following:

- Protocol : Specify the protocol to use for health check queries:
- HTTP
- HTTPS
- TCP
- UDP
- DNS : For more information on how to configure your health check policies for the DNS protocol, see[DNS Health Checking](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/../HealthCheckPolicies/health-check-policy-management.htm#dns-health-checks).
Important  
  
Configure the health check protocol to match the application or service. For more information, see[Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/../HealthCheckPolicies/health-check-policy-management.htm).

For both TCP and UDP, the provided data must be base64 encoded. Use any base64 encoding tool to convert the plain text strings to based64 encoded strings, and use the encoded strings for the health check configuration. For example, the following plain text string:

`this is the request data for my NLB backend health check`

is encoded as:

`dGhpcyBpcyB0aGUgcmVxdWVzdCBkYXRhIGZvciBteSBOTEIgYmFja2VuZCBoZWFsdGggY2hlY2s`

The encoded string is what undergoes the health check configuration.

The supported maximum length of the string before base64 encoding is 1024 bytes. If the string exceeds the limit, the configuration call fails with an HTTP status code 400.
- Transport protocol : (DNS only) Specify the transport protocol used to send traffic when DNS is selected as the protocol:
- UDP
- TCP
- Port : Specify the backend server port against which to run the health check. You can enter the value '0' to have the health check use the backend server's traffic port.
- Interval in MS : Specify how often to run the health check, in milliseconds. The default is 10000 (10 seconds).
- Timeout in MS : Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
- Number of retries : Specify the number of retries to try before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is 3.
- Request Data : (Required for UDP, and optional for TCP only) Enter the request message included in the request. This request data is included in the single request to the backend server. The request data is compared against the response data
- Response Data : (Required for UDP, and optional for TCP only) Enter the response message against which the health check feature sends a single request to the backend server is compared. If a match, the health check passes.
- Status code : (HTTP and HTTPS only) Specify the status code a healthy backend server must return.
- URL path (URI) : (HTTP and HTTPS only) Specify a URL endpoint against which to run the health check.
- Response body (regular expression) : Provide a regular expression for parsing the response body from the backend server.
- Query name : (DNS only) Provide a DNS domain name for the query.
- Query class : (DNS only) Select from the following options:
- IN : Internet (default)
- CH : Chaos
- Query type : (DNS only) Select from the following options:
- A : Indicates a hostname corresponding IPv4 address. (default)
- AAAA : Indicates a hostname corresponding IPv6 address.
- TXT : Indicates a text field.
- Acceptable response codes : Select one or more from the following options:
- RCODE:0 NOERROR DNS query completed successfully.
- RCODE:2 SERVFAIL Server failed to complete the DNS request.
- RCODE:3 NXDOMAIN Domain name doesn't exist.
- RCODE:5 REFUSED The server refused to answer for the query.
- Fail open : (Optional) Select to have the network load balancer continue to move traffic to the backend servers in this backend set using the current configuration, even if all the backend servers' states becomes unhealthy.
- Enable instant failover : (Required for DNS, optional for all other protocols) Select to redirect existing traffic to a healthy backend server if the current backend server becomes unhealthy. This feature doesn't work if Fail open is enabled and all backend servers become unhealthy.
- Send TCP reset : (L3 IP listeners only) Select to automatically reset the TCP connection to a failed backend server.
- Select Save changes .
- 

Use the[oci nlb health-checker update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/health-checker/update.html)command and required parameters to edit the health check policies of a network load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateHealthChecker](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/HealthChecker/UpdateHealthChecker)
