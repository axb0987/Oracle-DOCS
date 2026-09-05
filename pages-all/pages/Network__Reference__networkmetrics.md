# Networking Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/networkmetrics.htm
- Fetched: 2026-09-05 02:42 CDT

# Networking Metrics

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

Monitoring service metric namespaces related to networking resources:

For instance connectivity
- oci_vcn: Metrics related to VNICs . See[VNIC Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm).

For cloud connectivity
- oci_dynamic_routing_gateway: Metrics related to Dynamic Routing Gateway (DRG) . See[DRG Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/drgmetrics.htm).
- oci_fastconnect: Metrics related to FastConnect . See[FastConnect Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fastconnectmetrics.htm).
- oci_internet_gateway: Metrics related to internet gateway . See[Internet Gateway Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/IGWmetrics.htm).
- oci_nat_gateway: Metrics related to a NAT gateway See[NAT Gateway Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/nat-gateway-metrics.htm).
- oci_service_gateway: Metrics related to a service gateway. See[Service Gateway Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/SGWmetrics.htm).
- oci_vpn: Metrics related to an IPSec connection . See[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics.htm).

For other service metrics related to network traffic management

- oci_lbaas: Metrics related to a load balancer . See[Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm).
- oci_nlb: Metrics related to a network load balancer . See[Network Load Balancer Metrics](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/Metrics/metrics.htm).
- oci_network_firewall: Metrics related to a network firewall . See[Monitoring Firewalls](https://docs.oracle.com/iaas/Content/network-firewall/metrics.htm).
- For oci_vcn and oci_nlb metrics related to VTAP s, see[VTAP Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vtapmetrics.htm).

Note  
  
No service level metrics exist for local peering gateways (LPGs). See[Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm)
