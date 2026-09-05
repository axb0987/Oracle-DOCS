# Can't Delete VCN: Bastion Still Attached
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting_cannot_delete_vcn.htm
- Fetched: 2026-09-05 01:42 CDT

# Can't Delete VCN: Bastion Still Attached

Virtual Cloud Network (VCN) deletion failed because a bastion remains in the VCN.

Bastions let authorized users connect to target resources that reside in an organization's VCN for a predetermined amount of time. A bastion is associated with a single VCN. You must delete a bastion that remains in a VCN before you can delete the VCN.

- Note the OCID in the error message that you receive when you try to delete the VCN. Bastion OCIDs contain the identifier`bastion`. For example:

```

```

- Note the compartment and subnet information of the VCN that you want to delete to help navigate to and choose the correct bastion.
- [Delete the bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/delete-bastion.htm).
- Try to[delete the VCN](https://docs.oracle.com/iaas/Content/Network/Tasks/delete_vcn.htm)
