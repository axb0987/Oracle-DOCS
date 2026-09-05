# Deleting Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingfunctions-about.htm
- Fetched: 2026-09-05 02:08 CDT

# Deleting Functions

Find out about deleting functions.

You can delete functions in OCI Functions that you or other functions developers have created, provided you have been granted the necessary permission (FN_FUNCTION_DELETE, and potentially FN_APP_DELETE).

When using the Console to delete functions, note that:
- you can delete all of the functions in an application simply by deleting the application itself (hence the potential requirement for the FN_APP_DELETE permission)
- you're always prompted to confirm deletion because you cannot undelete an application or function later

Note the following:
- Deleting functions and applications is permanent. You cannot undelete a function or application that you've deleted.
- Deleting a function does not delete the Docker image on which the function is based. To delete the image, you have to delete it explicitly (see[Deleting and Undeleting an Image](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrydeletingimages.htm)).
- Deleting a function does not necessarily enable you to immediately delete the subnet and VCN in which the function runs. Expect to wait up to five minutes after the function was last invoked before you can delete the associated network resources.

You can delete functions using the Console, the Fn Project CLI, and the API. See[Deleting a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeleting.htm)
