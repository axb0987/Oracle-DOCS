# Writing Policy Statements with the Policy Builder
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-Using_the_Policy_Builder.htm
- Fetched: 2026-09-05 02:26 CDT

# Writing Policy Statements with the Policy Builder

Work with Policy Builder.

The policy builder in the Console helps you quickly create common policies without the need to manually type the policy statements. The policy builder automatically suggests the permissions that an administrator can grant to groups of users or resources in their tenancy, as well as target resources like instances, networks, and buckets. Users who don't need the suggestions offered by the policy builder or who have more complex policy requirements can bypass the builder's basic option and go straight to the advanced editor, where you can directly enter the policy statements in a free-form text box.

Features of the Policy Builder

The policy builder provides policy templates that you can complete to create policies for your tenancy. A policy template includes all the statements needed to provide the permissions to perform a task or set of related tasks in a service in OCI. To complete the template, select the group from a menu of existing groups in the tenancy and select the location from a list of compartments in the tenancy.

The policy templates in the policy builder are grouped by use case, such as network management, storage management, and account management, to make them easy to browse and find the permission set you need.

For example, assume you are setting up the network administrators for your tenancy. You need to grant a group of users the permissions required to work with all the resources in the Networking service. To create this policy in the policy builder:
- First, find the policy you want: From the Policy use cases menu, select Network Management . If you are not sure which use case a policy belongs to, you can leave this option set to All to browse all the templates.
- From the Common policy templates menu, select Let network admins manage a cloud network .

The policy builder displays the policy statements that will be created. In this case, there is only one statement:
```

```

- Now, all you need to do is select the identity domain and group for the policy: When you select a group, the {group name} in the displayed policy statement also updates with your selection.
- Finally, select the location. You can traverse the compartment hierarchy to find and select the appropriate compartment. To create the policy in the tenancy, choose the root compartment.

## Customizing Policies

If you find that a template doesn't fit your needs exactly, then you can customize the policies provided by adding statements, removing statements, adding conditions, or other changes to create the policy you need. Select Show manual editor to edit the statements in a free-form text box. When entering statements directly in the text box, see[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/../policieshow/Policy_Basics.htm).

Examples of customizing the Network Admins policy:
- You need to include another group (from the default identity domain), GroupB to this policy. To add a group:

Select Show manual editor . In the text box, type the changes to the policy (following the required syntax).
```

```

[
Note  
  
If you include only the group name without an identity domain, then the policy builder assumes the group is in the default identity domain.
- You want to add another statement to the policy. For example, you want GroupA to be allowed to use instances. To add another statement, enter it on the next line:
```

```

## Editing Policies with the Policy Builder
