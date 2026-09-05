# Listing Object Storage Buckets
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm
- Fetched: 2026-09-05 02:51 CDT

# Listing Object Storage Buckets

View a list of the Object Storage buckets in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm#)
- 

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
The Buckets list page opens. All buckets in the selected compartment are displayed in a table.
- To view the buckets in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the buckets in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a bucket to open its details page, where you can view its status and perform other tasks.

To perform an action on a bucket directly from the list table, select any of the following options from the Actions menu in the row for that bucket:
- View bucket details :[Open the details page for the bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm)
- Create pre-authenticated request :[Create a pre-authenication request for the bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm).
- Move resource :[Move the bucket to another compartment](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm).
- Edit visibility :[Change the visibility of the bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm)
- Manage tags : Add one or more tags to the bucket. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Delete the bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_delete_a_bucket.htm).

To create a bucket, select Create bucket .
- 

Use the[oci os bucket list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/list.html)command and required parameters to list the buckets in a compartment:
```

```

For example:
```

```

By default, getting a list of buckets returns up to the first 1,000 buckets in the compartment.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Using Field Tags

By default when listing buckets,`null`is returned as the value for both free-form and defined tags. To include[resource tag](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)data, include the`--fields tags`parameter:

```

```

For example:
```

```

- 

Run the[ListBuckets](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ListBuckets)operation to list the buckets in a compartment.

When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```

```
