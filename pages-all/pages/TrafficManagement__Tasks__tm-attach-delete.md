# Deleting a Domain Attachment
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm
- Fetched: 2026-09-05 03:07 CDT

# Deleting a Domain Attachment

Delete a domain attachment to a Traffic Management steering policy.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about traffic management steering policies and domain attachments.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm#)
- 

- On the Traffic management steering policies list page, select the policy you want to delete. If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).

Tip  
  
You can use search for a policy by name in the Search field. You can also use the Time Created sort filter to sort the policies chronologically in ascending or descending order.
- Select the Attached domains tab.
Domain attachments are listed in tabular form.
- Select the domain attachment in the list you want to delete, and then select Delete from the Actions menu (three dots) .
The domain attachment is staged for deletion.
- Select View changes to review the attached domain deletion information, and then select Publish .
- Select Publish changes .
- 

Use the[steering-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/delete.html)command and required parameters to delete a steering policy attachment.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/DeleteSteeringPolicyAttachment)
