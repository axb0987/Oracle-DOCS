# EBS Asserter Known Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/known-issues/known-issues-ebs-asserter.htm
- Fetched: 2026-09-05 02:23 CDT

# EBS Asserter Known Issues

Known issues for working with EBS Asserter in IAM.

## Resolve an Insufficient Privileges Error

After IAM authentication, instead of getting access to Oracle EBS, the user gets redirected back to EBS with the error message`You have insufficient privileges for the current operation.`The user is prompted to sign in again.

Generally, when the Oracle EBS application throws this error, it means that the cookie is set with an incorrect domain. To confirm this, check the EBS Asserter debug log, which you can find at`<HOME DIR> /ebsasserter.log`. For example

```

```

In this example, the EBS Asserter debug log shows that the`sessionCookieDomain`has an incorrect value, being set to`.oracle.com`.

The`ICX_PARAMETERS.SESSION_COOKIE_DOMAIN`must not be set to any value.
- Update the`SESSION_COOKIE_DOMAIN`setting in`ICX_PARAMETERS`

```

```

- Set`session_cookie_domain`to`NULL`in the`ICX_PARAMETERS`

```

```

- Restart all services.
- Retest the issue.

## Resolve Internal Server Error While Logging Out

When you're logging out from Oracle EBS, the browser throws an error message`Internal Server Error`.

This issue happens because there is an old version of`AppsLogoutRedirect.java`in the Oracle EBS side.

Check the header for`AppsLogoutRedirect.java`in the Oracle EBS to see the version number, for example

```

```

Resolve this by applying the latest Oracle E-Business Suite Release 12 Critical Patch Update Jan 2013, or a more recent version. This Critical Patch Update enables`AppsLogoutRedirect.java`to leverage the`APPS_SSO`and`APPS_AUTH_AGENT`profiles. Check the Knowledge Document (July 2018) (Doc ID 2379675.1) for information on how to apply this patch.

## Fix a Time Sync Issue

While you're accessing the EBS Asserter application URL, the Oracle EBS application sign-in flow resulted in an internal server error.

The HTTP header trace looks like this

```

```

The`session_exp`is set to`1537715029`. Use`EpochConverter`to convert the current Unix epoch time to a human readable date and time. Hence, the expiry time in the token is set to`Sunday, September 23, 2018 3:03:49 PM GMT`. However, the time in the EBS Asserter domain log is`Sep 23, 2018 6:53:31,380 PM AST`. Note that Greenwich Mean Time is 4 hours ahead of Atlantic Standard Time. Hence the time set is`Sep 23, 2018 10:53:31 PM GMT`.

The system where the EBS Asserter is deployed isn't in time sync with IAM, and as a result the token passed by IAM is effectively out of the validity period and hence the Token Expired error.

Ensure the date and time on the system where the EBS Asserter is deployed is in time sync with NTP servers, and hence the IAM host.

## Handle Java Error ExceptionInInitializerError

While you're accessing the EBS Asserter application URL, the Oracle EBS application throws the`java.lang.ExceptionInInitializerError`error.

The EBS Asserter debug log shows the following Java error

```

```

This occurs because of incorrect settings in the`bridge.properties`file. Verify the`bridge.properties`file and check that it has the required configuration. Also, check that the path specified in`wallet.path`in the`bridge.properties`file is valid.

## Handle Java Error RuntimeException

While you're accessing the EBS Asserter application URL, the Oracle EBS application throws the`java.lang.RuntimeException`error.

The EBS Asserter debug log shows the following Java error

```

```

To resolve this, set the`ebs.ds.name`value set to be the same as the datasource name created in WebLogic.

## Fix a Deep Link Issue

After IAM authentication, instead of getting access to Oracle EBS, the user gets redirected back to EBS with the error message`You have insufficient privileges for the current operation.`The user is prompted to sign in again.

This can happen because the deep link isn't working.

Check that the`whitelist.urls`bridge property is configured. If the issue persists, specify the port numbers explicitly in the`whitelist.urls`configuration. For example,`whitelist.urls=http://ebs.oracle.com:80/OA_HTML…`.

Also, check the JSESSION ID Cookie Name of the E-Business Suite Asserter App in the`weblogic.xml`file. If there is any other web app in the WebLogic with the same cookie name, it will cause a conflict.

## Issues During Sign Out

If you find issues during the sign-out process verify the Post Logout Redirect URL parameter value in IAM and the`post.logout.url`parameter value in the`bridge.properties`file.

The`post.logout.url`in the`bridge.properties`file is an optional parameter and by default you don't need to provide a value. You use this parameter to make the EBS Asserter application redirect the user browser to the specified URL after EBS Asserter finishes the sign-out process.

If enabled, the value of the`post.logout.url`in the`bridge.properties`file must match the value of the Post Logout Redirect URL parameter for EBS Asserter application in IAM.
- Open the EBS Asserter application in IAM and update the Post Logout Redirect URL value.
- Open the`ebs.war`file, update the`bridge.properties`file, regenerate the war file, and redeploy the file to the WebLogic server. Ensure the value of this parameter matches the Post Logout Redirect URL parameter in IAM.

## Invalid Client Error with Client Authentication Failed

You get an error which included invalid_client and Client authentication failed, such as this

```

```

- Check the Client ID and Client Secret generated in the IAM Confidential Application..
- Regenerate the wallet file using the correct Client ID and Client Secret.
- Redeploy the`asserter.war`file on the Weblogic Servers.

## Oracle EBS Core Profiles Not Available to Edit

You get an error saying that Oracle EBS core profiles aren't available to edit. To resolve this:
- In Oracle EBS, go to the Oracle Applications Administration page in Oracle EBS. Select the Core Services tab, and then select the Profiles tab.
- When the Oracle EBS application contains no value, the edit button is disabled.
- Select Define Profile and enter profile values.

## EBS Asserter Unable to Connect with Oracle EBS With Authorization Error

You get a message which includes

```

```

such as this one.

```

```

This error occurs when the asserter user present in EBS Application hasn't been assigned the correct role. Sign in to the Oracle EBS application and provide the`APPS_CONNECT_SCHEMA`role to the asserter user.

## JDBC Active Connection Usage for the EBS Asserter on Weblogic

The EBS Asserter uses the JNDI service within the WebLogic server to create DB connections with the Oracle EBS DB. Over time, the number of connections keeps increasing and the inactive sessions are closed. This leads to the connection pool getting full, and not able to make any new connections with the Oracle EBS DatabaseThis results in a connection error at the EBS Asserter.

```

```

A restart of the WebLogic servers acts as a temporary fix to make the asserter available for new connections.

The way to fix this permanently is to specify a value for`Inactive Connection Timeout`on the JDBC Data Source: Configuration: Connection Pool page in the Administration Console. When you set a value for

```

```

, the WebLogic Server forcibly returns a connection to the data source when there is no activity on a reserved connection for the number of seconds that you specify. When set to`0`(the default value), this feature is turned off.

To set positive value for:

```

```

- Sign in to the Weblogic Server Admin Console.
- Go to Data Sources .
- Search for the Data Source Name you want to change, and select Data Source .
- Select Configure a Connection Pool .
- Expand the Advanced tab.
- Update the Inactive Connection Timeout to the new value.

For example: Inactive Connection Timeout = 900 (15 minutes).
Note  
  
These configurations are specific to each customer's environment. We recommend that the you perform load testing in their environment and tune your configurations based on the results.

## Database Error in EBS Asserter

EBS Asserter's connection to the database fails with`invalid table name`. For example

```

```

This error due to a name mismatch, where the`ebs.ds.name`parameter in`bridge.properties`isn't same as the name of the datasource created in EBSAsserter's WebLogic.

To resolve this, set the`ebs.ds.name`
