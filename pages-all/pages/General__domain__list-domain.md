# Listing Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm
- Fetched: 2026-09-05 02:11 CDT

# Listing Domains

List domains in Domain Management .

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm#)
- 

To list domains, in the navigation menu select Governance &amp; Administration . Under Tenancy Management , select Domain Management .

The domains that have been added are listed on the Domain Management page.

## Filtering List Results

Use filters to limit the domains in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

### Actions

To perform an action on a domain directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that domain:
- Copy OCID : Copy the domain OCID.
- Enable Governance :[Enable domain governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm).
- Disable Governance :[Disable domain governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm).
- Update Email : For active domains,[update the domain notification email](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domain.htm).
- Remove Domain :[Remove the domain](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm).
- 

Use the[oci organizations domain list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain/list.html)command and required parameters to list domains:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListDomains](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Domain/ListDomains)
