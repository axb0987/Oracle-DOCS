# Updating Oracle E-Business Suite Profiles
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/update-oracle-e-business-suite-profiles.htm
- Fetched: 2026-09-05 02:22 CDT

# Updating Oracle E-Business Suite Profiles

Configure the URL allowlist property to prevent access to the Oracle E-Business Suite local login and direct all requests to the E-Business Suite Asserter log in instead.

- Log in to Oracle E-Business Suite console as a user that is assigned the Functional Administrator responsibility (typically sysadmin ).
- Use the drawer icon (E-Business Suite version 12.2.8) or navigator icon (E-Business Suite version 12.1/12.2), select Functional Administrator .
- In the Oracle Applications Administration page, select the Core Services tab, and then select Profiles .
- Enter APPS_AUTH_AGENT in the Code field and then select Go .
- On the list of profiles, select Application Authenticate Agent , and then select Define Profile Values .
- On the Define Profile Values: Application Authenticate Agent page, enter the E-Business Suite Asserter URL in the Site Value field, and then select Update .
- Select Profiles under the Core Services tab, enter APPS_SSO in the Code field, and then select Go .
- On the list of profiles, select Applications SSO Type , select Define Profile Values , change the Site Value field from SSWA to SSWA w/SSO , and then select Update .
- Select Profiles under the Core Services tab, enter ICX_SESSION_COOKIE_DOMAIN in the Code field, and then select Go .
- On the list of profiles, select Oracle Applications Session Cookie Domain , select Define Profile Values , replace the Site Value field from HOST to DOMAIN , and then select Update .
-
