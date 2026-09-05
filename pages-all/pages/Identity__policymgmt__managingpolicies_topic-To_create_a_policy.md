# Creating a Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm
- Fetched: 2026-09-05 02:26 CDT

# Creating a Policy

Create IAM policies to manage access to OCI resources.
Note  
  

If you use the name of a group, dynamic group, or compartment in a policy, the policy is mapped to the OCID of the group, dynamic group, or compartment when the policy is created. If the OCID of the group, dynamic group, or compartment changes, you must recompile one of the policies that applies to the group or compartment to update the OCID in all the policies.

To recompile the policy, open a policy, and make a small edit. Save the policy.

On the Policies list page, select Create Policies . If you need help finding the list page, see[Listing Polices](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_get_a_list_of_your_policies.htm#console).

Creating a Policies consists of the following sections:
- 

1. Basic details
- 

2. Policy Builder
- 

3. Review and Create

Run each of the following workflows in order. You can return to a previous page by selecting Previous .

## 1. Basic Details

- On the Policies list page, select Create Policy . If you need help finding the list page, see[Listing Polices](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_get_a_list_of_your_policies.htm#console).
- Enter the following information:

### 2. Policy Builder

Enter the policy statements using the[policy builder](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-Using_the_Policy_Builder.htm#builder). Use the basic option to select from common policy templates, which you can also customize. Select Show manual editor if you already know how to write the statements you need and you want to enter them in a text box.

To use the policy builder basic option:
- Select from the Policy use cases menu to filter the list of policy templates. If you're not sure which use case to select, you can browse all the templates in the Common policy templates list.
- Select the template that best matches your requirements from the Common policy templates list.

The policy builder displays the description of the chosen policy and lists the policy statements that it includes.
- Select the identity domain that contains the group to which you want to apply this policy.
- Select the group that this policy applies to.
- Select a location. The location is the compartment that this policy grants access to. The compartment you select here must be either the compartment you chose to attach the policy to in Step 3, or a compartment within the hierarchy of that compartment.
- If you need to update the policy statements, select Show manual editor .

### Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

## 3. Review and Create
