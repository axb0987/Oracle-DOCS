# Registering the KSP Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_register_ksp.htm
- Fetched: 2026-09-05 02:34 CDT

# Registering the KSP Provider

Learn how to register the KSP Provider in Dedicated KMS.

Run the following command to register the KSP provider and validate the registration:
Note  
  
You don't have to run the following command manually to register the KSP provider because the registration process is automated as part of the Windows Service installation. But you can perform this step to validate the KSP provider registration.
```

```

Validation

Run the`certutil -csplist`command in command prompt with administrator privilege and the output must display Cavium Key Storage Provider if your setup is working correctly.
```

```

```

```
