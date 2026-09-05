# Deleting Links to Invited Child Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm
- Fetched: 2026-09-05 02:12 CDT

# Deleting Links to Invited Child Tenancies

As a parent tenancy, you can remove an invited child tenancy from the organization. Only invited child tenancies can be removed. Removing an invited child tenancy unlinks the tenancy from the organization so that the parent doesn't have cost or governance access.

By removing the invited child tenancy, the parent tenancy can no longer manage it. The parent tenancy can't view the invited child tenancy's future cost and usage information, nor manage its subscription mapping. If you want the child tenancy to consume from another subscription that's within the organization, you don't need to remove the tenancy. Instead, you can use[subscription mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm)to map the tenancy to another subscription.

For created child tenancies, you can transfer the tenancy to another organization by using the CLI. For more information about using the[oci organizations organization-tenancy approve-organization-tenancy-for-transfer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/approve-organization-tenancy-for-transfer.html)and[oci organizations organization-tenancy unapprove-organization-tenancy-for-transfer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/unapprove-organization-tenancy-for-transfer.html)commands, see[Approving a Created Child Tenancy for Transfer](https://docs.oracle.com/en-us/iaas/Content/General/organization/approve-createdchildtenancy-for-transfer.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm#)
- 

To remove an invited child tenancy, you first need to[remove it from organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm), use the Subscription Mapping page to[assign the tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm)back to its original subscription, and then remove the tenancy from the Tenancies page after the tenancy has been remapped to its original subscription.
Important  
  
Before removing a child tenancy, ensure that the child tenancy's Oracle Universal Credits subscription isn't the organization's default Universal Credits subscription. For more information see[Setting the Default Subscription](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-setdefault.htm).

To remove an invited child tenancy, follow these steps:

- Open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Tenancies .
- On the Tenancies list page, select the invited tenancy that you want to remove.
- On the details page, remove the tenancy from[organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)by selecting Remove from organization governance and then confirming the removal.
For more information about removing governance rules, see[Removing Governance from Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm). For information about opting into and out of organization governance, see[Opting In Tenancies to Use Governance Rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm)and[Removing Governance from Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm).
- Go back to the Tenancies list page. Note that the tenancy is now listed as Not joined .
- In the navigation pane on the left side of the page, select Subscription Mapping .
- On the Subscription Mapping list page, select the child tenancy's original Universal Credits subscription in the Subscription ID column.
- On the subscription mapping details page, under Mapped tenancies , select Map subscription .
- In the Map subscription panel, select the checkbox next to the child tenancy to map back to this subscription. Then, select Map Subscription .

A notification message is displayed informing you that you successfully mapped the subscription to the tenancy. The tenancy then appears under Mapped Tenancies on the subscription mapping details page.

Note  
  
If other tenancies are mapped to this subscription, you must unmap any other tenancies from the subscription. See[Unmapping a Subscription from a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm).
- In the navigation pane on the left side of the page, select Tenancies .
- On the Tenancies list page, select the Actions menu (three dots) for the tenancy that you want to remove and select Remove Tenancy . Confirm the removal.

Any subscriptions mapped to this tenancy move with the tenancy and are no longer associated with your organization. You might also need to reload the Tenancies page to verify that the invited tenancy has been removed.

If you see the following error message in the Remove Tenancy dialog box, it means that you haven't yet mapped the child tenancy back to its own Oracle Universal Credits subscription:

"Child isn't consuming from its own UCM subscription,`ocid1.tenancy.oc1.. <unique_ID>`"

The child tenancy is removed from the organization with its original subscription. Because you mapped the child tenancy back to its original subscription, the tenancy now consumes from its own subscription, and is responsible for paying for the subscription usage. Furthermore, because the tenancy has been removed from the organization, it now becomes a standalone parent tenancy of its own, which is indicated on the removed tenancy's own Tenancies page (under Tenancy name , Parent tenancy is indicated).
- 

Use the[oci organizations link delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/link/delete.html)command and required parameters to start a link termination workflow:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteLink](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Link/DeleteLink)
