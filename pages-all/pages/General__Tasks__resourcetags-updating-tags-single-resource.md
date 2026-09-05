# Updating a Tag for a Single Resource
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm
- Fetched: 2026-09-05 02:11 CDT

# Updating a Tag for a Single Resource

Update a tag that has been applied to an existing resource in Oracle Cloud Infrastructure. When you update an existing tag applied to a resource, you can change only the tag’s value.

To update a defined tag for a resource, you must have permission to use the namespace. See[Required Permissions for Working with Defined Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#Who). For more information about how tagging works and tagging concepts, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm#)
- 

- In the Oracle Cloud Console, go to the details page of the resource that you want to update a tag for. For example, to update a tag for a Compute instance:

- Open the navigation menu and select Compute . Under Compute , select Instances . All instances in the selected compartment are displayed in a table. To view the instances in a different compartment, use the Compartment filter to switch compartments.
- Select the instance that you want to work with to open its details page.
- On the details page, select the Tags tab.

The list of tags applied to the resource is displayed.
- Perform one of the following actions depending on the option that you see:

- From the Actions menu (three dots) for the tag that you want to update, select Edit .
- Select the edit icon next to the tag name.
- Enter or select a new value.
- Select Save .
- 

For most resources, use the resource's`update`command with the`--defined-tags`or`--freeform-tags`option.

See[Get Started with the Command Line Interface](https://docs.oracle.com/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm)for more information.
- 

For most resources, use the resource's`update`operation with the`definedTags`or`freeformTags`attribute and their values.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm)
