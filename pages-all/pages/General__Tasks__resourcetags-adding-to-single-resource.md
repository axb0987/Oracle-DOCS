# Adding a Tag to a Single Resource
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-adding-to-single-resource.htm
- Fetched: 2026-09-05 02:11 CDT

# Adding a Tag to a Single Resource

Add one or more tags to a resource in Oracle Cloud Infrastructure to help you organize and list resources based on your business needs.

This page describes adding tags to an existing resource. You can also add tags to a resource when you create it.

To apply a defined tag to a resource, you must have permission to use the namespace. See[Required Permissions for Working with Defined Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#Who). For more information about how tagging works and tagging concepts, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-adding-to-single-resource.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-adding-to-single-resource.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-adding-to-single-resource.htm#)
- 

- In the Oracle Cloud Console, go to the details page of the resource that you want to add a tag to. For example, to add a tag to a Compute instance:

- Open the navigation menu and select Compute . Under Compute , select Instances . All instances in the selected compartment are displayed in a table. To view the instances in a different compartment, use the Compartment filter to switch compartments.
- Select the instance that you want to work with to open its details page.
- On the details page, perform one of the following actions depending on the option that you see:

- On the Tags tab, select Add .
- Select Add tags .
- Enter the following information for the new tag:

- Namespace: To apply a defined tag, select its tag namespace from the list. To add a free-form tag, select None .
- Key: If you’re applying a defined tag, select a key that’s associated with the tag namespace. If you’re adding a free-form tag, enter a key. Keys for free-form tags are case sensitive.
- Value: Enter a value or select one from the list. Values are case sensitive.
- Add more tags as needed.
- When you’re done adding tags, select Add tags .
- 

For most resources, use the resource's`update`command with the`--defined-tags`or`--freeform-tags`option.

See[Get Started with the Command Line Interface](https://docs.oracle.com/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm)for more information.
- 

For most resources, use the resource's`update`operation with the`definedTags`or`freeformTags`attribute and their values.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm)
