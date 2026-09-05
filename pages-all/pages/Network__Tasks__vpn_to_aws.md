# VPN Connection to AWS
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm
- Fetched: 2026-09-05 02:47 CDT

# VPN Connection to AWS

The Oracle Cloud Infrastructure (OCI) Site-to-Site VPN service offers a secure IPSec connection between an on-premises network and a Virtual Cloud Network (VCN). You can also use Site-to-Site VPN to connect Oracle Cloud Infrastructure resources to other cloud service providers.

This topic provides a best practices configuration for an IPSec VPN tunnel between OCI and AWS using the OCI Site-to-Site VPN service and the AWS Site-to-Site VPN service.
Note  
  
This document assumes you have already provisioned a[Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm)and[Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)and also configured all[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)and[Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm)required for this scenario and all equivalents in AWS.

## Considerations specific to AWS

Pre-Shared Key: If you rely on AWS to auto generate a pre-shared key for a tunnel, the generated key might contain period or underscore (. or _ ) characters. OCI doesn't support these characters in a pre-shared key. If the AWS auto generated password contains these characters, change the pre-shared key for the relevant tunnel before completing the VPN configuration.

Routing Type: This scenario uses Border Gateway Protocol (BGP) to exchange routes between AWS and OCI. Use BGP for IPSec tunnels whenever possible. Optionally, static routing can also be used between AWS and OCI.

## Verify OCI Site-to-Site VPN Version

You can verify the Site-to-Site VPN version used by the IPSec connection under the IPSec Connection Information tab on an IPSec connection page.

## Supported IPSec Parameters

For a vendor-neutral list of supported IPSec parameters for all OCI regions, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

## Configuration Process

[AWS - Create Temporary Customer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

The first step in the configuration process is to create a temporary customer gateway. This temporary customer gateway is used to initially provision the AWS Site-to-Site VPN, exposing the AWS VPN endpoint for the tunnel. OCI requires the public IP of the remote VPN peer before creating a IPSec connection. After this process has been completed, a new customer gateway is configured representing the actual OCI VPN endpoint public IP.
- From the main AWS portal, expand the Services menu at the top left of the screen. Browse to VPC under Networking &amp; Content Delivery .
- From the left-hand menu, scroll down and select Customer Gateways under Virtual Private Network (VPN) .
- Select Create Customer Gateway to create a Customer Gateway.
- 

You're taken to the Create Customer Gateway page. Enter the following details:
- Name: Give this customer gateway a temporary name. In this example, the name TempGateway is used.
- Routing: Select Dynamic .
- BGP ASN: Enter the OCI BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
- 

IP Address: Use any valid IPv4 address for the temporary gateway. This example uses 1.1.1.1.

When you're finished configuring your temporary customer gateway, select Create Customer Gateway to complete provisioning.

[AWS - Create and Attach Virtual Private Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

- From the AWS left-hand menu, scroll down and select Virtual Private Gateways under Virtual Private Network (VPN) .
- 

Select the Create Virtual Private Gateway button to create a new virtual private gateway.
- 

You're taken to the Create Virtual Private Gateway page. Enter the following details:
- Name: Give the Virtual Private Gateway (VPG) a name.
- 

ASN: Select Amazon default ASN .

When you're finished configuring the virtual private gateway, select the Create Virtual Private Gateway button to complete provisioning.
- After the VPG has been created, you need to attach it to the VPC of choice.

While still on the Virtual Private Gateway page, ensure that the VPG is selected, select the Actions menu (three dots) , and then Attach to VPC .
- You're taken to the Attach to VPC page for the selected Virtual Private Gateway.

Select the VPC from the list, then select the Yes, Attach button to complete attaching the VPG to the VPC.

[AWS - Create VPN Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

- From the left-hand menu, scroll down and select Site-to-Site VPN Connections under Virtual Private Network (VPN) .
- Select Create VPN Connection to create a new virtual private gateway.
- You're taken to the Create VPN Connection page. Enter the following details:
- Name tag: Give the VPN connection a name.
- Target Gateway Type: Select Virtual Private Gateway , then select the previously created Virtual Private Gateway from the list.
- Customer Gateway: Select Existing , then select the temporary Customer Gateway from the list.
- Routing Options: Select Dynamic (requires BGP) .
- Tunnel inside Ip Version: Select IPv4 .
- 

Local/Remote IPv4 Network Cidr: Leave both of these fields blank, creating an any/any route-based IPSec VPN.

Proceed to the next step. DON'T select the Create VPN Connection button yet.
- 

While still on the Create VPN Connection page, scroll down to Tunnel Options .

Select a /30 CIDR from within the link local 169.254.0.0/16 range. Input the full CIDR in the Inside IPv4 CIDR for Tunnel 1 field.

Ensure that OCI supports the chosen /30 address for the inside tunnel IPs. OCI doesn't allow you to use the following IP ranges for inside tunnel IPs:
- 169.254.10.0-169.254.19.255
- 169.254.100.0-169.254.109.255
- 169.254.192.0-169.254.201.255

Proceed to the next step. DON'T select the Create VPN Connection button yet.
- Under Advanced Options for Tunnel 1 , select the radio button for Edit Tunnel 1 Options . An extra set of options expands.

If you would like to be restrictive with the cryptography algorithms used for this tunnel, configure the wanted Phase 1 and Phase 2 options here. We recommend using IKEv2 for this connection. Disable the IKEv1 checkbox to prevent IKEv1 from being used. To see what Phase 1 and Phase 2 options OCI supports, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

After you have finished configuring all wanted options, select the Create VPN Connection button at the bottom to finish provisioning the VPN connection.

[AWS - Download Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

While the VPN connection is provisioning, download the configuration of all tunnel information. This text file is required to complete configuring the tunnel in the OCI Console.
- Ensure that the VPN connection is selected, then select the Download Configuration button.
- Select the Vendor and Platform setting "Generic" then select the Download button to save a text copy of the configuration to a local hard drive.
- Open the downloaded configuration file in any text editor.

Look under IPSec Tunnel #1 , section #1 Internet Key Exchange Configuration . Here you find an automatically generated pre-shared key for the tunnel. Save this value.

AWS might generate a pre-shared key using the period or underscore characters (. or _). OCI doesn't support using those characters in a pre-shared key. A key that includes these values must be changed. To change the pre-shared key in AWS for a tunnel, select the VPN connection, select the Actions menu (three dots) , then Modify VPN Tunnel Options .
- 

While still under Tunnel 1 in the downloaded configuration, scroll down to section #3 Tunnel Interface Configuration .

Note down the following values to complete the Site-to-Site VPN configuration in OCI:

- Outside IP address of the Virtual Private Gateway
- Inside IP for the Customer Gateway
- Inside IP for the Virtual Private Gateway
- Virtual Private Gateway BGP ASN. The default ASN is 64512.

[OCI - Create CPE Object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

- Open the navigation menu and select Networking . Under Customer connectivity , select Customer-premises equipment .
- Select Create Customer-Premises Equipment .
- 

Enter the following values:
- Create in Compartment: select the compartment for the VCN you want.
- Name: A descriptive name for the CPE object. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.

This example uses "TO_AWS" as the name.
- IP Address: Enter the outside IP address of the Virtual Private Gateway shown in the configuration downloaded from AWS.
- CPE Vendor: Select Other .
- Select Create CPE .

[OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

- Open the navigation menu and select Networking . Under Customer connectivity , select Site-to-Site VPN .
- Select Create IPSec Connection .
- 

Enter the following values:
- Create in Compartment: Leave as is (the VCN's compartment).
- Name: Enter a descriptive name for the IPSec connection (Example: OCI-AWS-1). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Customer-Premises Equipment Compartment: Leave as is (the VCN's compartment).
- Customer-Premises Equipment: Select the CPE object that you created earlier, named TO_AWS.
- Dynamic Routing Gateway Compartment: Leave as is (the VCN's compartment).
- Dynamic Routing Gateway: Select the DRG that you created earlier.
- Static Route CIDR: Enter a default route, 0.0.0.0/0. Because the active tunnel uses BGP, OCI ignores this route. An entry is required for the second tunnel of the IPSec connection, which by default uses static routing, but the address not used in this scenario. If you plan to use static routing for this connection, input static routes representing AWS virtual networks. Up to 10 static routes can be configured for each IPSec connection.
- 

Enter the following details on the Tunnel 1 tab (required):
- Name: Enter a descriptive name for the tunnel (Example: AWS-TUNNEL-1). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Provide custom shared secret: Enter the pre-shared key used by IPSec for this tunnel. Select this checkbox and input the pre-shared key from the AWS VPN configuration file.
- IKE Version: Select IKEv2.
- Routing Type: Select BGP Dynamic Routing .
- BGP ASN: Input the BGP ASN used by AWS as found in the AWS VPN configuration file. The default AWS BGP ASN is 64512.
- IPv4 Inside Tunnel Interface - CPE: Enter the Virtual Private Gateway inside IP address from the AWS VPN configuration file. Use full CIDR notation for this IP address.
- IPv4 Inside Tunnel Interface - Oracle: Enter the inside IP address used by OCI. Referring to the AWS VPN configuration file, enter the inside IP address for the Customer Gateway. Use full CIDR notation for this IP address.
- 

Select Create IPSec Connection .

The IPSec connection is created and displayed on the page. the connection is in the Provisioning state for a short period.
- After the IPSec connection is provisioned, make note of the Oracle VPN IP Address of the tunnel. This addressis used to create a new customer gateway in the AWS portal.
- Open the navigation menu and select Networking . Under Customer connectivity , select Site-to-Site VPN .

A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the policy you're looking for, verify that you're viewing the correct compartment. To view policies attached to a different compartment, under List scope , select that compartment from the list.
- Select the IPSec connection you're interested in (Example: OCI-AWS-1).
- Find the Oracle VPN IP Address of AWS-TUNNEL-1.

[AWS - Create New Customer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

In the AWS console, browse to Customer Gateways and create a Customer Gateway using the following details:
- Name: Give this customer gateway a name.
- Routing: Select Dynamic .
- BGP ASN: Enter the OCI BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
- 

IP Address: Enter the Oracle VPN IP address for tunnel 1. Use the IP saved in the previous task.

Select Create Customer Gateway to complete provisioning.

[AWS - Modify VPN Connection for New Customer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

This task replaces the temporary Customer Gateway with one that uses the OCI VPN IP address.
- 

Browse to Site-to-Site VPN Connections in the AWS console and select the VPN connection.
- 

Select the Actions menu (three dots) , then Modify VPN Connection .
- 

You're taken to the Modify VPN Connection page. Enter the following details:

- Target Type: Select Customer Gateway from the list.
- 

Target Customer Gateway ID: Select the new Customer Gateway with the OCI VPN IP address from the list.

Select the Save button to save the configuration when you're done.

After a couple minutes, AWS completes provisioning the VPN connection and the IPSec VPN between AWS and OCI comes up.
- At this point you can delete the temporary customer gateway.

[Verification](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm#)

Browse to the IPSec connection in OCI and the Site-to-Site VPN connections in AWS to verify tunnel status.
- The OCI tunnel under IPSec connection displays Up for IPSec status to confirm an operational tunnel.
- The IPv4 BGP Status also displays Up indicating an established BGP session.
- The tunnel status under the Tunnel Details tab for the Site-to-Site VPN connection in AWS displays Up .

A[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)is also available from OCI to actively and passively monitor cloud resources. For information about monitoring OCI Site-to-Site VPN, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ipsecmetrics.htm).

If you have issues, see[Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/ipsectroubleshoot.htm)
