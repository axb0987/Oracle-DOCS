# Understanding Automatic Tag Defaults
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingautomaticdefaulttags.htm
- Fetched: 2026-09-05 03:06 CDT

# Understanding Automatic Tag Defaults

Use tag defaults to manage resources in your tenancy, including tracking costs by principal name and the date resources are created. In tenancies created after December 17, 2019, the`Oracle-Tags`tag namespace and two tag defaults are automatically added to the root compartment. These tag defaults apply tags to all resources with the following values:
- `CreatedBy`tag: This tag is used to automatically record the name of the principal that created the resource.
- `CreatedOn`tag: This tag is used to automatically record the date and time the resource was created.

When users create resources in your tenancy, each tag is added to the resource by OCI, and the values are generated automatically through the use of tag variables. For more information on variables, see[Using Tag Variables](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/usingtagvariables.htm).

The tenancy administrator has permission to update or delete the`Oracle-Tags`tag namespace. If the`Oracle-Tags`namespace isn't present, the`CreatedBy`and`CreatedOn`tags aren't automatically applied during resource creation.

## Working with Automatic Tag Defaults

You can remove and update tags automatically applied to resources as you would any other tag. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

If you no longer want these tags applied to resources automatically, you can remove the tag defaults that Oracle created. Although Oracle created the tag defaults, they are ordinary tag defaults that you can manage as you would any other. For more information, see[Managing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagdefaults.htm)
