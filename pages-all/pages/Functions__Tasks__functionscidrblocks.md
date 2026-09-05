# CIDR Blocks and OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscidrblocks.htm
- Fetched: 2026-09-05 02:07 CDT

# CIDR Blocks and OCI Functions

Find out about the CIDR blocks to specify when using OCI Functions.

When configuring the VCN and subnets to use with OCI Functions, you specify CIDR blocks to indicate the IP addresses that can be allocated to resources.

The VCN must have a CIDR block that provides at least a certain minimum number of free IP addresses for OCI Functions to use. The required number of free IP addresses depends on the following factors:
- The amount of memory that has been specified for a function to use when executing, and the maximum number of concurrent executions of that function.
- The maximum amount of memory and the maximum number of concurrent executions of all other functions executing at the same time in subnets in the same VCN.

Note that other OCI services might require additional free IP addresses, but those requirements are not covered in this topic.

You can use the following method as a guideline to determine the minimum number of free IP addresses that OCI Functions requires, and therefore the size of the CIDR block to specify for the VCN.
Important  
  

It can be difficult to correctly identify when different functions, and different invocations of the same function, will be executing at the same time. It can also be difficult to identify when (or if) different function executions will simultaneously all be using all of the memory specified for them, all at the same time. As a result, the method described here can lead to an over-estimate (potentially a significant over-estimate) of the minimum number of free IP addresses that OCI Functions requires in a VCN. Therefore, we strongly recommend you consider this method of calculating the minimum number of free IP addresses as a guideline only, and supplement it with your own observations and experience of how your system operates.
- For each function you expect to execute concurrently in subnets in the same VCN:
- Identify the amount of memory that has been specified for the function to use while executing, in GB. For example, if 512 MB has been specified for the function, use 0.5 GB.
- Determine the expected maximum number of concurrent executions of the function.
- Multiply the amount of memory for the function by the expected maximum number of concurrent executions of the function, to determine the function's total maximum amount of required memory (in GB).
- Add together the total maximum amounts of required memory for every function that will execute concurrently in subnets in the same VCN, to produce an overall total maximum amount of required memory (in GB) for all functions.
- Divide the overall total maximum amount of required memory for all functions by 14, since each 14 GB of memory usage requires 1 additional IP address.
- For each subnet in the VCN, add 3 to the total number of IP addresses required, since 3 IP addresses are reserved for internal use for each subnet.

The result is the minimum number of IP addresses that OCI Functions requires in the VCN. Having obtained the minimum required number of IP addresses, you can use a CIDR calculator to determine the size to specify for the VCN's CIDR block. For reference, here's a[CIDR calculator](http://www.ipaddressguide.com/cidr).

The guideline can be expressed as the following formula:
```

```

Consider the following simple example with a single function, and a VCN that has one regional subnet. Let's say that 512 MB (rounded to 0.5 GB) has been specified as the amount of memory that the function can use, and that you expect 2000 to be the maximum number of concurrent executions of the function. Let's also say that you expect all 2000 concurrent executions to be simultaneously using the full amount of memory specified for the function, all at the same time. In this case, the function's total maximum amount of required memory is 1000 GB (that is,`(0.5 * 2000)`). The number of free IP addresses required for concurrent executions of the function is 72 (that is,`(1000 / 14)`). The number of IP addresses reserved for internal use is 3 (that is,`(3 * 1)`). Therefore, 75 (that is,`72 + 3`) is the minimum number of IP addresses that OCI Functions requires in the VCN . Using a CIDR calculator, you can see that a /25 CIDR block is sufficient for OCI Functions use of the VCN (since a /25 CIDR block has 128 distinct IP addresses).

If there are multiple subnets in the VCN, use different and non-overlapping CIDR blocks for each subnet to divide the IP addresses equally between the subnets.

For more information about configuring the VCN and subnets, see[Creating the VCN and Subnets to Use with OCI Functions, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingvcn.htm)
