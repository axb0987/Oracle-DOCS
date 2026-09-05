# Creating an IPSec Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm
- Fetched: 2026-09-05 02:44 CDT

# Creating an IPSec Connection

The Site-to-Site VPN service lets you create an IPSec connection containing IPSec tunnels that securely connect Oracle Cloud Infrastructure to an on-premises network.

Before you create an IPSec connection for Site-to-Site VPN, review[Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)and plan the Site-to-Site VPN. Also, review[Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm#)
- 

## Enter IPSec Connection Information

This section discusses basic information for the IPSec connection. The following sections cover specifics that depend on which of the three routing types you select for that tunnel.

You can think of an "IPSec connection object" as something that contains its own metadata, and the configuration information for IPSec tunnels it contains.

- On the Site-to-Site VPN list page, select Create IPSec connection . If you need help finding the list page, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- Enter a descriptive name for the IPSec connection. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Select a compartment for the IPSec connection. The default is the most recently used compartment, and is likely to be the same compartment as the VCN containing the resources you want to make available to the on-premises network.
- Select the compartment containing the CPE object to associate with the IPSec connection, then select the CPE object.
If you're configuring[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec), the CPE you select must have a label confirming that IPSec over FastConnect is enabled for that CPE. BGP routing is preferred for connections that use IPSec over FastConnect.
- If the CPE is behind a NAT device, select the appropriate checkbox.

If the checkbox is selected, provide the following information:
- CPE IKE Identifier Type: Select the type of identifier that internet key exchange (IKE) uses to identify the CPE device. Either an FQDN or an IPv4 address can be an identifier.
- CPE IKE Identifier: Enter the information that IKE uses to identify the CPE device. Oracle defaults to using the public IP address of the CPE. If the[CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/overviewIPsec.htm#components), you might need to enter a different value. You can either enter the new value here, or[change the value](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/workingwithIPsec.htm#edit_cpe_ike_id)later.
- Select the compartment containing the DRG to associate with the IPSec connection, then select the DRG. This DRG must already be attached to the VCN that you want to make available to an on-premises network.
- (Optional) If you intend to use static routing for any of the tunnels, enter at least one route in the Routes to your on-premises Network field. Otherwise, skip this option.
You can enter up to 10 static routes, and you can[change the static routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route)later. The routes correspond with VCN CIDRs you want the on-premises network to connect with.

Next, configure the two IPSec tunnels. If the actual CPE device only supports a single IPSec tunnel per connection, configuring tunnel 2 is optional. How you configure the tunnels depends on the routing method you planned to use, so select the matching section.

[Configure a Tunnel for BGP Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm#)

## Configure a Tunnel for BGP Routing

Enter the following information in the appropriate section for tunnel 1 and tunnel 2.

- Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- (Optional) Select the checkbox and enter a custom shared secret.
By default, Oracle provides the shared secret for the tunnel. To provide it yourself, select this checkbox and enter the shared secret. You can[change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/workingwithIPsec.htm#edit_shared_secret).
- Select the Internet Key Exchange (IKE) version to use for this tunnel. Only select[IKEv2](https://tools.ietf.org/html/rfc7296)if the CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
- Select BGP dynamic routing as the routing type.
- If the CPE selected earlier supports[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec), the following settings are required:

- Oracle tunnel headend IP: Enter the IP address of the Oracle IPSec tunnel endpoint (the VPN headend). Oracle advertises the VPN IP as a /32 host route by using the FastConnect BGP session. If any addresses overlap with a VCN route this takes precedence because of longest prefix match.
- Associated virtual circuit: Select a virtual circuit that was enabled for IPSec over FastConnect when it was created. The tunnel gets mapped to the chosen virtual circuit and the defined headend IP are only reachable from on-premises through the associated virtual circuit.
- DRG route table: Select or create a DRG route table. To prevent any issues with recursive routing, the virtual circuit attachment and the IPSec tunnel attachment used for IPSec over FastConnect must use different DRG route tables.
- Enter the on-premises network's BGP ASN.
- Enter the BGP IPv4 address with subnet mask (either /30 or /31) for the CPE end of the tunnel (the IPv4 inside tunnel interface - CPE ). For example: 10.0.0.16/31. The IP address must be part of Site-to-Site VPN's encryption domain.
- Enter the BGP IPv4 address with subnet mask (either /30 or /31) for the Oracle end of the tunnel (the IPv4 inside tunnel interface - Oracle ). For example: 10.0.0.17/31. The IP address must be part of Site-to-Site VPN's encryption domain.
- (Optional) If you plan to use both IPv6 and IPv4, select Enable IPv6 and enter the following details:

- IPv6 Inside Tunnel Interface - CPE: Enter the BGP IPv6 address with subnet mask (/126) for the CPE end of the tunnel. For example: 2001:db2::6/126. The IP address must be part of Site-to-Site VPN's encryption domain.
- IPv6 Inside Tunnel Interface - Oracle: Enter the BGP IP address with subnet mask (/126) for the Oracle end of the tunnel. For example: 2001:db2::7/126. The IP address must be part of Site-to-Site VPN's encryption domain.
- (Optional) If you select Show Advanced Options you can change the following settings for the tunnel:

- Oracle IKE Initiation: This setting indicates whether the Oracle end of the IPSec connection can start up the IPSec tunnel. The default is Initiator or Responder . You can also decide to set the Oracle end to be a responder only which would require the CPE device to start the IPSec tunnel. We recommend leaving this option at the default setting.
- NAT-T Enabled: This setting indicates whether the CPE device is behind a NAT device. The default is Auto . The other options are Disabled and Enabled . We recommend leaving this option at the default setting.
- Enable Dead Peer Detection Timeout: When you select this option, you can periodically check the stability of the connection to the CPE, and detect that the CPE has gone down. If you select this option you can also select the longest interval between CPE device health messages before the IPSec connection indicates that it has lost contact with the CPE. The default is 20 seconds. We recommend leaving this option at the default setting.
- (Optional) If you expand the Phase One (ISAKMP) Configuration section and select Set custom options , you can set the following optional settings (you must select one of each option):

- Custom Encryption Algorithms: You can select from the options provided in the pull-down menu.
- Custom Authentication Algorithms: You can select from the options provided in the pull-down menu.
- Diffie-Hellman Groups: You can select from the options provided in the pull-down menu.

If the Set custom configurations checkbox isn't selected, the default settings are proposed. You can still select the IKE Session Key Lifetime in Seconds . The default is 28800 which is equal to 8 hours.

To understand these options in more detail including the default proposals, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).
- If you expand the Phase Two (IPSec) Configuration options and select Set custom options , you can set the following optional settings for the tunnel (you must select an encryption algorithm):

- Custom Encryption Algorithms: You can select from the options provided in the pull-down menu. If you select an AES-CBC encryption algorithm, you must also select an authentication algorithm.
- Custom Authentication Algorithms: You can select from the options provided in the pull-down menu. The encryption algorithm you chose might have built-in authentication, in which case no selectable option is available.

If the Set custom configurations checkbox isn't selected, the default settings are proposed. You can still change the following settings:
- IPSec Session Key Lifetime in Seconds: The default is 3600 which is equal to 1 hour.
- Enable Perfect Forward Secrecy: By default, this option is on. It lets you select the Perfect Forward Secrecy Diffie-Hellman Group . You can select from the options provided in the pull-down menu. If you don't make a selection, GROUP5 is proposed.

For all Phase Two options, selecting a single option overrides the default set and is the only option proposed to the CPE device.
- For Tunnel 2 you can use the same options described for Tunnel 1. You can also select different options or decide to leave the tunnel unconfigured because the CPE device only supports a single tunnel.
- When finished, select Create IPSec Connection .
- Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location so you can deliver it to the network engineer who configures the CPE device.

You can view this tunnel information here in the Console at any time.

The IPSec connection is created and displayed on the page. It stays in the Provisioning state for a short period.

The displayed tunnel information includes:
- The Oracle VPN IPv4 or IPv6 address (for the Oracle VPN headend).
- The tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. The network engineer must configure the CPE device before the tunnel or tunnels can be established.
- The tunnel's BGP status. At this point, the status is Down. The network engineer must configure the CPE device.

To view the tunnel's shared secret, select the tunnel to view its details, and then select Show next to Shared Secret .

You can also select the Phase Details tab to see the Phase One (ISAKMP) and Phase Two (IPSec) details for the tunnel.

By now you have created all the components required for Site-to-Site VPN. Next, the on-premises network engineer must configure the CPE device before network traffic can flow between the on-premises network and a VCN.

For more information, see[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm).

[Configure a Tunnel for Static Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm#)

## Configure a Tunnel for Static Routing

Note  
  
We recommend that you use BGP route-based IPSec connections for IPSec over FastConnect.

Enter the following information in the appropriate section for tunnel 1 and tunnel 2.

- Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- (Optional) Select the checkbox and enter a custom shared secret.
By default, Oracle provides the shared secret for the tunnel. To provide it yourself, select this checkbox and enter the shared secret. You can[change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/workingwithIPsec.htm#edit_shared_secret).
- Select the Internet Key Exchange (IKE) version to use for this tunnel. Only select[IKEv2](https://tools.ietf.org/html/rfc7296)if the CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
- Select Static routing as the routing type.
- Enter the BGP IPv4 address with subnet mask (either /30 or /31) for the CPE end of the tunnel (the IPv4 inside tunnel interface - CPE ). For example: 10.0.0.16/31. The IP address must be part of Site-to-Site VPN's encryption domain.
- Enter the BGP IPv4 address with subnet mask (either /30 or /31) for the Oracle end of the tunnel (the IPv4 inside tunnel interface - Oracle ). For example: 10.0.0.17/31. The IP address must be part of Site-to-Site VPN's encryption domain.
- (Optional) If you plan to use both IPv6 and IPv4, select Enable IPv6 and enter the following details:

- IPv6 Inside Tunnel Interface - CPE: Enter the BGP IPv6 address with subnet mask (/126) for the CPE end of the tunnel. For example: 2001:db2::6/126. The IP address must be part of Site-to-Site VPN's encryption domain.
- IPv6 Inside Tunnel Interface - Oracle: Enter the BGP IP address with subnet mask (/126) for the Oracle end of the tunnel. For example: 2001:db2::7/126. The IP address must be part of Site-to-Site VPN's encryption domain.
- (Optional) If you select Show Advanced Options you can change the following settings for the tunnel:

- Oracle IKE Initiation: This setting indicates whether the Oracle end of the IPSec connection can start up the IPSec tunnel. The default is Initiator or Responder . You can also decide to set the Oracle end to be a responder only which would require the CPE device to start the IPSec tunnel. We recommend leaving this option at the default setting.
- NAT-T Enabled: This setting indicates whether the CPE device is behind a NAT device. The default is Auto . The other options are Disabled and Enabled . We recommend leaving this option at the default setting.
- Enable Dead Peer Detection Timeout: When you select this option, you can periodically check the stability of the connection to the CPE, and detect that the CPE has gone down. If you select this option you can also select the longest interval between CPE device health messages before the IPSec connection indicates that it has lost contact with the CPE. The default is 20 seconds. We recommend leaving this option at the default setting.
- (Optional) If you expand the Phase One (ISAKMP) Configuration section and select Set custom options , you can set the following optional settings (you must select one of each option):

- Custom Encryption Algorithms: You can select from the options provided in the pull-down menu.
- Custom Authentication Algorithms: You can select from the options provided in the pull-down menu.
- Diffie-Hellman Groups: You can select from the options provided in the pull-down menu.

If the Set custom configurations checkbox isn't selected, the default settings are proposed. You can still select the IKE Session Key Lifetime in Seconds . The default is 28800 which is equal to 8 hours.

To understand these options in more detail including the default proposals, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).
- If you expand the Phase Two (IPSec) Configuration options and select Set custom options , you can set the following optional settings for the tunnel (you must select an encryption algorithm):

- Custom Encryption Algorithms: You can select from the options provided in the pull-down menu. If you select an AES-CBC encryption algorithm, you must also select an authentication algorithm.
- Custom Authentication Algorithms: You can select from the options provided in the pull-down menu. The encryption algorithm you chose might have built-in authentication, in which case no selectable option is available.

If the Set custom configurations checkbox isn't selected, the default settings are proposed. You can still change the following settings:
- IPSec Session Key Lifetime in Seconds: The default is 3600 which is equal to 1 hour.
- Enable Perfect Forward Secrecy: By default, this option is on. It lets you select the Perfect Forward Secrecy Diffie-Hellman Group . You can select from the options provided in the pull-down menu. If you don't make a selection, GROUP5 is proposed.

For all Phase Two options, selecting a single option overrides the default set and is the only option proposed to the CPE device.
- For Tunnel 2 you can use the same options described for Tunnel 1. You can also select different options or decide to leave the tunnel unconfigured because the CPE device only supports a single tunnel.
- When finished, select Create IPSec Connection .
- Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location so you can deliver it to the network engineer who configures the CPE device.

You can view this tunnel information here in the Console at any time.

The IPSec connection is created and displayed on the page. It stays in the Provisioning state for a short period.

The displayed tunnel information includes:
- The Oracle VPN IP address (for the Oracle VPN headend).
- The tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. A network engineer still must configure the CPE device.

To view the tunnel's shared secret, select the tunnel to view its details, and then select Show next to Shared Secret .

By now you have created all the components required for Site-to-Site VPN. Next, the on-premises network engineer must configure the CPE device before network traffic can flow between the on-premises network and a VCN.

For more information, see[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm).

[Configure a Tunnel for Policy-based Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm#)

## Configure a Tunnel for Policy-based Routing

Note  
  
We recommend that you use BGP route-based IPSec connections for IPSec over FastConnect.
Note  
  
The policy-based routing option isn't available in all ADs, and might require creating a new IPSec tunnel.

Enter the following information in the appropriate section for tunnel 1 and tunnel 2.

- Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- (Optional) Select the checkbox and enter a custom shared secret.
By default, Oracle provides the shared secret for the tunnel. To provide it yourself, select this checkbox and enter the shared secret. You can[change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/workingwithIPsec.htm#edit_shared_secret).
- Select the Internet Key Exchange (IKE) version to use for this tunnel. Only select[IKEv2](https://tools.ietf.org/html/rfc7296)if the CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
- Select Policy-based routing as the routing type.
- In the Associations section, enter information in the appropriate fields:

- On-premises CIDR blocks: You can provide several IPv4 CIDR or IPv6 prefix blocks used by resources in the on-premises network, with routing decided by the CPE device policies.
Note  
  
See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for limitations on how many IPv4 CIDR or IPv6 prefix blocks can be used.
- Oracle Cloud CIDR blocks: You can provide several IPv4 CIDR or IPv6 prefix blocks used by resources in a VCN.
Note  
  
See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for limitations on how many IPv4 CIDR or IPv6 prefix blocks can be used.
- (Optional) If wanted for troubleshooting or monitoring, enter information in the following fields:

- IPv4 inside tunnel interface - CPE : You can provide an IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel. For example: 10.0.0.16/31.
- Inside Tunnel Interface - Oracle : You can provide an IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel. For example: 10.0.0.17/31.

These IP addresses must be part of one of Site-to-Site VPN's encryption domains.
- (Optional) If you select Show Advanced Options you can change the following settings for the tunnel:

- Oracle IKE Initiation: This setting indicates whether the Oracle end of the IPSec connection can start up the IPSec tunnel. The default is Initiator or Responder . You can also decide to set the Oracle end to be a responder only which would require the CPE device to start the IPSec tunnel. We recommend leaving this option at the default setting.
- NAT-T Enabled: This setting indicates whether the CPE device is behind a NAT device. The default is Auto . The other options are Disabled and Enabled . We recommend leaving this option at the default setting.
- Enable Dead Peer Detection Timeout: When you select this option, you can periodically check the stability of the connection to the CPE, and detect that the CPE has gone down. If you select this option you can also select the longest interval between CPE device health messages before the IPSec connection indicates that it has lost contact with the CPE. The default is 20 seconds. We recommend leaving this option at the default setting.
- (Optional) If you expand the Phase One (ISAKMP) Configuration section and select Set custom options , you can set the following optional settings (you must select one of each option):

- Custom Encryption Algorithms: You can select from the options provided in the pull-down menu.
- Custom Authentication Algorithms: You can select from the options provided in the pull-down menu.
- Diffie-Hellman Groups: You can select from the options provided in the pull-down menu.

If the Set custom configurations checkbox isn't selected, the default settings are proposed. You can still select the IKE Session Key Lifetime in Seconds . The default is 28800 which is equal to 8 hours.

To understand these options in more detail including the default proposals, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).
- If you expand the Phase Two (IPSec) Configuration options and select Set custom options , you can set the following optional settings for the tunnel (you must select an encryption algorithm):

- Custom Encryption Algorithms: You can select from the options provided in the pull-down menu. If you select an AES-CBC encryption algorithm, you must also select an authentication algorithm.
- Custom Authentication Algorithms: You can select from the options provided in the pull-down menu. The encryption algorithm you chose might have built-in authentication, in which case no selectable option is available.

If the Set custom configurations checkbox isn't selected, the default settings are proposed. You can still change the following settings:
- IPSec Session Key Lifetime in Seconds: The default is 3600 which is equal to 1 hour.
- Enable Perfect Forward Secrecy: By default, this option is on. It lets you select the Perfect Forward Secrecy Diffie-Hellman Group . You can select from the options provided in the pull-down menu. If you don't make a selection, GROUP5 is proposed.

For all Phase Two options, selecting a single option overrides the default set and is the only option proposed to the CPE device.
- For Tunnel 2 you can use the same options described for Tunnel 1. You can also select different options or decide to leave the tunnel unconfigured because the CPE device only supports a single tunnel.
- When finished, select Create IPSec Connection .
- Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location so you can deliver it to the network engineer who configures the CPE device.

You can view this tunnel information here in the Console at any time.

The IPSec connection is created and displayed on the page. It stays in the Provisioning state for a short period.

The displayed tunnel information includes:
- The Oracle VPN IP address (for the Oracle VPN headend).
- The tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. The network engineer must configure the CPE device before the status can change.

To view the tunnel's shared secret, select the tunnel to view its details, and then select Show next to Shared Secret .

By now you have created all the components required for Site-to-Site VPN. Next, the on-premises network engineer must configure the CPE device before network traffic can flow between the on-premises network and a VCN.

For more information, see[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm).
- 

Use the[network ip-sec-connection create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-connection/create.html)command and required parameters to create an IPSec connection:

```

```

The`--static-routes`option is only required when using static routing.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/CreateIPSecConnection)
