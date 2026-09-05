# Attaching a Domain to a Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm
- Fetched: 2026-09-05 03:07 CDT

# Attaching a Domain to a Policy

Create a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about traffic management steering policies and domain attachments.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm#)
- 

- On the Traffic management steering policies list page, select the policy you want to work with. If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).

Tip  
  
You can use search for a policy by name in the Search field. You can also use the Time Created sort filter to sort the policies chronologically in ascending or descending order.
- Select the Attached domains tab.
- Select Add Attached Domain(s)
- In the Add Attached Domain(s) panel, enter the domain and then select a compartment and zone.
- Select Add .
- Select View changes to review the attached domain information, and then select Publish .
- Select Publish changes .
- 

Use the[steering-policy-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy-attachment/create.html)command and required parameters to create a steering policy domain attachment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/CreateSteeringPolicyAttachment)operation to create a steering policy domain attachment.

See[Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/trafficmanagementapi.htm)
