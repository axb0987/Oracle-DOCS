# Passing Custom Configuration Parameters to Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams-about.htm
- Fetched: 2026-09-05 02:09 CDT

# Passing Custom Configuration Parameters to Functions

Find out about passing custom configuration parameters to running functions with OCI Functions.

The code in functions you deploy to OCI Functions will typically require values for different parameters. Some pre-defined parameters are available to your functions as environment variables (see[Environment Variables Populated by OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenvironmentvariables.htm)). But you'll often want your functions to use parameters that you've defined yourself. For example, you might create a function that reads from and writes to a database. The function will require a database connect string, comprising a username, password, and hostname. You'll probably want to define username, password, and hostname as parameters that are passed to the function when it's invoked.

To pass user-defined parameters to a function deployed in OCI Functions, you create key-value pairs known as custom configuration parameters. You can create custom configuration parameters that are:
- application-wide, meaning they are passed to every function in an application
- function-specific, meaning they are passed to the particular function for which they are defined (function-specific parameters override application-wide parameters with the same name)

The custom configuration parameters you create are also set as environment variables.

To create custom configuration parameters, you can use:
- the`config:`section of a function's func.yaml file, to define function-specific custom configuration parameters
- the Console and the Fn Project CLI, to define both application-wide and function-specific custom configuration parameters

OCI Functions combines all the custom configuration parameters (both application-wide and function-specific) in the application into a single, serially encoded configuration object with a maximum allowable size of 4 Kb.

Note that if you subsequently change the value of a custom configuration parameter, the change is applied almost immediately but the change does not take effect until the function is next invoked.

You can specify custom configuration parameters to pass to functions using the Console, the Fn Project CLI, and the API. See[Specifying Custom Configuration Parameters to Pass to Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams.htm)
