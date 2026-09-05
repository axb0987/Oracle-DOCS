# Accessing Other Oracle Cloud Infrastructure Resources from Running Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm
- Fetched: 2026-09-05 02:07 CDT

# Accessing Other Oracle Cloud Infrastructure Resources from Running Functions

Find out how to access other Oracle Cloud Infrastructure resources from running functions deployed to OCI Functions.

When a function you've deployed to OCI Functions is running, it can access other Oracle Cloud Infrastructure resources. For example:
- You might want a function to get a list of VCNs from the Networking service.
- You might want a function to read data from an Object Storage bucket, perform some operation on the data, and then write the modified data back to the Object Storage bucket.

To enable a function to access another Oracle Cloud Infrastructure resource, you have to include the function in a dynamic group, and then create a policy to grant the dynamic group access to that resource. For more information about dynamic groups, including the permissions required to create them, see[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm).

Having set up the policy and the dynamic group, you can then include a call to a 'resource principal provider' in your function code. The resource principal provider uses a resource provider session token (RPST) that enables the function to authenticate itself with other Oracle Cloud Infrastructure services. The token is only valid for the resources to which the dynamic group has been granted access.

Note also that the token is cached for 15 minutes. So if you change the policy or the dynamic group, you will have to wait for 15 minutes to see the effect of your changes.

We recommend that you use the resource principal provider included in the Oracle Cloud Infrastructure SDK. However, you might be writing a function in a language that the Oracle Cloud Infrastructure SDK does not support. Or you might simply not want to use the Oracle Cloud Infrastructure SDK. In either case, you can write your own custom resource principal provider to enable a function to authenticate itself with other Oracle Cloud Infrastructure services, using files and environment variables in the container in which the function is executing.

## Using the Console

To enable a running function to access other Oracle Cloud Infrastructure resources:
- 

Log in to the Console and create a new dynamic group:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Under Identity domain , select Dynamic groups .
- Follow the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), and give the dynamic group a name (for example,`acme-func-dyn-grp`).
- 

When specifying a rule for the dynamic group, consider the following examples:
- 

If you want all functions in a compartment to be able to access a resource, enter a rule similar to the following that adds all functions in the compartment with the specified compartment OCID to the dynamic group:

```

```

- 

If you want a specific function to be able to access a resource, enter a rule similar to the following that adds the function with the specified OCID to the dynamic group:

```

```

- 

If you want all functions with a specific defined tag to be able to access a resource, enter a rule similar to the following that adds all functions with the defined tag to the dynamic group :

```

```

Note that free-form tags are not supported. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Select Create Dynamic Group .

Having created a dynamic group that includes the function, you can now create a policy to give the dynamic group access to the required Oracle Cloud Infrastructure resource.
- 

Create a new policy:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example,`acme-func-dyn-grp-policy`).
- 

When specifying a policy statement, consider the following examples:
- 

If you want functions in the`acme-func-dyn-grp`to be able to get a list of all the VCNs in the tenancy, enter a rule similar to the following:

```

```

- 

If you want functions in the`acme-func-dyn-grp`to be able to read and write to a particular Object Storage bucket, enter a rule similar to the following:

```

```

- 

If you want functions in the`acme-func-dyn-grp`to be able to read and write to all resources in a compartment, enter a rule similar to the following:

```

```

- Select Create to create the new policy.
- Include a resource principal provider in the function code to enable the function to authenticate with other Oracle Cloud Infrastructure services. See:
- [Example: Adding the Oracle Resource Principal Provider to a Python Function to Get a List of VCNs from the Networking Service](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm#oracleprovider)
- [Example: Adding a Custom Resource Principal Provider to a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm#customprovider)

For a sample Java function, see[Function that returns the list of instances in the calling Compartment](https://github.com/oracle-samples/oracle-functions-samples/tree/master/samples/oci-list-instances-java)in the[OCI Functions samples repository on GitHub](https://github.com/oracle/oracle-functions-samples).

## Example: Adding the Oracle Resource Principal Provider to a Python Function to Get a List of VCNs from the Networking Service

Having added a function to a dynamic group, and created a policy that allows the dynamic group to list the VCNs in the tenancy, you could include code similar to the following example to get a list of VCNs from the Networking service. This example uses the Oracle resource principal provider to extract credentials from the RPST token.

```

```

## Example: Adding a Custom Resource Principal Provider to a Function

We recommend that you use the resource principal provider included in the Oracle Cloud Infrastructure SDK. However, you might be writing a function in a language that the Oracle Cloud Infrastructure SDK does not support. Or you might simply not want to use the Oracle Cloud Infrastructure SDK. In either case, you can write your own custom resource principal provider to enable a function to authenticate itself with other Oracle Cloud Infrastructure services, using files and environment variables in the container in which the function is executing.

The container in which a function executes includes a directory tree that holds Oracle Cloud Infrastructure compatible credentials, specifically:
- A resource principal session token (RPST) in a file named rpst . The RPST token is formatted as a[JWT token](https://tools.ietf.org/html/rfc7519), and includes claims that identify the function's host tenancy and compartment.
- A private key for use in making requests to Oracle Cloud Infrastructure services on behalf of the function, in a file named private.pem .

The following environment variables are set inside the container in which the function executes:
- OCI_RESOURCE_PRINCIPAL_VERSION, containing the value`2.2`.
- OCI_RESOURCE_PRINCIPAL_RPST, containing the absolute path to the rpst file (including the filename).
- OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM, containing the absolute path to the private.pem file (including the filename).
- OCI_RESOURCE_PRINCIPAL_REGION, containing the region identifier in which the function is deployed (for example,`us-phoenix-1`).

To enable a function to access another Oracle Cloud Infrastructure service, add code to the function so that it can authenticate itself with the other resource:
- Add code that loads the RPST token from the path in the OCI_RESOURCE_PRINCIPAL_RPST environment variable.
- 

Add code that loads the private key from the path in the OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM environment variable.
- 

Add code that uses the RPST token and the private key to create an Oracle Cloud Infrastructure request signature (see[Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm)).
- 

Add code that constructs the request to the other Oracle Cloud Infrastructure resource.

If necessary, you can identify:
- The endpoints of other Oracle Cloud Infrastructure services in the same (local) region as the function, using the region identifier in the OCI_RESOURCE_PRINCIPAL_REGION environment variable.
- The function's host tenancy and compartment, using the`res_tenant`and`res_compartment`claims in the RPST token.

For example, the sample Python function below includes a custom resource principal provider that extracts credentials from the RPST token. It then submits a GET request to the IAM API's getTenancy operation to return the OCID of the function's tenancy.

```

```
