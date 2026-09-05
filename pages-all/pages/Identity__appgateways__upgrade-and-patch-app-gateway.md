# Upgrading and Patching App Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/upgrade-and-patch-app-gateway.htm
- Fetched: 2026-09-05 02:18 CDT

# Upgrading and Patching App Gateway

The App Gateway patch is installed when you run the upgrade script when you're performing a patch upgrade.

As patches become available they're listed on the Downloads page, which is available from the Settings page for an identity domain.

See the first steps in[Downloading and Extracting the App Gateway Binary File](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/download-and-extract-app-gateway-open-virtual-applicance-file.htm).

## App Gateway Installed as VM

App Gateway versioning uses the following convention:`<release version>-<major version>.<minor version>.<build number>`. For example, App Gateway version`19.3.3-1.0.1`, means release`19.3.3`, major version`1`, minor version`0`, and patch version`1`.

If you have multiple App Gateway instances, then repeat the following procedure for each App Gateway server.

- Use an SSH client such as`PuTTY`to sign in to the App Gateway server.
- Run`cd /scratch/oracle/cloudgate`, and verify two information in this folder:

- 

In the command prompt, run the following command`cat /scratch/oracle/cloudgate/INSTALLED_VERSION`to verify the version of the App Gateway.
The following example shows that the version of the App Gateway is`19.3.3-1.0.0`:
```

```

- 

Run the following command`ls -la`and verify that the`home`folder links to the folder named the App Gateway version:
The following example shows that the`home`folder is linked to the`19.3.3.-1.0.0`folder:
```

```

- Run`cd /scratch/oracle/cloudgate/home/bin`, and then`./cg-upgrade`to start the upgrade process.

Note  
  

If you are using Cloud Gate OVA Base Version: 25.1.1-9.0.0, execute the below command once before running ./cg-upgrade
```

```

During the upgrade process, App Gateway contacts IAM to verify if a patch for your App Gateway is available. If so, then the process downloads the patch and applies the patch to your App Gateway server.
- After the upgrade process finishes, Run the commands described in step 2 and verify whether their return refers to the App Gateway patch or the upgraded version.
During this procedure, App Gateway restarts. Access to your application through this App Gateway server might be affected.

## App Gateway Installed as Docker Container
