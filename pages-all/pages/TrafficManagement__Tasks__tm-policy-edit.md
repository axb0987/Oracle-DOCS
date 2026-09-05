# Editing a Steering Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm
- Fetched: 2026-09-05 03:07 CDT

# Editing a Steering Policy

Edit information for a Traffic Management steering policy such as name, TTL, answers, health checks, and tags.
Domain attachments are added and published in a different workflow. See[Attaching a Domain to a Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm)for more information. See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and general information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm#)
- 

- On the Traffic management steering policies list page, select the policy you want to work with. If you need help finding the list page, see[Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top).
- Select Manage policy .
- Update the policy information.
For descriptions of the fields, see[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)and select the task that pertains to the type of policy you're editing.
- Select Save changes .
- On the policy details page, edit, add, or delete tags as follows:

- To edit or remove a tag, select the Tags tab, select the edit icon next to a tag, and change its value or remove it.
- To add one or more tags, select Add tags and enter the tag namespace (for a defined tag), key, and value.
- 

Use the[steering-policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/update.html)command and required parameters to edit a steering policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/UpdateSteeringPolicy)
