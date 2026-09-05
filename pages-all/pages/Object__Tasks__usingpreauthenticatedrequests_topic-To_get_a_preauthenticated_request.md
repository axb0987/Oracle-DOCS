# Getting an Object Storage Pre-Authenticated Request's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm
- Fetched: 2026-09-05 02:51 CDT

# Getting an Object Storage Pre-Authenticated Request's Details

View the details of a pre-authenticated request in a bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Management and find the Pre-authenticated requests section.
All pre-authenticated requests are displayed in a table.
- From the Actions menu for the pre-authenticated request you want, select View pre-authenticated request details .
The Pre-authenticated request details panel opens, containing details of the pre-authenticated request such as the status, the access type, and the expiration date.
- 

Use the[oci os preauth-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/get.html)command and required parameters to get the details of a pre-authenticated request in a bucket:

```

```

The`pre-authenticated_request_id`value is the identification number assigned to the pre-authorized request when it was created. See[Accessing the Pre-Authorized Request ID](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm)for more information.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetPreauthenticatedRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/GetPreauthenticatedRequest)
