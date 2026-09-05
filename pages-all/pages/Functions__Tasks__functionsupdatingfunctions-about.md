# Updating Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions-about.htm
- Fetched: 2026-09-05 02:09 CDT

# Updating Functions

Find out about updating functions.

Having previously created a function definition in the OCI Functions server, you can change some, but not all, of the function's properties. For example, you can change the maximum length of time a function is allowed to execute for, but you cannot change the function's name.

You can change the Docker image on which a function is based. If you do want to change the image, the replacement image must be suitable for use with OCI Functions, and must have already been pushed to the Docker registry. With the replacement image in the Docker registry, you can then update a function's definition so that it is based on the replacement image, as described in this topic. If the replacement image has the same name and tag as the image on which the function was originally based, see[Notes About Image Digests](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions-about.htm#notesdigest).

You can update functions using the Console, the Fn Project CLI, and the API. See[Updating a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions.htm).

## Notes About Image Digests

Images in a Docker registry are identified by repository, name, and a tag. In addition, Docker gives each version of an image a unique alphanumeric digest. When pushing an updated Docker image, it's recommended best practice to give the updated image a new tag to identify it, rather than reusing an existing tag. However, even if you push an updated image and give it the same name and tag as an earlier version, the newly pushed version will have a different digest to the earlier version.

When you create a function with OCI Functions, you specify the name and tag of a particular version of an image on which to base the function. To avoid later inconsistencies, OCI Functions also records the unique digest of that particular version of the image.

By default, if you push an updated version of an image to the Docker registry with the same name and tag as the original version of the image on which a function is based, OCI Functions continues to use the original digest to pull the original version of the image. This might be the behavior you require. However, if you want OCI Functions to pull the later version of the image, you can explicitly change the digest that OCI Functions uses to identify which version of the image to pull in one of the following ways:
- 

Use the`fn update function`command and specify the original name and tag of the version of the image on which you want the function to be based. For example:

```

```

OCI Functions will update the digest recorded for the image on which the function is based to be the digest of the image in the Docker registry that has the name and tag you specify.
- 

Use the`fn update function`command and specify the digest of the version of the image on which you want the function to be based. For example:

```

```

OCI Functions will update the digest recorded for the image on which the function is based to be the digest you specify.
- Use the Console and select Edit on the function's Details tab, re-select the original name and tag of the version of the image on which the function is currently based, and select Save Changes . OCI Functions will update the digest recorded for the image on which the function is based.
- Use the Oracle Cloud Infrastructure API or an Oracle Cloud Infrastructure SDK (for more information, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
