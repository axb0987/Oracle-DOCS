# Cloud Shell Networking
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm
- Fetched: 2026-09-05 01:35 CDT

# Cloud Shell Networking

This section describes the three networking modes provided by Cloud Shell.
- [OCI Service Network](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm#cloudshellintro_topic-Cloud_Shell_OCI_Service_Network): this is the default mode, and provides access only to other OCI resources in your home region for your tenancy
- [Cloud Shell Public Network](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm#cloudshellintro_topic-Cloud_Shell_Public_Network): this networking mode allows access to the public internet, but must be enabled by your administrator
- [Private Network Access](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm#Cloud_Shell_Private_Access): a configurable network that allows you to access resources in your private network without having the network traffic flow over public networks

The networking mode for your Cloud Shell session depends on how your administrator has configured your Identity policy.

## Cloud Shell OCI Service Network

The Cloud Shell OCI Service Network allows you to access OCI wide services without providing access to the public internet. This is the default Cloud Shell network access if your administrator hasn't configured an Identity policy.

If your administrator hasn't[set up an Identity policy](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm#cloudshellintro_topic-Cloud_Shell_Public_Network), you will see the following dialog when Cloud Shell starts:

Cloud Shell restricted network dialog

Select Private Network to connect to or create and configure a new[Private Network](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm#Cloud_Shell_Private_Access), or select OCI Service Network to keep the default setting.

## Cloud Shell Public Network

Cloud Shell Public Network allows access to the public Internet from your Cloud Shell session.
Note  
  
Your administrator must configure access to the Cloud Shell Public Network using an Identity policy.

### Requirements and IAM Policy

To allow users to access the Cloud Shell managed Public Network, you'll need to grant user access by using an Identity policy.
The resource name for Cloud Shell managed Public Network is `cloud-shell-public-network`. The following is an example policy to grant access to Cloud Shell Public Network:
```

```

Note  
  
Public network IAM policies and Security Zone policies may take up to 24 hours to take effect for existing Cloud Shell Sessions. You can enact policy updates immediately by restarting your Cloud Shell from the Actions menu. If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

Cloud Shell Administrators can use the Cloud Shell Security Zone policy to restrict Public Network usage for all users in the tenancy (including tenancy administrators) regardless of the IAM policy. Security zone policy restricts cloud shell managed Public Network usage for all users in the tenancy including tenancy administrators. See[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/security-zones.htm)for more details.

## Cloud Shell Private Networking

Cloud Shell Private Networking allows you to connect a Cloud Shell session to a private network so you can access resources in your private network without having the network traffic flow over public networks. Examples of where Private Networking can be useful include using it to SSH into compute instances inside of a private network or managing a private OKE cluster.
Note  
  
A Cloud Shell instance is a private instance, and works like a private instance for the purposes of network setup. Using only an internet gateway will not allow egress to the internet from a private subnet - you must use a service gateway or a NAT gateway. For more information, see the[Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)documentation.

### Requirements and IAM Policy

To use Private Networking, you (or an administrator) will need to specify the following policies:
- 
```

```

- 
```

```

- 
```

```

- 
```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

You also need to create private VCNs and Subnets in the appropriate compartments. For more information, see[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm)in the[Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm)documentation.

### Cloud Shell Private Networking Limitations
When using Private Networking, keep the following limitations in mind:
- You'll need to create private VCNs and Subnets in the appropriate compartments. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)in the[Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm)documentation.
- You can have up to 5 favorite private networks assigned.
- A temporary ephemeral network is only valid for the length of your Cloud Shell session, and will not be persisted to your list of defined private networks.
- Only VCNs and Subnets in your home region are available for creating a Private Network. If you need to access a subnet in a region that is not your home region, you can use peering from the subnet used by Private Networking to reach it. For more information, see[VCN Cross-Region Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions).
- A subnet chosen for a Cloudshell Private Network must have at least one non-reserved IP address for the subnet's CIDR block available. If all non-reserved IP addresses have been allocated, Cloudshell cannot attach to that subnet.
- A subnet can only have a maximum of 5 associated network security groups.
- Resolving endpoints through custom DNS resolvers is not supported.

### Using Cloud Shell Private Networking

This section covers how to use Cloud Shell Private Networking.

### Selecting a Network

To change which network your Cloud Shell session is using, use the drop-down Network menu at the top of the Cloud Shell terminal window:

The network selection menu appears:

From this menu you can select a network connection, access the list of private network definitions, or create an ephemeral (temporary) private network.

### Using the Private Network Definition List

The Private Network Definition List item on the network selection menu displays the Private Network Definition List panel:

This panel allows you to create or modify private networks, designate favorite private networks, and select a default network.

Designating favorite networks

You can designate up to 5 favorite networks. To designate a network as a favorite, click the star in the Favorite column.

Selecting a default network

You can select a default network from the drop-down list in the Default network panel. This is the network that's used when a new Cloud Shell session starts.

### Creating a new private network definition
You can create a new private network definition by clicking the Create private network definition button. This brings up the Create Private Network Definition panel.
Note  
  
To create a temporary ephemeral network, select Ephemeral Private Network Setup from the network selection drop-down. This is temporary network and only valid for the length of the Cloud Shell session, and isn't persisted to the list of defined private networks. To use security attributes for[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/overview.htm), create a Private Network Definition instead of ephemeral network.

Enter a name for the private network definition in the Name text box.
Select the VCN and the Subnet to use from the drop-down list boxes. You can also optionally select one or more Network Security groups to use.
Note  
  

Only VCNs and Subnets in the home region are available. If you need to access a subnet in a region that's not the home region, you can use peering from the subnet used by Private Networking to reach it. For more information, see[VCN Cross-Region Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions).

A subnet chosen for a Cloudshell Private Network must have at least one non-reserved IP address for the subnet's CIDR block available. If all non-reserved IP addresses have been allocated, Cloudshell can't attach to that subnet.

In addition, if the network has OCI[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/overview.htm)setup and enabled, you can select a maximum of three security attributes to apply to the VNIC that egresses to the network.
Note  
  

To use security attributes with Cloud Shell Private Network access, you must add the following IAM policy to the tenancy:

```

```

To access OCI services from a Cloud Shell terminal with security attributes applied, add a[Zero Trust Packet Routing policy](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/zpr-policy-syntax.htm)that targets`osn-services-ip-addresses`.

To set this definition as the active network, enable the Use as active network checkbox.

Click the Create button to create the Cloud Shell private network definition.

If you selected the Use as active network checkbox, the Cloud Shell session is connected to the private network, as indicated in the Network drop-down at the top of the Cloud Shell terminal session:

You can see details about the private network connection by clicking the Details link:
