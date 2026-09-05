# Getting Started with Cloud Advisor
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm
- Fetched: 2026-09-05 01:47 CDT

# Getting Started with Cloud Advisor

Start using the Cloud Advisor service. Cloud Advisor recommendations can help you save money and improve performance, fault tolerance, and security.

## Required IAM Policies

This page describes the Identity and Access Management requirements and security policies that Cloud Advisor uses to ensure that your resources are protected.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

To get started with Cloud Advisor, an administrator must grant each user access to Cloud Advisor and to the resources that Cloud Advisor recommendations impact through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

The resource name for Cloud Advisor is`optimizer-api-family`. The following is an example policy to grant users access to Cloud Advisor to the resources that Cloud Advisor recommendations impact:

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For more information about Cloud Advisor policies, see[Creating Cloud Advisor policies](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Reference/cloudadvisorpolicyreference.htm).

Additional Cloud Advisor required permissions

Although the permissions described above let you view the recommendations and some information about them, Cloud Advisor features granular permissions to support compartment and resource based security policies. These permissions are granted at the compartment level rather than the tenancy level as was previously done. If you do not have the correct permissions, you might not be able to view all the recommendation details, or the resource details for the recommendation you are viewing. To view all the recommendation and resource metadata, contact your account administrator to get the permissions for your compartment. For more information, see[Additional Required Permissions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Concepts/additional_required_permissions.htm).

## Operational Status

This section describes the Cloud Advisor operational (enrollment) statuses and explains how to get, list, and change them.

[Listing the Cloud Advisor Operational Status](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm#list-enrollment-statuses)

[Getting the Cloud Advisor Operational Status](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm#get-enrollment-status)

[Enabling and Disabling Cloud Advisor](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm#update-enrollment-status)

### Listing the Cloud Advisor Operational Status

This section describes how to list the Cloud Advisor operational status for a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm#)
- 

Open the navigation menu and select Governance &amp; Administration . Under Cloud Advisor, select Settings .
The Cloud Advisor Settings page opens. The operational status of Cloud Advisor is shown, either Active or Disabled.
- 

Use the command[oci optimizer enrollment-status-summary list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/enrollment-status-summary/list.html)to list the operational statuses for a compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[ListEnrollmentStatuses](https://docs.oracle.com/iaas/api/#/en/advisor/latest/EnrollmentStatusSummary/ListEnrollmentStatuses)operation to list the operational statuses for a compartment.

### Getting the Cloud Advisor Operational Status

This section describes how to obtain the Cloud Advisor operational status for a compartment.
Note  
  
The Console function is not available for this task. It can be performed only with the CLI or API.

#### Using the CLI

Use the[oci optimizer enrollment-status get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/enrollment-status/get.html)command to get the status of a Cloud Advisor enrollment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).

#### Using the API

Use the[GetEnrollmentStatus](https://docs.oracle.com/iaas/api/#/en/advisor/latest/EnrollmentStatus/GetEnrollmentStatus)operation to get the Cloud Advisor operational status.

### Enabling and Disabling Cloud Advisor

This section explains how to activate or deactivate Cloud Advisor.
Note  
  
You can use only the Console to complete this task.

#### To enable Cloud Advisor

The following procedure explains how to enable Cloud Advisor. This task can be performed only from the Console.

Note  
  
The tenancy that you are signed in to must have resources in it before you can activate Cloud Advisor. If Cloud Advisor fails to activate, check the tenancy to see if resources exist, and add resources as needed.
Note  
  
When you sign in to a tenancy with resources, Cloud Advisor is automatically activated by default.

- Navigate to the Cloud Advisor Settings page. If you need help finding the Settings page, see[Listing the Cloud Advisor Operational Status](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/cloudadvisor-getting_started.htm#list-enrollment-statuses).
- Select Activate .
- In the Activate Cloud Advisor dialog box, select Enable .

#### To disable Cloud Advisor

The following procedure explains how to disable Cloud Advisor. This task can be performed only from the Console.

- Navigate to the Cloud Advisor Settings page. If you need help finding the Settings page, see[Listing the Cloud Advisor Operational Status](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/cloudadvisor-getting_started.htm#list-enrollment-statuses).
- Select Disable .
- In the Disable Cloud Advisor dialog box, select Disable .

## Enabling Cloud Guard

Cloud Guard integrates with Cloud Advisor to display security recommendations in the Cloud Advisor dashboard. After you enable Cloud Advisor, you can integrate Cloud Guard.

To enable Cloud Guard, follow the steps in[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm)
