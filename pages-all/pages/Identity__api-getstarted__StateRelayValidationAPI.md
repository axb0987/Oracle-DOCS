# Configuring the State Relay Validation with an IdP-Initiated SSO
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/StateRelayValidationAPI.htm
- Fetched: 2026-09-05 02:17 CDT

# Configuring the State Relay Validation with an IdP-Initiated SSO

OCI identity domains validates the relay state URL based on the configuration settings.
The state relay validates using the configured URL when the following conditions are met:
- OCI identity domains acts as a Service Provider (SP).
- Identity Providers (IdP), for example Azure and Pinfederate, act as external identity providers.

## Before You Begin

Perform the following actions before you configure the state relay validation.
- Submit a service request (SR) to enable Relay State Validation on your identity domains. Provide the following details in the SR:
- The Identity Domain's GUID. For example,`idcs-xxxx`.
- Provide your reason and use case for the request.
- Tenancy region.
- The component must be "`SAML`".
- Create an access token with an`Identity Domain Administrator`role to perform the following API commands. For more information on how to create an Access token, see[Generating an Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../usersettings/generate-personal-access-tokens.htm).
- Create a confidential application in the identity domain. For more information, see[Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../applications/add-confidential-application.htm).
- Configure the application as a client.
- On the page to configure OAuth, select Add app roles , and then select the application roles you want to apply to this application. Assign Identity Domain Administrator to the list of app roles.
- Use the client GUID and client secret to generate the Access token using a token endpoint.

## 1: Getting an Identity Provider ID

Use a CURL command to view the`id`of the Identity Domains.

```

```

Sample response:
```

```

Find the`id`of the identity providers you want to update. Note the`id`and`partnerName`listed in the response.

## 2: PATCH the Allowed-IdP-Initiated-Relay-States attribute

Use a CURL command to patch the`allowedIdPInitiatedRelayStates`of selected Identity Providers.

```

```

In the response, look for the following replies:
- `"partnerName"`: Confirm that the partner name is accurate.
- 
```

```
