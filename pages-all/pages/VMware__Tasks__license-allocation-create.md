# Creating VMware Solution License Allocations
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-create.htm
- Fetched: 2026-09-05 03:08 CDT

# Creating VMware Solution License Allocations

Create a Oracle Cloud VMware Solution license allocation in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-create.htm#)
- 

## Navigate to Allocations

- 

Navigate to the Allocations list page. If you need help finding the Allocations list page, see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm).

The Allocations list page opens. All allocations in the selected compartment are displayed in a table.
- To create an allocation, select Create Allocation . The Create Allocation dialog is displayed.

## Fill out Allocation License Information

Fill out the allocation license information.
- Region: Select the region for the allocation. This value can be changed by editing the region in the main menu.
- Name: Enter a name for the allocation.
- Create in compartment: Select the compartment for this license.
- Type: Enter one of the following license types.
- vSAN: A vSAN license measured in Tebibytes (TiBs).
- VMware Cloud Foundation: A VMware Cloud Foundation license that's measured using cores.
- VMware vDefend Firewall: A VMWare license that's measured using cores.
- VMware Avi Load Balancer: A VMWare license that's measured using instances.
- License: Select the license to allocate resources from. Depending upon the license type, set the value for the resource.
- TiB count
- Cores count
- Instances count

## Tags

Select Tags to add tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)for details.

## Proceed to Create Allocation

To create the license allocation, select Create .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/byol-allocation/create.html)byol-allocation create`command and required parameters to create a license allocation:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the BYOL details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[CreateByolAllocation](https://docs.oracle.com/iaas/api/#/en/vmware/latest/ByolAllocation/CreateByolAllocation)
