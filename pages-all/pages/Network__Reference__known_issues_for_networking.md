# Known Issues for Networking
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/known_issues_for_networking.htm
- Fetched: 2026-09-05 02:42 CDT

# Known Issues for Networking

These known issues have been identified in the Networking family of services, including internal connections within a VCN and connectivity to on-premises networks.

See also:[Troubleshooting VCNs and Connectivity](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Concepts/troubleshooting.htm).

## Active FTP not supported on Windows Instances
Details The default FTP client provided by Microsoft Windows only supports FTP in active mode, which doesn't work with the Oracle's stateful firewall rules or with instances deployed behind a NAT gateway. Workaround Oracle recommends that Windows instances use a third-party FTP client running in passive mode.

## CPE Configuration Helper trouble specifying the CPE vendor
Details

If the following things occur, in the Oracle Console you receive an error that says The CPE is missing the vendor information (the device type). Update the CPE and add the vendor information:
- You have a CPE that existed before the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/CPEconfigurationhelper.htm)feature was released.
- You have not yet edited the CPE in the Oracle Console and specified which vendor makes your CPE.
- You try to generate the Helper content for the CPE or any IPSec connections that use that CPE. Workaround

Perform the following actions:
- In the Oracle Console, view the CPE.
- Click Edit .
- In the CPE Vendor Information section, select the vendor that makes your CPE. If you're not sure which vendor makes your CPE, or it's not in the list, select Other .
- 

If prompted, select a value for Platform/Version . Here are guidelines:
- Oracle recommends using a route-based configuration if possible.
- If you do not see your specific CPE platform or version in the list, choose the closest platform/version that predates your CPE version.
- Click Save Changes . It's important to click this even if you did not change the value for the vendor.

You can then generate the Helper content successfully for the CPE or any IPSec connections that use that CPE.

## Private access issues from your on-premises network to Oracle Analytics Cloud through a service gateway
Details
If you do all of the following, asymmetric routing can occur for the traffic between your on-premises network and Oracle Analytics Cloud:
- Set up your on-premises network with[private access to Oracle services through a service gateway on a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/transitroutingoracleservices.htm).
- Also use the internet or FastConnect public peering for public access to Oracle services.
- Also use Oracle Analytics Cloud so that it that initiates connection to clients in your on-premises network, and you are not yet using a[Data Gateway](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmgp/prepare-migrate-oracle-analytics-cloud-classic-instances.html#GUID-F4221878-5446-48D4-A020-48D927FFBD7F)in your network. Asymmetric routing means that the request traffic and response traffic go over different paths. Here are more details about why asymmetric routing can occur: When Oracle Analytics Cloud initiates connections to clients in your on-premises network, the connection requests must go over a public path (either the internet or FastConnect public peering). However, the response travels over a private path , based on the recommendation in[Routing Preferences for Traffic from An On-premises Network to Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Concepts/routingonprem.htm#on-prem-to-oracle). A workaround is required only if you use Oracle Analytics Cloud so that it initiates connections to clients in your on-premises network, and you are not yet using a Data Gateway in your network. Workaround 1 (preferred) With Oracle Analytics Cloud, switch from using a Remote Data Connector to a[Data Gateway](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmgp/prepare-migrate-oracle-analytics-cloud-classic-instances.html#GUID-F4221878-5446-48D4-A020-48D927FFBD7F). Workaround 2 Configure your customer-premises equipment (CPE) to prefer either an internet or FastConnect public peering path by adding static routes for the[regional source IP address for Oracle Analytics Cloud](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoci/find-ip-address-or-host-name-your-analytics-cloud-instance.html). That way, any response traffic to Oracle Analytics Cloud will return on the same path as the incoming connection request.

## Issues with access to your public instances from Oracle services through a service gateway
Details
If the route table associated with your public subnet in a VCN includes the following two conflicting route rules, Oracle services might be unable to access your public instances in that subnet.
- Route rule with the Target Type set as internet gateway .
- Route rule with the Destination Service set as All &lt;region&gt; Services in Oracle Services Network and the Target Type set as service gateway . The foregoing two route rules can lead to asymmetric routing when Oracle services initiate connections to public instances in your VCN. Oracle Cloud Infrastructure does not support these rules simultaneously within the same route table. Oracle has updated the service APIs and the Console to disable support for this configuration. Workaround

We recommend that you remove the route rule that has the Destination Service set as All &lt;region&gt; Services in Oracle Services Network and the Target Type set as service gateway . Revert to the configuration you used before adopting the service gateway for Oracle Services Network. With this change, your public instances retain access to all Oracle services through the internet gateway. Oracle services can continue to access your public instances.

However, your instances in the public subnet can continue to access Object Storage through the service gateway. Update the subnet's route table to include a route rule with Destination Service set as OCI &lt;region&gt; Object Storage and the Target set to the VCN's service gateway.

This known issue applies only to public subnets that have access to an internet gateway. Regarding private subnets: you can still configure a private subnet's route table to provide access to All &lt;region&gt; Services in Oracle Services Network or to OCI &lt;region&gt; Object Storage through the VCN's service gateway.

## Access issues for instances to Oracle yum services through service gateway
Details If you want to use a service gateway with your VCN without also using an internet gateway or NAT gateway for internet access , your instances might not have access to the applicable regional Oracle yum server. There are two possible issues:
- Instances created before November 2018 might have their repos pointed to URLs that are not accessible through the service gateway
- Instances that were not able to contact their local region's yum server before may have fallen back to using yum.oracle.com, which is not accessible through the service gateway To use either of the following mitigation strategies, you must have one of the following gateways configured so you can reach out to the region's yum server: service gateway, NAT gateway, or internet gateway. Workaround 1 (automated)

Try the following automated mitigation. If it fails for some reason, use the manual mitigation method that follows.

Copy the following script the to local system and run it. The script disables existing repos and downloads the repo file, which directs the system to the region's local yum servers accessible through the service gateway.

```

```
Workaround 2 (manual)

If the automated mitigation fails, you can manually mitigate the issue. Here you disable the existing repo files and pull down the latest repo file from your region's yum server. To identify your instance's region key, look at the region list in[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

To disable the existing repo files, navigate to the`/etc/yum.repos.d`directory and rename all files present to include`.disabled`at the end of the file name.

Example:
```

```

Download the repo file for your region to the local system. The following example uses Ashburn (with region key`iad`). Replace`iad`with the region key applicable to your instance.
```

```
