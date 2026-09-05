# Configuring Load Balancers and Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm
- Fetched: 2026-09-05 01:54 CDT

# Configuring Load Balancers and Network Load Balancers

Find out how to define the Oracle Cloud Infrastructure load balancers and network load balancers that Kubernetes Engine (OKE) provisions for a Kubernetes service of type LoadBalancer.

## Creating Internal Load Balancers

You can create Oracle Cloud Infrastructure load balancers and network load balancers to control access to services running on a cluster:
- When you create a cluster in the 'Custom Create' workflow you select an existing VCN that contains the network resources to be used by the new cluster. If you want to use a load balancer or network load balancer to control traffic into the VCN, you select an existing public or private subnet in that VCN to host it.
- When you create a cluster in the 'Quick Create' workflow, the VCN that's automatically created contains a public regional subnet to host a load balancer or network load balancer. If you want to host a load balancer or a network load balancer in a private subnet, you can add a private subnet to the VCN later.

Alternatively, you can define an internal Kubernetes service of type LoadBalancer (often referred to simply as an 'internal load balancer') in a cluster to enable other programs running in the same VCN as the cluster to access services in the cluster. An internal load balancer can be provisioned:
- as a load balancer, or as a network load balancer
- with a public IP address, or with a private IP address (assigned by the Load Balancer service or the Network Load Balancer service)
- in a public subnet, or in a private subnet

A load balancer or network load balancer with a public IP address is referred to as public. A public load balancer or network load balancer can be hosted in a public subnet or in a private subnet.

A load balancer or network load balancer with a private IP address is referred to as private. A private load balancer or network load balancer can be hosted in a public subnet or in a private subnet.

By default, internal load balancers are provisioned with public IP addresses and hosted in public subnets.

For more information:
- about Oracle Cloud Infrastructure public and private load balancers, see[Load Balancer Types](https://docs.oracle.com/iaas/Content/Balance/Concepts/load_balancer_types.htm).
- about Oracle Cloud Infrastructure public and private network load balancers, see[Network Load Balancer Types](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#NetworkLoadBalancerTypes)

[Create an internal load balancer as an OCI load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To create an internal load balancer as an OCI load balancer with a private IP address, hosted on the subnet specified for load balancers when the cluster was created, add the following annotation in the metadata section of the manifest file:

```

```

To create an internal load balancer as an OCI load balancer with a private IP address hosted, hosted on an alternative subnet to the one specified for load balancers when the cluster was created, add both the following annotations in the metadata section of the manifest file:

```

```

```

```

where`ocid1.subnet.oc1..aaaaaa....vdfw`is the OCID of the alternative subnet. The alternative subnet can be a private subnet or a public subnet.

For example:

```

```

[Create an internal network load balancer as an OCI network load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To create an internal network load balancer as an OCI network load balancer with a private IP address, hosted on the subnet specified for load balancers when the cluster was created, add the following annotation in the metadata section of the manifest file:

```

```

To create an internal network load balancer as an OCI network load balancer with a private IP address, hosted on an alternative subnet to the one specified for load balancers when the cluster was created, add both of the following annotations in the metadata section of the manifest file:

```

```

```

```

where`ocid1.subnet.oc1..aaaaaa....vdfw`is the OCID of the private subnet. The alternative subnet can be a private subnet or a public subnet.

For example:

```

```

## Specifying Reserved Public IP Addresses

When a Kubernetes service of type LoadBalancer is deployed on a cluster, Kubernetes Engine creates an Oracle Cloud Infrastructure public load balancer or network load balancer to accept traffic into the cluster. By default, the Oracle Cloud Infrastructure public load balancer or network load balancer is assigned an ephemeral public IP address. However, an ephemeral public IP address is temporary, and only lasts for the lifetime of the public load balancer or network load balancer.

If you want the Oracle Cloud Infrastructure public load balancer or network load balancer that Kubernetes Engine creates to have the same public IP address deployment after deployment, you can assign it a reserved public IP address. You can assign:
- a reserved public IPv4 address to a load balancer or network load balancer
- a reserved public IPv4 address and reserved public IPv6 address to a load balancer

You can assign reserved public IP addresses in the following ways:
- [Method 1: Using the oci.oraclecloud.com/reserved-ips annotation (recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Reserved_IP__section_reserved-ipv4-address-annotation). Use this method to assign a reserved public IPv4 address, or to assign a reserved public IPv4 address and a reserved public IPv6 address to a load balancer.
- [Method 2: Using the spec.loadBalancerIP field](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Reserved_IP__section_reserved-ipv4-address-loadbalancerip-field). Use this method only to assign a reserved public IPv4 address.

In clusters running Kubernetes version 1.32 and later, reserved public IPv6 addresses are supported only for Oracle Cloud Infrastructure load balancers, and only when you use the`oci.oraclecloud.com/reserved-ips`annotation. To assign a reserved public IPv6 address to a load balancer, the cluster and the subnet in which the load balancer is created must support IPv6. The service manifest must also specify both IPv6 and IPv4 address families. Reserved public IPv6 addresses are not supported for network load balancers, and are not supported with the`spec.loadBalancerIP`field.
Note  
  

In earlier releases of Kubernetes Engine (supporting clusters running Kubernetes versions prior to version 1.30), you could use the`spec.loadBalancerIP`field to specify IPv4 reserved public IP addresses. Although the`spec.loadBalancerIP`field is still supported for clusters running Kubernetes version 1.30 and later, it will be deprecated in a future release. For this reason, Oracle recommends that you use the`oci.oraclecloud.com/reserved-ips`annotation in new configurations, instead of the`spec.loadBalancerIP`field. To assign a reserved public IPv6 address to a load balancer, you must use the`oci.oraclecloud.com/reserved-ips`annotation and specify the reserved public IPv4 and IPv6 addresses as a comma-separated list.

### Method 1: Using the oci.oraclecloud.com/reserved-ips annotation (recommended)

For load balancers and network load balancers, you can assign a reserved public IPv4 address by adding the following annotation in the metadata section of the service manifest:
```

```

where`"<reserved_ipv4_address>`" is the string value of the reserved public IPv4 address (for example,`"203.0.113.10"`).

For load balancers, in clusters running Kubernetes version 1.32 and later, you can also assign a reserved public IPv4 address and a reserved public IPv6 address by specifying the addresses as a comma-separated list:
```

```

where:
- `<reserved_ipv4_address>`is the string value of the reserved public IPv4 address.
- `<reserved_ipv6_address>`is the string value of the reserved public IPv6 address.

When specifying reserved public IPv4 and IPv6 addresses:
- The cluster and the subnet in which the load balancer is created must support IPv6.
- The reserved public IPv6 address must belong to the same subnet in which the load balancer is created.
- The service must be configured to use both IPv6 and IPv4 address families.
- You can specify the reserved public IPv4 and IPv6 addresses in any order in the annotation.

[Assign a reserved public IPv4 address to a load balancer using the annotation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

[Assign reserved public IPv4 and IPv6 addresses to a load balancer using the annotation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

For more information about using`spec.ipFamilyPolicy`and`spec.ipFamilies`to configure IPv4 and IPv6 addresses for load balancers, see[Specifying IP Address Families for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_IPAddressfamily).

[Assign a reserved public IPv4 address to a network load balancer using the annotation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

Reserved public IPv6 addresses are not supported for network load balancers. For network load balancers, use this annotation only to specify reserved public IPv4 addresses.

### Method 2: Using the spec.loadBalancerIP field

You can assign a reserved public IPv4 address by adding the`loadBalancerIP`property in the`spec`section of the service manifest and specifying the reserved public IPv4 address value. You cannot use the`spec.loadBalancerIP`field to assign a reserved public IPv6 address. To assign reserved public IPv4 and IPv6 addresses to a load balancer, use[Method 1: Using the oci.oraclecloud.com/reserved-ips annotation (recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Reserved_IP__section_reserved-ipv4-address-annotation).

[Assign a reserved public IPv4 address to a load balancer using the loadBalancerIP property](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

[Assign a reserved public IPv4 address to a network load balancer using the loadBalancerIP property](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

### Notes
- Annotation takes precedence: If you specify both the`oci.oraclecloud.com/reserved-ips`annotation and the`spec.loadBalancerIP`property in the same manifest, the annotation takes precedence.
- Address family support: With Method 1, you can specify a reserved public IPv4 address for a load balancer or network load balancer. For load balancers only, you can also specify a reserved public IPv4 address and a reserved public IPv6 address as a comma-separated list. With Method 2, only reserved public IPv4 addresses are supported.
- Reserved IPv6 support: In clusters running Kubernetes version 1.32 and later, reserved public IPv6 addresses are supported only for load balancers. Reserved public IPv6 addresses are not supported for network load balancers. If load balancer creation fails after you specify a reserved public IPv6 address, verify that the IPv6 address is reserved, available for use, and belongs to the subnet in which the load balancer is created.
- Subnet requirement for reserved IPv6: The reserved public IPv6 address must belong to the same subnet in which the load balancer is created. If you use the`service.beta.kubernetes.io/oci-load-balancer-subnet1`annotation to specify an alternative subnet, the reserved public IPv6 address must belong to that alternative subnet.
- Service IP address family requirement: To assign a reserved public IPv6 address to a load balancer, specify the IP address family fields in the service manifest. For example:
```

```

- Single assignment: With Method 2, you can specify only a single reserved public IPv4 address. With Method 1, specify either a single reserved public IPv4 address, or for load balancers only, a comma-separated reserved public IPv4 address and reserved public IPv6 address.
- Change of address: With both methods, you cannot later directly change the IP address of the load balancer or network load balancer that Kubernetes Engine creates. To change the IP address, delete the service of type LoadBalancer, update the manifest with the new address, and redeploy.
- Switching from ephemeral to reserved: If you do not set a reserved public IP address initially, you cannot later switch from an ephemeral to a reserved IP address without deleting and recreating the service of type LoadBalancer.
- Exclusivity: You must not assign a reserved public IP address that is already in use by another resource (such as a compute instance or another service of type LoadBalancer).
- Internal services: You cannot specify a reserved public IP address for an internal load balancer service (that is, a service with a manifest file that includes the`service.beta.kubernetes.io/oci-load-balancer-internal: "true"`or`oci-network-load-balancer.oraclecloud.com/internal: "true"`annotation).
- 

Compartments: With both methods, by default, the reserved public IP address is expected to be a resource in the same compartment as the cluster. If you want to specify a reserved public IP address in a different compartment, add the required IAM policies:
- 

For public load balancers, add the following policy to the tenancy:

```

```

When assigning a reserved public IPv6 addresses to a load balancer, the cluster requires permission to use IPv6 resources in the compartment that contains the reserved public IPv6 address. For example:
```

```

- 

For network load balancers, add the following policy to the tenancy:

```

```

## Specifying Reserved Private IP Addresses

When a Kubernetes service of type`LoadBalancer`is deployed on a cluster as an internal load balancer or internal network load balancer, Kubernetes Engine creates an Oracle Cloud Infrastructure private load balancer or private network load balancer to accept traffic into the cluster. By default, the Oracle Cloud Infrastructure private load balancer or private network load balancer is assigned a private IP address from the subnet used for load balancers.

If you want the Oracle Cloud Infrastructure private load balancer or private network load balancer that Kubernetes Engine creates to have the same private IP address deployment after deployment, you can assign it a reserved private IPv4 address. Reserved private IPv4 addresses are supported in clusters running Kubernetes version 1.32 and later. For more information about creating and viewing reserved private IPv4 addresses, see[Private IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm).

You assign a reserved private IPv4 address by adding the following annotation in the metadata section of the service manifest.
```

```

where`<reserved_private_ipv4_address>`is the string value of the reserved private IPv4 address.

[Assign a reserved private IP address to a load balancer using the annotation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

[Assign a reserved private IP address to a network load balancer using the annotation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

```

```

### Notes
- Internal services only: You can specify a reserved private IPv4 address only for an internal load balancer or internal network load balancer. To create an internal load balancer or internal network load balancer, include the appropriate internal annotation in the manifest file.
- IPv4 only: Only reserved private IPv4 addresses are supported. Specifying an IPv6 address, a public IP address, or a private IPv4 address that has not been reserved might cause load balancer or network load balancer creation to fail.
- Same subnet: The reserved private IPv4 address must be in the subnet used by the load balancer or network load balancer. If you specify an alternative subnet for the load balancer or network load balancer, the reserved private IPv4 address must be in that alternative subnet.
- Single assignment: You can specify only one reserved private IPv4 address. If you specify multiple reserved private IPv4 addresses, or an IPv4 address in an invalid format, creating or updating the load balancer or network load balancer might fail.
- Change of address: You cannot later directly change the IP address of the load balancer or network load balancer thatKubernetes Engine creates. To change the IP address, delete the service of type`LoadBalancer`, update the manifest with the new address, and redeploy.
- Switching from automatically assigned to reserved: If you do not set a reserved private IPv4 address initially, you cannot later switch from an automatically assigned private IP address to a reserved private IP address without deleting and recreating the service of type`LoadBalancer`.
- Exclusivity: You must not specify a reserved private IPv4 address that is already assigned to another resource.

## Specifying Network Security Groups (recommended)

Oracle Cloud Infrastructure network security groups (NSGs) enable you to control traffic into and out of resources, and between resources. The security rules defined for an NSG ensure that all the resources in that NSG have the same security posture. For more information, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).

You can use NSGs to control access to the Oracle Cloud Infrastructure load balancer or network load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer.

When using NSGs to control access, appropriate security rules must exist to allow inbound and outbound traffic to and from the load balancer's or network load balancer's subnet. See[Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).

If you decide to use NSGs to control access to load balancers or network load balancers:
- You can have the NSGs and security rules entirely managed for you by the oci-cloud-controller-manager (see[Specifying Security Rule Management Options for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Options)).
- You can manage the NSGs and security rules yourself, and add the load balancer or network load balancer to the existing NSGs (as described in this section).
- You can have the oci-cloud-controller-manager manage some security rules in one NSG, whilst you manage other security rules in a different NSG.

To control access using an NSG that you manage, you include annotations in the manifest file to specify the NSG to which you want to add the load balancer or network load balancer.

[Add a load balancer to an existing NSG](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To add the Oracle Cloud Infrastructure load balancer created by Kubernetes Engine to an NSG that you manage, add the following annotation in the metadata section of the manifest file:

```

```

where`<nsg-ocid>`is the OCID of an existing NSG.

For example:

```

```

[Add a network load balancer to an existing NSG](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To add the Oracle Cloud Infrastructure network load balancer created by Kubernetes Engine to an NSG that you manage, add the following annotation in the metadata section of the manifest file:

```

```

where`<nsg-ocid>`is the OCID of an existing NSG.

For example:

```

```

Note the following:
- The NSG you specify must be in the same VCN as the Oracle Cloud Infrastructure load balancer or network load balancer.
- If the NSG you specify belongs to a different compartment to the cluster, you must include a policy statement similar to the following in an IAM policy:
```

```

If you consider this policy statement to be too permissive, you can restrict the permission to explicitly specify the compartment to which the NSG belongs, and/or to explicitly specify the cluster. For example:
```

```

- You can specify up to five NSGs, in a comma-separated list, in the format:

```

```

- To remove a load balancer or network load balancer from an NSG, or to change the NSG that the load balancer or network load balancer is in, update the annotation and re-apply the manifest.
- 

If you decide to control access to an Oracle Cloud Infrastructure load balancer or network load balancer using an NSG that you manage, Oracle recommends that you disable Kubernetes security list management by adding one of the following annotations in the metadata section of the manifest file for the load balancer or network load balancer respectively:

```

```

```

```

Alternatively, you can add the following equivalent annotation:
```

```

If you do follow the recommendation and add the annotation, Kubernetes security list management is not enabled. You have to set up NSGs with ingress and egress security rules for node pools and for the Kubernetes API endpoint (for more information, see[Security Rule Configuration in Network Security Groups and/or Security Lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig)and[Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfigexample.htm)). You also have to set up NSGs with ingress and egress security rules for the kube-proxy health port, for the health check port range, and for load balancers.

## Specifying Security Rule Management Options for Load Balancers and Network Load Balancers

Security rules control access to the Oracle Cloud Infrastructure load balancers and network load balancers that are provisioned for Kubernetes services of type LoadBalancer. The security rules can be managed (that is, created, updated, and deleted) in the following ways:
- In a network security group, or NSG (recommended) The security rules in an NSG apply to any Kubernetes resource added to the NSG. As such, NSGs can provide fine-grained access control to individual resources.
- In a security list. The security rules in a security list apply to all the Kubernetes resources in a subnet. Security lists don't provide fine-grained access control to individual resources in the subnet.

For important information about how security rules work, and a general comparison of security lists and network security groups, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm#rules).
Note  
  

If security rules are managed in security lists, security configuration and management can become complicated when the infrastructure is complex and when using tools like Terraform. Also note that the ability to use security lists to manage security rules will be deprecated in a future release. For these reasons, Oracle recommends the use of network security groups (NSGs) and the`oci.oraclecloud.com/security-rule-management-mode`annotation to manage security rules.

You can manage the security rules yourself, creating, updating, and deleting rules as required. Alternatively, you can specify that the oci-cloud-controller-manager (which runs on the cluster control plane) is to manage some, or all, of the security rules for you. Kubernetes Engine uses the oci-cloud-controller-manager to provision load balancers and network load balancers for Kubernetes services of type LoadBalancer.

You use different annotations to specify whether the oci-cloud-controller-manager manages security rules for a load balancer or network load balancer in an NSG or in a security list, as follows:
- 

To manage security rules in an NSG, use the`oci.oraclecloud.com/security-rule-management-mode: "NSG"`annotation (recommended).

If you want the oci-cloud-controller-manager to manage security rules in an NSG (as recommended by Oracle), you must use the`oci.oraclecloud.com/security-rule-management-mode: "NSG"`annotation. For more information about using this annotation, see[Using the oci.oraclecloud.com/security-rule-management-mode annotation to manage security rules in NSGs and security lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation).
- 

To manage security rules in a security list, use either the`oci.oraclecloud.com/security-rule-management-mode`annotation, or use the`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`and`oci-network-load-balancer.oraclecloud.com/security-list-management-mode`annotations.

If you want the oci-cloud-controller-manager to manage security rules in the security list of a load balancer or network load balancer's subnet, do one of the following:
- Use the`oci.oraclecloud.com/security-rule-management-mode`annotation, set to`"SL-All"`or`"SL-Frontend"`. For more information about using this annotation, see[Using the oci.oraclecloud.com/security-rule-management-mode annotation to manage security rules in NSGs and security lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation).
- Use the`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`and`oci-network-load-balancer.oraclecloud.com/security-list-management-mode`annotations respectively, set to`"All"`or`"Frontend"`. For more information about using these two annotations, see[Specifying Security List Management Options When Provisioning an OCI Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#listmgmt)and[Specifying Security List Management Options When Provisioning an OCI Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingloadbalancer_topic_Specifying_Network_Load_Balancer_Security_List_Management_Options)respectively.

Regardless of the annotations you use, and regardless of whether you or the oci-cloud-controller-manager manages security rules in a security list or in an NSG, you can also specify the OCID of one or more additional NSGs to which you want the oci-cloud-controller-manager to add the load balancer or network load balancer. In this case, you use the`oci.oraclecloud.com/oci-network-security-groups`or`oci-network-load-balancer.oraclecloud.com/oci-network-security-groups`annotation. Note that the oci-cloud-controller-manager does not manage the security rules in the additional NSGs specified by these annotations, so it is your responsibility to manage the security rules. For more information about using the`oci.oraclecloud.com/oci-network-security-groups`or`oci-network-load-balancer.oraclecloud.com/oci-network-security-groups`annotations, see[Specifying Network Security Groups (recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Network_Security_Group).

### Using the`oci.oraclecloud.com/security-rule-management-mode`annotation to manage security rules in NSGs and security lists

#### Required IAM Policies for Managing Security Rules in NSGs

To enable the oci-cloud-controller-manager to manage the security rules for a cluster's load balancer in NSGs, you must give the cluster permission to manage NSGs. For example, to grant this permission in a particular compartment:
```

```

In addition, to enable the oci-cloud-controller-manager to create a network security group, you must also give the cluster permission to manage VCNs or to manage virtual network families. For example, by specifying one or other of the following policy statements:
- `ALLOW any-user to manage vcns in compartment <compartment-name> where request.principal.type = 'cluster'`
- `ALLOW any-user to manage virtual-network-family in compartment <compartment-name> where request.principal.type = 'cluster'`

#### Using the`oci.oraclecloud.com/security-rule-management-mode`annotation

To specify that the oci-cloud-controller-manager is to manage security rules for a load balancer or network load balancer in an NSG (as recommended by Oracle), you must first set up the necessary IAM policies. See[Required IAM Policies for Managing Security Rules in NSGs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation__section_required-iam-policies-for-nsgs). Having set up the prerequisite IAM policies, you can then add the following annotation in the metadata section of the manifest file:

```

```

The oci-cloud-controller-manager manages all required security rules for ingress to the load balancer or network load balancer service, in an NSG that the oci-cloud-controller-manager creates for the purpose. This NSG is known as the frontend NSG, and allows inbound traffic to the load balancer or network load balancer from 0.0.0.0/0, or from the source CIDR block (and on the source port range) if specified in the manifest file. The oci-cloud-controller-manager creates the following security rules in the frontend NSG:

Direction Source Protocol/Dest. Port Description
Ingress 0.0.0.0/0 (or source CIDR block if specified in the manifest file) Ports specified in the manifest file. Allow inbound traffic to OCI load balancer.
Egress Backend NSG (if the OCID of a backend NSG is specified in the manifest file) ALL/(Nodeports for service) Allow traffic to worker nodes.
Egress Backend NSG (if the OCID of a backend NSG is specified in the manifest file) TCP/ health check port (10256)

If source IP address is preserved, health check port is automatically picked by the service. Allow OCI load balancer or network load balancer to communicate with kube-proxy on worker nodes for health check port.

If you want the oci-cloud-controller-manager to manage security rules for ingress traffic to the worker nodes in the backend set, along with egress traffic from the load balancer or network load balancer service, you have to specify the OCID of an existing NSG to use for that purpose. This NSG is known as the backend NSG. The oci-cloud-controller-manager only adds egress rules to the frontend NSG if you specify a backend NSG. To specify the NSG to use as the backend NSG, add the following annotation in the metadata section of the manifest file:

```

```

where &lt;nsg-ocid&gt; is the OCID of an existing NSG that is both in the same VCN as the cluster, and also an NSG to which the compute instances hosting worker nodes have already been added. For example:

```

```

You can specify the OCIDs of multiple backend NSGs in a comma-delimited list. For example:

```

```

Note that the compute instances hosting the worker nodes in the backend set must have already been added to the backend NSG that you specify as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation. You can add the compute instances to the backend NSG in one of the following ways:
- By specifying the NSG when creating a node pool (in the case of managed nodes and virtual nodes).
- By manually adding the primary VNICs of the compute instances hosting the worker nodes to the NSG using the Compute service (in the case of managed nodes). For example, by using the Compute service's Console pages (or the Compute service's CLI or API).

The oci-cloud-controller-manager creates the following security rules in the backend NSG:

Direction Source Protocol/Dest. Port Description
Ingress Frontend NSG OCID TCP/ health check port (10256)

If source IP address is preserved, health check port is automatically picked by the service. Allow OCI load balancer or network load balancer to communicate with kube-proxy on worker nodes for health checks.
Ingress Frontend NSG OCID ALL/(Nodeports for service) Allow OCI load balancer or network load balancer to communicate with worker nodes.

If you do not specify an OCID for the backend NSG, the oci-cloud-controller-manager does not manage either the security rules for ingress traffic to the worker nodes in the backend set, or the security rules for egress traffic from the load balancer or network load balancer.

You can also set the`oci.oraclecloud.com/security-rule-management-mode`annotation to other values to specify that you want to manage security rules yourself, or you want the oci-cloud-controller-manager to manage security rules in security lists. The complete syntax for the annotation is as follows:

```

```

where`<value>`is one of:
- `"NSG"`: (recommended) The oci-cloud-controller-manager manages all required security rules for ingress to the load balancer or network load balancer service, in a network security group (NSG) that it creates for that purpose.
- `"None"`: (default for network load balancers) No security list management is enabled, and the oci-cloud-controller-manager does not manage security rules. It is your responsibility to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. Additionally, you have to set up security rules to allow inbound traffic to load balancers and network load balancers (see[Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers)). This is equivalent to setting`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`or`oci-network-load-balancer.oraclecloud.com/security-list-management-mode`to`"None"`.
- `"SL-All"`: (default for load balancers) The oci-cloud-controller-manager manages all required security rules for ingress and egress to and from the load balancer or network load balancer service, in a security list. This is equivalent to setting`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`or`oci-network-load-balancer.oraclecloud.com/security-list-management-mode`to`"All"`.
- `"SL-Frontend"`: The oci-cloud-controller-manager only manages security rules for ingress to load balancer and network load balancer services, in a security list. It is your responsibility to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. This is equivalent to setting`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`or`oci-network-load-balancer.oraclecloud.com/security-list-management-mode`to`"Frontend"`.

In clusters with managed nodes, if you don't explicitly specify a management mode or you specify an invalid value, the oci-cloud-controller-manager manages all required security rules for ingress and egress to and from the load balancer or network load balancer service, in a security list (equivalent to`"SL-All"`). Be aware that in this case, the oci-cloud-controller-manager creates a security rule that allows inbound traffic from 0.0.0.0/0 (or from the source port ranges specified in the manifest file) to listener ports. In clusters with virtual nodes, security list management is never enabled and you always have to manually configure security rules (equivalent to`"None"`).

Note the following:
- If you include both the`oci.oraclecloud.com/security-rule-management-mode`annotation and either of the`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`or`oci-network-load-balancer.oraclecloud.com/security-list-management-mode`annotations in the manifest, the oci-cloud-controller-manager always uses the`oci.oraclecloud.com/security-rule-management-mode`and ignores the other annotation.
- There are limits to the number of ingress and egress rules that are allowed in both security lists and network security groups (see[Security List Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#sec_list_limits)and[Network Security Group Limits](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#nsg_limits)respectively). If the number of ingress or egress rules exceeds the limit, creating or updating the load balancer or network security group fails.
- A load balancer or network load balancer can be added to a maximum of five NSGs. If the number of NSGs exceeds the limit, an error is returned.
- If the Kubernetes service of type LoadBalancer is deleted, the OCI resources created by the oci-cloud-controller-manager (the frontend NSG, and security rules created in either the frontend NSG or the backend NSG) are removed. The backend NSG, and any security rules that the oci-cloud-controller-manager did not create, are not removed.
- When provisioning a network load balancer for a Kubernetes service of type LoadBalancer, you can use the`is-preserve-source: "true"`annotation to specify the preservation of the client IP address in the headers of IP packets (only valid when the`externalTrafficPolicy`annotation is set to`"Local"`). In this case, the oci-cloud-controller-manager creates security rules in the backend NSG to allow access to the worker nodes in the backend set from the CIDR blocks specified by`loadBalancerSourceRanges`in the LoadBalancer service manifest. Note that if CIDR blocks are not specified by`loadBalancerSourceRanges`, the oci-cloud-controller-manager creates a security rule to allow access from the internet (0.0.0.0/0) on the port number specified by`nodePort`.
- The backend NSG that you specify as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation must be in the same VCN as the cluster.
- The compute instances hosting the worker nodes in the backend set must have already been added to the backend NSG that you specify as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation.
- 

To simplify rule management for large or standardized environments, you can optionally specify one or more default backend NSGs when creating or updating a cluster (for example, using the OCI API, SDK, or CLI). To specify default backend NSGs, set the`backendNsgIds`attribute of the`ServiceLbConfigDetails`object when using the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)and[Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)operations. For example, the following section of a JSON file that you might use to create a cluster specifies two default backend NSGs:
```

```

When you specify`"NSG"`as the value of the`oci.oraclecloud.com/security-rule-management-mode`annotation for a service of type LoadBalancer, the NSG you have specified as the default at the cluster level is used as the backend NSG for that service, unless you override the default at the individual service level.

To override the default and specify an alternative backend NSG for a particular service of type LoadBalancer, add the`oci.oraclecloud.com/oci-backend-network-security-group`annotation in the metadata section of the manifest file. Use the annotation to specify the OCID of an existing NSG that you want to use instead of the default backend NSG.

### Examples of security rule management annotations

#### Example 1: Create a new frontend NSG with managed security rules, and have managed security rules in an existing backend NSG

In this example:
- You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
- You want the oci-cloud-controller-manager to use an existing backend NSG, and manage the security rules in that NSG.

You specify`"NSG"`as the value of the`oci.oraclecloud.com/security-rule-management-mode`annotation, and specify the OCID of the existing NSG as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation:
```

```

In this case:
- The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules.
- The oci-cloud-controller-manager manages the security rules of the backend NSG that has the OCID specified by the`oci-backend-network-security-group`annotation.

Note the following:
- The backend NSG that you specify as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation must be in the same VCN as the cluster.
- The compute instances hosting the worker nodes in the backend set must have already been added to the backend NSG that you specify as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation.

#### Example 2: Create a new frontend NSG with managed security rules, and manually manage security rules in an existing backend NSG

In this example:
- You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
- You want to manually define security rules to control traffic from the load balancer's front end to the back end in an NSG that you create and manage. For example, you might want to create security rules to prevent traffic being routed from the LB to the worker nodes.

You specify`"NSG"`as the value of the`oci.oraclecloud.com/security-rule-management-mode`annotation:
```

```

In this case:
- The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules.
- You are responsible for creating and managing security rules in a backend NSG to control traffic from the frontend NSG to the backend NSG.

#### Example 3: Create a new frontend NSG with managed security rules, and have managed security rules in an existing backend NSG (but annotations used incorrectly)

In this example:
- You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
- You want the oci-cloud-controller-manager to use an existing backend NSG, and manage the security rules in that NSG. However, you specify the annotations incorrectly.

You correctly specify`"NSG"`as the value of the`oci.oraclecloud.com/security-rule-management-mode`annotation. However, you mistakenly include the`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`annotation, and omit the`oci.oraclecloud.com/oci-backend-network-security-group`annotation:
```

```

In this case:
- The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules.
- The oci-cloud-controller-manager ignores the`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`annotation (because the`oci.oraclecloud.com/security-rule-management-mode`annotation is present).
- You are responsible for creating and managing security rules in a backend NSG to control traffic from the frontend NSG to the backend NSG (because the`oci.oraclecloud.com/oci-backend-network-security-group`annotation is not present).

#### Example 4: Create a new frontend NSG with managed security rules, have managed security rules in an existing backend NSG, and add the load balancer to an existing NSG

In this example:
- You want the oci-cloud-controller-manager to create a frontend NSG for a load balancer and manage the security rules in that NSG.
- You want the oci-cloud-controller-manager to use an existing backend NSG, and manage the security rules in that NSG.
- You want the oci-cloud-controller-manager to add the load balancer to an existing NSG that has security rules that you manage.

You specify:
- `"NSG"`as the value of the`oci.oraclecloud.com/security-rule-management-mode`annotation.
- The OCID of the existing NSG that you want the oci-cloud-controller-manager to use, as the value of the`oci.oraclecloud.com/oci-backend-network-security-group`annotation.
- The OCID of the existing NSG to which you want the oci-cloud-controller-manager to add the load balancer.

The manifest is as follows:
```

```

In this case:
- The oci-cloud-controller-manager creates the frontend NSG for the load balancer, and manages its security rules.
- The oci-cloud-controller-manager manages the security rules of the backend NSG that has the OCID specified by the`oci.oraclecloud.com/oci-backend-network-security-group`annotation.
- The oci-cloud-controller-manager adds the load balancer to the NSG specified by the`oci.oraclecloud.com/oci-network-security-groups`annotation.

## Specifying ZPR Security Attributes for Load Balancers and Network Load Balancers

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type`LoadBalancer`, you can assign Zero Trust Packet Routing (ZPR) security attributes to the load balancer by adding the`oci.oraclecloud.com/security-attributes`annotation to the service manifest.

The annotation value is a JSON string that specifies the security attributes to assign to the load balancer or network load balancer. You use the annotation for both load balancers and network load balancers.

For example:
```

```

When Kubernetes Engine provisions or updates the load balancer or network load balancer for the service, it assigns the specified security attributes to the load balancer resource.

Do not update the security attributes directly on the Oracle Cloud Infrastructure load balancer or network load balancer. To change the security attributes, update the annotation on the Kubernetes service.

Note that to enable Kubernetes Engine to apply ZPR security attributes to a load balancer or network load balancer, a suitable IAM policy must exist to enable Kubernetes Engine to use the appropriate security attribute namespace. For example:

```

```

Note  
  
Assigning ZPR security attributes to a load balancer or network load balancer does not, by itself, allow traffic. You must also create ZPR policies that allow the required traffic. Existing network security groups and security lists continue to apply.

For more information about adding ZPR security attributes, see[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm).

## Specifying Health Check Parameters

Oracle Cloud Infrastructure load balancers and network load balancers apply a health check policy to continuously monitor backend servers. A health check is a test to confirm backend server availability, and can be a request or a connection attempt. If a server fails the health check, the load balancer or network load balancer takes the server temporarily out of rotation. If the server subsequently passes the health check, the load balancer or network load balancer returns it to the rotation.

Health check policies include a number of parameters, which each have a default value. When Kubernetes Engine provisions an OCI load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can override health check parameter default values by including annotations in the metadata section of the manifest file. You can later add, modify, and delete those annotations. If you delete an annotation that specified a value for a health check parameter, the load balancer or network load balancer uses the parameter's default value instead.

[Configure health check parameters for load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To configure health check parameters when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotations in the metadata section of the manifest file:
- 

To specify how many unsuccessful health check requests to attempt before a backend server is considered unhealthy, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is the number of unsuccessful health check requests.
- 

To specify the interval between health check requests, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is a numeric value in milliseconds. The minimum is 1000.
- 

To specify the maximum time to wait for a response to a health check request, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is a numeric value in milliseconds. A health check is successful only if the load balancer receives a response within this timeout period.

For example:

```

```

[Configure health check parameters for network load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To configure health check parameters when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotations in the metadata section of the manifest file:
- 

To specify how many unsuccessful health check requests to attempt before a backend server is considered unhealthy, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is the number of unsuccessful health check requests.
- 

To specify the interval between health check requests, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is a numeric value in milliseconds. The minimum is 1000.
- 

To specify the maximum time to wait for a response to a health check request, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is a numeric value in milliseconds. A health check is successful only if the network load balancer receives a response within this timeout period.

For example:

```

```

Note that if you don't explicitly specify health check parameter values by including annotations in the metadata section of the manifest file, the following defaults are used:

Load Balancer Annotation Network Load Balancer Annotation

Default Value Used
`service.beta.kubernetes.io/oci-load-balancer-health-check-retries``oci-network-load-balancer.oraclecloud.com/health-check-retries`"3"
`service.beta.kubernetes.io/oci-load-balancer-health-check-interval``oci-network-load-balancer.oraclecloud.com/health-check-interval`"10000"
`service.beta.kubernetes.io/oci-load-balancer-health-check-timeout``oci-network-load-balancer.oraclecloud.com/health-check-timeout`"3000"

Also note that the health check annotations shown in the table apply when using nodes as backends. Specifically, do not set the`oci-load-balancer.oraclecloud.com/health-check`or`oci-network-load-balancer.oraclecloud.com/health-check`annotations when using nodes as backends, because these two annotations only apply when using pods as backends (see[Specifying Pods as Backends](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_pods_as_backends)).

For more information about Oracle Cloud Infrastructure load balancer and network load balancer health check policies, see:
- [Health Checks for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)
- [Health Check Policies for Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/health-check-policy-management.htm)

## Selecting Worker Nodes To Include In Backend Sets

Incoming traffic to an Oracle Cloud Infrastructure load balancer or network load balancer is distributed between the backend servers in a backend set. By default, when Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, all the worker nodes in the cluster are included in the backend set.

However, you have the option to select only a subset of worker nodes in a cluster to include in the backend set of a given load balancer or network load balancer. Including subsets of a cluster's worker nodes in the backend sets of different load balancers and network load balancers enables you to present a single Kubernetes cluster as multiple logical clusters (services).

[Select worker nodes to include in load balancer backend set](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To select the worker nodes to include in the backend set when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:

```

```

where`<label>`is one or more label keys and values, identified using standard Kubernetes label selector notation. For example,`lbset=set1`

For example:

```

```

[Select worker nodes to include in network load balancer backend set](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To select the worker nodes to include in the backend set when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:

```

```

where`<label>`is one or more label keys and values, identified using standard Kubernetes label selector notation. For example,`lbset=set1`

For example:

```

```

Use standard Kubernetes label selector notation to specify the label keys and values in the annotations in the metadata section of the manifest file. For more information about standard Kubernetes label selector notation, see[Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)in the Kubernetes documentation.

The table gives some examples of standard Kubernetes label selector notation.

Load Balancer Annotation Network Load Balancer Annotation

Include in the backend set:
`oci.oraclecloud.com/node-label-selector: lbset=set1``oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset=set1`

All worker nodes with the label key`lbset`that has the value`set1`
`oci.oraclecloud.com/node-label-selector: lbset in (set1, set3)``oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset in (set1, set3)`

All worker nodes with the label key`lbset`that has the value`set1`or`set3`
`oci.oraclecloud.com/node-label-selector: lbset``oci-network-load-balancer.oraclecloud.com/node-label-selector: lbset`All worker nodes with the label key`lbset`, regardless of its value.
`oci.oraclecloud.com/node-label-selector: env=prod,lbset in (set1, set3)``oci-network-load-balancer.oraclecloud.com/node-label-selector: env=prod,lbset in (set1, set3)`

All worker nodes with the label key`env`that has the value`prod`, and with the label key`lbset`that has the value`set1`or the value`set3`
`oci.oraclecloud.com/node-label-selector: env!=test``oci-network-load-balancer.oraclecloud.com/node-label-selector: env!=test`

All worker nodes with the label key`env`that does not have the value`test`

## Specifying Backend Set Policies

When Kubernetes Engine provisions a load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can define a policy for the backend set to specify how to distribute incoming traffic to the backend servers.

For more information:
- About load balancers and backend set policies, see[Load Balancer Policies](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).
- About network load balancers and backend set policies, see[Network Load Balancer Policies](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#Policies)

[Specifying a backend set policy for a load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To specify a policy for the backend set when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is one of:
- `"ROUND_ROBIN"`: Routes incoming traffic sequentially to each server in a backend set list.
- `"LEAST_CONNECTIONS"`: Routes incoming non-sticky request traffic to the backend server with the fewest active connections.
- `"IP_HASH"`: Routes incoming non-sticky request traffic from the same client to the same backend server as long as that server is available, using the incoming request's source IP address as a hashing key.

For example:

```

```

Note that if you don't explicitly specify a policy for the backend set, "ROUND_ROBIN" is used as the default value.

[Specifying a backend set policy for a network load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To specify a policy for the backend set when Kubernetes Engine provisions a network load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is one of:
- `"TWO_TUPLE"`: Routes incoming traffic based on 2-Tuple (source IP, destination IP) Hash.
- `"THREE_TUPLE"`: Routes incoming traffic based on 3-Tuple (source IP, destination IP, protocol) Hash.
- `"FIVE_TUPLE"`: Routes incoming traffic based on 5-Tuple (source IP and port, destination IP and port, protocol) Hash.

For example:

```

```

Note that if you don't explicitly specify a policy for the backend set, "FIVE_TUPLE" is used as the default value.

## Specifying Pod Readiness Gates

Warning  
  

Do not specify pod readiness gates when`externalTrafficPolicy`is set to`Local`in the manifest file.

Also note that Kubernetes Engine injects a pod readiness gate into the pod spec of each pod in the namespace whose labels match the selector of any service of type LoadBalancer in that namespace. Pods that do not match any LoadBalancer service’s selector are unaffected.

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can use a pod readiness gate to ensure traffic is only routed to pods that have both been successfully added to the backend set, and that are ready to receive traffic.

Pod readiness gates are additional conditions to indicate that a pod is ready to receive traffic. Pod readiness gates enable you to implement complex custom readiness checks, and can help to achieve zero downtime during rolling deployments. For more information, see[pod readiness details in the Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate).

When provisioning a load balancer or network load balancer, the backend set comprises the IP addresses of a deployment's pod replicas that have a condition of`Ready`. Updating the deployment (for example, to use a new image) triggers the replacement of existing pod replicas with new pod replicas. However, replacing all of the pod replicas can take some time and cause backend unavailability because:
- The existing pod replicas might be terminated before the backend set has been updated with the IP addresses of the new pod replicas.
- The backend set might be updated with the IP addresses of the new pod replicas before the new pod replicas are ready to receive traffic.

Specifying the use of a pod readiness gate ensures that backends are always available for the load balancer or network load balancer. Existing pods are not terminated until new pods have been added to the backend set, and the new pods are ready to receive traffic.

To specify that Kubernetes Engine is to inject a pod readiness gate into the pod spec of pods in a particular namespace whose labels match the selector of any service of type LoadBalancer, add the`loadbalancer.oci.oraclecloud.com/pod-readiness-gate-inject=enabled`label to the namespace by entering:
```

```

The following example shows you how to create a load balancer with a pod readiness gate.

First, label the`pdr`namespace to specify the pod readiness gate for the namespace, by entering:
```

```

The output from the command confirms the namespace has been labeled:
```

```

Then, deploy Nginx in the`pdr`namespace by entering:
```

```

List the pods in the`pdr`namespace by entering:
```

```

Now you can demonstrate the use of the pod readiness gate by updating the image version in the Nginx manifest and reapplying the manifest, so that existing pods are replaced with new pods.
Download the Nginx manifest from[https://raw.githubusercontent.com/oracle-devrel/oci-oke-virtual-nodes/main/nginx-svc/nginx.yaml](https://raw.githubusercontent.com/oracle-devrel/oci-oke-virtual-nodes/main/nginx-svc/nginx.yaml), and change the image version to`nginx:1.25.1`, as shown:
```

```

Re-apply the manifest by entering:
```

```

Observe the new pods being rolled out by entering:
```

```

For example:
```

```

Observe the status of one of the new pods by entering:
```

```

For example:
```

```

The output from the command confirms the status of the`podreadiness.loadbalancer.oraclecloud.com`readiness gate. For example:
```

```

## Specifying IPMode to adjust traffic routing

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can specify how to route traffic originating from within a cluster to the load balancer's or network load balancer's IP address.

In clusters running Kubernetes version 1.30 or later, the`LoadBalancerIPMode`Kubernetes feature gate is enabled, and the`ipMode`field of a service of type LoadBalancer has the default value of "VIP". When`ipMode`has the value of "VIP", traffic sent to the IP address of a service of type LoadBalancer from a pod within the cluster is routed straight to application pods to optimize performance, bypassing the LoadBalancer service. For more information, see[Specifying IPMode of load balancer status](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-ip-mode)in the Kubernetes documentation.

However, in some situations, you might decide that routing traffic straight to application pods is not appropriate. For example, if traffic that originates within a cluster is routed straight to application pods, you cannot implement SSL termination at the load balancer level.

To specify how to route traffic that is sent to the load balancer's or network load balancer's IP address from within the cluster, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is one of:
- `"VIP"`: All traffic originating from within the cluster and sent to the IP address of a service of type LoadBalancer is routed straight to the application pods to optimize performance, bypassing the LoadBalancer service.
- `"proxy"`: All traffic originating from within the cluster and sent to the IP address of a service of type LoadBalancer is routed to the Oracle Cloud Infrastructure load balancer or network load balancer that has been provisioned for the LoadBalancer service. The load balancer or network load balancer then forwards the traffic to the application pods.

For example:

```

```

Note that if you do not specify the`oci.oraclecloud.com/ingress-ip-mode`annotation, or subsequently remove the annotation, the`ipMode`property of a service of type LoadBalancer has the default value of`"VIP"`.

Also note that when using a private network load balancer with the`oci-network-load-balancer.oraclecloud.com/is-preserve-source`annotation set to`true`, the network load balancer has a known limitation that does not allow traffic where the source node and the destination backend node are the same node. This limitation prevents communication between pods on the same node via the network load balancer when the following conditions are all met:
- The`oci.oraclecloud.com/ingress-ip-mode`annotation is set to`proxy`.
- The`oci-network-load-balancer.oraclecloud.com/is-preserve-source`annotation is set to`true`.
- The network load balancer is private.

## Specifying IP Address Families for Load Balancers and Network Load Balancers

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, the load balancer subnet determines the control you have over the IP address family of the IP address on which the load balancer or network load balancer receives traffic.
- If the subnet is an IPv4 single stack subnet, the subnet is configured for IPv4 addressing only. The load balancer or network load balancer is only allocated an IPv4 address on which to receive external traffic. You cannot change the IP address family of the IP address on which the load balancer or network load balancer receives external traffic.
- If the subnet is an IPv4/IPv6 dual stack subnet, the subnet is configured for both IPv4 and IPv6 addressing. The load balancer or network load balancer can be allocated either or both an IPv4 address and an IPv6 address on which to receive external traffic. In this situation, you can use the Kubernetes`spec.ipFamilyPolicy`and`spec.ipFamilies`fields in the service manifest to specify whether the load balancer or network load balancer receives external traffic on the IPv4 address only, or on the IPv6 address only, or on both the IPv4 address and the IPv6 address.

Note that the IP address family used for traffic between the listener and the backend set is determined differently for load balancers and network load balancers:
- Load balancers: The traffic between a load balancer listener and the backend set always uses IPv4 addresses.
- Network load balancers: The traffic between a network load balancer listener and the backend set uses the same IP address family as the IP address on which the network load balancer listener receives external traffic.

The table shows the interaction between the load balancer subnet's IP address family, the settings of`spec.ipFamilyPolicy`and`spec.ipFamilies`, the IP address family from which IP addresses are allocated to the load balancer or network load balancer, and the IP protocol between the listener and the backend set. Note that only valid combinations are shown.

Subnet IP Address Family`ipFamilyPolicy`set to:`ipFamilies`set to: IP address family of the network load balancer endpoint IP address family of the load balancer Network load balancer listener to backend set traffic Load balancer listener to backend set traffic
IPv4`SingleStack``IPv4`IPv4 IPv4 IPv4 IPv4
IPv4/IPv6`SingleStack``IPv4`IPv4 IPv4 IPv4 IPv4
IPv4/IPv6`SingleStack``IPv6`IPv6 not supported IPv6 not supported
IPv4`PreferDualStack``IPv4`IPv4 IPv4 IPv4 IPv4
IPv4`PreferDualStack``IPv6`IPv4 IPv4 IPv4 IPv4
IPv4`PreferDualStack``IPv4,IPv6`IPv4 IPv4 IPv4 IPv4
IPv4`PreferDualStack``IPv6,IPv4`IPv4 IPv4 IPv4 IPv4
IPv4/IPv6`PreferDualStack``IPv4`IPv4(primary) and IPv6 IPv4(primary) and IPv6 IPv4(primary) and IPv6 IPv4
IPv4/IPv6`PreferDualStack``IPv6`IPv6(primary) and IPv4 IPv6(primary) and IPv4 IPv6(primary) and IPv4 IPv4
IPv4/IPv6`PreferDualStack``IPv4,IPv6`IPv4(primary) and IPv6 IPv4(primary) and IPv6 IPv4(primary) and IPv6 IPv4
IPv4/IPv6`PreferDualStack``IPv6,IPv4`IPv6(primary) and IPv4 IPv6(primary) and IPv4 IPv6(primary) and IPv4 IPv4
IPv4/IPv6`RequireDualStack``IPv4,IPv6`IPv4(primary) and IPv6 IPv4(primary) and IPv6 IPv4(primary) and IPv6 IPv4
IPv4/IPv6`RequireDualStack``IPv6,IPv4`IPv6(primary) and IPv4 IPv6(primary) and IPv4 IPv6(primary) and IPv4 IPv4

Note that if you use the`service.beta.kubernetes.io/oci-load-balancer-subnet1`annotation to specify an alternative subnet to the subnet specified for load balancers when the cluster was created, make sure the alternative subnet's address family is compatible with the`spec.ipFamilyPolicy`and`spec.ipFamilies`fields in the service manifest.

For more information about IPv4 and IPv6 support in Kubernetes, see[IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/)in the Kubernetes documentation.

### Example 1:

In this example:
- You want to use the subnet specified for load balancers when the cluster was created.
- You only want to deploy the service of type LoadBalancer if it can be assigned both an IPv4 and an IPv6 address, so you set`ipFamilyPolicy: RequireDualStack`.
- You want the load balancer's primary IP address to be an IPv6 address (and its secondary address to be an IPv4 address), so you set`spec.ipFamilies: IPv6,IPv4`.

```

```

In this example, the cluster's load balancer subnet is a dual stack IPv4/IPv6 subnet, so the deployment is successful. The load balancer is assigned an IPv6 address as its primary address, and an IPv4 address as its secondary address.

### Example 2:

In this example:
- You want to host the service of type LoadBalancer on an alternative subnet to the one specified for load balancers when the cluster was created, so you use the`service.beta.kubernetes.io/oci-load-balancer-subnet1`annotation to specify the alternative subnet's OCID.
- You want to allocate both IPv4 and IPv6 addresses to the service of type LoadBalancer if the service is hosted on a dual stack IPv4/IPv6 subnet. Otherwise, if the service is hosted on a single stack IPv4 subnet, you want an IP address allocated to the service from that IP address family. So you set`ipFamilyPolicy: PreferDualStack`.
- You want the load balancer's primary IP address to be an IPv4 address (and its secondary address to be an IPv6 address, if supported by the subnet), so you set`spec.ipFamilies: IPv4,IPv6`.

```

```

In this example, the alternative subnet is a dual stack IPv4/IPv6 subnet, so the deployment is successful. The load balancer is assigned an IPv4 address as its primary address, and an IPv6 address as its secondary address.

## Assigning Specific IPv4 and IPv6 Addresses to Network Load Balancers

When Kubernetes Engine provisions an Oracle Cloud Infrastructure network load balancer for a Kubernetes service of type`LoadBalancer`, the Network Load Balancer service assigns one or more IP addresses to the network load balancer.

The Network Load Balancer service assigns a private IPv4 address and, in the case of an external network load balancer, also assigns an additional public IPv4 address. If the network load balancer's subnet is compatible, the Network Load Balancer service can also assign an IPv6 address (see[Specifying IP Address Families for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_IPAddressfamily)).

In clusters running Kubernetes version 1.29 or later, you can specify the IP address to assign to the network load balancer, instead of the Network Load Balancer service selecting the IP address to assign. The IP address you can assign depends on the network load balancer subnet's IP address family, as follows:
- IPv4: If the network load balancer's subnet is an IPv4 single stack subnet or an IPv4/IPv6 dual stack subnet, you can assign a private IPv4 address to the network load balancer.
- IPv4 and IPv6: If the network load balancer's subnet is an IPv4/IPv6 dual stack subnet, you can assign either or both a private IPv4 address and an IPv6 address to the network load balancer.

To specify a private IPv4 address to assign to a network load balancer, add the following annotation in the metadata section of the manifest file:
```

```

where`<ipv4-address>`is a valid IPv4 address, from the IPv4 CIDR block specified for the network load balancer's subnet. For example:
```

```

To specify an IPv6 address to assign to a network load balancer, add the following annotation in the metadata section of the manifest file:
```

```

where`<ipv6-address>`is a valid IPv6 ULA or GUA address, from the IPv6 CIDR block specified for the network load balancer's subnet. For example:
- `oci-network-load-balancer.oraclecloud.com/assigned-ipv6: "fd8a:4b3c:7d91:abcd::1"`
- `oci-network-load-balancer.oraclecloud.com/assigned-ipv6: "2607:9b80:9a0a:9a7e:abcd:ef01:2345:6789"`

For example:

```

```

It is your responsibility to specify a valid IP address. For an IP address to be valid, the following conditions must be met:
- The IP address must be in the correct format for the annotation you use (either IPv4 or IPv6).
- The IP address must be from the appropriate CIDR block specified for the network load balancer's subnet.
- The IP address must not already be in use by another resource.

Note the following:
- If the IP address is not in the correct format, or not from the appropriate CIDR block, the network load balancer creation request is not accepted.
- If the IP address is in the correct format and from the appropriate CIDR block, but the IP address is already in use by another resource, the network load balancer creation request is accepted. However, the associated work request will fail, and the compartment will contain a network load balancer in a Failed state.
- If the IP address is valid, the network load balancer is created with the specified IP address assigned to it.

## Concealing a Network Load Balancer's Private IP Address

When Kubernetes Engine provisions a public Oracle Cloud Infrastructure network load balancer for a Kubernetes service of type LoadBalancer, the Network Load Balancer service assigns both a public IP address and a private IP address to the network load balancer. The private IP address is used for health checks and port address translation (PAT), but cannot receive external traffic from outside the VCN (including from the public internet).

To see the public and private IP addresses that the Network Load Balancer service has assigned to the network load balancer, enter the`kubectl get service`command (or similar). For example:
```

```

In some situations, you might only want to expose the network load balancer's public IP address, and hide the private IP address. For example:
- You might specify a friendly DNS name for the network load balancer when using the ExternalDNS add-on, by including the`external-dns.alpha.kubernetes.io/hostname`annotation in the manifest of the Kubernetes service of type LoadBalancer. ExternalDNS creates a DNS record for the network load balancer in the external DNS provider you've configured for the cluster. The DNS record maps the DNS name to both the public IP address and the private IP address. As a result, if external traffic uses the DNS name, there is a possibility that traffic might be routed to the network load balancer's private IP address, even though the private IP address cannot receive external traffic.
- You might set up automation that uses the`kubectl get service`command (or similar) to obtain the IP address of the network load balancer. If your usecase includes routing external traffic, you only want the network load balancer's public IP address. However, by default, the`kubectl get service`command returns both the network load balancer's public IP address and its private IP address.

To specify that the`kubectl get service`command (or similar) only returns the network load balancer's public IP address, add the following annotation in the metadata section of the manifest file:

```

```

Note that`"false"`is the default value of the`oci-network-load-balancer.oraclecloud.com/external-ip-only`annotation. If you do not explicitly include the annotation in the service definition, the`kubectl get service`command (or similar) returns both the network load balancer's public IP address and private IP address

For example:

```

```

If you include the`oci-network-load-balancer.oraclecloud.com/external-ip-only: "true"`annotation in the manifest, when you enter the`kubectl get service`command (or similar), only the public IP address is returned. For example:
```

```

## Preventing Nodes from Handling Traffic

You can exclude particular worker nodes from the list of backend servers in the backend set of an Oracle Cloud Infrastructure load balancer or network load balancer. For more information, see[node.kubernetes.io/exclude-from-external-load-balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengsupportedlabelsusecases.htm#exclude-from-external-load-balancers).

## Tagging Load Balancers and Network Load Balancers

You can add tags to a load balancer or network load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See[Applying Tags to Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_load-balancer-tags.htm).

## Enabling Proxy Protocol

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can specify whether to enable the proxy protocol feature with TCP-based listeners. Enabling proxy protocol allows transport connection information such as a client's IP address to be securely transported across multiple layers of proxies to the backend server. The following proxy protocol versions are available:
- Version 1, which uses a text-based header to pass information across proxies, and is best for small implementations.
- Version 2, which uses a text-based and binary header for greater efficiency in producing and parsing, and is best for larger implementations.

Load balancers provisioned by Kubernetes Engine support proxy protocol version 1 and version 2. Network load balancers provisioned by Kubernetes Engine support proxy protocol version 2.

For more information:
- About load balancers and the proxy protocol feature, see[Proxy Protocol for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm#proxy-protocol).
- About network load balancers and the proxy protocol feature, see[Proxy Protocol for Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm#proxy-protocol).

[Enabling proxy protocol for load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To enable proxy protocol for load balancers provisioned by Kubernetes Engine, add the following annotation in the metadata section of the manifest file:
```

```

where`"<value>"`is one of:
- `"1"`to specify that you want to enable proxy protocol version 1 on all listeners of the load balancer.
- `"2"`to specify that you want to enable proxy protocol version 2 on all listeners of the load balancer.

Having enabled the proxy protocol feature for load balancers, note the following:
- You cannot disable the proxy protocol feature on load balancer listeners.
- You can switch between proxy protocol version 1 and proxy protocol version 2 by updating the annotation.
- If you subsequently remove the annotation from the manifest, or unset the annotation (by setting`"<value>"`to`""`), the last successfully applied setting for`"<value>"`is retained on all listeners.

[Enabling and disabling proxy protocol for network load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

To enable proxy protocol for network load balancers provisioned by Kubernetes Engine, add the following annotation in the metadata section of the manifest file:
```

```

where`"<value>"`is one of:
- `"true"`to specify that you want to enable proxy protocol version 2 on all listeners of the network load balancer.
- `"false"`to specify that you want to disable proxy protocol version 2 on all listeners of the network load balancer.

Having enabled the proxy protocol feature for network load balancers, note the following:
- You can disable the proxy protocol feature on network load balancer listeners by setting`"<value>"`to`"false"`.
- If you subsequently remove the annotation from the manifest, or unset the annotation (by setting`"<value>"`to`""`), or specify an invalid value (such as`"enable"`) for the annotation, the last successfully applied setting for`"<value>"`is retained on all listeners.

## Specifying Pods as Backends

Incoming traffic to an Oracle Cloud Infrastructure load balancer or network load balancer is distributed between the backends in a backend set. By default, when Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, the worker nodes in the cluster are the backends in the backend set. In this default configuration, the load balancer or network load balancer routes external traffic to worker nodes, which then forward traffic to the appropriate pods running applications in the cluster.

However, you have the option to specify an alternative configuration in which pods are used directly as the backends in the backend set. In this "pods as backends" configuration, the load balancer or network load balancer forwards traffic straight to the pod IPs, bypassing the nodes entirely. Kubernetes Engine creates one listener and backend set pair per service port, using pod IPs as the backends with the configured health checks. Traffic is handled as follows:
- The client sends a request to the load balancer.
- The load balancer matches the request to a backend set, and then selects a healthy pod IP.
- The request is routed directly to the pod's IP.
- The pod processes and responds to the request.
- The response is returned to the client via the load balancer.

Using pods (rather than nodes) as backends has the following advantages:
- Improved network efficiency: Eliminating intermediate node routing reduces network congestion and overhead.
- Optimized resource utilization: Only healthy pods are registered as backends, simplifying backend management and potentially improving scalability.
- Simpler health checks: The load balancer probes each application pod directly, resulting in more accurate health monitoring.
- Lower load on nodes: Offloading traffic from nodes reduces their processing burden and can lead to more predictable application performance.

Note the following when using pods (rather than nodes) as backends:
- OCI load balancers and network load balancers support up to 512 backends per backend set or per load balancer. If a service of type LoadBalancer selects more pods than this, only the first 512 are registered as backends.
- Using pods as backends is only supported on clusters that use the OCI VCN-Native Pod Networking CNI plugin for pod networking.
- Using pods as backends for a service of type LoadBalance is only supported when node ports are disabled for the service.
- You can migrate an existing service of type LoadBalancer that is currently using nodes as backends to instead start using pods as backends (see[Migrating Services of Type LoadBalancer From Using Nodes as Backends to Using Pods as Backends, and Vice Versa](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_pods_as_backends__section_migrating-to-from-pods-as-backends)).

### Prerequisites for Using Pods as Backends

To use pods as backends, the cluster must meet the following prerequisites:
- The cluster must be running Kubernetes version 1.30 or later.
- The cluster must use the OCI VCN-Native Pod Networking CNI plugin for pod networking.

### Using Pods as Backends

To use pods as backends for a load balancer or network load balancer provisioned by Kubernetes Engine:
- Add the`allocateLoadBalancerNodePorts`field in the spec section of the manifest file, and set the field to`false`.
- Add the`oci-load-balancer.oraclecloud.com/health-check`annotation (for load balancers) or`oci-network-load-balancer.oraclecloud.com/health-check`annotation (for network load balancers) to the manifest file that defines the service of type LoadBalancer. Define a valid health check configuration as the value of the annotation, by specifying a JSON object. For more information, see[Health Check Configurations for Pods as Backends](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_pods_as_backends__section_health-checks-for-pods-as-backends).
- Do not specify that you want the oci-cloud-controller-manager to manage security rules in a security list for the backend set. For more information, see[Valid Security Rule Management Options for Pods as Backends](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_pods_as_backends__section_security-mgmt-for-pods-as-backends).

[Specifying pods as backends for a load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

Example:
```

```

[Specifying pods as backends for a network load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#)

Example:
```

```

### Health Check Configurations for Pods as Backends

When you use pods as backends for a load balancer or network load balancer, you use the following annotations to define a health check that checks the health of each pod in the backend set:
- the`oci-load-balancer.oraclecloud.com/health-check`annotation (for load balancers)
- the`oci-network-load-balancer.oraclecloud.com/health-check`annotation (for network load balancers)

Only pods that pass the health check are considered healthy and eligible to receive traffic from the load balancer.

You define a health check by specifying a JSON object as the value of the`oci-load-balancer.oraclecloud.com/health-check`or`oci-network-load-balancer.oraclecloud.com/health-check`annotation. The JSON object can include the following fields:
- `protocol`: (required) The protocol to use for the health check (such as HTTP, TCP, UDP, HTTPS).
- `port`: The port number to use for the health check.
- `urlPath`: The URL path to use for the health check (only applicable for HTTP protocol).
- `returnCode`: The expected return code for the health check.
- `retries`: The number of retries for the health check.
- `timeoutInMillis`: The timeout in milliseconds for the health check.
- `responseBodyRegex`: A regular expression to match against the response body (only applicable for HTTP protocol).

The annotations and the associated JSON objects enable you to define all of the health check configurations supported by load balancers and network load balancers. For more information about all of the fields allowed in the JSON object:
- For load balancers, see[Editing a Load Balancer's Health Check Policies](https://docs.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm).
- For network load balancers, see[Editing Network Load Balancer Health Check Policies](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/update-health-check-policy.htm).

You can define a single health check configuration for all backend sets. For example:
```

```

```

```

Note that the health check configuration you define using the`oci-load-balancer.oraclecloud.com/health-check`or`oci-network-load-balancer.oraclecloud.com/health-check`annotations only applies when using pods as backends. The`oci-load-balancer.oraclecloud.com/health-check`and`oci-network-load-balancer.oraclecloud.com/health-check`annotations replace the annotations that apply when using nodes as backends. Specifically, the following annotations do not take effect when using pods as backends:
- 

For load balancers, the following annotations do not take effect when using pods as backends:
- `service.beta.kubernetes.io/oci-load-balancer-health-check-retries`
- `service.beta.kubernetes.io/oci-load-balancer-health-check-timeout`
- `service.beta.kubernetes.io/oci-load-balancer-health-check-interval`
- 

For network load balancers, the following annotations so not take effect when using pods as backends:
- `oci-network-load-balancer.oraclecloud.com/health-check-retries`
- `oci-network-load-balancer.oraclecloud.com/health-check-timeout`
- `oci-network-load-balancer.oraclecloud.com/health-check-interval`

As already stated, although these annotations do not take effect when using pods as backends, you can specify values for the corresponding health check configuration settings using the`oci-load-balancer.oraclecloud.com/health-check`or`oci-network-load-balancer.oraclecloud.com/health-check`annotations and the associated JSON objects.

### Valid Security Rule Management Options for Pods as Backends

When you use pods (rather than nodes) as backends for a load balancer or network load balancer, you can specify one of the following security rule management options:
- You can specify that the oci-cloud-controller-manager is to use security lists to manage security rules for ingress to the frontend load balancer or network load balancer. It is your responsibility to set up security rules to allow inbound traffic to backend pods.

In this case, you can use the following annotations:
- `oci.oraclecloud.com/security-rule-management-mode: "SL-Frontend"`
- `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "Frontend"`
- `oci-network-load-balancer.oraclecloud.com/security-list-management-mode: "Frontend"`

Note that you cannot specify that the oci-cloud-controller-manager is to use security lists to manage security rules for backend pods.
- You can specify that the oci-cloud-controller-manager is to use network security groups (NSGs) to manage security rules for:
- ingress to the frontend load balancer or network load balancer, in an NSG created for this purpose (known as the frontend NSG)
- ingress to the backend pods, in an existing NSG for which you specify the OCID (known as the backend NSG)

In this case, you can use the following annotations and values:
- `oci.oraclecloud.com/security-rule-management-mode: NSG`
- `oci.oraclecloud.com/oci-backend-network-security-group:`to specify the OCID of an existing NSG that is both in the same VCN as the cluster, and also an NSG to which the compute instances hosting worker nodes have already been added.
- You can specify that the oci-cloud-controller-manager is not to manage secrity rules. It is your responsibility to set up security rules to allow inbound traffic to load balancers and network load balancers, and to backend pods.

In this case, you can use the following annotations and values:
- `oci.oraclecloud.com/security-rule-management-mode: "None"`
- `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "None"`
- `oci-network-load-balancer.oraclecloud.com/security-list-management-mode: "None"`

Note that you must not specify that the oci-cloud-controller-manager is to use security lists to manage security rules for backend pods. In other words, you must not specify the following annotations and values:
- `oci.oraclecloud.com/security-rule-management-mode: "SL-All"`
- `service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "All"`
- `oci-network-load-balancer.oraclecloud.com/security-list-management-mode: "All"`

For more information about security rule management (including the IAM policies required to use NSGs to manage security rules), see[Specifying Security Rule Management Options for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Options).

### Support for Pod Readiness Gates and Readiness Probes when Using Pods as Backends
Warning  
  

Do not specify pod readiness gates when`externalTrafficPolicy`is set to`Local`in the manifest file.

Also note that Kubernetes Engine injects a pod readiness gate into the pod spec of each pod in the namespace whose labels match the selector of any service of type LoadBalancer in that namespace. Pods that do not match any LoadBalancer service’s selector are unaffected.

When using pods as backends for a load balancer or network load balancer provisioned by Kubernetes Engine, you can use pod readiness gates to indicate that a pod is ready to receive traffic. Pod readiness gates enable you to implement complex custom readiness checks, and can help to achieve zero downtime during rolling deployments.

To specify that Kubernetes Engine is to inject a pod readiness gate into the pod spec of pods in a particular namespace whose labels match the selector of any service of type LoadBalancer, add the`loadbalancer.oci.oraclecloud.com/pod-readiness-gate-inject=enabled`label to the namespace by entering:
```

```

For more information, see[Specifying Pod Readiness Gates](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_pod_readiness_gates). Also see[pod readiness details in the Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate).

Readiness probes are also supported when using pods as backends for a load balancer or network load balancer provisioned by Kubernetes Engine. For more information about readiness probes, see[Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)in the Kubernetes documentation.

### Migrating Services of Type LoadBalancer From Using Nodes as Backends to Using Pods as Backends, and Vice Versa
Warning  
  

Traffic disruption is expected when you migrate a service of type LoadBalancer from using nodes as backends to using pods as backends.

You can migrate an existing service of type LoadBalancer that is currently using nodes as backends to instead start using pods as backends by updating the service manifest as described in[Using Pods as Backends](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_pods_as_backends__section_using-pods-as-backends), and summarized as follows:
- Set the`allocateLoadBalancerNodePorts`field to`false`.
- Set the`oci-load-balancer.oraclecloud.com/health-check`annotation (for load balancers) or`oci-network-load-balancer.oraclecloud.com/health-check`to a valid health check configuration
- Set the`oci.oraclecloud.com/security-rule-management-mode`annotation to "None", "SL-Frontend", or "NSG"

In addition, to migrate an existing service of type LoadBalancer from using nodes as backends to using pods as backends, ensure that no NodePorts have been allocated to the existing service. If NodePorts have been allocated to the existing service, you have to remove them.

You can migrate an existing service of type LoadBalancer that is currently using pods as backends to start using nodes as backends by updating the service manifest as follows:
- Set the`allocateLoadBalancerNodePorts`field set to`true`.

## Specifying the Compartment for Load Balancers and Network Load Balancers

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, you can specify the compartment in which the load balancer or network load balancer is created. By default, Kubernetes Engine creates the load balancer or network load balancer in the same compartment as the cluster.

To specify an alternative compartment in which to create the load balancer or network load balancer, add the following annotation in the metadata section of the manifest file:
```

```

where`<compartment-ocid>`is the OCID of the compartment in which you want to create the load balancer or network load balancer.

For example, to specify an alternative compartment in which to create a load balancer:
```

```

This manifest specifies that the load balancer is to be created in the compartment with the OCID`ocid1.compartment.oc1..aaaaaaaay______t6q`.

Note that Kubernetes Engine does not support the moving of a load balancer or network load balancer between compartments after it has been created. Consider the following recommendations:
- As best practice, we recommend that you carefully plan compartment assignment before deploying a service of type LoadBalancer.
- If you want to change the compartment in which a load balancer or network load balancer created by Kubernetes Engine currently resides, we recommend that you delete the service of type LoadBalancer. You can then update the`oci.oraclecloud.com/compartment-id`annotation in the service manifest to specify the required compartment, and then redeploy the service.
- Although possible in the Load Balancer service and the Network Load Balancer service, we strongly recommend that you do not move a load balancer or network load balancer that Kubernetes Engine has created, from one compartment to another. Moving a load balancer or network load balancer between compartments might result in an 'orphan' load balancer or network load balancer being created in the original compartment. The orphan load balancer or network load balancer is not managed by Kubernetes Engine and might cause lifecycle and governance issues.

### Required IAM Policies for Specifying Load Balancer and Network Load Balancer Compartments

To specify an alternative compartment in which to create the load balancer or network load balancer, you must give the cluster permission to inspect, manage, and use other resources by specifying policy statements similar to the following:

```

```

where`<compartment-ocid>`is the OCID of the compartment in which to create the load balancer or network load balancer.

If you consider these policy statements to be too permissive, you can restrict the permissions in either or both of the following ways:
- 

By explicitly specifying the compartment OCID of the cluster that is to create the load balancer or network load balancer. For example:

```

```

- 

By explicitly specifying the OCID of the cluster that is to create the load balancer or network load balancer. For example:

```

```

Note that although it is Kubernetes Engine that initiates the creation of the load balancer or network load balancer, the IAM policies reference the cluster as the resource principal making the OCI API requests.

## Configuring Cookie-Based Session Persistence for Load Balancers

When Kubernetes Engine provisions an OCI load balancer for a Kubernetes service of type`LoadBalancer`, you can configure session persistence ("sticky sessions") to ensure that requests from the same client are consistently routed to the same backend server.

Session persistence is useful for applications that maintain client state on backend servers.

OCI load balancers support two types of cookie-based session persistence:
- Application cookie persistence : The backend application sets and manages the cookie.
- Load balancer cookie persistence : The load balancer sets and manages the cookie.

For more information about OCI load balancer support for cookie-based session persistence, see[Load Balancer Session Persistence](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm).

You configure session persistence by adding one of two persistence annotations to the metadata section of the service manifest.

Note the following:
- Session persistence is supported for load balancers (`oci.oraclecloud.com/load-balancer-type: "lb"`).
- Session persistence is not supported for network load balancers (`oci.oraclecloud.com/load-balancer-type: "nlb"`). If session persistence annotations are specified for network load balancers, the annotations are ignored.
- The two persistence annotations are mutually exclusive. If both are specified, the service fails to reconcile.
- If no persistence annotation is specified, session persistence is disabled.

### Configuring application cookie persistence

To configure application cookie persistence, add the following annotation in the metadata section of the manifest file:
```

```

where`<json>`defines the application cookie persistence configuration.

For example:
```

```

Optional fields you can include to control cookie behavior include:
- `cookieName`to specify the name of the cookie set by the application.
- `disableFallback`to specify whether fallback behavior is disabled if the cookie is not present.

For more information about OCI load balancer support for application cookie persistence, see[Application Cookie Stickiness](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm#app-cookie-stickiness).

### Configuring load balancer cookie persistence

To configure load balancer cookie persistence, add the following annotation in the metadata section of the manifest file:
```

```

where`<json>`defines the load balancer cookie persistence configuration.

For example:
```

```

In this example, the load balancer manages the cookie used to maintain session persistence.

Optional fields you can include to control cookie behavior include:
- `cookieName`
- `disableFallback`
- `domain`
- `path`
- `maxAgeInSeconds`
- `isSecure`
- `isHttpOnly`

For more information about OCI load balancer support for load balancer cookie persistence, see[Load Balancer Cookie Stickiness](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm#lb-cookie-stickeiness).

### Validation rules

When configuring session persistence, note the following validation rules:
- If both persistence annotations are specified, configuration fails.
- If the JSON value in the annotation is malformed, configuration fails.
-
