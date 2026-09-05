# Changing Default Memory and Timeout Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm
- Fetched: 2026-09-05 02:08 CDT

# Changing Default Memory and Timeout Settings

Find out how to use configuration parameters to change OCI Functions defaults.

You can change several aspects of OCI Functions default behavior using configuration parameters.

The following table indicates the parameters you can set, the default value, and where the default value can be overridden.

Parameter Description Default Value Units func.yaml Parameter Fn CLI option Console field OCI CLI option API attribute Notes
Maximum time a function will be allowed to run in Sync invocation 30 Seconds`timeout:``--timeout-in-seconds`Synchronous invocation timeout`--timeout-in-seconds``timeoutInSeconds`

Maximum value: 300

Best practice is to specify a timeout that is close to that likely to be required, rather than significantly more.
Maximum time a function will be allowed to run in Detached invocation none

(Value of`timeoutInSeconds`is used as default) Seconds not applicable`--detached-mode-timeout-in-seconds`Detached invocation timeout`--detached-mode-timeout-in-seconds``detachedModeTimeoutInSeconds`

Minimum value: 5

Maximum value: 3600
Maximum memory threshold for a function 128 MB`memory:``--memory`Memory`--memory-in-mbs``memoryInMBs`

One of:
- 128
- 256
- 512
- 1024
- 2048
- 3072

If this limit is exceeded during execution, the function is stopped and an error message is logged.

Depending on the parameter, you can override a default value by specifying an alternative value in the following ways:
- By adding or updating an entry in the func.yaml file directly. For example,`memory: 1024`. Note that if you edit the func.yaml file, you must re-deploy the function to OCI Functions before invoking it again.
- By using the Fn Project CLI to add or update entries in the func.yaml file. For example,`fn update function --memory 1024 <app-name> <function-name>`
- By using the Oracle Cloud Infrastructure Console, CLI, and API to update the function definition in the OCI Functions server (the function definition takes precedence over the func.yaml file).

Note that how you invoke a function also determines the maximum amount of time the function can run for. For more information, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm).

For more information about the above parameters, and other configuration parameters, see[Func files](https://github.com/fnproject/docs/blob/master/fn/develop/func-file.md)in the[Fn Project documentation](https://github.com/fnproject/docs).

## Recommendations

When setting configuration parameter values, note the following recommendations:
- Set the maximum memory threshold for Java functions to at least 256 MB.
- It's a good idea to set a maximum memory threshold value for a function that is close to what the function is actually likely to require.
- If you encounter 504 timeout messages when invoking a function, increase the maximum memory threshold for the function. See[Issues invoking functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm)
