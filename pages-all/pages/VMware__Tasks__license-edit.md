# Editing VMware Solution Licenses
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-edit.htm
- Fetched: 2026-09-05 03:08 CDT

# Editing VMware Solution Licenses

Edit a Oracle Cloud VMware Solution license in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-edit.htm#)
- 

## Navigate to Licenses

- 

Navigate to the License Management list page. If you need help finding the License Management list page, see[Listing Licenses](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-list.htm).
- Select the license to edit.
- Select Edit .

## Edit License Information

Edit the license information.
- Name: Enter a name for the license.
- Software Type: Enter one of the following license types.
- vSAN: A vSAN license measured in Tebibytes (TiBs).
- VMware Cloud Foundation: A VMware Cloud Foundation license that is measured using cores.
- VMware vDefend Firewall: A VMWare license that's measured using cores.
- VMware Avi Load Balancer: A VMWare license that's measured using instances.
- Description: Enter a description for the license. Avoid entering confidential information.
Important  
  
If resources from the license have been allocated, the license detail information does not appear in the dialog.

### License Details: VCF

Fill out the license details for a VCF license.
- Cores Count: Enter the number of cores for the license.
- Entitlement Key: Enter the key for the license here.
- Site ID: Enter the ID for the site.
- Valid From: Enter the start date for the entitlement.
- Valid To: Enter the end date for the entitlement.

### License Details: vSAN

Fill out the license details for a vSAN license.
- TiB Count: Enter the number of TiBs for the license.
- Entitlement Key: Enter the key for the license here.
- Site ID: Enter the ID for the site.
- Valid From: Enter the start date for the entitlement.
- Valid To: Enter the end date for the entitlement.

## License Details: VMware vDefend Firewall

Fill out the license details for a VMware vDefend Firewall license.
- Cores Count: Enter the number of cores for the license.
- Entitlement Key: Enter the key for the license here.
- Site ID: Enter the ID for the site.
- Valid From: Enter the start date for the entitlement.
- Valid To: Enter the end date for the entitlement.

## License Details: VMware Avi Load Balancer

Fill out the license details for a VMware Avi Load Balancer license.
- Instance Count: Enter the number of instances for the license.
- Entitlement Key: Enter the key for the license here.
- Site ID: Enter the ID for the site.
- Valid From: Enter the start date for the entitlement.
- Valid To: Enter the end date for the entitlement.

## Update

To complete the edit, select Update .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/byol/update.html)byol update`command and require parameters to edit a license:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the BYOL details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[UpdateByol](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Byol/UpdateByol)
