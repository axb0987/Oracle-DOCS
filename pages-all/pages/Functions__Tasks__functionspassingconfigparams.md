# Specifying Custom Configuration Parameters to Pass to Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams.htm
- Fetched: 2026-09-05 02:09 CDT

# Specifying Custom Configuration Parameters to Pass to Functions

Find out how to specify custom configuration parameters to pass to running functions with OCI Functions.

For prerequisites and more information, see[Passing Custom Configuration Parameters to Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams-about.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams.htm#)
- 

- On the Applications list page, select the application containing functions to which you want to pass custom configuration parameters. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- Do one of the following:
- 

To pass one or more custom configuration parameters to every function in the application, select Configuration to display the Configuration page for the application.
- 

To pass one or more custom configuration parameters to a particular function, select the Functions tab, select the function's name, and then select Configuration to see the Configuration page for the function.
- 

In the Configuration page, select Manage configuration , and then select Add configuration to specify the following details for the first custom configuration parameter:
- Key: The name of the custom configuration parameter. The name must only contain alphanumeric characters and underscores, and must not start with a number. For example,`username`
- Value: A value for the custom configuration parameter. The value must only contain printable Unicode characters. For example,`jdoe`
- (Optional) Select Add configuration to enter other custom configuration parameters as required.
- 

Select Save changes to save the new custom configuration parameter.

OCI Functions combines the key-value pairs for all the custom configuration parameters (both application-wide and function-specific) in the application into a single, serially encoded configuration object with a maximum allowable size of 4 Kb. You can't save the new custom configuration parameter if the size of the serially encoded configuration object would be greater than 4 Kb.
- 

Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To specify custom configuration parameters to pass to functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer and open a terminal window.
- 

To specify one or more custom configuration parameters to pass to every function in an existing application, enter:

```

```

where:
- `<app-name>`is the name of the application containing the functions to which you want to pass the custom configuration parameter.
- `<key>`is the name of the custom configuration parameter. The name must only contain alphanumeric characters and underscores, and must not start with a number.
- `<value>`is the value to give to the custom configuration parameter. The value must only contain printable Unicode characters.

For example:

```

```

Note the following:
- You can also define application-wide custom configuration parameters when you create a new application using the`fn create app`command.
- OCI Functions combines the key-value pairs for all the custom configuration parameters (both application-wide and function-specific) in the application into a single, serially-encoded configuration object with a maximum allowable size of 4Kb.
- 

To specify one or more custom configuration parameters to pass to a particular function, enter:

```

```

where:
- `<app-name>`is the name of the application containing the function to which you want to pass the custom configuration parameter.
- `<function-name>`is the name of the function to which to pass the custom configuration parameter.
- `<key>`is the name of the custom configuration parameter. The name must only contain alphanumeric characters and underscores, and must not start with a number.
- `<value>`is the value to give to the custom configuration parameter. The value must only contain printable Unicode characters.

For example:

```

```

Note the following:
- You can also define function-specific custom configuration parameters when you create a new function using the`fn create function`command.
- OCI Functions combines the key-value pairs for all the custom configuration parameters (both application-wide and function-specific) in the application into a single, serially-encoded configuration object with a maximum allowable size of 4Kb.
- 

Run these API operations to define custom configuration parameters:
- [CreateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/CreateFunction)
- [UpdateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/UpdateFunction)
- [CreateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/CreateApplication)
- [UpdateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/UpdateApplication)
