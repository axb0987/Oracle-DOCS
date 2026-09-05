# Overview of Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm
- Fetched: 2026-09-05 01:39 CDT

# Overview of Load Balancer

Learn how Load Balancer provides automated traffic distribution from one entry point to multiple servers reachable from your virtual cloud network.

The Load Balancer service provides automated traffic distribution from one entry point to multiple servers reachable from your virtual cloud network (VCN). The service offers a load balancer with your choice of a public or private IP address, and provisioned bandwidth.
Note  
  

Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31621)to the Load Balancer service.

A load balancer improves resource utilization, facilitates scaling, and helps ensure high availability. You can configure multiple load balancing policies and application-specific health checks to ensure that the load balancer directs traffic only to healthy instances. The load balancer can reduce your maintenance window by draining traffic from an unhealthy application server before you remove it from service for maintenance.

This overview contains the following separate topics:

[Load Balancer Types](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/load_balancer_types.htm)

[Load Balancer Concepts](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview_topic-Load_Balancing_Concepts.htm)

[Load Balancer Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/lbpolicies.htm)

[Load Balancer Headers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/httpheaders.htm)

[Load Balancer Session Persistence](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/sessionpersistence.htm)

[Load Balancer Timeout Connection Settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/connectionreuse.htm)

You can also view topics on the following load balancer-related subjects:

[Load Balancer Management](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingloadbalancer.htm)

[Health Checks](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/load_balancer_health_management.htm)

[Backend Sets](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingbackendsets.htm)

[Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingbackendservers.htm)

[Listeners](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managinglisteners.htm)

[Cipher Suites](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingciphersuites.htm)

[Request Routing](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingrequest.htm)

[SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingcertificates.htm)

[Work Requests](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/viewingworkrequest.htm)

[Diagnosing Load Balancer Issues Using Smart Check](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/smart_check.htm)

[Logging](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingloadbalancer_topic-Logging.htm)

[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/loadbalancermetrics.htm)

[Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/troubleshooting_load_balancer.htm)

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Monitoring Resources

Use Monitoring to query metrics and manage alarms. Metrics and alarms help monitor the health, capacity, and performance of your cloud resources.

For information about monitoring the traffic passing through your load balancer, see[Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/loadbalancermetrics.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## Limits on Load Balancing Resources

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

Other limits include:
- You can't convert an AD-specific load balancer to a regional load balancer or the reverse.
- The maximum number of concurrent connections is limited when you use stateful security rules for your load balancer subnets. In contrast, no theoretical limit on concurrent connections exists if you use stateless security rules. The practical limitations depend on various factors. The larger your load balancer shape, the greater the connection capacity. Other considerations include system memory, TCP timeout periods, TCP connection state, and so forth.

Tip  
  
To accommodate high-volume traffic, we recommend that you use stateless security rules for your load balancer subnets. See[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)for more information.
- Each load balancer has the following configuration limits:
- One IPv4 address and one IPv6 address
- 16 backend sets
- 512 backend servers per backend set
- 512 backend servers total
- 16 listeners
- 16 virtual hostnames

## Required IAM Policies

For administrators: For a typical policy that gives access to load balancers and their components, see[Let network admins manage load balancers](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-load-balancers).

Also, be aware that a policy statement with`inspect load-balancers`gives the specified group the ability to see all information about the load balancers. For more information, see[Details for Load Balancing](https://docs.oracle.com/iaas/Content/Identity/policyreference/lbpolicyreference.htm).

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

## IPv6 Support

You can set up your load balancer to support IP version 6 (IPv6) in the following ways, depending on the IP address type:
- Ephemeral : Create your load balancer with the supplied`ipv6SubnetCidr`within the given subnet.
- Reserved : Create your load balancer using a pre-reserved IPV6 address that's created outside the Load Balancer service.
Note  
  
Load Balancer support for IPv6 doesn't include backend servers.

IPv6 is only supported on regional subnets. When an IPv6 subnet has several prefixes, only one prefix is used.
Private load balancers can be in either public or private subnets with the following configurations:
- Public subnet support includes the ULA prefix only.
- Private subnet support includes the Oracle-GUA, BYOIPv6-GUA, or ULA prefix. Public load balancers can be in only a public subnet with the following configurations:
- Public subnet support includes the Oracle-GUA or BYOIPv6-GUA prefix.

The following table shows what subnet types support IPv6:

IPv6 Support for Load Balancer
Visibility Type VCN Private Subnet VCN Public Subnet
Oracle GUA ULA BYOIPv6 Oracle GUA ULA BYOIPv6
Private Yes Yes Yes No Yes No
