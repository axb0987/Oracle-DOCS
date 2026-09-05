# Configuring Hostname Verification in WebLogic Console
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/configure-hostname-verification-weblogic-console.htm
- Fetched: 2026-09-05 02:21 CDT

# Configuring Hostname Verification in WebLogic Console

You can configure the hostname verification in Oracle WebLogic Server Administration Console.

- Start the Oracle WebLogic Server Administration Console by entering`http://wls_host:wls_port/console`in the URL line of a web browser. For example,`https://ebsasserter.example.com:7002/console`.
- Sign in to WebLogic console as an administrator.
- In the left panel, select Lock &amp; Edit , expand Environment , select Servers .
- Select the name of the target server where you want to deploy the EBS Asserter. In this example, AdminServer .
- Select the SSL tab. Scroll down and expand the Advanced section.
- Update the Hostname Verification parameter with the value None , and then select Save .
- Select Activate Changes .
-
