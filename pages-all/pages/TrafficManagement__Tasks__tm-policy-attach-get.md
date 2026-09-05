# Viewing Details for an Attached Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm
- Fetched: 2026-09-05 03:07 CDT

# Viewing Details for an Attached Domain

View details about a domain attached to a Traffic Management steering policy.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about traffic management steering policies and domain attachments.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm#)
- 

Use these steps to view information about the domain (zone) attached to a policy.

- On the Traffic management steering policies list page, select the policy you want to work with. If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).

Tip  
  
You can use search for a policy by name in the Search field. You can also use the Time Created sort filter to sort the policies chronologically in ascending or descending order.
- Select the Attached domains tab.
Domain attachments are listed in tabular form.
- Select the domain name to view details about it.
The domain's zone details page contains information about the domain zone, both general information and links to its resources. Items in this page are read-only.
- 

Use the[steering-policy get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/get.html)command and required parameters to view details about a steering policy attachment.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/GetSteeringPolicy)
