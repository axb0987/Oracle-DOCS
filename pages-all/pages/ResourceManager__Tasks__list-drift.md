# Listing Drift Status for a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Drift Status for a Stack

List drift status for each resource in a stack in Resource Manager. Drift status is available for completed drift detections.

For information about drift detection, see[Detecting Drift in a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- To view the latest drift detection report: In the Stack information section of the stack's details page, select View drift detection report .
A panel lists the drift status of the specified resources defined by the stack. Resources are identified by resource names.
- To view an older drift detection report: On the Work requests tab, select the older drift detection work request, and then select the Drift detection report tab.
The report lists the drift status of the specified resources defined by the stack. Resources are identified by resource names.
- To view details of drift status for a resource, expand the resource.
Actual and expected properties are listed.
To generate a drift detection report (if the stack doesn't have one, or if you want to create a new report): In the Stack information section of the stack's details page, select Run drift detection now . Or, select Run drift detection from the Actions menu at the top of the page.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list-resource-drift-details.html)oci resource-manager stack list-resource-drift-details`command and required parameters to list drift status.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ListStackResourceDriftDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/StackResourceDriftSummary/ListStackResourceDriftDetails)operation to list drift status for each resource in a stack, for a completed[drift detection](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm).

## Making Resources Match

After listing drift status, if drift was detected, optionally make the stack's managed resources match the properties of the stack's Terraform configuration.

To make resources match the properties of the Terraform configuration,[run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)
