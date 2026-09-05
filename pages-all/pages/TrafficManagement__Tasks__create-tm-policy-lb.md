# Creating a Load Balancer Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-lb.htm
- Fetched: 2026-09-05 03:07 CDT

# Creating a Load Balancer Policy

Create a Load Balancer traffic management policy that distributes traffic across many endpoints.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about Load Balancer policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-lb.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-lb.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-lb.htm#)
- 

- On the Traffic management steering policies list page, select Create traffic management steering policy . If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).
- For Policy type , select Load balancer .
- Enter the following information:

- Policy name: A unique name that identifies the policy. Avoid entering confidential information.
- Compartment: The compartment to create the policy in, if it's different than the one you selected before.
- Policy TTL : The time to live for responses from the policy. If not specified, the system sets this value.
- Maximum answer count : The maximum number of answers returned for the policy.
- 

Answer(s): Answer pools contain the group of answers to serve in response to DNS queries.
- Name: A unique name to identify the answer. Avoid entering confidential information.
- Type: The record type to provide as the answer.
- Rdata: A valid domain name or IP address to add as an answer.
- Weight: A number between 0 and 255 used to decide how often an answer is served in relation to other answers. Answers with higher values are more likely to be served.
- Eligible: Select the checkbox to indicate that the answer is available within the pool to be used in response to queries.
- Attach health check: Select an existing health check to be included as part of the policy, add a new one, or select None .
- Attach domain(s): (Optional) The domain name and domain OCID that you want to attach to the policy. You can add more domains as needed.
- (Optional) Select Show Advanced Options: to apply tags to the policy.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create policy .
- 

Use the[steering-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/create.html)command and required parameters to create a Load Balancer steering policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy)operation to create a Load Balancer steering policy. Specify the`TemplateType`parameter as`LOAD_BALANCE.`

See[Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/trafficmanagementapi.htm)
