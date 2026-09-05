# Implementing Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/bulk-apply-recommendations.htm
- Fetched: 2026-09-05 01:47 CDT

# Implementing Recommendations

You can implement a recommendation and apply it to one or more resources at the same time.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/bulk-apply-recommendations.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/bulk-apply-recommendations.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/bulk-apply-recommendations.htm#)
- 

To implement recommendations, you typically complete these steps. Note that the fix-it flow might be different depending on the type of recommendation you're implementing. For more details, see[Categories and Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Concepts/recommendations.htm#recommendations).

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- Select a recommendation to view its details.
- On the recommendation's details page, select Resource recommendations .
- Select the resources that you want to implement and then select Implement selected .
A page opens with more details about the recommendation and shows the list of resources impacted by the changes.
- Select Implement .

A notification displays with a link to the work request page, where you can view the work request's progress.

When the work request is complete, the recommendation status changes from Pending to Implemented .
- 

Use the[oci optimizer recommendation bulk-apply](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/bulk-apply.html)command to implement recommendations.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[BulkApplyRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/BulkApplyRecommendations)
