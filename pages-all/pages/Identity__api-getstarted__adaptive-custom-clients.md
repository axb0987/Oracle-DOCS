# Adaptive Risk Analysis for Custom Client Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/adaptive-custom-clients.htm
- Fetched: 2026-09-05 02:17 CDT

# Adaptive Risk Analysis for Custom Client Applications

Customers moving to the Cloud can leverage IAM identity domain adaptive capabilities to meet risk-based analysis for their on-premises access management system, such as Oracle Access Manager (OAM), or client applications.

Identity domains provide an adaptive REST API interface to enable these on-premises access management systems or client applications to use an identity domain risk-based engine to evaluate authentication activities for users.

For example, John Doe is a user in the OAM identity store and in an identity domain. John accesses a finance application protected by OAM. The OAM server redirects him to the OAM sign-in page for authentication. John Doe submits his credentials and based on the risk score returned by the identity domain adaptive risk-based engine, the OAM server may challenge the user with a second factor. If the risk score is high, then OAM may deny access to John and present him a message indicating his attempt to sign in failed.
The adaptive REST API interface implements three use cases in the form of the corresponding endpoints:
- 

Populate Risk :`/admin/v1/sdk/adaptive/PopulateRisks`
- 

Fetch Risk Info :`/admin/v1/sdk/adaptive/FetchRisks`
- 

Mitigate Risk :`/admin/v1/sdk/adaptive/MitigateRisks`
To make REST API calls to these endpoints, your access management system or custom application needs an access token from a client credential application registered in an identity domain.
Note  
  
To obtain an access token, see[Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm).

The adaptive REST API interface requires the client application to send information such as user identification, information of the device the user uses to sign in, and client's true IP address.

To gather device information that your access management system needs to use a device fingerprint JavaScript file. You can download the device fingerprint JavaScript file from the identity domain console.

- Sign in to identity domain Console as an application administrator.
- Expand the Navigation Drawer , select Settings , and then select Downloads .
- In the Downloads page, download the Identity Cloud Service Device Fingerprint Utility .

The file you download is a compressed (zip) file. Inside the zip file there's a JavaScript file that the access management system sign-in page or the client application itself needs to load to collect fingerprint information. Then use the`getFingerprint()`function to collect user's device fingerprint to send to the identity domains adaptive REST API interface.

See also[Enable the Access for an unknown device Event for a Custom Sign-In Page](https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:26834).

## Populate Risk

This endpoint is used to submit risk data to an identity domain to increase the user's risk score.
The cURL command structure is:
```

```

The following is the structure of the request body for the Populate Risk endpoint.
```

```

The`event`attribute is optional. If not present in the request then all risk events are going to be used to evaluate risk score. You can use`MAX_MFA_FAILED_ATTEMPTS`or`MAX_PASSWORD_FAILED_ATTEMPTS`values.
The following is an example of a request body to evaluate risk for John Doe trying to sign in the access management system from the IP address`10.11.12.13`. The device fingerprint and IP address will be validated against all enabled risk events in an identity domain.
```

```

The following is an example of response body of the populate risk endpoint.
```

```

## Fetch Risk Info

This endpoint enables clients to get current risk information for a single user, multiple users, or for all users in an identity domain.
The cURL command structure is:
```

```

The following is the structure of the Request Body for the Fetch Risk Info cURL command.
```

```

You can call the fetch risk info endpoint for multiple users. To do so, use the following request body structure with the cURL command.
```

```

If you want to fetch risk info for all users in an identity domain, use the following request body structure with the cURL command.
```

```

The following is an example of a request body to fetch risk info for John Doe.
```

```

The following is an example of response body of the fetch risk info endpoint.
```

```

## Mitigate Risk

This endpoint enables client applications to request mitigation of a user's risk score because the user has logged in or reset their password successfully.
The cURL command structure is:
```

```

The following is the structure of the request body for the Mitigate Risk cURL command.
```

```

The`event`attribute of the request body can receive multiple values:
- For successful user sign-in, provide`SSO_THREAT_MITIGATION_SUCCESS`.
- For successful user password reset, provide`ADMIN_ME_PASSWORD_CHANGE_SUCCESS`.
The following is an example of a request body to the Mitigate Risk endpoint for John Doe because he successfully signed in to the access management system from the IP address`10.11.12.13`.
```

```

The following is an example of response body of the populate risk endpoint:
```

```
