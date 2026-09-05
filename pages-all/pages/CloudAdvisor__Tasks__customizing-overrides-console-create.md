# Creating Recommendation Overrides
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/customizing-overrides-console-create.htm
- Fetched: 2026-09-05 01:47 CDT

# Creating Recommendation Overrides

Create overrides for one or more Cloud Advisor recommendations.

You can customize recommendations for resources in specific compartments and for resources with certain tags by creating recommendation overrides. You can create up to 50 recommendation customizations, including overrides. To create an override, you must specify at least one compartment or tag.

In addition to the standard[Cloud Advisor permissions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Reference/cloudadvisorpolicyreference.htm), to use overrides on compartments, you must belong to a group that has the COMPARTMENT_INSPECT permission. To use overrides with tags, you must belong to a group that has the TAG_NAMESPACE_INSPECT permission. For more information, see[Details for IAM with Identity Domains](https://docs.oracle.com/iaas/Content/Identity/policyreference/iampolicyreference.htm).

- Navigate to the Cloud Advisor Settings page. If you need help finding the Settings page, see[Viewing Customizations and Overrides](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/customizing-overrides-console-view.htm#customizing-overrides-console-view).
- Select Overrides .
- Select Create override .
- On the Create new override page, enter the following information:

- In the Name field, enter a unique name for the override.
- In the Recommendation field, select the recommendation that the override applies to. The menu lists only recommendations that are customizable.
- Select Next .
- In the Recommendation logic section, specify the recommendation profile to use for the resources impacted by this override:

- In the Evaluation period field, select the time span that you want Cloud Advisor to use to collect data for recommendations.
- In the Methodology field, select either P95 or Average and then select the Conservative , Standard , or Aggressive profile. For more information, see[Profile Descriptions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-customizing-profiles.htm).
- 
Note  
  
The Evaluation period and Methodology fields are only available for some profile types and might not apply.
- Select Next .
- In the Overrides section, select up to 10 compartments for this override. You can select a compartment using the name, OCID, or path.
The override applies to the resources in the selected compartments.
- Optional : In the Tag overrides section, select Add tag override . The override you're creating applies to the resources that contain the specified tags.

Note  
  
Only defined tags are supported. The tag must be for the compartment, inherited from one compartment to another, or inherited from a compartment to the resource.
- 
- For Tag namespace , select the tag namespace that contains your tags. Cloud Advisor supports the following characters for the tag namespace: 0-9, a-z, A-Z, _, @, -, : .
- For Tag key , select the name that refers to the tag. Cloud Advisor supports the following characters for the tag key: 0-9, a-z, A-Z, _, @, -, : .
- For Match type , select either Match any value or Specify matching values . With Match any value , the override applies to any resource with the tag selected in the Tag key field. With Specify matching values , select or enter tag values. The override applies only to resources with the tag key and tag values specified. The tag values can contain any UTF-8 characters except single quotation marks.
- To add another tag override, select Add tag override and repeat the previous step. You can create up to 10 tag overrides.
- Select Next .
- On the Review and create page, review the override and then select Save .
