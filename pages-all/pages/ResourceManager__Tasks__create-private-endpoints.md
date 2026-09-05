# Creating a Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Private Endpoint

Create a private endpoint in Resource Manager.

## Before You Begin

Gather the network information that you need:
- 

[Virtual cloud network (VCN) and subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)
- 

The private endpoint connection is at the VCN level. If you have many subnets per VCN, you need to create only one private endpoint for that VCN. Ensure that security rules meet your requirements.
- 

[Network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)(optional)
- 

[DNS zones](https://docs.oracle.com/iaas/Content/DNS/Concepts/gettingstarted.htm)(optional, for private Git servers)

For example, for a private Git server at`https://privateGitServer.examplesub.exampledomain`, create a DNS zone for`examplesub.exampledomain`.

Additionally:
- Ensure that the subnet allows access to the private resource: Set up a[security rule](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm#rules)for ingress.
- Ensure that the subnet has available IP addresses.

If no IP addresses are available in the specified subnet, then the work request for creating the private endpoint[fails](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Troubleshoot/pe-work-request-fails.htm).
- For private Git servers, import the certificates you want to use. See the[GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#import-cert)and[GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#import-cert)instructions.

## Using a Terraform Configuration

Create a private endpoint by using a Terraform configuration.

- To create a stack that creates a Resource Manager private endpoint, use the Resource Manager create private endpoint[template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Reference/templates.htm).
- 

For example Terraform configurations that use Resource Manager private endpoints, see[Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager). Also, review[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm).

- Add code to the Terraform configuration that creates a private endpoint.
For an example, see[Example Usage (oci_resourcemanager_private_endpoint)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/resourcemanager_private_endpoint#example-usage).
- [Create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm)that references this Terraform configuration.
- [Run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)on the stack.
A work request for creation runs, and then the private endpoint is created. You can now[reference](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm#tf-config-ref)the private endpoint from any Terraform configuration or[configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#)
- 

To create a private endpoint by using the Console, follow these steps.

- On the Private endpoints list page, select Create private endpoint . If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- In the Create private endpoint panel, enter a name and optional description for the private endpoint. Avoid entering confidential information.
- Select the compartment that you want to store the private endpoint in.
- Enter the following values:

- Virtual cloud network : The virtual cloud network (VCN) to use with the private endpoint. See[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm). To select a VCN in a different compartment, select Change Compartment .
- Subnet : The subnet to use with the private endpoint. See[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm). To select a subnet in a different compartment, select Change Compartment .
- Allow this private endpoint to be used with a configuration source provider : When enabled, allows use with[configuration source providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/managingconfigurationsourceproviders.htm)(for example, private Git servers). If you enable this option, it can't be disabled after the endpoint is created.
- DNS zones : The DNS zones to use with the private endpoint. This field is displayed when Allow this private endpoint to be used with a configuration source provider is selected. For more information about DNS zones, see[Public DNS](https://docs.oracle.com/iaas/Content/DNS/Concepts/gettingstarted.htm).
- Network security groups : The[network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)to use with the private endpoint. To select a NSG in a different compartment, select Change Compartment .
- (Optional) Add one or more security attributes to the private endpoint: Select Show advanced options to show security attribute options.
If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- (Optional) Add one or more tags to the private endpoint: Select Show advanced options to show tagging options.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
The new private endpoint appears on the Private endpoints list page. While the work request for creation runs, the new private endpoint's status is Creating , and the new private endpoint's[details page](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm)shows the work request in progress. When the work request reaches succeeded status, the new private endpoint's status is Active .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/create.html)oci resource-manager private-endpoint create`command to create a private endpoint.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/CreatePrivateEndpoint)operation to create a private endpoint.

## What's Next

To troubleshoot a failed work request for creation of a private endpoint, see[Private Endpoint Work Request Fails](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Troubleshoot/pe-work-request-fails.htm)
