# Moving a Steering Policy Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm
- Fetched: 2026-09-05 03:07 CDT

# Moving a Steering Policy Between Compartments

Move a steering policy from one compartment to another.

See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for information about compartments and access control.

See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about traffic management steering policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm#)
- 

- On the Traffic management steering policies list page, find the policy you want to move. If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).
- From the Actions menu (three dots) for the policy you want to move, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[steering-policy change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/change-compartment.html)command and required parameters to move a steering policy to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeSteeringPolicyCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/ChangeSteeringPolicyCompartment)
