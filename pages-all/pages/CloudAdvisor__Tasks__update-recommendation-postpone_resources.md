# Postponing a Recommendation for Specific Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_resources.htm
- Fetched: 2026-09-05 01:48 CDT

# Postponing a Recommendation for Specific Resources

Postpone a Cloud Advisor recommendation for one or more resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_resources.htm#)
- 

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- Select a recommendation to view its details.
- On the recommendation's details page, select Resource recommendations .
- Select the resources that you want to postpone and then, from the Actions menu, select Postpone selected .
- In the Postpone recommendations panel, select a date when the recommendation reactivates, and then select Postpone .
The recommendation status for the selected resources changes to Postponed. On the selected date, the recommendation status changes back to Pending for the selected resources.
- 

Use the[oci optimizer recommendation update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/update.html)command to update recommendations for all resources.

```

```

You can update recommendations for one or more resources using[oci optimizer recommendation bulk-apply](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/bulk-apply.html), or for a single resource using[oci optimizer resource-action update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/resource-action/update.html).

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[UpdateRecommendation](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/UpdateRecommendation)operation to update recommendations for all resources.

You can update recommendations for one or more resources using[BulkApplyRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/BulkApplyRecommendations), or for a single resource using[UpdateResourceAction](https://docs.oracle.com/iaas/api/#/en/advisor/latest/ResourceAction/UpdateResourceAction)
