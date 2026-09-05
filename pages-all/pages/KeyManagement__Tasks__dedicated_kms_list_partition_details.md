# Listing HSM Partitions
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_partition_details.htm
- Fetched: 2026-09-05 02:33 CDT

# Listing HSM Partitions

Learn how to list HSM partitions in OCI Dedicated Key Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_partition_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_partition_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_partition_details.htm#)
- 

- On the HSM cluster list page, find the HSM cluster that you want to work with. If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- Select the name of the HSM cluster containing the partitions you want to list.
- Select the HSM partitions tab to see a list of the partitions in the cluster.

## Filtering List Results

Use filters to limit the partitions in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a partition to open its details page, where you can view its status and perform other tasks.

To perform an action on a partition directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that partition:
- Copy OCID : Copy the OCID of the HSM partition to the clipboard.
- 

Open a command prompt and run[oci kms kms-hsm-cluster hsm-partition list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-partition/list.html)to list HSM partitions.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ListHsmPartitions](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmPartition/ListHsmPartitions)API with the KMSHSMCLUSTER endpoint to list HSM partitions.
Note  
  

The HSM Cluster Endpoint is used for is used for cluster management operations including Create, Update, List, Get, and Delete. This endpoint is also called the KMSHSMCLUSTER endpoint.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
