# Managing Maintenance Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managing-maintenance-events.htm
- Fetched: 2026-09-05 01:51 CDT

# Managing Maintenance Events

You can interact with maintenance events using the following options.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managing-maintenance-events.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managing-maintenance-events.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managing-maintenance-events.htm#)
- 

Open the navigation menu and select Compute . Under Compute , select Instance Maintenance .

The Instance Maintenance list page opens. All existing maintenance events in the selected compartment are displayed in a list table.

To view the resources in a different compartment, use the Compartment filter to switch compartments.
Note  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see Understanding Compartments.

Select a maintenance event to view its details. The information provided includes:
- Description
- OCID
- Type
- Affected Service
- Action date
- 

Use the following commands and required parameters to interact with maintenance events.
- [List Instance Maintenance Events](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-maintenance-event/list.html)
- [Get Instance Maintenance Event Details](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-maintenance-event/get.html)
- [Update Instance Maintenance Event](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-maintenance-event/update.html)

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following API operations to manage maintenance events:
- [List Instance Maintenance Events](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceMaintenanceEventSummary/ListInstanceMaintenanceEvents)
- [Get Instance Maintenance Event Details](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceMaintenanceEvent/GetInstanceMaintenanceEvent)
- [Update Instance Maintenance Event](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceMaintenanceEvent/UpdateInstanceMaintenanceEvent)
