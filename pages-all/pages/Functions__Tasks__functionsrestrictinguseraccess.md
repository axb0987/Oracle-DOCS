# Controlling Access to Invoke and Manage Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsrestrictinguseraccess.htm
- Fetched: 2026-09-05 02:09 CDT

# Controlling Access to Invoke and Manage Functions

Find out how to control the functions that users can invoke and manage in OCI Functions.

When configuring a tenancy for function development, you specify the following identity policy statement (as described in[Policy Statements to Give OCI Functions Users Access to Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#userfunctionpolicy)):

```

```

This identity policy enables authenticated users in the specified group to manage (that is, create, update, and delete) functions and applications in the named compartment, and also enables those users to invoke functions in the compartment. This policy typically meets the requirements of functions developers developing and testing multiple functions in your organization.

However, this identity policy might be too permissive to meet your security requirements to control the invocation and management of functions in production environments. For example, in a production environment you might want to prevent users from invoking functions completely, or restrict users to invoking just functions in a specific application, or to invoking just a particular function.
Note  
  

Specifying a private subnet for an application does not prevent access from the internet to the invoke endpoints of functions in the application. Use identity policies to control access to function invoke endpoints, as described in this topic.

To control the functions that users in a group can invoke and manage, set up identity policies:
- 

To control the functions that a user can invoke and manage, confirm that they are not in a group that has been given the`manage functions-family`permission.
- If you want to enable users in a group to create, update, and delete applications and functions in a compartment, but to be unable to invoke functions, enter the following policy statements:

```

```

```

```

- 

If you want to allow invocations of particular functions only, or invocations of functions in particular applications only, include the appropriate function and application OCIDs in suitable policy statements. For example:
- To enable users to invoke all the functions in a specific application, enter a policy statement in the following format:

```

```

- To enable users to invoke one specific function, enter a policy statement in the following format:

```

```

- To enable users to invoke all the functions in all applications except for functions in one specific application, enter a policy statement in the following format:

```

```

- To enable users to invoke all the functions in a compartment except for one specific function, enter a policy statement in the following format:

```

```

- To enable users to invoke two specific functions, enter a policy statement in the following format:

```

```

- To enable users to invoke one specific function along with all the functions in a specific application, a policy statement in the following format:

```

```

- 

If you want to allow function invocation and management requests only from particular IP addresses:
- Create a network source to specify the allowed IP addresses, if a suitable network source doesn't exist already (see[https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm)).
- 

Add a policy statement to enable only those IP addresses in the network source to invoke or manage functions. For example:
- 

To only allow function invocation requests from IP addresses defined in a network source named`corpnet`, enter a policy statement in the following format:

```

```

- 

To only allow function management requests from IP addresses defined in a network source named`corpnet`, enter a policy statement in the following format:

```

```
