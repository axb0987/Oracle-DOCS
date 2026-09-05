# Moving a VMware Solution SDDC Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-move.htm
- Fetched: 2026-09-05 03:09 CDT

# Moving a VMware Solution SDDC Between Compartments

Move an SDDC to a different compartment in VMware Solution.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-move.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, find the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- To view the SDDCs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the Actions menu (three dots) for the SDDC, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[sddc change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/change-compartment.html)command and required parameters to move the SDDC to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeSddcCompartment](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/ChangeSddcCompartment)
