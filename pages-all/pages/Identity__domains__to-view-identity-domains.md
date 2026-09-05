# Listing Identity Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm
- Fetched: 2026-09-05 02:21 CDT

# Listing Identity Domains

Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .

The Domains list page opens. All identity domains in the selected compartment are displayed in a table.

If you have only one identity domain, it's the Default identity domain. For more information about the Default identity domain, see[The Default Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/the_default_domain.htm).
- To view the domains in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the domains in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, perform any of the following actions:

- Select the name of a domain to open its details page, where you can view its status and perform other tasks.
- Select the link in the Users column to access the Users page of the identity domain.
- Select the link in the Groups column to access the Groups page of the identity domain

To perform an action on a domain directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that domain:
- Copy OCID : Copy the OCID of the domain to the clipboard.
- View details : Open the details page for the domain.
- Manage tags : Add one or more tags to the domain. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

To create a domain, select Create domain .
- 

Use the[oci iam domain list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/list.html)command and required parameters to list the identity domains in a specific compartment in a tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
-
