# File System Resources Aren't Visible in the Console
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/resources_aren_t_visible.htm
- Fetched: 2026-09-05 02:06 CDT

# File System Resources Aren't Visible in the Console

You create a resource, but can't view it after it's created. Learn about why a file system resource might not be visible to you.

Cause: You don't have permission to work in the compartment that the resource resides in. Resources in a compartment that you don't have access to aren't visible to you.

When you create a resource, you can specify the compartment you want to create it in. The resource doesn't have to be in the same compartment as related file system resources. Another user might move the resource from one compartment (that you have access to) to another (that you don't).

Solution 1: Create the resource in a compartment you have permission to work in.

Solution 2: Obtain permission to work in the compartment that the resource resides in. For information about setting up user access, see[Overview of Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm)
