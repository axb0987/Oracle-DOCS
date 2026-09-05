# Creating a CPE
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a CPE

Create a CPE object that represents the device an on-premises network uses for Site-to-Site VPN connection to Oracle Cloud Infrastructure.

Before you create a CPE object, review[Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)and plan the Site-to-Site VPN implementation. Also, review[Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm).

After you configure Site-to-Site VPN a network engineer needs to update the configuration of the actual edge device for the on-premises network to match the configuration of the CPE object. The CPE configuration helper is available to make this task easier.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm#)
- 

- On the Customer-premises equipment list page, select Create CPE . If you need help finding the list page, see[Listing CPEs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm).
- Enter a descriptive name for the CPE (this is required). It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API or CLI). Avoid entering confidential information.
- (Optional) Check the Enable IPSec over FastConnect option only when configuring the[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)feature.
When this option is enabled, the IP Address provided in the next field can be either public or private because the IP address used as the CPE IKE identifier can be either public or private. Checking this option signals to Oracle that the CPE IP address isn't reachable over the internet and is reachable over private peering only. If the CPE object isn't created to allow IPSec over FastConnect, you can't change that decision later.
- Enter the public IP address of the actual CPE device at the on-premises end of the VPN (see the list of information to gather in[Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before)). If you plan to set up IPSec over FastConnect this can be a private IP address.
- Select the CPE vendor information of the actual CPE device at the on-premises end of the VPN (see the list of information to gather in[Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before)). This might also include a hardware platform and software version. If you're not sure which vendor makes the CPE, or it's not in the list, select Other .
- If prompted, select a value for Platform/Version . Use these guidelines:

- We recommend using a route-based configuration if possible.
- If you don't see a specific CPE platform or version in the list, select the closest platform/version that predates the CPE version.
- Select Create CPE .

The CPE object you created appears in the Customer-premises equipment list page.
- 

Use the[network cpe create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/cpe/create.html)command and required parameters to create a CPE object:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/CreateCpe)
