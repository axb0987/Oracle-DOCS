# Network Security Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm
- Fetched: 2026-09-05 02:41 CDT

# Network Security Groups

The Networking service offers two virtual firewall features to control traffic at the packet level:
- Network security groups: Covered in this topic. Network security groups (NSGs) are supported only for[specific services](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#support).
- Security lists: The original type of virtual firewall offered by the Networking service. See[Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm).

Both of these features use security rules . For important information about how security rules work, and a general comparison of security lists and network security groups, see[Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm).
Note  
  
You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

## Highlights

- Network security groups (NSGs) act as a virtual firewall for Compute instances and[other kinds of resources](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison). An NSG consists of a set of ingress and egress[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)that apply only to a set of VNICs in a single VCN (for example: all the Compute instances that act as web servers in the web tier of a multitier application in a VCN).
- Compared to security lists, NSGs let you separate a VCN's subnet architecture from the application security requirements. See[Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
- You can use NSGs with certain resource types. For more information, see[Support for Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#support).
- NSG security rules function the same as security list rules. However, for an NSG security rule's source (for ingress rules) or destination (for egress rules), you can specify an NSG instead of a CIDR. This means you can easily write security rules to control traffic between two NSGs in the same VCN , or traffic within a single NSG. See[Parts of a Security Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).
- Unlike with security lists, the VCN doesn't have a default NSG. Also, each NSG you create is initially empty. It has no default security rules.
- Network security groups have separate and different limits compared to security lists. See[Security List Limits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#sec_list_limits).

## Support for Network Security Groups

NSGs are available for you to create and use. However, they're not yet supported by all the relevant Oracle Cloud Infrastructure services.

The following types of[parent resources](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison)support the use of NSGs:
- Autonomous Recovery Service (Subnets for Recovery Service): When you[register a Recovery Service subnet](https://docs.oracle.com/iaas/recovery-service/doc/register-recovery-subnet.html), you can associate one or more NSGs (maximum five) that contain the ingress rules for Recovery Service.
- Compute instances: When you create an instance, you can specify one or more NSGs for the instance's primary VNIC. If you add a secondary VNIC to an instance, you can specify one or more NSGs for that VNIC. You can also update existing VNICs on an instance so that they're in one or more NSGs.
- Load balancers: When you create a Load Balancer, you can specify one or more NSGs for the Load Balancer (not the backend set). You can also update an existing Load Balancer to use one or more NSGs.
- DB systems: When you create a DB system, you can specify one or more NSGs. You can also update an existing DB system to use one or more NSGs.
- Autonomous AI Databases: When you create an Autonomous AI Database on dedicated Exadata infrastructure, you can specify one or more NSGs for the infrastructure resource.
- Mount targets: When you create a mount target for a file system, you can specify one or more NSGs. You can also update an existing mount target to use one or more NSGs.
- DNS resolver endpoint: When you create an endpoint for a[private DNS resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm), you can specify one or more NSGs. You can also update an existing endpoint to use one or more NSGs.
- Kubernetes clusters: When you[create a Kubernetes cluster](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)using Kubernetes Engine, you can specify one or more NSGs to control access to the Kubernetes API endpoint and to worker nodes. You can also specify NSGs when[defining a load balancer for a cluster](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Network_Security_Group).
- API gateways: When you[create an API gateway](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm), you can specify one or more NSGs to control access to the API gateway.
- Functions: When you[set up an application](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsusingnsgs.htm)in OCI Functions, you can specify one or more NSGs to define ingress and egress rules that apply to all the functions in that particular application.
- GoldenGate deployments: When you[create a GoldenGate deployment](https://docs.oracle.com/en/cloud/paas/goldengate-service/llyhq/#GUID-899C1348-58CA-43EE-B775-EAD3B365A7A9), you can specify one or more NSGs to control access to the deployment.
- Redis clusters: When you[create a Redis cluster](https://docs.oracle.com/iaas/Content/ocicache/createcluster.htm), you can specify one or more NSGs to control access to the Redis cluster. You can also update an existing cluster to use one or more NSGs

For resource types that don't yet support NSGs, continue to use security lists to control traffic in and out of those parent resources.

## Overview of Network Security Groups

A network security group (NSG) provides a virtual firewall for a set of cloud resources that all have the same security posture. For example: a group of Compute instances that all perform the same tasks and thus all need to use the same set of ports.

An NSG consists of two types of items:
- VNICs: One or more[VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingVNICs.htm)(for example, the VNICs attached to the set of Compute instances that all have the same security posture). All the VNICs must be in the same VCN as the NSG. Also see[Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
- Security rules: The NSG's[Security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)define the types of traffic allowed in and out of the VNICs in the group. For example: ingress TCP port 22 SSH traffic from a particular source.

If you have resources with different security postures in the same VCN , you can write NSG security rules to control traffic between the resources with one posture compared to another. For example, in the following diagram, NSG1 has VNICs running in one tier of a multitier architecture application. NSG2 has VNICs running in a second tier. Both NSGs must belong to the same VCN. The assumption is that both NSGs need to start connections to the other NSG.

For NSG1, you set up egress security rules that specify NSG2 as the destination, and ingress security rules that specify NSG2 as the source. Likewise for NSG2, you set up egress security rules that specify NSG1 as the destination, and ingress security rules that specify NSG1 as the source. The rules are assumed to be[stateful](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful)in this example.
[

The preceding diagram assumes that each NSG needs to start connections to the other NSG.

The next diagram assumes that you instead want to only allow connections started from NSG1 to NSG2. To do that, remove the ingress rule from NSG1 and the egress rule from NSG2. The remaining rules don't allow connections started from NSG2 to NSG1.
[

The next diagram assumes that you want to control traffic between VNICs in the same NSG . To do that, set the rule's source (for ingress) or destination (for egress) as the rule's own NSG.
[

A VNIC can be in a maximum of five NSGs. A packet in question is allowed if any rule in any of the VNIC's NSGs allows the traffic (or if the traffic is part of an existing connection being tracked), unless the lists happen to contain both stateful and stateless security rules that cover the same traffic. For more information, see[Stateful Compared to Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).

Network security groups are regional entities. For limits related to network security groups, see[Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).

See[Network Security Group Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#nsg_limits)and[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)for limits-related information.

## Security Rules

If you're not yet familiar with the basics of NSG security rules, see these sections in the security rules topic:
- [Parts of a Security Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts)
- [Stateful Compared to Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful)

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Some differences in the REST API model for NSGs compared to security lists:
- Security lists have an`IngressSecurityRule`object and a separate`EgressSecurityRule`object. Network security groups only have a`SecurityRule`object, and the object's`direction`attribute shows whether the rule is for ingress or egress traffic.
- With security lists, the rules are part of the`SecurityList`object, and you work with the rules by calling the security list operations (such as`UpdateSecurityList`). With NSGs, the rules aren't part of the`NetworkSecurityGroup`object. Instead you use separate operations to work with the rules for a particular NSG (example:`UpdateNetworkSecurityGroupSecurityRules`).
- The model for updating existing security rules is different between security lists and NSGs. With NSGs, each rule in a particular group has a unique Oracle-assigned identifier (example: 04ABEC). When you call`UpdateNetworkSecurityGroupSecurityRules`, you provide the IDs of the specific rules that you want to update. For comparison, with security lists, the rules have no unique identifier. When you call`UpdateSecurityList`, you must pass in the entire list of rules, including rules that aren't being updated in the call.
- Security rules a limit of 25 rules when calling the operations to add, remove, or update.

## Working with Network Security Groups

### General Process for Working with NSGs
- Create an NSG.
- Add security rules to the NSG.
- Add parent resources (such as VNICs) to the NSG. You can do this when you create the parent resource, or you can update the parent resource and add it to one or more NSGs. When you create a Compute instance and add it to an NSG, the instance's primary VNIC is added to the NSG. Separately, you can create secondary VNICs and optionally add them to NSGs.

### Deleting NSGs

To[delete an NSG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/delete_nsg.htm), it must not contain any VNICs or parent resources. When a parent resource (or a Compute instance VNIC) is deleted, it's automatically removed from the NSGs it was in. You might not have permission to delete a particular parent resource. Contact the tenancy administrator to find who owns a particular resource.

### Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)covers management of all Networking components, including NSGs.

If you have security admins who need to manage NSGs but not other components in the Networking service, you could write a more restrictive policy:

```

```

The first statement lets the NSGAdmins group create and manage NSGs and their security rules.

The second statement is required because the creation or deletion of an NSG affects the VCN that the NSG is in. The statement restricts the VCN-related permissions to only those required to create or delete an NSG. The statement doesn't allow the NSGAdmins group to create or delete VCNs, or work with any resources in a VCN except NSGs.

The third statement is required for listing the VCNs, which is a prerequisite for creating or deleting an NSG in a VCN. For information about why both the second and third statements are required, see[Conditions](https://docs.oracle.com/iaas/Content/Identity/policiesadvfeatures/policyadvancedfeatures.htm#conditions).

The fourth statement is required if the NSGAdmins need to put VNICs into an NSG. Whoever creates the parent resource of the VNIC (for example, a Compute instance) must already have this level of permission to create the parent resource.

For more information about Networking service policies, see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Policies)
