# Enabling an Object Storage Bucket Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-log.htm
- Fetched: 2026-09-05 02:50 CDT

# Enabling an Object Storage Bucket Log

Enable a read access events log or write access events log for a bucket.
Note  
  
You can only enable an read access events or write access events log when there no existing logs of that type present. A bucket can only have one read access events and one write access events log each.

## Using the Console

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Monitoring and find the Logs section.
All logs are displayed in a table.
- From the Actions menu for the log you want, select Enable log .
The Enable log panel opens.
- Enter the following information:

- Compartment : Select the compartment within which the log file resides from the list.
- Log group : Select an existing log group from the list or select Create new group where you can enter the name and description of a new logging group within which your log resides.
- Log name : Enter the name of the log.
- Log retention : Select the time period in months each logging entry is to be retained from the list. One month equals 30 days.

For more information on log and log groups, including naming syntax guidelines, see[Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm).
-
