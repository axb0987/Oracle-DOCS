# Getting an Object Storage Work Request's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm
- Fetched: 2026-09-05 02:50 CDT

# Getting an Object Storage Work Request's Details

View the details of an Object Storage work request.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Work requests .
The Work requests tab opens. All work requests for the bucket are displayed in a table.
The Work requests list displays details on each work request. These details include the status, resource type, operation type, resource name, and time accepted for each work request.
- 

Use the[oci os work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/work-request/get.html)command and required parameters to get the details of a Object Storage work request:

```

```

List the work requests in a compartment to get their IDs. See[Listing Work Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Tasks/list-work-request.htm)for more information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/WorkRequest/GetWorkRequest)
