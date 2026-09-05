# Creating a Dynamic Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_create_a_dynamic_group.htm
- Fetched: 2026-09-05 02:21 CDT

# Creating a Dynamic Group

Create a dynamic group in IAM.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/../domains/to-view-identity-domains.htm).
- On the details page, select Dynamic groups . A list of dynamic groups in the domain is displayed.
- Select Create dynamic group .
- Enter the following information:

- Name: A unique name for the group. The name must be unique across all groups in the tenancy (dynamic groups and user groups). You can't change the name later. Avoid entering confidential information.
- Description: A friendly description.
- Enter the Matching rules . Resources that meet the rule criteria are members of the group.

- Rule 1: Enter a rule following the guidelines in[Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm). You can manually enter the rule in the text box or open the rule builder.
- 

Enter more rules as needed. To add a rule, select +Additional rule .
- To assign tags to the group, select Add tag and enter the tagging details.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. You can apply tabs later.
- Select Create .

The matching rule syntax is verified, but the OCIDs aren't. Be sure that the OCIDs you enter are correct.

To give the dynamic group permissions, you need to write a policy. See[Writing Policies for Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/../callresources/Writing_Policies_for_Dynamic_Groups.htm)
