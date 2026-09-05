# Testing Delegated Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/test-delegated-authentication.htm
- Fetched: 2026-09-05 02:21 CDT

# Testing Delegated Authentication

Verify that a user's Microsoft Active Directory (AD) credentials from a domain associated with an AD Bridge can be used to sign in to IAM. This way, if there are any issues, then you can resolve them before activating delegated authentication for the AD domain.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- Select Security .
- Select Delegated Authentication .
- Expand the node to the right of the AD Bridge for which you want to test delegated authentication.
- Select Test Delegated Authentication .
- In the Test Delegated Authentication window, enter the AD user name and password that you want to use to sign in to IAM.
- Select Test .
If the test fails and you can't sign in with the AD user name and password:
- Check that you are using the correct credentials, or try testing using another AD user name and password.
- Consult the[troubleshooting information](https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/../troubleshooting/ms_ad_bridge.htm)
