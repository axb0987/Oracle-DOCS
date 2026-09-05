# Public IP Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm
- Fetched: 2026-09-05 02:41 CDT

# Public IP Pools

Learn how to manage public IP address pools in a virtual cloud network.

A public IP pool is a set of IPv4 CIDR blocks allocated to a tenancy. These CIDR blocks can be all or part of a BYOIP CIDR block. Public IP CIDR blocks assigned to a pool are only available for your tenancy. Public IP pools are available as a source for IP allocation when launching a NAT gateway, load balancer, or compute instance. You can add more IP CIDR blocks to a public IP pool at any time. You can also:
- Create a Reserved IP : You can reserve individual IPs from your public IP pools. These reserved IP addresses can be attached to your resources.
- Direct launch from pool : You can launch resources with an IP directly allocated from a public IP pool without previously creating a reserved IP for that resource.
- Delete CIDR blocks and pools : You can delete the entire public IP pool or certain IP CIDR blocks within the pool, provided none of the IP addresses are currently attached or reserved.
Note  
  
IPv6 addresses don't use the IP Pools functionality described here. Instead, you can directly assign IPv6 prefixes to VCNs and subnets.

## Requirements and Preparation

- To use public IP pools with BYOIP addresses, you need to import your addresses.
- To reserve Oracle-supplied public IP addresses, select "Oracle" as the public IP pool when creating the reserved public IP address.

## Limits and Quotas

- You can create one or up to 10 public IP pools in a compartment.
- A public IP pool can have zero or more IP CIDR ranges assigned to it, with a minimum size of /28 to a maximum size of /24.

See[IP Management Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#byoip_limits)for general information and[requesting a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)when necessary.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/overview.htm#Policies).

## Limits on IAM Resources

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm), see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

## Managing IP Pools Using the Console

[To view your public IP pools](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#)

- Confirm you're viewing the region and compartment you're interested in.
- Open the navigation menu and select Networking . Under IP management , select Public IP pools .

The Public IPv4 pools page lists all the public IP pools in the selected compartment.

[To create a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#)

- Confirm you're viewing the region and compartment you're interested in.
- Open the navigation menu and select Networking . Under IP management , select Public IP pools .
- Select Create public IP pool .
- Enter the following information:
- A name for the pool. Avoid entering confidential information.
- The compartment in which you want to create the public IP pool, which could be different from the compartment you're working in.
- (Optional) In the Tags section, add one or more tags for the pool.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create public IP pool .

[To delete a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#)

You can't delete a public IP pool that contains reserved public IP addresses currently in use.
- Confirm you're viewing the region you're interested in.
- Open the navigation menu and select Networking . Under IP management , select Public IP pools .
- Select the Actions menu (three dots) for the public IP pool that you want to delete, and then select Delete public IP pool .
- If there're no warnings or errors, select Delete public IP pool . If this public IP pool contains reserved public IP addresses in use, you can't delete the public IP pool.

[To rename a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#)

- Confirm you're viewing the region and compartment you're interested in.
- Open the navigation menu and select Networking . Under IP management , select Public IP pools .
- Select the Actions menu (three dots) for the public IP pool that you want to rename, and then select Rename .
- Enter a new name for the public IP pool. Avoid entering confidential information.
- Select Update .

[To reserve a public IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#)

- Confirm you're viewing the region you're interested in.
- Open the navigation menu and select Networking . Under IP management , select Public IP pools .
- Select the public IP pool that you want to reserve a public IP for.
- On the IPv4 management tab, in the Reserved public IPv4 address section select the Reserved public IP address .
- (Optional) In the Tags section, add one or more tags for the public IP address.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Reserve public IP address .

[To move a public IP pool to another compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#)

- Confirm you're viewing the region you're interested in.
- Open the navigation menu and select Networking . Under IP management , select Public IP pools .
- Select the Actions menu (three dots) (three dots) for the public IP pool that you want to move, and then select Move resource .
- Select a new compartment for the public IP pool.
- Select Move resource .

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To manage the[Public IP Pool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool)object, use these operations:
- [AddPublicIpPoolCapacity](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/AddPublicIpPoolCapacity)
- [ChangePublicIpPoolCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/ChangePublicIpPoolCompartment)
- [CreatePublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/CreatePublicIpPool)
- [DeletePublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/DeletePublicIpPool)
- [GetPublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/GetPublicIpPool)
- [ListPublicIpPools](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/ListPublicIpPools)
- [RemovePublicIpPoolCapacity](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/RemovePublicIpPoolCapacity)
- [UpdatePublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/UpdatePublicIpPool)
