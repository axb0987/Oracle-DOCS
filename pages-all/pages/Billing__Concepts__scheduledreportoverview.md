# Scheduled Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/scheduledreportoverview.htm
- Fetched: 2026-09-05 01:43 CDT

# Scheduled Reports

You can generate scheduled reports based on saved reports from Cost Analysis.

After you have created a[saved report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports)in Cost Analysis, use the Scheduled Reports page to create a scheduled report that runs a single time, or that recurs daily or monthly. Scheduled reports are saved in an Object Storage[Standard storage tier](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)bucket, which you can access from the scheduled report details page.
Note  
  
Only[Standard tier](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)buckets are supported. No other storage tiers are supported with scheduled reports.

You can perform the following Cost Analysis scheduled reports tasks:
- 

[Listing Scheduled Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/schedule-list.htm)
- 

[Creating a Scheduled Report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/schedule-create.htm)
- 

[Getting a Scheduled Report's Details](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/schedule-get.htm)
- 

[Editing a Scheduled Report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/schedule-update.htm)
- 

[Listing a Scheduled Reports Run History](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/scheduled-run-list.htm)
- 

[Getting a Scheduled Report Run's Details](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/scheduled-run-get.htm)
- 

[Deleting a Scheduled Report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/schedule-delete.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).
- 

To use Scheduled reports in the Console, the same IAM policies that grant you access to Cost Analysis also give you access to the Scheduled reports pages. See[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#policy)for more information.
- 
To use scheduled report API operations, and to grant write permissions to the Object Storage bucket and compartment where scheduled reports are saved, the following policy is required in the compartment the bucket is located in:
```

```

Where &lt;BUCKET-NAME&gt; is the name of the Object Storage bucket and &lt;COMPARTMENT-NAME&gt; is the compartment that you want the scheduled report results saved to, and`metering_overlay`refers to the[commercial realm](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
Note  
  
For any Object Storage buckets that reside in subcompartments, the Scheduled reports policies must also be enabled for the corresponding subcompartments, in addition to the root compartment, for full scheduled report functionality.

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
