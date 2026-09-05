# Listing HSM Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm
- Fetched: 2026-09-05 02:33 CDT

# Listing HSM Clusters

Learn how to navigate to the list view for Dedicated Key Management HSM Clusters in the OCI Console.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Dedicated Key Management .

The HSM cluster list page opens. All HSM clusters in the selected compartment are displayed in a table.
- To view the HSM clusters in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the HSM clusters in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of an HSM cluster to open its details page, where you can view its status and perform other tasks.

To perform an action on a HSM cluster directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that HSM cluster:
- View details : Open the details page for the HSM cluster.
- Copy OCID : Copy the OCID of the HSM cluster to the clipboard.
- Manage tags : Add one or more tags to the HSM cluster. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete HSM cluster :[Schedule the detetion of an HSM cluster](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_deleting_hsm_cluster.htm).

To create an HSM cluster, select Create HSM cluster .
- 

Use the[oci kms kms-hsm-cluster hsm-cluster list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/list.html)command and required parameters to list HSM clusters:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListHsmClusters](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/ListHsmClusters)operation with the KMSHSMCLUSTER endpoint to list HSM clusters .
Note  
  

The HSM Cluster Endpoint is used for is used for cluster management operations including Create, Update, List, Get, and Delete. This endpoint is also called the KMSHSMCLUSTER endpoint.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/)
