# Roving Edge Infrastructure Device Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm
- Fetched: 2026-09-05 03:02 CDT

# Roving Edge Infrastructure Device Compartments

Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.

Each Roving Edge Infrastructure device contains a single compartment. This compartment also functions as your tenancy when you are working with the device. The single compartment is fixed. You cannot add or remove compartments.

When you use the command line utilities with your device, you often must specify the compartment OCID as a parameter of the command. You can determine the OCID of your device's compartment by following either of these procedures:
- 

Open a command window on your Roving Edge Infrastructure device and enter the following:
```

```

The compartment OCID is the value of the`"id"`in the return.
- 

Open a browser connected to the Roving Edge Infrastructure device and enter the following URL:

`https:// ip_address :12060/v1/tenants/orei`
