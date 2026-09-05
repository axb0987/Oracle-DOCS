# Deleting a Steering Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm
- Fetched: 2026-09-05 03:07 CDT

# Deleting a Steering Policy

Delete a Traffic Management steering policy.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about traffic management steering policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm#)
- 

- On the Traffic management steering policies list page, select the policy you want to delete. If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).
- From the Actions menu (three dots) for the policy you want to delete, select Delete .
The policy is staged for deletion, along with any associated domain attachments.
- Review the policy deletion information, and then select Delete .
- When the deletion is complete, select Close .
- 

Use the[steering-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/delete.html)command and required parameters to delete a steering policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/DeleteSteeringPolicy)
