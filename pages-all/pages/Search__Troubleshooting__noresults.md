# Query or Search Results are Not as Expected
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Troubleshooting/noresults.htm
- Fetched: 2026-09-05 03:03 CDT

# Query or Search Results are Not as Expected

There are several reasons why you might not see results that you expect from a search or query.

Not all resource types have been indexed for Search. For a list of currently supported resource types, see[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Troubleshooting/../Concepts/queryoverview.htm#resourcetypes).

You might not have the required permissions for the resource type that you want to view in search or query results. If there's no policy that grants you the permissions you need, then an administrator must create one for you or add you to a group that's already named in a policy. For more information, see[Details for Search](https://docs.oracle.com/iaas/Content/Identity/Reference/searchpolicyreference.htm#Details_for_Search).

The query syntax you used might need adjustment. Verify that the conditions in your query language haven't restricted the results to a narrower set than you intended.
