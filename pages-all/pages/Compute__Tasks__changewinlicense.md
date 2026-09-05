# Changing the Windows License Type of an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/changewinlicense.htm
- Fetched: 2026-09-05 01:50 CDT

# Changing the Windows License Type of an Instance

When working with a Windows instance, you must select the type of license to use.

## Selecting Windows Licensing Type

For Windows Server images there are two licensing options:
- Microsoft bring your own license : You provide your own Windows Server license for an instance.
- OCI provided : You use OCI provided Windows licenses. See the[Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os)for prices.

For both types of license, you must agree to the Oracle and Microsoft license terms of use for the selected Windows version.

Edit the license type using one of the following options.
Important  
  
After the change is saved, the instance immediately reboots.
- If an instance changed to Microsoft bring your own license , once the instance starts you are no longer charged for the Windows Server license.
- If the instance changed to OCI Provided , once the instance starts you are charged for the Windows Server license. See the[Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os)for prices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/changewinlicense.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/changewinlicense.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/changewinlicense.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- On the instance details page, find the Instance Details section.
- Find the License type field.
- Select Edit . The Edit license type dialog appears.
- Select one of the Windows license type options:
- Microsoft bring your own license : You provide the own Windows Server license for an instance.
- OCI provided : You use OCI provided Windows Server licenses. See the[Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os)for prices.

If you're changing from one type to the other, check the check box to agree to the Oracle and Microsoft license terms of use.
- To save the changes, select Save Changes .
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to update an instance:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
