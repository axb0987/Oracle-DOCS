# Accessing the Object Storage Pre-Authenticated Request ID
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm
- Fetched: 2026-09-05 02:51 CDT

# Accessing the Object Storage Pre-Authenticated Request ID

Get access to your pre-authenticated request ID.

When you create a pre-authenticated request, a unique identification number for the request is generated. You use this identification number to perform certain tasks, such as getting a pre-authenticated request's details or deleting it using the CLI.

## Using the Console

You can access and copy this number from the pre-authenticated request using the Console. List the pre-authenticated requests as described in[Listing Pre-authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm). Select the Actions menu (three dots) next to the pre-authenticated request whose ID you want to copy and select Copy pre-authenticated request ID . The ID for the selected pre-authentication request is copied to the clipboard.

You can also access and copy the ID from the Pre-authenticated request details panel of the pre-authenticated request. See[Getting a Pre-Authenticated Request's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm)for more information.

## Using the CLI and API

You can access and copy the pre-authenticated request IDs using the List and Get commands in the CLI and API. The IDs appear in the returned output when running these commands and operations. See the following topics for more information:
- [Listing a Pre-Authenticated Request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm)
- [Getting a Pre-Authenticated Request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm)
