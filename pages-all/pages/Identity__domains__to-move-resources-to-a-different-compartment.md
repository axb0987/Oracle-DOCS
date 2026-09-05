# Moving an Identity Domain Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm
- Fetched: 2026-09-05 02:21 CDT

# Moving an Identity Domain Between Compartments

Move identity domains between compartments in IAM.

You can move any identity domain between compartments within the same tenancy, except the Default identity domain. The Default identity domain can't be moved from the root compartment of the tenancy.

When you move a domain, all its resources are moved with it. For information about moving resources, see[Moving a Resource Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../compartments/To_move_a_resource_to_a_different_compartment.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm#)
- 

- On the Domains list page, select the domain that you want to move. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Move resource .
- Select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci iam domain change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/change-compartment.html)command and required parameters to move an identity domain between compartments within the same tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeDomainCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/ChangeDomainCompartment)
