# Listing Load Balancer Cipher Suites
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list_ssl-cipher-suite.htm
- Fetched: 2026-09-05 01:41 CDT

# Listing Load Balancer Cipher Suites

View a list of the cipher suites for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list_ssl-cipher-suite.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list_ssl-cipher-suite.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list_ssl-cipher-suite.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Cipher suites section.
The Cipher suites list opens. All cipher suites in the selected load balancer are displayed in a table.
- To view the cipher suites in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the cipher suites in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a cipher suite to open its details page, where you can view its status and perform other tasks.

To perform an action on a cipher suite directly from the list table, select an available option from the Actions menu in the row for that cipher suite:
- View details : Open the details page for the cipher suite.
- Edit :[Edit the cipher suite's settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Editing_Cipher_Suites.htm).
- Delete :[Delete the cipher suite](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Deleting_Cipher_Suites.htm).

To create a cipher suite, select Create cipher suite .
- 

Use the[oci lb ssl-cipher-suite list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/list.html)command and required parameters to view a list of the cipher suites for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSSLCipherSuites](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/ListSSLCipherSuites)
