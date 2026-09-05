# Deleting a VMware Solution SDDC
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-delete.htm
- Fetched: 2026-09-05 03:09 CDT

# Deleting a VMware Solution SDDC

Delete (terminate) an SDDC in VMware Solution.

Deleting an SDDC removes the SDDC's associated instances and boot volumes. With a failed SDDC, you can also delete all its associated networking resources. These resources include the subnet and its route table and security list, and the VLANs and their route tables and NSGs. A networking resource can't be deleted if that resource is used by another SDDC or networking resource. A networking resource in use remains after the SDDC is deleted.
Warning  
  
Deletion removes the SDDC and its associated resources. Deleted resources can't be restored.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-delete.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, find the SDDC that you want to delete. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- From the Actions menu (three dots) for the SDDC, select Terminate .
The Terminate SDDC panel opens.
- To delete networking resources, select Terminate Networking Resources .
- To delete datastore resources, select Delete datastore resources .
This option is shown only when the SDDC contains a cluster that uses a standard shape. For other shapes, the option isn't relevant.
- Follow the prompt to confirm termination, and select Terminate all .
- 

Use the[sddc delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/delete.html)command and required parameters to terminate the SDDC and remove its associated resources:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSddc](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/DeleteSddc)
