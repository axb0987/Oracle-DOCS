# Finding a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_find_single_key.htm
- Fetched: 2026-09-05 02:32 CDT

# Finding a Key

Configure command for finding key.

The`findKey`command lets you to find all keys that matches a specified key class, key label, and modulus.

Open a command prompt and run`findKey`command to find all keys that matches a specified key class, a key label, and a modulus.

Command
```

```

Where,

Parameter Description
-h Displays this information
-c specifies the Key Label, if label contains spaces it should be written in between " characters. 2 = public 3 = private 4 = secret
-t Specifies the key type to find (optional) 0 = RSA 1 = DSA 3 = EC 16 = GENERIC_SECRET 19 = DES 21 = DES3 31 = AES
-l Specifies the key label to find (optional), if label contains spaces it should be written in between " characters.
-id Specifies key ID (optional)
-sess Specifies option to find only session keys(1) or only token keys(0) (optional) .

Example
```

```
