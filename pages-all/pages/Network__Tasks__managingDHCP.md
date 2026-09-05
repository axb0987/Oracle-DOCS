# DHCP Options
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm
- Fetched: 2026-09-05 02:45 CDT

# DHCP Options

This topic describes how to manage the Dynamic Host Configuration Protocol (DHCP) options in a Virtual Cloud Network (VCN).

## Overview of DHCP Options

The Networking service uses DHCP to automatically provide configuration information to instances when they boot up. Although DHCP lets you change some settings dynamically, others are static and never change. For example, when you create a Compute instance, either you or Oracle specifies the instance's private IP address. Each time the instance boots up or the instance's DHCP client restarts, DHCP passes that same private IP address to the instance. The address never changes during the instance's lifetime.

The Networking service provides DHCP options to let you control certain types of configuration on the instances in the VCN. You can change the values of these options at any time, unlike the static information that DHCP provides to the instance. The changes take effect the next time the instance's DHCP client restarts or the instance reboots. For more details, see[Important Notes about Instances and DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/managingDHCP.htm#Importan).

Each subnet in a VCN can have a single set of DHCP options associated with it. That set of options applies to all instances in the subnet. Each VCN comes with a default set of DHCP options with initial values that you can change. If you don't specify otherwise, every subnet uses the VCN's default set of DHCP options.

The following table summarizes the available DHCP options you can configure.

DHCP Option Possible Values Initial Value in the Default DHCP Options Notes
Domain Name Server

[DNS Type](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#Choices):
- Internet and VCN Resolver
- Custom Resolver DNS Type = Internet and VCN resolver. For more information, see[Choices for DNS in a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#Choices).

If you set DNS Type = Custom Resolver, you can specify up to three DNS servers. For more information, see[Choices for DNS in a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#Choices).

By default, the Internet and VCN resolver listens on 169.254.169.254. (IPv4) and fd00:00c1::a9fe:a9fe (IPv6).
Search Domain A single search domain

If the VCN is set up with a DNS label, the default value for the Search Domain option is the[VCN domain name](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#About)(`<VCN DNS label> .oraclevcn .com`). Otherwise, the Search Domain option isn't present in the default set of DHCP options.

In general, when any set of DHCP options is initially created (the default set or a custom set you create), the Networking service automatically adds the Search Domain option and sets it to the VCN domain name (`<VCN_DNS_label> .oraclevcn .com`) if all conditions are met :
- The VCN has a DNS label.
- DNS Type = Internet and VCN Resolver.
- You didn't specify a search domain during creation of the set of DHCP options.

After the set of DHCP options is created, you can always remove the Search Domain option or set it to a different value.

You can specify only a single search domain in a set of DHCP options.

## Working with DHCP Options

When you create a subnet, you specify which set of DHCP options to associate with the subnet. If you don't, the default set of DHCP options for the VCN is used. You can[change which set of DHCP options the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#change_subnet_dhcp_options)at any time.

When creating a new set of DHCP options, you can optionally assign it a friendly name. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the set of options a unique identifier called an Oracle Cloud ID (OCID). For more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You can change the values of an individual DHCP option in a set, but notice that when you use the REST API to update a single option in a set, the new set of options replaces the entire existing set.

To delete a set of DHCP options, it must not be associated with a subnet yet. You can't delete a VCN's default set of DHCP options.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

### Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).

## Important Notes about Instances and DHCP Options

Whenever you change the value of one of the DHCP options, you must do one of the following for the change to take effect on existing instances in the subnets associated with that set of DHCP options: either restart the DHCP client on the instance, or reboot the instance.

Ensure that the DHCP client keeps running so you can always access the instance. If you stop the DHCP client manually or disable NetworkManager (which stops the DHCP client on Linux instances), the instance can't renew its DHCP lease and becomes inaccessible when the lease expires (typically within 24 hours). Don't disable NetworkManager unless you use another method to ensure renewal of the lease.

Stopping the DHCP client might remove the host route table when the lease expires. Also, loss of network connectivity to iSCSI connections might result in loss of the boot drive.

Any changes you make to the`/etc/resolv.conf`file are overwritten whenever the DHCP lease is renewed or the instance is rebooted.

Changes you make to the`/etc/hosts`file are overwritten whenever the DHCP lease is renewed or the instance is rebooted. To persist changes to the`/etc/hosts`file in Oracle Linux or CentOS instances, add the following line to`/etc/oci-hostname.conf`:

```

```

If the`/etc/oci-hostname.conf`file doesn't exist, create it.

## Using the Console

[To list a VCN's DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#)

- On the Virtual Cloud Networks list page, select the VCN that contains the DHCP options you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- On the IP Administration tab, go to the DHCP Options section.
- Under Resources , select DHCP Options .

The default set and its details are displayed in the list.

[To update options in an existing set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#)

- On the Virtual Cloud Networks list page, select the VCN that contains the DHCP options you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- On the IP Administration tab, go to the DHCP Options section.
- Under Resources , select DHCP Options .
- 

For the set you're interested in, select the Actions menu (three dots) , and then select Edit
- For DNS Type : If want instances in the subnet to resolve internet hostnames and hostnames of instances in the VCN, select Internet and VCN Resolver . Or to use a specific DNS server, select Custom Resolver and then enter the server's IP address (three servers maximum). For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).
- For Search Domain : If you want instances in the subnet to append a particular search domain when resolving DNS queries, enter it here. If the Search Domain option is already set to the[VCN domain name](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#About)and you're not sure why, see the details in[Overview of DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#overview).
- When you're done, select Save Changes .
- If you have any existing instances in a subnet that uses this set of DHCP options, ensure that you restart the DHCP client on each affected instance, or reboot the instance itself so that it picks up the new setting.

[To create a new set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#)

- On the Virtual Cloud Networks list page, select the VCN that contains the DHCP options you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- On the IP Administration tab, go to the DHCP Options section.
- Under Resources , select DHCP Options .
- Select Create DHCP Options .
- Enter a friendly name. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the DHCP Options in. Select another compartment if needed.
- Select a DNS Type . If want instances in the subnet to resolve internet hostnames and hostnames of instances in the VCN, select Internet and VCN Resolver . To use a specific DNS server, select Custom Resolver and then enter the server's IP address (three servers maximum). For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).
- Enter a Search Domain . If you want instances in the subnet to append a particular search domain when resolving DNS queries, enter it here. Be aware that the Networking service automatically sets the Search Domain option in certain situations. See the details in[Overview of DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#overview).
- 

(Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- When you're done, select Create DHCP Options .

The set of options is created and then displayed on the DHCP Options list. You can now specify this set of options when creating or updating a subnet.

[To change which set of DHCP options a subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#)

- On the Virtual Cloud Networks list page, select the VCN that contains the DHCP options you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:.
- On the details page, select the Subnets tab.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN.
- Find the subnet in the Subnets list, select the Actions menu (three dots) for it, and then select Edit .
- In the DHCP Options section, select the new set of DHCP options you want the subnet to use.
- 

Select Save Changes .

The changes take effect within a few seconds.

[To move a set of DHCP options to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#)

You can move a set of DHCP options from one compartment to another. When you move a set of DHCP options to a new compartment, inherent policies apply immediately.
- On the Virtual Cloud Networks list page, select the VCN that contains the DHCP options you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- On the IP Administration tab, go to the DHCP Options section.
- Under Resources , select DHCP Options .
- For the set you're interested in, select the Actions menu (three dots) , and then select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .

For more information about using compartments and policies to control access to a VCN, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

[To delete a set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#)

Prerequisite: To delete a set of DHCP options, it must not be associated with a subnet yet. You can't delete the default set of DHCP options in a VCN.
- On the Virtual Cloud Networks list page, select the VCN that contains the DHCP options you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- On the IP Administration tab, go to the DHCP Options section.
- Under Resources , select DHCP Options .
- For the set you want to delete, select the Actions menu (three dots) , and then select Terminate .
- Confirm when prompted.

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To manage a VCN's DHCP options, use these operations:
- [ListDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/ListDhcpOptions)
- [GetDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/GetDhcpOptions)
- [UpdateDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/UpdateDhcpOptions)
- [CreateDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/CreateDhcpOptions)
- [DeleteDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/DeleteDhcpOptions)
- [ChangeDhcpOptionsCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/ChangeDhcpOptionsCompartment)
