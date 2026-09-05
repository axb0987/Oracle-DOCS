# Getting Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/get-recommendation.htm
- Fetched: 2026-09-05 01:48 CDT

# Getting Recommendations

This section explains how to get recommendations.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/get-recommendation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/get-recommendation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/get-recommendation.htm#)
- 

This section explains how to use the Console to get recommendations.

- Navigate to the Cloud Advisor Recommendations page. If you need help finding the Recommendations page, see[Listing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Tasks/list-recommendations.htm#list-recommendations-console).
- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list.
- Select a recommendation to view its details.

## To filter the resources in a recommendation list

From a recommendation's details page, you can filter the recommendation's resources by compartment, tag, and region.

- On the recommendation's details page, select Resource recommendations .
- From the Search and Filter box above the list table, use the Tags and Region filters to filter the recommendation's resources.
- To view a recommendation's resources in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

This topic explains how to use the Cloud Advisor CLI to get recommendations.

Use the[oci optimizer recommendation get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation/get.html)command to list recommendations.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[GetRecommendation](https://docs.oracle.com/iaas/api/#/en/advisor/latest/Recommendation/GetRecommendation)
