# Viewing Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm
- Fetched: 2026-09-05 01:57 CDT

# Viewing Work Requests

Find out how to view the operations of Kubernetes Engine (OKE) as work requests.

Many Kubernetes Engine service requests do not take effect immediately. For example, the creation of a node pool isn't completed until all required nodes are active. In these cases, the request is fulfilled asynchronously, and its progress tracked by an associated work request. A work request is an activity log that provides visibility into in-progress asynchronous operations, enabling you to track each step in the operation's progress. Each work request has an OCID that allows you to interact with it programmatically and use it for automation.

Work requests include information about the time the request started and finished. If an operation fails, a work request can help you determine which step of the process had an error. Some operations affect multiple resources. For example, creating a node pool also affects nodes. A work request provides a list of the resources that an operation affects.

For more information, see[Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm)and the[Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/).

## Node Pool Work Requests

Resources managed by Kubernetes Engine can only support one work request at a time. Work requests launched while another work request is in progress will fail and return a conflict. Because some operations depend on the completion of other operations, you must monitor each operation's work request and confirm it has succeeded before proceeding to the next operation. A create node pool work request has a status of Succeeded when the workflow successfully creates a node and the node is registered with an Active status.

## Work Request Status

The following table lists work request states:

Status

Description

Accepted

The request is in the work request queue to be processed.

In Progress

A work request record exists for the specified request, but no associated WORK_COMPLETED record exists.

Succeeded

A work request record exists for this request and an associated WORK_COMPLETED record has the state Succeeded .

Failed

A work request record exists for this request and an associated WORK_COMPLETED record has the state Failed .

Canceling

The work request is in the process of canceling.

Canceled

The work request has been canceled.

## Required IAM Policy for Viewing Work Requests

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: Work requests inherit the permissions of the operation that spawns the work request. To enable users to view the work requests, logs, and error messages for an operation, write a policy that grants users permission to do the operation. For example, to let users see the work requests associated with launching instances, write a policy that enables users to launch instances.

To enable users to list all work requests in a tenancy, use the following policy:

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Listing Work Requests

Find out how to list the work requests for a cluster or node pool resource using Kubernetes Engine (OKE).

You can display a list of work requests for a selected cluster or node pool resource using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#)
- 

- On the Clusters list page, select the name of the cluster for which you want to list work requests. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Work requests tab to list recent work requests for the cluster.
- If you want to list work requests for a particular node pool in the cluster, select the Node pools tab, and then select the name of the node pool.
- 

Select the Work requests tab to list recent work requests for the node pool.
- 

Use the command line interface (CLI) to list the work requests for a cluster or node pool resource.

Enter the following command:

```

```

See the CLI online help for a list of options:

```

```

See[oci ce work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/work-request/list.html)for a complete description of the command.
- 

Run the[ListWorkRequests method to list the work requests for a cluster or node pool resource.

## Getting a Work Request's Details

Find out how to get the details of a work request for a cluster or node pool resource using Kubernetes Engine (OKE).

You can get the details of a work request for a selected cluster or node pool resource using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#)
- 

- On the Clusters list page, select the name of the cluster for which you want to get work request details. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- If you want to get work request details for a particular node pool in the cluster, select the Node pools tab, and then select the name of the node pool.
- 

Select the Work requests tab to list recent work requests.
- 

In the Work Requests list, find the work request for which you want to get details. For each recent work request, you can see the following:
- Operation Type: The operation being performed by the work request.
- Status: See[Work Request Status](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests__conteng-work-request-status)for a list of statuses and their descriptions.
- ID: OCID of the work request.
- Resource: The name of the resource.
- Time Started: UTC-based date-time group when the work request was started.
- Time Finished: UTC-based date-time group when the work request was finished.
- Select a particular work request to see:
- Logs: Information about the stage of the workflow and a timestamp for each stage.
- Errors: Information about errors and the timestamp of the error.
- Associated resources: The name, type, and OCID of resources impacted by the work request.
- 

Use the command line interface (CLI) to get the details of a work request for a cluster or node pool resource.

Enter the following command:

```

```

See the CLI online help for a list of options:

```

```

See[oci ce work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/work-request/get.html)for a complete description of the command.
- 

Run the[
