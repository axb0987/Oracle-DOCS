# Editing a Global Recommendation Override
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/customizing-overrides-console-edit-global.htm
- Fetched: 2026-09-05 01:47 CDT

# Editing a Global Recommendation Override

Edit a global override for one or more recommendations.

For some recommendation types, you can customize the logic that Cloud Advisor uses. The default configuration uses the standard profile and the average methodology.
Note  
  
Changes made to recommendation settings take effect the next time Cloud Advisor scans the tenancy.

- Navigate to the Cloud Advisor Settings page. If you need help finding the Settings page, see[Viewing Customizations and Overrides](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/customizing-overrides-console-view.htm#customizing-overrides-console-view).
- Select Global recommendations .
- Find the recommendation that you want to edit, select the Actions menu (three dots) , and then select Edit .
- In the Edit recommendation logic panel, select the following items (if applicable):

Note  
  
The Evaluation period and Methodology fields are available for only certain profile types and might not apply.

- In the Evaluation period field, select the time span that Cloud Advisor uses to collect data for recommendations.
- In the Methodology field, select either P95 or Average .
- In the Profile section, select the Conservative , Standard , or Aggressive profile. For more information, see[Profile Descriptions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-customizing-profiles.htm).
-
