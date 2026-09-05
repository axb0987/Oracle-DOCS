# Managing Private Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm
- Fetched: 2026-09-05 02:56 CDT

# Managing Private Endpoints

Create, edit, and delete private endpoints in Resource Manager.

With private endpoints, you can access nonpublic cloud resources in your tenancy from Resource Manager. For example, configure a private compute instance using Terraform's remote exec functionality and access Terraform configurations in a private GitHub server.

You can perform the following tasks with private endpoints:
- [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm)
- [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-private-endpoints.htm)
- [Getting a Private Endpoint's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-private-endpoints.htm)
- [Getting the Reachable IP Address for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-private-endpoint-reachable-ip.htm)
- [Updating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-private-endpoints.htm)
- [Managing Security Attributes for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-private-endpoint-security.htm)
- [Moving a Private Endpoint to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/move-private-endpoints.htm)
- [Deleting a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/delete-private-endpoints.htm)

## Required IAM Policy

To manage private endpoints, you must have permission to manage private endpoints in the tenancy, and to use virtual network resources, such as VCNs and subnets. For more information, see[Manage Private Templates](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__templates).

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).

## Scenarios

Review common scenarios for using private endpoints with Resource Manager.

Other scenarios also exist. You can reach any private resource with a private IP, using a private endpoint in Resource Manager. For example, connect to a[Kubernetes cluster](https://docs.oracle.com/iaas/Content/ContEng/home.htm).

### Private Git Server

Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.

- If the private server is on-premises, then set up site-to-site VPN or FastConnect.
For more information, see[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)and[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).
- Import the private Git server's associated SSL certificate into the Certificates service.

For more information, see the relevant page:
- [Bitbucket Server prerequisites
- [GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#import-cert)
- [GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#import-cert)
- [Create a private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm)
- [Get the reachable IP address for the private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm)
- [Create a configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm)that references this private endpoint (and the associated SSL certificate that you imported into the Certificates service).
- [Create a stack that references this configuration source provider.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm)

### Private Remote Exec

Access private instances with Remote Exec.

Note  
  
When accessing a private instance with Remote Exec, note the following points:
- You must use a reachable IP address.
- You might need to configure[security rules](https://docs.oracle.com/iaas/private-cloud-appliance/cmn/network/security-rules.htm)to allow Remote Exec access to private instances.

See also[Getting the Reachable IP Address for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm).

- Write a Terraform configuration that creates a private instance.
- In the Terraform configuration, either create or reference a private endpoint:
- [Add code to your Terraform configuration to create the private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#tf-config-create)
Note  
  
You can also create a private endpoint using the Console, SDK, CLI, or API. See[Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm).
- [Add code to your Terraform configuration to reference an existing private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm#tf-config-ref)

For example Terraform configurations that use Resource Manager private endpoints, see[Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager).
- Add code to your Terraform configuration to convert the private IP address to a reachable IP address.

The reachable IP address is in the range 240.0.0.0 to 255.255.255.255[(Class E; see RFC 1112, Section 4)](https://tools.ietf.org/html/rfc1112).

To get the reachable IP address, see[Getting the Reachable IP Address for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm).

[Example code](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#)

```

```

For example Terraform configurations that use Resource Manager private endpoints, see[Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager).
- Store the Terraform configuration in a[supported location](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm#sources).
- [Create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm)that references this Terraform configuration.
- [Run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)on the stack.
The private instance and private endpoint are created. You can now use[Remote Exec](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/usingremoteexec.htm)to access your private instance.

## Managing Security Attributes

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
