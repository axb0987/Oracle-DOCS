# Get CPE Device Configuration Information
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get_device_config_content.htm
- Fetched: 2026-09-05 02:43 CDT

# Get CPE Device Configuration Information

Get a configuration information file for an IPSec connection that uses the specified CPE object.

This CPE configuration content is needed by an on-premises network engineer to configure the actual CPE device (for example, a hardware router) represented by the specified CPE object.

See[Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)for more details.

After you get the configuration content, share the following with the on-premises network engineer:
- The helper content that you generated.
- A link to the configuration topic for the CPE type. See[Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get_device_config_content.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get_device_config_content.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get_device_config_content.htm#)
- 

How you find the CPE configuration helper affects the scope of the information the helper includes.

- Navigate to the helper as described at[Open the Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using__Open_the_Helper_from_one_of_three_locations).
- Review the template of information in the Helper. Fill in any blank fields if some information is missing.

Tip  
  
For certain CPE vendors, the helper displays fields for vendor-specific information that's used for CPE configuration. The fields might be blank or already have values. You can fill in the blank fields or leave them as is. For blank fields, the resulting content displays placeholder variables to show where the network engineer needs to fill in the values.
- Select Create Content at the bottom of the Helper.

The Helper generates the content.
Note  
  
See this[known issue](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/known_issues_for_networking.htm#cpe-config-vendor)if you see an error that says The CPE is missing the vendor information (the device type). Update the CPE and add the vendor information.
- Select either Copy Configuration to Clipboard or Download Configuration (to download it to a file).
- Select Close .
- Give the following items to the on-premises network engineer:

- A link to the configuration topic for the CPE type. See[Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm).
- The Helper content that you generated.
- 

Use the[network cpe get-cpe-device-config-content](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/cpe/get-cpe-device-config-content.html)command and required parameters to get configuration information for IPSec connections that use the specified CPE object:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetCpeDeviceConfigContent](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
