# Updating a Policy's Statements
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_update_the_statements_in_an_existing_policy.htm
- Fetched: 2026-09-05 02:26 CDT

# Updating a Policy's Statements

Update the statements in an IAM policy.

Note  
  

If you use the name of a group, dynamic group, or compartment in a policy, the policy is mapped to the OCID of the group, dynamic group, or compartment when the policy is created. If the OCID of the group, dynamic group, or compartment changes, you must recompile one of the policies that applies to the group or compartment to update the OCID in all the policies.

To recompile the policy, open a policy, and make a small edit. Save the policy.

- On the Policies list page, select the name of a policy to view its details. If you need help finding the list page, see[Listing Polices](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_get_a_list_of_your_policies.htm).
- Under Statements , select Edit Policy Statements .
- Use the Basic policy builder if you want to interact with the statements using graphical controls. Use the Advanced policy builder option to edit the statements in a simple text box.

Basic option:
- To revise a statement, enter the changes by using the format in[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/../policieshow/Policy_Basics.htm).
- To add a statement, select + Another Statement and enter the statement by using the required format.
- To delete a statement, select the X next to the statement.
- To rearrange the order of the statements, use the up and down arrows to move statements to the correct order, or grab the handle to drag statements.

Advanced option:
- Select Advanced .
- Revise the policy statements in the text box by using the format in[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/../policieshow/Policy_Basics.htm).
- Select Save Changes .
