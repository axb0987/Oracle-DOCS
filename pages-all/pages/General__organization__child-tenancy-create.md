# Creating a Child Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm
- Fetched: 2026-09-05 02:12 CDT

# Creating a Child Tenancy

Create a child tenancy in your organization.

To create a child tenancy, you provide the necessary information, such as tenancy name and designated administrator email. Then, sign-in instructions are provided in an email notification to the child tenancy administrator. The created (child) tenancy automatically consumes from the default subscription of the organization, so all usage is charged based on the rate card of the subscription. The parent tenancy is also responsible for the child tenancy's usage.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm#)
- 

- Open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Tenancies .
- On the Tenancies list page, select Create new tenancy.
- In the Tenancy details step of the workflow, enter the following information:

- Tenancy name : A name for the child tenancy. The tenancy name must be unique and all lowercase without any special characters. Avoid entering confidential information.
- Home region : The home region is one of the parent's subscribed regions.
- Administrator email : The email address of the tenancy administrator.
- Confirm Email : The email address that you just entered.

The tenancy name must be unique and all lowercase without any special characters. Avoid entering confidential information.
- In the Subscription mapping step of the workflow, you can select the subscription that you want to be associated with the new tenancy.

The tenancy consumes from your organization's default subscription unless you select a different subscription in this step. Only Oracle Universal Credits subscriptions appear as alternate subscription selections.
- In the Governance rules step of the workflow, select[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)to attach to the tenancy, or skip this step and attach them later. You can[attach](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm)or[detach](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-detachrule.htm)rules later, or[opt the tenancy out](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm)of organization governance in the future.

If you want to select governance rules now, select them from the table. You can filter the table by rule name, type, or OCID, or the targeted tenancy. You can expand any rule entry and view its details.

Otherwise, if no governance rules are selected, a message indicates that you're choosing to skip attaching governance rules for now.
- In the Review summary step of the workflow, verify the child tenancy settings that you specified.
- Select Create tenancy .

A notification is displayed, indicating that you successfully requested to create a child tenancy. If the request completes successfully, then your authentication credentials are sent by email momentarily.

The child tenancy administrator receives instructions to activate the tenancy, and to set up a password and[MFA](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-IAM_MFA.htm).
- 

Use the[oci organizations child-tenancy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/child-tenancy/create.html)command and required parameters to create a child tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateChildTenancy](https://docs.oracle.com/iaas/api/#/en/organizations/latest/methods/CreateChildTenancy)operation to create a child tenancy.
Note  
  
When the subscriptionId attribute is specified for a created child tenancy, then more permissions are required. For more information see[CreateChildTenancyDetails Reference](https://docs.oracle.com/iaas/api/#/en/organizations/latest/datatypes/CreateChildTenancyDetails)and[Permissions Required for Each API Operation](https://docs.oracle.com/iaas/Content/Identity/Reference/organizationsreference.htm#organizationsreference_permissions_required_each_api_operation)
