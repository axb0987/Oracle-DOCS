# Testing the SSO Using the E-Business Suite Asserter Direct URL with a Redirect Parameter
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/test-sso-ebs-asserter-direct-url-redirect-param.htm
- Fetched: 2026-09-05 02:22 CDT

# Testing the SSO Using the E-Business Suite Asserter Direct URL with a Redirect Parameter

You can use the URL for the E-Business Suite Asserter with a redirect parameter to verify the integration and ensure that the SSO works.

- Open a browser and enter the URL for the E-Business Suite Asserter along with the`requestUrl`parameter. In the following example, the parameter value points to one of the Oracle E-Business Suite pages (for example, Self-Service Reports page - P11D Reports).

```

```

The`requestUrl`parameter value must match one of the`whitelist.urls`and must be URL encoded.
- The IAM Sign In page appears. Use the username and password of the previously created user to sign in.
- Upon successful authentication, the user is redirected to the page passed as a parameter to the E-Business Suite Asserter URL in the`requestUrl`parameter.
-
