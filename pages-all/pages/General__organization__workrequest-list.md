# Listing Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list.htm
- Fetched: 2026-09-05 02:13 CDT

# Listing Work Requests

List all work requests in Organization Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list.htm#)
- 

You can view[work requests](https://docs.oracle.com/en-us/iaas/Content/General/organization/../Concepts/workrequestoverview.htm)for[sender tenancy invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm), governance rule opt-in join requests,[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm), and[subscription mappings](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-get.htm)in Organization Management.

To view governance rule attachment and detachment work requests:
- Open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Governance Rules .
- On the Governance rules list page, select the rule.
- On the governance rule details page, under Tenancies , select the Actions menu (three dots) for the particular tenancy and then select View work requests .
- In the Work requests panel, the work request operations are listed.
- 

Use the[oci organizations work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/work-request/list.html)command and required parameters to list the work requests in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/organizations/latest/WorkRequest/ListWorkRequests)
