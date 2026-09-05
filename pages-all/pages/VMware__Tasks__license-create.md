# Creating VMware Solution Licenses
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-create.htm
- Fetched: 2026-09-05 03:08 CDT

# Creating VMware Solution Licenses

Create a Oracle Cloud VMware Solution license in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-create.htm#)
- 

## Navigate to Licenses

- 

Navigate to the License Management list page. If you need help finding the License Management list page, see[Listing Licenses](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-list.htm).

The License Management list page opens. All licenses in the selected compartment are displayed in a table.
- To create a license, select Register BYOL License . The Register BYOL License dialog is displayed.

## License Information

Fill out the license information.
- Name: Enter a name for the license.
- Software Type: Enter one of the following license types.
- vSAN: A vSAN license measured in Tebibytes (TiBs).
- VMware Cloud Foundation: A VMware Cloud Foundation license that is measured using cores.
- VMware vDefend Firewall: A VMWare license that's measured using cores.
- VMware Avi Load Balancer: A VMWare license that's measured using instances.
- Description: Enter a description for the license. Avoid entering confidential information.
- Compartment: Select the compartment for this license.

## License Details: VCF

Fill out the license details for a VCF license.
- Cores Count: Enter the number of cores for the license.
- Entitlement Key: Enter the key for the license here.
- Site ID: Enter the ID for the site.
- Valid From: Enter the start date for the entitlement.
- Valid To: Enter the end date for the entitlement.

## License Details: vSAN

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

## Terms and Conditions

Select the following terms and conditions options.
- I confirm that I have purchased above license for use on Oracle Cloud VMware Solution and that the information provided is accurate.
- I understand that providing false information may impact the continuity of Software-Defined Data Centers.
- The license information will be shared with Broadcom.

## Tags

Select Tags to add tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)for details.

## Proceed to Register License

To complete the registration, select Register .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/byol/create.html)byol create`command and required parameters to create a license:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the BYOL details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[CreateByol](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Byol/CreateByol)
