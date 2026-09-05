# Configuring Keystores in WebLogic Console
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/configure-keystores-weblogic-console.htm
- Fetched: 2026-09-05 02:21 CDT

# Configuring Keystores in WebLogic Console

Using If you are using Custom Trust Store in WebLogic for asserter deployment, instead of using Custom Identity and Custom Trust Store with WebLogic server, use Custom Identity and Java Trust Store. With this configuration, you do not need to import IAM certificate.

- Start the Oracle WebLogic Server Administration Console by entering`http://wls_host:wls_port/console`in the URL line of a web browser. For example,`https://ebsasserter.example.com:7002/console`.
- Sign in to WebLogic console as an administrator.
- In the left panel, select Lock &amp; Edit , expand Environment , select Servers .
- Select the name of the target server where you want to configure the keystore.
- Select Keystores under the Configuration tab.
- In the left panel, select Lock &amp; Edit to make the changes.
- Select Custom Identity and Java Trust Store .
- Select Save and Activate Changes .
-
