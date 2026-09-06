# Actionable Insights
- Source: https://docs.oracle.com/iaas/operations-insights/doc/actionable-insights.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/operations-insights/doc/actionable-insights.html#dcoc-content-body)

# Actionable Insights

You can receive implementable actionable insights from news reports in JSON format. These insights can be used to further automate tasks on monitored resources, such as increasing CPU or memory based on capacity insights, or adding queries based on SQL Insights information to optimize database performance.

Create an Actionable Insight

To create an actionable insight:
- Open the navigation menu, click Observability &amp; Management , and then click Ops Insights .
- In the left pane, click Administration , and then click Actionable insights .
- Click Create actionable insights .
- Enter a Name and Description .
- Select the Compartment . To include resources from child compartments, select Include child compartments .
- Select the frequency: Daily or Weekly . If you select Weekly , select the day of the week on which the actionable insight is generated and sent.
- In the Actionable insights section, select the insights that you want to receive:

Insight Category Description
New highs Capacity planning Resources that reached a new recorded high utilization level last week.
Big changes Capacity planning Resources with average usage change exceeding plus or minus 25% over the prior week.
Databases with degrading SQLs SQL insights Database list with degradation based on degrading SQLs.
Degrading SQL details by database SQL insights SQL list that had the biggest degradation by average latency change.
Degraded plan changes by SQL ID SQL insights Plan changes (by estimated DB time) that resulted in degradation in average latency across the database instances over last week.
Databases with invalidation storms SQL insights Top databases with the invalidation storms by invalidation rate.
Databases with cursor sharing issues SQL insights Top databases with cursor sharing issues by excess hard parse CPU time.
SQL with cursor sharing issues SQL insights SQL with highest estimated CPU time spent doing excess parsing due to non-sharable cursors.
- Under Notifications service , select a Notifications service topic to be used; or create a new topic. If you are creating a new topic, this will take you to the Notification service user interface. For information, see[Creating a Topic](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-topic.htm).
- After entering and verifying the required information, click Create actionable insight .

Additional Actions with Actionable Insights

Maintenance is an important activity for actionable insights, and under Ops Insights Administration , click Actionable insights to view the list of actionable insights. The Actionable insights page lists actionable insights by name, compartment, actionable insights status, description, frequency, topic OCID, state, and last updated date. Use Search and Filter to filter actionable insights by criteria such as actionable insights status, frequency, and state.
Enable or Disable an Actionable Insight
- Click the Actions menu for the actionable insight and select either Disable or Re-enable .
- In the confirmation dialog, click Disable or Re-enable .
Move a Resource
Note  
  
Moving an actionable insight to a different compartment will NOT modify the resources that are in scope of the report. It will only change the report to a new compartment.
- Click the Actions menu for the actionable insight and select Move resource .
- In the Move resource panel, select the new compartment, and then click Move resource .
Edit an Actionable Insight
- Click the Actions menu for the actionable insight and select Edit actionable insights .
- In the Edit actionable insights panel, update the available fields, such as name, description, and frequency, and click Save changes .
Add Tags
- Click the Actions menu for the actionable insight and select Manage tags .
- In the Manage tags panel, click Add tag to add a tag, and click Save .

Sample Payloads The following are sample JSON payloads for actionable insights:
- New highs for databases sample:
```

```

- Big changes for databases sample:
```

```

- Degrading SQL by database sample:
```

```

- Database with highest invalidation storm sample:
```

```

- Most impacted database by cursor sharing duplicates sample:
```

```

- Top SQL by cursor sharing issues sample:
```

```

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
