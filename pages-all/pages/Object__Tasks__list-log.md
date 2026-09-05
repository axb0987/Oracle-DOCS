# Listing an Object Storage Bucket's Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-log.htm
- Fetched: 2026-09-05 02:50 CDT

# Listing an Object Storage Bucket's Logs

List the read access events and write access events logs for a Object Storage bucket.

## Using the Console

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Monitoring and find the Logs section.
All logs are displayed in a table.

## Filtering List Results

Use filters to limit the logs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a log to open its details page, where you can view its status and perform other tasks.

To perform an action on a log directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that log:
- View details :[Open the details page for the log](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-log.htm).
- Disable/Enable log :[Enable a disabled log](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-log.htm), or[disable a log that's enabled](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/disable-log.htm).
- Delete :[Remove the log from the bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-log.htm)
