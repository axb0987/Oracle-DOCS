# Dismissing a Recommendation for Specific Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-dismiss_resources.htm
- Fetched: 2026-09-05 01:48 CDT

# Dismissing a Recommendation for Specific Resources

Dismiss a Cloud Advisor recommendation for one or more resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-dismiss_resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-dismiss_resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-dismiss_resources.htm#)
- 

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- Select a recommendation to view its details.
- On the recommendation's details page, select Resource recommendations .
- Select the resources that you want to dismiss and then, from the Actions menu, select Dismiss selected .
- In the Dismiss recommendation panel, select Dismiss .
The recommendation status for the selected resources changes to Dismissed. Dismissed recommendations are removed from the default view of the details page. You can view them again by filtering the list for the Dismissed status.
- 

Use the[oci optimizer recommendation update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/update.html)command to update recommendations for all resources.

```

```

You can update recommendations for one or more resources using[oci optimizer recommendation bulk-apply](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/bulk-apply.html), or for a single resource using[oci optimizer resource-action update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/resource-action/update.html).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[UpdateRecommendation](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/UpdateRecommendation)operation to update recommendations for all resources.

You can update recommendations for one or more resources using[BulkApplyRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/BulkApplyRecommendations), or for a single resource using[UpdateResourceAction](https://docs.oracle.com/iaas/api/#/en/advisor/latest/ResourceAction/UpdateResourceAction)
