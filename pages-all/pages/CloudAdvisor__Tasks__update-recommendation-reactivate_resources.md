# Reactivating a recommendation for specific resources
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_resources.htm
- Fetched: 2026-09-05 01:48 CDT

# Reactivating a recommendation for specific resources

Reactivate a Cloud Advisor recommendation for one or more resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_resources.htm#)
- 

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- Select a recommendation to view its details.
- On the recommendation's details page, select Resource recommendations .
- Next to Applied filters , select the Dismissed or Postponed status, depending on whether the recommendation that you want to reactivate was dismissed or postponed.
- Select the resources that you want to reactivate and then, from the Actions menu, select Reactivate selected .
- In the Reactivate selected resources panel, select Reactivate .
The recommendation status changes to Pending for the selected resources.
- 

Use the[oci optimizer recommendation update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/update.html)command to update recommendations for all resources.

```

```

You can update recommendations for one or more resources using[oci optimizer recommendation bulk-apply](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/bulk-apply.html), or for a single resource using[oci optimizer resource-action update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/resource-action/update.html).

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[UpdateRecommendation](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/UpdateRecommendation)operation to update recommendations for all resources.

You can update recommendations for one or more resources using[BulkApplyRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/BulkApplyRecommendations), or for a single resource using[UpdateResourceAction](https://docs.oracle.com/iaas/api/#/en/advisor/latest/ResourceAction/UpdateResourceAction)
