# Configuring the App Gateway Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/configure-app-gateway-server.htm
- Fetched: 2026-09-05 02:18 CDT

# Configuring the App Gateway Server

Before you start the App Gateway server for the first time, you need to configure the server to connect with IAM.

- Use an SSH client such as`PuTTY`and the following credentials to sign in to the App Gateway server.
- Localhost login :`oracle`
- Password :`cloudgateR0X!`

You're required to change the provisioned password on the first login.
- Run the`sudo yum updateinfo list security all`command and provide sudo password.
This command lists the security errata for your App Gateway Oracle Linux server. To update all packages for which security-related errata are available to the latest versions of the packages enter`sudo yum --security update`.
- Run the`telnet <identity-domain-tenant>.identity.oraclecloud.com`command to confirm that the App Gateway server can reach the IAM instance.
- Restart the App Gateway server after applying the updates.
- Navigate to the`/scratch/oracle/cloudgate/ova/bin/setup`folder, and then edit the`cloudgate-env`file present in this folder (`vi cloudgate-env`).
- Enter values for the following parameters, and then save the file:

- 

IDCS_INSTANCE_URL : The URL of your Identity Domains instance.

For example,`https://idcs-123456789.identity.oraclecloud.com`
- CG_APP_TENANT : The tenant name of the Identity Domains instance.

For example,`idcs-123456789`
- 

CG_APP_NAME : The client ID value you made note during the App Gateway registration in the IAM Console.
- 

CG_APP_SECRET : The client secret value you made note during the App Gateway registration in the IAM Console.
- 

CG_CALLBACK_PREFIX : If App Gateway is configured in SSL mode (HTTPs), then set the value to`https://%hostid%`. Otherwise, use`http://%hostid%`as the value for this parameter.
- Confirm that the resolver entry in`/usr/local/nginx/conf/nginx-cg-resolv.conf`has the right DNS server IP address.

Run the`nslookup <your_identity_cloud_service_domain>`command, and verify the`Server`IP Address is the same one of the`resolver`entries in the`/usr/local/nginx/conf/nginx-cg-resolv.conf`file. If not, then update this file accordingly.
- In the`/scratch/oracle/cloudgate/ova/bin/setup`folder, run`./setup-cloudgate`command.
When prompted, enter`y`to proceed with the configuration.
