# Deploying the E-Business Suite Asserter on Oracle WebLogic Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/deploy-ebs-asserter-weblogic-server.htm
- Fetched: 2026-09-05 02:21 CDT

# Deploying the E-Business Suite Asserter on Oracle WebLogic Server

You must deploy the E-Business Suite Asserter to the Administration Server instance of Oracle WebLogic Server to perform end-to-end testing of the integration.

- Copy the E-Business Suite Asserter war file (`ebs.war`) to the working folder in the Oracle WebLogic Server`/opt/ebssdk`.
- Enter the following URL in a web browser, replacing`host:port`with the host name and port for the Oracle WebLogic Server Administration Console:

```

```

For example,`https://ebsasserter.example.com:7002/console`.
- Sign in to the WebLogic console as an administrator.
- In the Change Center , select the Lock &amp; Edit button.
- Under Domain Structure, select Deployments .
- On the right, under Deployments , select the Install button.
- Enter the path for the E-Business Suite Asserter war file as`/opt/ebssdk`.
- Select the`ebs.war`file and select Next .
- Select Install this deployment as an application , and then select Next .
- Select the target server (for example, EBSAsserter_server ) and then select Next .
- Accept the default values and select Finish .
-
