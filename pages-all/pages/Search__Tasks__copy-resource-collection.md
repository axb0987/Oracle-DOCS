# Copying a Resource Collection
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/copy-resource-collection.htm
- Fetched: 2026-09-05 03:03 CDT

# Copying a Resource Collection

Copy a resource collection to use it as the basis of a new resource collection.

You can use an existing resource collection to create a new resource collection. You can either keep all the details of the resource collection the same as the existing resource collection or update details as you create the copy. After you create a copy, the existing and new resource collections are treated independently. Changes to one don't affect the other.

## Using the Console

- On the Resource collections list page, select the name of the resource collection that you want to copy. If you need help finding the list page, see[Listing Resource Collections](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/list-resource-collections.htm).
- On the details page, perform one of the following actions, depending on the option available:
- Select Actions , and then select Copy .
- Select Copy .
- Select Name , and then enter a name for the resource collection. Avoid entering confidential information.
- Select Description , and then enter a description for the resource collection. Avoid entering confidential information.
- In Search query , confirm that the query language specifies the search criteria that you want for the new copy of the resource collection.
For more information about query syntax, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- Under Visibility , select one of the following:
- Personal collection : Create the resource collection so that only you can view and use it.
- In compartment : Create the resource collection in a compartment so that you can use permissions to define who in the tenancy can view and use the resource collection.
- (Optional) If, in the previous step, you selected In compartment , select Compartment , and then select the name of the compartment where you want to create the resource collection. Otherwise, continue to the next step.
- Select Create .
