# Using REST APIs to Update the Custom SCIM Gateway Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/scim/update-custom-scim-gateway-application-using-rest-api.htm
- Fetched: 2026-09-05 02:28 CDT

# Using REST APIs to Update the Custom SCIM Gateway Application

Use REST APIs to update the`port`, and`sslEnabled`parameters of the custom SCIM gateway application.

- To acquire an access token, use a client credential application in an identity domain. If a client credential application hasn't been created in your environment, then add one.
- Use the access token as an authorization bearer to run a`GET`request to the following endpoint:`https://domainURL.identity.oraclecloud.com/admin/v1/Apps?filter=displayName co "SCIM Gateway Application"`
The JSON response contains an ID value for this application.
- Use the ID value and the access token from the previous steps to run a`PATCH`request to the following endpoint:`https://domainURL.identity.oraclecloud.com/admin/v1/Apps/"ID"`
Replace the ID value with the ID value of your application, set the Content-type header to`application/json`, and provide the following content for the body:
```

```

- In the Console, expand the Navigation Drawer , select Applications , and then select SCIM Gateway Application .
- In the Provisioning pane, select Test Connectivity to verify that a connection can be established between IAM and your custom SCIM gateway application.
-
