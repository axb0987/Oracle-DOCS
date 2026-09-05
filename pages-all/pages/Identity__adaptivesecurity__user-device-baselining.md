# User Device Baselining
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/user-device-baselining.htm
- Fetched: 2026-09-05 02:16 CDT

# User Device Baselining

Enable this feature to automatically baseline a user's device the first time they sign in to OCI.

The first time a user signs in to OCI a baseline is created for the user's device. When a user signs in from this device, they don't receive an email notification. If a user accesses their account using an unknown device, then the user receives an email notifying them that a new device was used to sign in to their account.

## Enabling Device Baselining
To enable device baselining:
- Enable Adaptive Security, see[Activating Adaptive Security](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-adaptive-security.htm).
- Enable`deviceBaseliningEnabled`flag in`SsoSettings`.
```

```

Note  
  
Include the following attribute in the body of the API command:`deviceBaseliningEnabled = true`

## Getting the Baseline Status of a Device
The tenant administrator can use the following endpoint to retrieve the device details associated with a user:
```

```

`isBaselined`: If the value of this attribute is`true`, then this particular device is baselined for the user. Sample response:
```

```

## Deleting a User Device
To delete a user device, use the following endpoint:
```

```
