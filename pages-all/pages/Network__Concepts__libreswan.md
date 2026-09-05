# Access to Other Clouds with Libreswan
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm
- Fetched: 2026-09-05 02:41 CDT

# Access to Other Clouds with Libreswan

Learn how to connect your Oracle Cloud Infrastructure Virtual Cloud Network (VCN) with another cloud provider by using Site-to-Site VPN with a Libreswan VM as the customer-premises equipment (CPE).

[Libreswan](https://libreswan.org/)is an open source IPSec implementation that is based on FreeS/WAN and Openswan. Most Linux distributions include Libreswan or make it easy to install. You can install it on hosts in either your on-premises network or a cloud provider network. This topic shows how to connect your Oracle Cloud Infrastructure Virtual Cloud Network (VCN) with another cloud provider by using Site-to-Site VPN with a Libreswan VM as the customer-premises equipment (CPE).

In the example shown here, the other cloud provider is Amazon Web Services (AWS). Site-to-Site VPN provides a secure and encrypted site-to-site IPSec connection between the Oracle and Amazon environments. It enables resources in the two clouds to communicate with each other using their private IP addresses as if they're in the same network segment.

A[Libreswan CPE guide](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Reference/libreswanCPE.htm)is also available for all other use cases.

Virtual tunnel interface (VTI) support for this route-based configuration requires minimum Libreswan version 3.18 and a recent Linux 3.x or 4.x kernel. This configuration was validated using Libreswan version 3.29.

## Architecture

The following diagram shows the general layout of the connection.
[

## Supported IPSec Parameters

For a vendor-neutral list of supported IPSec parameters for all regions, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Reference/supportedIPsecparams.htm).

The Oracle BGP ASN for the commercial cloud realm is 31898. If you're configuring Site-to-Site VPN for the US Government Cloud, see[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params)and also[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn). For the Oracle UK Sovereign Cloud, see[Regions](https://docs.oracle.com/iaas/Content/gov-cloud/govuksouth.htm#Regions).

## Configuration

Important  
  
The configuration instructions in this section are provided by Oracle Cloud Infrastructure for Libreswan. If you need support or further assistance, consult the[Libreswan documentation](https://libreswan.org/wiki/).

Libreswan supports both route-based and policy-based tunnels. The tunnel types can coexist without interfering with each other. The Oracle VPN headends use route-based tunnels. Oracle recommends that you configure Libreswan with the[Virtual Tunnel Interface (VTI) configuration syntax](https://libreswan.org/wiki/Route-based_VPN_using_VTI).

Refer to[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#ipsec_params)for more details about the specific parameters used in this document.

### Default Libreswan Configuration Files

The default Libreswan installation creates the following files:
- `etc/ipsec.conf`: The root of the Libreswan configuration.
- `/etc/ipsec.secrets`: The root of the location where Libreswan looks for secrets (the tunnel pre-shared keys).
- `/etc/ipsec.d/`: A directory for storing the`.conf`and`.secrets`files for your Oracle Cloud Infrastructure tunnels (for example:`oci-ipsec.conf`and`oci-ipsec.secrets`). Libreswan encourages you to create these files in this folder.

The default`etc/ipsec.conf`file includes this line:

```

```

The default`etc/ipsec.secrets`file includes this line:

```

```

The preceding lines automatically merge all the`.conf`and`.secrets`files in the`/etc/ipsec.d`directory into the main configuration and secrets files that Libreswan uses.

### About Using IKEv2

Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you[configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/workingwithIPsec.htm#using_ikev2), you must configure your CPE to use only IKEv2 and related IKEv2 encryption parameters that your CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Reference/supportedIPsecparams.htm).

You specify the IKE version when setting up the IPSec configuration file in[task 4](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#task4)in the next section. In that example file, there's a comment showing how to configure IKEv1 versus IKEv2.

### Configuration Process

[Task 1: Prepare the AWS Libreswan instance](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

- Using the AWS Console or APIs, create a Libreswan VM by using its provisioning process. Use Oracle Linux, CentOS, or Red Hat as the main operating system.
- 

After the new instance starts, connect to it with SSH and install the Libreswan package:

```

```

- 

In the AWS Console, disable the source and destination checks on the Libreswan VM instance by right-clicking the instance, clicking Networking , and then clicking Change Source/Dest. Check . When prompted, click Yes, Disable.
[
- 

On the Libreswan VM, configure IP_forward to allow AWS clients to send and receive traffic through the Libreswan VM. In the`/etc/sysctl.conf`file, set the following values and apply the updates with`sudo sysctl -p`.

```

```

- 

In the AWS Console, edit your AWS route table. Add a rule with the VCN CIDR (172.0.0.0/16) as the destination and the AWS Libreswan instance ID (i-016ab864b43cb368e in this example) as the target.
[
- 

In the AWS Console, enable inbound TCP and UDP traffic on ports 4500 and 500 to allow an Oracle Cloud Infrastructure Site-to-Site VPN IPSec connection with the AWS Libreswan VM. This task includes editing both the AWS security groups and network ACLs. You can set the source value can be the Oracle public IP (the Oracle VPN headend IPSec tunnel endpoint) instead of 0.0.0.0/0.

For security groups:
[

For network ACLs:
[

[Task 2: Configure the Oracle Cloud Infrastructure DRG and CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

- 

In the Oracle Console, create a customer-premises equipment (CPE) object that points to the Libreswan AWS instance public IP address (34.200.255.174). This is easily done using the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/CPEconfigurationhelper.htm).
- 

If you don't already have a DRG attached to your VCN: in the Oracle Console,[create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/drg-create.htm)and then[attach it to the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/attach-vcn-drg.htm)(172.0.0.0/16).
- 

In the Oracle Console,[create an IPSec connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/settingupIPsec.htm#create_ipsec)and point it to the AWS VPC CIDR (10.0.0.0/16). In other words, when you create the IPSec connection, set its static route to the AWS VPC CIDR.

For each configured IPSec connection, Oracle creates two tunnels and assigns these items to each one:
- Oracle VPN headend IPSec tunnel endpoint
- Oracle VPN tunnel shared secret

You can view the IPSec tunnel status and Oracle VPN headend IP by clicking the Actions menu (three dots) for the IPSec connection, and then clicking View Details . Initially each tunnel is in the DOWN state (offline) because you still have some additional configuration to do later on the AWS Libreswan VM.

To view the shared secret, click the Actions menu (three dots) for an individual tunnel, and then click View Details . Next to Shared Secret , click Show .
- 

In the Oracle Console, edit the VCN's security rules to enable ingress TCP and UDP traffic on ports 4500 and 500 like you did for the AWS security groups and network ACLs. You can use the AWS Libreswan VM public IP address instead of 0.0.0.0/0 if it's a persistent public IP. Also open all protocols and ports for ingress traffic from the AWS VPC CIDR (10.0.0.0/16). Remember:[Security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm)are associated with a subnet, so edit the security list associated with each subnet that needs to communicate with the AWS VPC. Or, if you're using VCN[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm), edit the rules in the relevant NSGs.
- 

In the Oracle Console, edit the VCN's route tables to add a rule that has the AWS VPC CIDR (10.0.0.0/16) as the destination CIDR block and the DRG you created earlier as the target. Remember: Route tables are associated with a subnet, so edit the route table associated with each subnet that needs to communicate with the AWS VPC.

[Task 3: Determine the required configuration values](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

The Libreswan configuration uses the following variables. Determine the values before proceeding with the configuration.
- `${cpeLocalIP}`: The IP address of your Libreswan device.
- `${cpePublicIpAddress}`: The public IP address for Libreswan. This is the IP address of your outside interface. Depending on your network topology, the value might be different from`${cpeLocalIP}`.
- `${oracleHeadend1}`: For the first tunnel, the Oracle public IP endpoint obtained from the Oracle Console.
- `${oracleHeadend2}`: For the second tunnel, the Oracle public IP endpoint obtained from the Oracle Console.
- `${vti1}`: The name of the first VTI used. For example, vti1.
- `${vti2}`: The name of the second VTI used. For example, vti2.
- `${sharedSecret1}`: The pre-shared key for the first tunnel. You can use the default Oracle-provided pre-shared key, or provide your own when you set up the IPSec connection in the Oracle Console.
- `${sharedSecret2}`: The pre-shared key for the second tunnel. You can use the default Oracle-provided pre-shared key, or provide your own when you set up the IPSec connection in the Oracle Console.
- `${vcnCidrNetwork}`: The VCN IP range.

[Task 4: Set up the configuration file: /etc/ipsec.d/oci-ipsec.conf](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

Libreswan configuration uses the concept of left and right to define the configuration parameters for your local CPE device and the remote gateway. Either side of the connection (the conn in the Libreswan configuration) can be left or right, but the configuration for that connection must be consistent. In this example:
- Left: Your local Libreswan CPE
- Right: The Oracle VPN headend

Use the following template for your`/etc/ipsec.d/oci-ipsec.conf`file. The file defines the two tunnels that Oracle creates when you set up the IPSec connection.
Important  
  
If your CPE is behind a 1–1 NAT device, uncomment the`leftid`parameter and set it equal to the`${cpePublicIpAddress}`.

```

```

[Task 5: Set up the secrets file: /etc/ipsec.d/oci-ipsec.secrets](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

Use the following template for your`/etc/ipsec.d/oci-ipsec.secrets`file. It contains two lines per IPSec connection (one line per tunnel).

```

```

[Task 6: Restart the Libreswan configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

After setting up your configuration and secrets files, you must restart the Libreswan service with the following command.
Important  
  
Restarting the Libreswan service may impact existing tunnels.

```

```

[Task 7: Configure IP routing](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#)

Use the following`ip`command to create static routes that send traffic to your VCN through the IPSec tunnels. If you're logged in with an unprivileged user account, you might need to use`sudo`before the command.
Important  
  
Static routes created with the`ip route`command do not persist through a reboot. To determine how to make your routes persist, refer to the documentation of your Linux distribution of choice.

```

```

## Verification

A[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Reference/ipsecmetrics.htm).

If you have issues, see[Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Troubleshoot/ipsectroubleshoot.htm).

### Verifying the Libreswan Status

Verify the current state of your Libreswan tunnels by using the following command:

```

```

The tunnel is established if you see a line that includes the following:

```

```

If you're using IKEv2, you see the following:
```

```

In the future, if you need to open a support ticket with Oracle about your Libreswan tunnel, include the output of the preceding`ipsec status`command.

### Checking the Tunnel Interface Status

Check if the virtual tunnel interfaces are up or down by using the`ifconfig`command or the`ip link show`command. You can also use applications such as[tcpdump](https://www.tcpdump.org/)with the interfaces.

Here's an example of the`ifconfig`output with a working Libreswan implementation that shows the available VTIs.
```

```

Here's an example of the`ip link show`output:
```

```
