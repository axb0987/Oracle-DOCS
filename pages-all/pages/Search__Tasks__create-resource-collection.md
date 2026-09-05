# Creating a Resource Collection
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/create-resource-collection.htm
- Fetched: 2026-09-05 03:03 CDT

# Creating a Resource Collection

Save search criteria and results to create a resource collection that you can access later.

## Using the Console

These steps assume that you already ran an advanced resource query according to the instructions in[Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm)or performed a free text search and selected the Resources category of results according to the instructions in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Tasks/queryingresources_topic-To_perform_a_free_text_search.htm).

- On the Resource Explorer or Resources page, depending on the option available, after you refine the search terms and filters or advanced resource query as needed, select Save as resource collection .
- Select Name , and then enter a name for the resource collection. Avoid entering confidential information.
- Select Description , and then enter a description for the resource collection. Avoid entering confidential information.
- (Optional) In Search query , confirm that the query language specifies the search criteria that you provided.
Search converts the search terms and any filter criteria applied to free text searches and searches performed in basic search mode to query syntax. For more information about query syntax, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- Under Visibility , select one of the following:
- Personal collection : Create the resource collection so that only you can view and use it.
- In compartment : Create the resource collection in a compartment so that you can use permissions to define who in the tenancy can view and use the resource collection.
- (Optional) If, in the previous step, you selected In compartment , select Compartment , and then select the name of the compartment where you want to create the resource collection. Otherwise, continue to the next step.
- Select Create .
