# Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm
- Fetched: 2026-09-05 02:54 CDT

# Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures

Find out how to add free-form tags and defined tags to repositories, images, and image signatures with Container Registry.

You can use Oracle Cloud Infrastructure tags to organize, control, manage, and report on the Container Registry resources (repositories, images, image signatures) you use. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata.

Typically, you'll find tagging useful for:
- 

Resource tracking: For example, to report on some or all of the Container Registry resources you use.
- 

Cost tracking: For example, to obtain detailed cost reports for Container Registry repositories, to enable the charging back of usage to the appropriate cost center. Note that you can only use tags applied to repositories for cost tracking purposes.
- 

Authorization grouping: For example, to grant or limit access to repositories with a particular tag. See[Notes on the use of tags to control access to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm#registrytaggingresourceswithfreeformdefinedtagsaccessnotes).

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Using the Console to Specify the Free-form Tags and Defined Tags to Apply to Repositories

To add a free-form tag or defined tag when creating a new repository:
- 

Follow the instructions in[Creating a Repository: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#console)to create a new repository using the Create repository dialog.
- 

Select Add tag .
- 

To add a defined tag to the repository, specify:
- 

Namespace : Select the tag namespace to which the tag belongs.
- 

Key : Select the name of the defined tag to apply to the repository.
- 

Value : Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- 

To add a free-form tag to the repository, specify:
- 

Namespace : Set to None (free-form tags do not belong to a tag namespace).
- 

Key : Enter a name for the free-form tag to apply to the repository.
- 

Value : Enter a value for the tag to apply to the repository.

To add a free-form tag or defined tag to an existing repository:
- 

Follow the instructions in[Editing a Repository: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm#edit-repository-console)to update an existing repository.
- 

Select the Tags tab and select Add .
- 

To add a defined tag to the repository, specify:
- 

Namespace : Select the tag namespace to which the tag belongs.
- 

Key : Select the name of the defined tag to apply to the repository.
- 

Value : Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- 

To add a free-form tag to the repository, specify:
- 

Namespace : Set to None (free-form tags do not belong to a tag namespace).
- 

Key : Enter a name for the free-form tag to apply to the repository.
- 

Value : Enter a value for the tag to apply to the repository.

To update an existing free-form tag or defined tag applied to a repository:
- 

Follow the instructions in[Editing a Repository: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm#edit-repository-console)to update an existing repository.
- 

Select the Tags tab.
- 

Select Edit from the Actions menu (three dots) beside the free-form tag or defined tag you want to change.
- 

Update the tag in the Edit tags panel.

To remove an existing free-form tag or defined tag applied to a repository:
- 

Follow the instructions in[Editing a Repository: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm#edit-repository-console)to update an existing repository.
- 

Select the Tags tab.
- 

Select Delete from the Actions menu (three dots) beside the free-form tag or defined tag you want to delete.
- 

When prompted, confirm the deletion.

## Using the Console to Specify the Free-form Tags and Defined Tags to Apply to Images

To add a free-form tag or defined tag to an image:
- 

Follow the instructions in[Getting an Image's Details: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#console)to see details of the image.
- 

Select the Tags tab and select Add .
- 

To add a defined tag to the image, specify:
- 

Namespace : Select the tag namespace to which the tag belongs.
- 

Key : Select the name of the defined tag to apply to the image.
- 

Value : Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- 

To add a free-form tag to the image, specify:
- 

Namespace : Set to None (free-form tags don't belong to a tag namespace).
- 

Key : Enter a name for the free-form tag to apply to the image.
- 

Value : Enter a value for the tag to apply to the image.

To update an existing free-form tag or defined tag applied to an image:
- 

Follow the instructions in[Getting an Image's Details: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#console)to see details of the image.
- 

Select the Tags tab.
- 

Select Edit from the Actions menu (three dots) beside the free-form tag or defined tag you want to delete.
- 

Update the tag in the Edit tags panel.

To remove an existing free-form tag or defined tag applied to an image:
- Follow the instructions in[Getting an Image's Details: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#console)to see details of the image.
- Select the Tags tab.
- 

Select Delete from the Actions menu (three dots) beside the free-form tag or defined tag you want to change.
- 

When prompted, confirm the deletion.

## Using the Console to Specify the Free-form Tags and Defined Tags to Apply to Image Signatures

To add a free-form tag or a defined tag to an image signature created when an image was signed:
- 

Follow the instructions in[Getting an Image's Details: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#console)to see details of the signed image for which the signature was created.
- 

Select the Signatures tab to view details of the signature(s) created when the image was signed.

The Tag column shows the number of free-form tags or defined tags already applied to the image signature.
- 

Add a tag to the signature as follows:
- 

To add a tag to a signature to which no tags have been applied yet, select Add tags from the Actions menu beside the signature.
- 

To add a tag to a signature to which one or more tags have already been applied, select View tags from the Actions menu beside the signature and then select Add tags in the View tags dialog.
- 

To add a defined tag to the image signature, specify:
- 

Namespace : Select the tag namespace to which the tag belongs.
- 

Key : Select the name of the defined tag to apply to the image signature.
- 

Value : Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- 

To add a free-form tag to the image signature, specify:
- 

Namespace : Set to None (free-form tags do not belong to a tag namespace).
- 

Key : Enter a name for the free-form tag to apply to the image signature.
- 

Value : Enter a value for the tag to apply to the image signature.

To update an existing free-form tag or defined tag applied to an image signature:
- 

Follow the instructions in[Getting an Image's Details: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#console)to see details of the signed image for which the signature was created.
- 

Select the Signatures tab to view details of the signature(s) created when the image was signed.

The Tag column shows the number of free-form tags or defined tags already applied to the image signature.
- 

Select View tags from the Actions menu beside the signature.
- 

Select the edit button beside the free-form tag or defined tag you want to change.
- 

Update the tag in the Edit tag dialog.

To remove an existing free-form tag or defined tag applied to an image signature:
- 

Follow the instructions in[Getting an Image's Details: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#console)to see details of the signed image for which the signature was created.
- 

Select the Signatures tab to view details of the signatures created when the image was signed.

The Tag column shows the number of free-form tags or defined tags already applied to the image signature.
- 

Select View tags from the Actions menu beside the signature.
- 

Select the edit button beside the free-form tag or defined tag you want to remove.
- 

Select Remove tag in the Edit tag dialog.

## Notes on the use of tags to control access to Repositories, Images, and Image Signatures

Having applied free-form tags and defined tags to Container Registry resources, you can include the`target.resource.tag`policy variable in where conditions in IAM policies to control access to those resources.

As with other OCI services:
- You cannot use tags in policy statements that allow the creation of Container Registry resources. A request to create a resource would fail because the target resource has not been created yet and therefore does not have the appropriate tag to be evaluated. See[Policies that Require a Tag on the Target Resource Can't Grant Create Permissions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#lim2).
- You cannot use tags in policy statements that allow the listing of Container Registry resources. Permissions to allow the return of a list of resources must be granted through an additional policy statement. See[Permissions to List a Resource Must Be Granted Separately](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#list).

Note the following when writing policy statements to control access to Container Registry resources using the`target.resource.tag`policy variable:
- 

The use of`repos`in policy statements covers all Container Registry resources, namely repositories, images, and image signatures. For example, consider the following policy statement:
```

```

This policy allows read access to repositories, images, and image signatures to which the`Sales`tag has been applied.
- You must apply a tag directly to the resource to which you want to allow access. When you apply a tag to a repository, the tag is not applied to images or image signatures in the repository. Similarly, if you apply a tag to an image, the tag is not applied to an image signature created for the image. For example, consider the following policy statement:
```

```

This policy allows manage access to any repository, any image, and any image signature to which the`Marketing`tag has been applied. Note that access is not granted to images or image signatures in a repository to which the`Marketing`tag has been applied, unless the`Marketing`tag has also been directly applied to them.
- When authorizing an API operation to access a Container Registry resource using a tag specified by the`target.resource.tag`policy variable, you must apply the tag to a resource appropriate for the API operation. See[Details for Container Registry](https://docs.oracle.com/iaas/Content/Identity/Reference/registrypolicyreference.htm)
