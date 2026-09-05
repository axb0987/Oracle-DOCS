# Load Balancer Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Metrics

Understand the metrics emitted by the Load Balancer service in the oci_lbaas metric namespace.

You can monitor the health, capacity, and performance of your load balancers by using metrics, alarms, and notifications. See[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)for general information on how to understand and use the various Oracle Cloud Infrastructure monitoring tools available to you.

Your load balancer acts as an intermediary for data traffic between clients and your application servers. Clients send requests to your load balancer and the load balancer distributes the requests to your backend servers according to rules you establish. See the diagram in[Overview of Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Concepts/balanceoverview.htm)for a high-level view of a simple public load balancing system configuration.

The Load Balancer service metrics help you measure the number and type of connections, and quantity of data managed by your load balancer. You can use metrics data to diagnose and troubleshoot load balancer and client issues. The metrics also help you analyze the HTTP responses returned by the servers in your backend set.

To view a default set of metrics charts in the Console, navigate to the load balancer or backend set you're interested in, and then select Metrics . You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

See[Viewing Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics_topic-Using_the_Console.htm)to view the available types of metrics for a load balancer.

The emit frequency of all Load Balancer service metrics is 60 seconds.

## Prerequisites

- IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
- The metrics listed on this page are automatically available for any load balancer, listener, and backend set you create. You don't need to enable monitoring on the resource to get these metrics.

## Available Metrics: oci_lbaas

Learn about the available metrics for a load balancer.

The Load Balancer service metrics include the following dimensions :

Dimension Description
`availabilityDomain`The availability domain in which the load balancer resides.
`backendSetName`The name of the backend set to which the metrics apply.
`lbComponent`The load balancer component to which the metrics apply.

Valid metrics for the Load Balancer service vary among the`lbComponent`dimension values:
- `backendSet`
- `listener`
- `loadBalancer`

The tables on this page describe which data is valid for each of these dimension values. If you select a metric that doesn't apply to the specified dimension value, the metric returns no data.
`lbHostId`A unique ID that represents the current load balancer host. This ID is subject to change.
`lbName`The name of the load balancer.
`listenerName`The name of the listener to which the metrics apply.
`region`The region in which the load balancer resides.
`resourceId`The OCID of the resource to which the metrics apply.

### Metrics for the lbComponent Dimension Value "Backendset"

Metric Metric Display Name Unit Description Dimensions
`activeConnections`Active Connections count The number of active connections from the load balancer to all backend servers.`availabilityDomain`

`backendSetName`

`lbComponent`

`lbHostId`

`lbName`

`region`

`resourceId`
`backendServers`Backend Servers count The number of backend servers in the backend set.
`backendTimeouts`Backend Timeouts count The number of timeouts across all backend servers.
`bytesReceived`Bytes Received bytes The number of bytes received across all backend servers.
`bytesSent`Bytes Sent bytes The number of bytes sent across all backend servers.
`closedConnections`Closed Connections count The number of connections closed between the load balancer and backend servers.
`httpRequests`Inbound Requests count The number of incoming client requests to the backend set.
`httpResponses`Responses count The number of HTTP responses across all backend servers.
`httpResponses200`HTTP 200 Responses count The number of HTTP 200 responses received from backend servers.
`httpResponses2xx`HTTP 2xx Responses count The number of HTTP 2xx responses received from backend servers.
`httpResponses3xx`HTTP 3xx Responses count The number of HTTP 3xx responses received from backend servers.
`httpResponses4xx`HTTP 4xx Responses count The number of HTTP 4xx responses received from backend servers.
`httpResponses502`HTTP 502 Responses count The number of HTTP 502 responses received from backend servers.
`httpResponses504`HTTP 504 Responses count The number of HTTP 504 responses received from backend servers.
`httpResponses5xx`HTTP 5xx Responses count The number of HTTP 5xx responses received from backend servers.
`invalidHeaderResponses`Invalid Header Responses count The number of invalid header responses across all backend servers.
`keepAliveConnections`Keep-alive Connections count The number of keep-alive connections.
`responseTimeFirstByte`Average Response Time (TCP only) ms Average time to the first byte of response from backend servers. TCP only.
`responseTimeHttpHeader`Average Response Time (HTTP only) ms Average response time of backend servers. HTTP only.
`unhealthyBackendServers`Unhealthy Backend Servers count The number of unhealthy backend servers in the backend set.

### Metrics for the lbComponent Dimension Value "Loadbalancer"

Metric Metric Display Name Unit Description Dimensions
`acceptedConnections`Accepted Connections count The number of connections accepted by the load balancer.

`availabilityDomain`

`lbComponent`

`lbHostId`

`lbName`

`region`

`resourceId`
`acceptedSSLHandshake`Accepted SSL Handshakes count The number of accepted SSL handshakes.
`activeConnections`Active Connections count The number of active connections from clients to the load balancer.
`activeSslConnections`Active SSL Connections count The number of active SSL connections.
`bytesReceived`Bytes Received bytes The number of bytes received by the load balancer.
`bytesSent`Bytes Sent bytes The number of bytes sent by the load balancer.
`failedSSLClientCertVerify`Failed Client SSL Cert Verifications count The number of failed client SSL certificate verifications.
`FailedSslHandshake`Failed SSL Handshakes count The number of failed SSL handshakes.
`handledConnections`Handled Connections count The number of connections handled by the load balancer.
`httpRequests`Inbound Requests count The number of incoming client requests to the load balancer.
`peakBandwidth`Peak Bandwidth bits Maximum bits per second bandwidth used during the specified interval. Use the default.

### Metrics for the lbComponent Dimension Value "Listener"

Metric Metric Display Name Unit Description Dimensions
`httpResponses 200`HTTP 200 Responses count The number of HTTP 200 responses received from backend sets.`availabilityDomain`

`lbComponent`

`lbHostId`

`lbName`

`listenerName`

`region`

`resourceId`
`httpResponses 2xx`HTTP 2xx Responses count The number of HTTP 2xx responses received from backend sets.
`httpResponses 3xx`HTTP 3xx Responses count The number of HTTP 3xx responses received from backend sets.
`httpResponses 4xx`HTTP 4xx Responses count The number of HTTP 4xx responses received from backend sets.
`httpResponses 502`HTTP 502 Responses count The number of HTTP 502 responses received from backend sets.
`httpResponses 504`HTTP 504 Responses count The number of HTTP 504 responses received from backend sets.
`httpResponses 5xx`HTTP 5xx Responses count The number of HTTP 5xx responses received from backend sets.
`httpResponses`
