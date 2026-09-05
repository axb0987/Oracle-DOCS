# Reactivating a recommendation for All Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_rec.htm
- Fetched: 2026-09-05 01:48 CDT

# Reactivating a recommendation for All Resources

Reactivate a Cloud Advisor recommendation for all resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_rec.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_rec.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/update-recommendation-reactivate_rec.htm#)
- 

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- Next to Applied filters , select the Dismissed or Postponed status, depending on whether the recommendation that you want to reactivate was dismissed or postponed.
- For the recommendation that you want to reactivate, select the Actions menu (three dots) and then select Reactivate .
- In the Reactivate recommendation dialog box, select Reactivate .
The status of the recommendation changes to Active for all resources.
- 

Use the[oci optimizer recommendation update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/update.html)command to update recommendations for all resources.

```

```

You can update recommendations for one or more resources using[oci optimizer recommendation bulk-apply](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/bulk-apply.html), or for a single resource using[oci optimizer resource-action update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/resource-action/update.html).

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[UpdateRecommendation](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/UpdateRecommendation)operation to update recommendations for all resources.

You can update recommendations for one or more resources using[BulkApplyRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/BulkApplyRecommendations), or for a single resource using[UpdateResourceAction](https://docs.oracle.com/iaas/api/#/en/advisor/latest/ResourceAction/UpdateResourceAction)
