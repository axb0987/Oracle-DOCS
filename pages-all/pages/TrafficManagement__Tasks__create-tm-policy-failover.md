# Creating a Failover Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm
- Fetched: 2026-09-05 03:07 CDT

# Creating a Failover Policy

Create a failover traffic management policy to prioritize the order in which you want answers served in response to DNS queries.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about failover policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm#)
- 

- On the Traffic management steering policies list page, select Create traffic management steering policy . If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).
- For Policy type , select Failover .
- Enter the following information:

- Policy name: A unique name that identifies policy. Avoid entering confidential information.
- Compartment: The compartment to create the policy in, if it's different than the one you selected before.
- Policy TTL : The time to live for responses from the policy. If not specified, the system sets this value.
- Maximum answer count : The maximum number of answers returned for the policy. For priority-based policies, the first valid answer is returned.
- 

Answer pool(s): Answer pools contain the group of answers that are served in response to DNS queries.
- Answer pool name: : A user-friendly name for the answer pool, unique within the steering policy. Avoid entering confidential information.
- Name: A unique name to identify the answer. Avoid entering confidential information.
- Type: The record type to provide as the answer.
- Rdata: A valid domain name or IP address to add as an answer.
- Weight: A number between 0 and 255 used to decide how often an answer is served in relation to other answers. Answers with higher values are more likely to be served.
- Eligible: Select the checkbox to indicate that the answer is available within the pool to be used in response to queries. Or, select the Actions menu (three dots) and select Mark pool answers eligible or Mark pool answers ineligible .
- 

Pool priority : Failover priority rules specify the priority of answers that are served in a policy. If the primary answer is unavailable, traffic is steered to the next answer in the list.
- Pool: : Select the priority in which the answers are served.
- Attach health check : Select an existing health check to be included as part of the policy, add a new one, or select None .
- Attach domain(s) : The domain name and domain OCID that you want to attach to the policy. You can add more domains as needed.
- (Optional) Select Show Advanced Options: to apply tags to the policy.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create policy .
- 

Use the[steering-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/create.html)command and required parameters to create a failover steering policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy)operation to create a failover steering policy. Specify the`TemplateType`parameter as`FAILOVER.`

See[Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/trafficmanagementapi.htm)
