# Creating an ASN Steering Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm
- Fetched: 2026-09-05 03:07 CDT

# Creating an ASN Steering Policy

Create an ASN traffic management steering policy that steers DNS traffic based on Autonomous System Numbers (ASN).
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about ASN steering policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm#)
- 

- On the Traffic management steering policies list page, select Create traffic management steering policy . If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).
- For Policy type , select ASN steering .
- Enter the following information:

- Policy name: A unique name that identifies the policy. Avoid entering confidential information.
- Compartment: The compartment to create the policy in, if it's different than the one you selected before.
- Policy TTL: The time to live for responses from the steering policy. If not specified, the system sets this value.
- Maximum answer count: The maximum number of answers returned for the policy. For priority-based policies, the first valid answer is returned.
- Answer pool(s): Answer pools contain the group of answers served in response to DNS queries.
- Answer pool name: A user-friendly name for the answer pool, unique within the steering policy. Avoid entering confidential information.
- Name: A unique name to identify the answer. Avoid entering confidential information.
- Type: The record type provided as the answer.
- Rdata: A valid domain name or IP address to add as an answer.
- Eligible: Select the checkbox to indicate that the answer is available within the pool to be used in response to queries. Or, select the Actions menu (three dots) and select Mark pool answers eligible or Mark pool answers ineligible .
- ASN steering rules: ASN steering rules specify the priority of answers that are served in a policy. If the primary answer is unavailable, traffic is steered to the next answer in the list.
- ASN: Enter an Autonomous System Number (ASN) used to distribute DNS traffic.
- Pool Priority: Select the priority in which the answers are served.
- Global catch-all: Adding a global catch-all lets you specify answer pools for queries that don't match any of the specified rules that you have added. Select Add global catch-all and select the pool priorities.
- Attach health check: Select an existing health check to be included as part of the policy, add a new one, or select None .
- Attach domain(s) : The domain name and domain OCID that you want to attach to the policy. You can add more domains as needed.
- (Optional) Select Show Advanced Options: to apply tags to the policy.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create policy .
- 

Use the[steering-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/create.html)command and required parameters to create an ASN steering policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy)operation to create an ASN steering policy. Specify the`TemplateType`parameter as`ROUTE_BY_ASN`.

See[Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/trafficmanagementapi.htm)
