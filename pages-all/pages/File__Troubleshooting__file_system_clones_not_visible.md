# File System Clones Aren't Visible
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/file_system_clones_not_visible.htm
- Fetched: 2026-09-05 02:05 CDT

# File System Clones Aren't Visible

You use a file system snapshot to create a clone, but can't view the clone after it's created. Learn about why your clones may not be visible in the Console.

Cause: You don't have permission to work in the compartment that the clone resides in. Resources in a compartment that you don't have access to aren't visible to you.

When you create a clone, you can specify the compartment you want to create it in. The clone doesn't have to be in the same compartment as the parent file system. Another user might move the clone from one compartment (that you have access to) to another (that you don't).

Solution 1: Create the clone in a compartment you have permission to work in.

Solution 2: Obtain permission to work in the compartment that the clone resides in. For information about setting up user access, see[Overview of Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

For general information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm)
