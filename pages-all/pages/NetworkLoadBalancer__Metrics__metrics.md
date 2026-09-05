# Network Load Balancer Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Metrics/metrics.htm
- Fetched: 2026-09-05 02:48 CDT

# Network Load Balancer Metrics

Use metrics to measure the number and type of connections, and quantity of data managed by your network load balancer.

Network Load Balancer service metrics help you monitor the number and type of connections, and quantity of traffic processed by your network load balancer. You can use metrics data to diagnose and troubleshoot network load balancer and client issues.

To view a default set of metrics charts in the Oracle Cloud Infrastructure Console, navigate to the network load balancer or backend set you're interested in, and then select Metrics .

You can use the Oracle Cloud Infrastructure Monitoring service to create custom queries. Use the information contained in this topic for setting up monitoring. See[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)for more information.

## Prerequisites

- IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
- 

The metrics listed on this page are automatically available for any load balancer, listener, and backend set you create. You do not need to enable monitoring on the resource to get these metrics.

## Available Metrics: oci_nlb

Network Load Balancer metrics include the following dimensions :
- RESOURCEID: The OCID of the network load balancer resource to which the metrics apply.
- RESOURCENAME: The display name of the network load balancer resource to which the metrics apply.

Metric Metric Display Name Unit Description
ProcessedBytes Processed Bytes by the NLB bytes The total number of bytes processed by the network load balancer, including TCP/IP headers.
ProcessedPackets Processed Packets by the NLB- count The total number of packets processed by the network load balancer.
IngressPacketsDroppedBySL Ingress Packets Dropped by Security List count The packets received from the network, destined for the network load balancer, dropped because of security rule violations.
EgressPacketsDroppedBySL Egress Packets Dropped by Security List count The packets sent by the network load balancer, destined for the network, dropped because of security rule violations.
NewConnections New Connections count The total number of new connections established between client and a backend server.
NewConnectionsTCP New TCP Connections count The total number of new TCP connections established between client and a backend server.
NewConnectionsUDP New UDP Connections count The total number of new UDP connections established between client and a backend server.
NLBVTAPReceivedPackets VTAP Packets Received by the NLB count The number of VTAP packets received by the network load balancer.
NLBVTAPReceivedBytes VTAP Bytes received by the NLB bytes The number of VTAP bytes received by the network load balancer.
NLBVTAPTransmittedPackets VTAP Packets Transmitted by the NLB count The number of VTAP packets transmitted by the network load balancer.
NLBVTAPTransmittedBytes VTAP Bytes Transmitted by the NLB bytes The number of VTAP bytes transmitted by the network load balancer.
NLBVTAPFwdDrops VTAP Packets Dropped by the NLB count The number of VTAP packets dropped by the network load balancer.
HealthyBackendsPerNlb Number of Healthy Backends for NLB count The number of healthy backend servers present in the network load balancer.
UnhealthyBackendsPerNlb Number of Unhealthy Backends for NLB count The number of unhealthy backend servers present in the network load balancer.

## Viewing Metrics

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Monitoring .
