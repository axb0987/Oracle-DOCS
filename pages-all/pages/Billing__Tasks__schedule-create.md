# Creating a Cost Analysis Scheduled Report
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-create.htm
- Fetched: 2026-09-05 01:43 CDT

# Creating a Cost Analysis Scheduled Report

Create a Cost Analysis scheduled report in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-create.htm#)
- 

- On the Scheduled reports list page, select Create a scheduled report . If you need help finding the list page or the scheduled report, see[Listing Cost Analysis Scheduled Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Tasks/schedule-list.htm).
- In the Create a scheduled report panel, enter the following information:
- Name : Enter a name for the scheduled report. Avoid entering confidential information.
- Description : (Optional) Enter a description of the scheduled report. Avoid entering confidential information.
- Saved report : Select the[saved report](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Concepts/costanalysisoverview.htm#saving_reports)to associate with the scheduled report.
- Start date : Select the date to start the scheduled report on.
- Recurrence : Select the frequency of the scheduled report.
- Format : Select the format for the scheduled report: CSV or PDF
- Region : Select the region for the scheduled report.

Scheduled reports can be saved only in one region, so you can select the region where your files are saved.
- Bucket : Select the Object Storage[Standard storage tier](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)bucket to save the scheduled report results to.
Note  
  
Only[Standard tier](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)buckets are supported. No other storage tiers are supported with scheduled reports.

You must have the required policy to grant write permissions to the bucket. For more information, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Concepts/scheduledreportoverview.htm#scheduledreports_required_IAM_policy).
- Select Create .

A message indicates that the scheduled report was saved successfully.
- 

Use the[oci usage-api schedule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/usage-api/schedule/create.html)command and required parameters to create a Cost Analysis scheduled report:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateSchedule](https://docs.oracle.com/iaas/api/#/en/usage/latest/Schedule/CreateSchedule)
