# Listing Load Balancer Certificates
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-certificate.htm
- Fetched: 2026-09-05 01:41 CDT

# Listing Load Balancer Certificates

View a list of the Load Balancer service-managed SSL certificates for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-certificate.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Load balancer certificates section.
The Load balancer managed certificates list opens. All Load Balancer service-managed certificates in the selected load balancer are displayed in a table.
- To view the Load Balancer managed certificates in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the Load Balancer managed certificates in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a Load Balancer managed certificate to open its details page, where you can view its status and perform other tasks.

To perform an action on a Load Balancer managed certificate directly from the list table, select an available option from the Actions menu in the row for that &lt;resourceType&gt;:
- View public certificate :[View the Load Balancer managed certificate's details](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_certificate.htm).
- Delete :[Delete the Load Balancer managed certificate](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_certificate.htm).

To add a Load Balancer managed certificate, select Add certificate .
- 

Use the[oci lb certificate list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/certificate/list.html)command and required parameters to list a load balancer's certificates:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListCertificates](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Certificate/ListCertificates)
