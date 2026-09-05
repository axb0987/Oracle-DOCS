# Updating Dynamic Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Updating_Dynamic_Groups.htm
- Fetched: 2026-09-05 02:21 CDT

# Updating Dynamic Groups

Update dynamic groups.

You can update the matching rules that define the members of a dynamic group. For example, you might change a matching rule that includes all instances in a compartment to exclude a particular instance. Or, you might update a rule to include a new tag value.
Important  
  

When you make a change to a matching rule you must allow about one hour for the updated policy to take effect. For example, if you update a rule to include instances with a specific tag in the dynamic group, you must wait about one hour before instances with that tag have the access granted in the policy.
