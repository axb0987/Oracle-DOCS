# Known Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/knownissues_tagging.htm
- Fetched: 2026-09-05 03:06 CDT

# Known Issues

These known issues have been identified in Tagging.

## Creating a tag default fails under specific conditions

Details: The creation of a tag default fails when both of the following conditions are met: The tag namespace contains only one active key definition and the tag namespace contains multiple retired tag key definitions.

Workaround: To work around this issue, you can create another tag key definition in the tag namespace.

## Deleting a tag default fails when the tag is retired

Details: If you try to delete a tag default for a tag that is retired, you will get an error.

Workaround: Reactivate the tag definition and then delete the tag default.

## Terraform state drift with tag defaults and tags for secondary resources

Details: In some Terraform builds, no tags are created for secondary resources and default tags configured for a compartment are not automatically applied to resources. This can result in missing default tags and secondary resources that do not have tags that match primary resources. In some cases, Terraform can go into an infinite loop.

Workaround: Evaluate your Terraform script and each compartment in the tenancy for potential tagging issues.
- 

Evaluate your Terraform script .
- 

For any primary resource you find that contain tags, copy the free-form or defined tag to the secondary resource. For example, if your Terraform configuration has a primary resource such as a compute instance and a nested secondary resource such as an attached VNIC, copy the tags on the compute instance to the VNIC. VCNs and instance pools are also primary resources that can create secondary resources.
- 

Evaluate the directory tree in the tenancy you will create .
- 

Start at the root compartment and determine if that compartment has any default tags configured. Although tag values are optional, tag defaults can specify that a tag requires a value.
- 

Tag defaults are defined for a specific compartment, and in the Console you manage them on the Compartment Details page.
- If the compartment has any default tags for resources created in this compartment, apply the tags and required tag values that would be created by these defaults to all the resources you will create with your Terraform script. Because of tag inheritance , the default tag is applied to all resources that get created in the compartment, including child compartments and the resources created in the child compartments. See[Tag Inheritance](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults.htm#taginheritance).
-
