# Additional Required Permissions
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/additional_required_permissions.htm
- Fetched: 2026-09-05 01:47 CDT

# Additional Required Permissions

Cloud Advisor supports a dedicated IAM policy that improves data security and safeguards resource metadata. The new policy is optional for Cloud Advisor APIs that provide resource metadata. When the new policy is granted to users, they can create a request to include this information in the response.

The dedicated policy grants users specific permissions at their compartment or tenancy level to view resource information such as current compute instance shape, object storage namespace, size of boot volume, and more. The policy lets administrators tailor the access to resource metadata, listed by specific resource types, compartments, and recommendations.
For example, policies granting access to O ptimizer-api-family automatically have access to Optimizer-resource-metadata as shown here.
```

```
Policies that are structured with optimizer-resource-action must be updated. An original policy as shown in this example
```

```
must add an additional policy to see resource metadata, as shown in this example:
```

```
To add a policy to your tenancy, use the format shown in this example.
```

```

The policy and associated permissions affects Cloud Advisor users who are granted access to Cloud Advisor APIs without the optimizer-api-family collection (see[Cloud Advisor API](https://docs.oracle.com/iaas/api/index.html#/en/advisor/20200606/)). Users who have access to Resource Action also have access to the details of the underlying resource if they have a policy statement granting access to optimizer-resource-metadata .

When you view recommendations with the Console, you can see the subset of the information about the resources that you have access to. To see all the resource metadata, you must have the optimizer-resource-metadata permission. When you try to view resource details without it, Cloud Advisor displays a message telling you to contact your account administrator to grant you that permission.

Managing the information you can see
When you first display the recommendation or resource details page, only the default columns are displayed. Sometimes these are all the columns that are available for the recommendation you're viewing. To display more columns, in the Recommendation Details page, select Manage Columns to show the list of available columns for the recommendation or the resource. Select the columns you want to view and select Save to display them in the current and future sessions.
Note  
  
If you don't have the correct permissions to view the data in a column, Cloud Advisor replaces the data with notes as described below, displays messages that explain why you can't view the data, and tells what to do to view it.
- On the Resource details page, if the Estimated Savings column shows Not available , select the information Icon in the title of the column to see the explanation. The page also includes an information box that explains about the new Cloud Advisor granular permissions and refers to this documentation.
-
