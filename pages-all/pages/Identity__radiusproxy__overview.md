# Setting Up RADIUS Proxy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/overview.htm
- Fetched: 2026-09-05 02:27 CDT

# Setting Up RADIUS Proxy

Remote Authentication Dial In User Service (RADIUS) is a network protocol that defines rules and conventions for communication between network devices. RADIUS Proxy authenticates and authorizes users or devices and also tracks the usage of those services.

## Required Policy or Role

To set up and validate RADIUS Proxy, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/../policieshow/Policy_Basics.htm).

## Setting up RADIUS Proxy

Install, setup, and test RADIUS Proxy.

Before You Begin :
- Ensure that your RADIUS Proxy is available for your identity domain. RADIUS Proxy is available only for Oracle Apps Premium and Premium Identity Domain Types. To learn about identity domain types and the features and limits associated with each, see[IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/../sku/overview.htm).
- Install the latest[Postman](https://learning.postman.com/docs/getting-started/installation-and-updates/)client.
- Download the[RADIUS Proxy Postman collection](https://github.com/oracle/idm-samples/blob/master/idcs-rest-clients/Oracle%20Identity%20Cloud%20Service%20RADIUS%20Proxy.postman_collection.json).
- Review the RADIUS Proxy mapping instructions. See[RADIUS Proxy Mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/overview.htm#radius-proxy-mapping).
- Review these checkpoints. As you're setting up RADIUS Proxy, use the following checkpoints to verify that your configuration is correct at each step of the process.
- Check that the RADIUS Proxy and the RADIUS Proxy Client App are activated in the identity domain.
- Check the IP address of Database and port number of RADIUS Proxy are correctly configured in the RADIUS App.
- Check that the RADIUS Agent is up and running.
- Check that the proxy server is up and running.
- Check that the database is up.

- Download the latest RADIUS Proxy Installer from the Downloads page in the Console.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click Settings and then Downloads .
- Choose Oracle Identity Cloud Service RADIUS Proxy for Linux , and then select Download .
- Create the RADIUS App from the RADIUS App Template. Note: For REST go to RADIUS Proxy , RADIUS App , Search , and then Search all apps (with search criteria).
- In the Console, select Applications , Add , and then App Catalog .
- Search for the Oracle Database Radius App Template and select Add .
- Complete the App details similar to the following example.

- Name: dbserver
- Description: App representing the Oracle database server as a RADIUS client
- IP Address of Oracle Database server: 10.242.230.122 (This IP address is where the database is installed.)
- Port of RADIUS Proxy: 1812 (The port number on which RADIUS Proxy listens for requests from this Oracle database. The same port number must be configured in the RADIUS settings of Oracle Database.)
- Secret key: testing123 (The secret key used to secure communication between RADIUS Proxy and the Oracle Database server. The same key must be configured in the RADIUS settings of Oracle Database.)
- Select Add , Activate , and then select the Users tab.

Note  
  

Assign the users who are allowed to sign in to Oracle Database, to this Radius App by selecting Assign Users . Instead of assigning individual users, a Group which contains those users, can also be assigned. Select the Groups tab, and then Assign Groups .

Note : Create the group name in the identity domain according to the following format defined in Step 3C: Configure the RADIUS Server in[Configuring RADIUS Authentication](https://docs.oracle.com/database/121/DBSEG/asoradus.htm#GUID-78799317-4902-43D7-8EB2-5645F731F530):`ORA_databaseSID_rolename[_[A]|[D]]`.

For every role in Oracle database to be identified by IAM, create a corresponding group using the format above. Assign a user to this group in IAM so that the respective database user is associated with the respective database role.
- Create a RADIUS Proxy in IAM.
- Register a Client Application. See[Register a Client Application](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/idcs/idcs_rest_postman_obe/rest_postman.html#RegisteraClientApplication).
- Open Postman and import the[RADIUS Proxy.postman_collection.json](https://github.com/oracle/idm-samples/blob/master/idcs-rest-clients/Oracle%20Identity%20Cloud%20Service%20RADIUS%20Proxy.postman_collection.json)collection to make the REST requests in this section.
- Import the[RADIUS Proxy Example Environment with Variables.postman_environment.json](https://github.com/oracle/idm-samples/blob/master/idcs-rest-clients/Oracle%20Identity%20Cloud%20Service%20RADIUS%20Proxy%20Example%20Environment%20with%20Variables.postman_environment.json)environment file which contains the environment variables used in the collection.
- Set the following environment variables.

For HOST , use the IAM address, for example,[https://yourtenant.identity.oraclecloud.com/](https://yourtenant.identity.oraclecloud.com/).

For CLIENT_ID and CLIENT_SECRET , use the values that you copied above.
Note  
  
Other environment variables are automatically set when REST requests are made. Ensure that following REST requests are made in the same order.
- Obtain an access token. To make API calls to IAM, you must authenticate your client against IAM, and then obtain an OAuth access token. The access token provides a session between a client (in this case, Postman) and IAM. By default, the access token has a timeout interval of 60 minutes, and then you must request a new access token to perform additional REST API calls. To obtain an OAuth access token, make the request in the Postman collection under RADIUS Proxy , OAuth Token , and then Obtain access_token (client credentials) .
- Create the RADIUS Proxy by using a POST Operation. Go to RADIUS Proxy , Create , and then Create a RADIUS Proxy .

End point:`admin/v1/RadiusProxies/ {{RPid}}`

```

```

- Use this Patch Operation to activate the RADIUS Proxy. Go to RADIUS Proxy , Lifecycle , and then Activate a RADIUS Proxy .

End point:`/admin/v1/RadiusProxies/{{RPid}}`

```

```

- Create the RADIUS Proxy Listener using a POST Operation. Go to RADIUS Proxy , RADIUS Proxy Listeners , Create , and then Create a RADIUS Proxy Listener .

End point:`{{HOST}}/admin/v1/RadiusProxyListeners`

```

```

- Get the`dbserver`App ID. Perform a GET call on`admin/v1/Apps?filter=displayName eq "dbserver"`. Fetch the App ID from the response of this GET call. Go to RADIUS Proxy , RADIUS App , Search , and then Search all apps (with search criteria) .
You can also get the App ID from the URL of the`dbserver`.
- Create a RADIUS Proxy Mapping using a POST Operation. Go to RADIUS Proxy , RADIUS Proxy Mappings , Create , and then Create a RADIUS Proxy Mapping .

End point:`{{HOST}}/admin/v1/RadiusProxyMappings/`

Note  
  
For "value" below, the ID is the ID of Radius Proxy which you created above.

```

```

For RADIUS Proxy mapping instructions, see[RADIUS Proxy Mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/overview.htm#radius-proxy-mapping).
- GET`client_id`and`clientSecret`of the RADIUS Proxy. The`client_id`and`clientSecret`are required during RADIUS Proxy installation. RADIUS Proxy uses these credentials to authenticate with IAM. Go to RADIUS Proxy , Search , Create , Get client ID, and client secret of the App corresponding to RADIUS Proxy .

End point:`{{HOST}}/admin/v1/Apps/{{RPOAuthClientAppId}}?attributes=clientSecret,name`

`RPOAuthClientAppId`: is the ID of the App corresponding to RADIUS Proxy. You can find it in the response [response.oauthClient.value] in step 3f, Create a RADIUS Proxy Mapping using a POST Operation .
Response:
```

```

- Run the Installer.
- Unzip the downloaded`idcs_radius_proxy-xxxx.zip`file into a folder.
- Name the folder`<radius bin location-xxxx>`. Where`xxxx`is the version number (for example, 20.1.3).
Three files are extracted: FileInfo.json , idcs_radius_proxy_installer.bin , and InstallerValidation.jar . The InstallerValidation.jar file and the idcs_radius_proxy_installer.bin file are located in the same directory post extraction. They must remain in the same directory.
- Login as root user or run the following command as sudo:`./idcs_radius_proxy_installer.bin`

Note  
  
The installer supports only Graphical User Interface mode. It does not support console mode. So, if you see the error: "`Graphical installers are not supported by the VM.`", then ensure X server is configured properly. Then, run this command as non root user :`xhost +si:localuser:root`and run installer again.
- Install RADIUS Proxy.
- Read the Welcome screen, and then select Next .
- Read the Information screen, and then select Next .
- Select the Destination Folder (default is`/root/oracle_radius_proxy`), where the RADIUS Proxy installer will be installed. Select Next .
- On the HTTP Proxy screen, select Use HTTP Proxy if RADIUS Proxy needs to use HTTP proxy to connect to IAM. If not, then leave this checkbox unchecked. Select Next .
- On the IAM screen, enter the Cloud Service URL in the following format:`https://yourtenant.identity.oraclecloud.com`. Provide the Client ID and Client Secret of the RADIUS Proxy created in IAM. (This is the RADIUS Proxy you created using the POST Operation above.) Select Next .
- On the RADIUS User and Group Information screen, provide the Username and user Group information, for example:

- Username : &lt;client&gt;
- Group : &lt;dba&gt;

IAM RADIUS Proxy daemon will run under the specified username and group.
- Select Next .
- On the preinstall screen, verify that all the information is correct. If the information is correct, select Install .
- When the installation is complete, select Done .
- Check that the RADIUS Agent and RADIUS Proxy are running. The RADIUS Agent obtains configuration data from IAM at regular intervals. Then, it updates the configuration files used by RADIUS Proxy.
- Use the following RADIUS Agent commands to check whether the agent is running:

- `python <RADIUS_PROXY_INSTALLER_LOCATION>/oracle_radius_proxy/radius_agent/scripts/src/radius_agent.py status`
- You can also use`stop`,`start`and`restart`if needed.
- Use the following command to run RADIUS Proxy:`/sbin/service idcs_radiusd start`
- Run these RADIUS server commands to verify that the RADIUS service isRADIUS running.

- `/sbin/service idcs_radiusd status`
- You can also use`stop`,`start`, and`restart`if needed.
- (Optional) Use the NTRadPing Test Utility to validate that RADIUS proxy is working.
- Install the NTRadPing Test Utility in Windows, and then create a User in IAM.
- Use the below screenshot as an example. In the below screenshot client is the user created in IAM and testing123 is the secret key given in RADIUS Settings, Secret key of App Details page.

The following image shows the NTRadPing test utility in Windows:

- Set up and Configure Oracle Database 12c. Follow the instructions at[Configuring Authentication](https://docs.oracle.com/database/121/DBSEG/asoradus.htm#DBSEG040)and then use the following commands to create a user/role in the database.
- Set up and Configure Oracle Database 12c. For more information, see[Configuring RADIUS Authentication](https://docs.oracle.com/database/121/DBSEG/asoradus.htm#DBSEG040). Follow the instructions in the Configuring RADIUS Authentication section to create a user and role in the database.
- You can't add an IP address in CIDR format using the IAM user interface. If the IP address of the Oracle Database is in CIDR format, use the following request from the Postman collection. See[Change an IP Address from CIDR Format](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/../known-issues/known-issues-radius-proxy.htm#radius-proxy-config-issue-10).
- Set up MFA. To set up MFA follow these instructions, see[Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/../mfa/understand-multi-factor-authentication.htm).

## RADIUS Proxy Log Files and Configuration Information

Note the following RADIUS Proxy file locations for log and configuration information. This information can be useful for troubleshooting.

Installer Logs &lt;radius_proxy_installer_location&gt;/oracle_radius_proxy/_Oracle/ Identity/ Cloud/ Service/ RADIUS/ Proxy_installation/Logs/
Agent Logs &lt;radius_proxy_installer_location&gt;/oracle_radius_proxy/radius_agent/logs/agent.log
Proxy logs &lt;radius_proxy_installer_location&gt;/oracle_radius_proxy/radius_proxy/log/radius_proxy.log
Proxy Configuration &lt;radius_proxy_installer_location&gt;/radius_proxy/conf/radius_proxy.conf
Agent Configuration &lt;radius_proxy_installer_location&gt;/radius_agent/conf/radius_agent.conf
Client Configuration &lt;radius_proxy_installer_location&gt;/radius_proxy/conf/radius_clients.conf

## RADIUS Proxy Mapping

RADIUS Proxy and RADIUS Proxy Listener has a 1-1 mapping, for example for each RADIUS Proxy there is one RADIUS Proxy Listener. Multiple Oracle DB RADIUS clients can be mapped to one RADIUS Proxy, that is, a RADIUS Proxy has a 1-n mapping with Oracle DB RADIUS clients.
