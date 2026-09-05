# Postponing a Recommendation for All Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_rec.htm
- Fetched: 2026-09-05 01:48 CDT

# Postponing a Recommendation for All Resources

Postpone a Cloud Advisor recommendation for all resources and specify the date to reactivate the recommendation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_rec.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_rec.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-postpone_rec.htm#)
- 

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- For the recommendation that you want to postpone, select the Actions menu (three dots) and then select Postpone .
- In the Postpone recommendation panel, select a new date when the recommendation reactivates, and then select Postpone .
The recommendation continues to have the Postponed status for all resources. On the selected date, the recommendation status changes to Active for all resources.
- 

Use the[oci optimizer recommendation update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/update.html)command to update recommendations for all resources.

```

```

You can update recommendations for one or more resources using[oci optimizer recommendation bulk-apply](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/bulk-apply.html), or for a single resource using[oci optimizer resource-action update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/resource-action/update.html).

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[UpdateRecommendation](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/UpdateRecommendation)operation to update recommendations for all resources.

You can update recommendations for one or more resources using[BulkApplyRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/BulkApplyRecommendations), or for a single resource using[UpdateResourceAction](https://docs.oracle.com/iaas/api/#/en/advisor/latest/ResourceAction/UpdateResourceAction)
