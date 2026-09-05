# Using the Authenticate API to Develop a Custom Sign-in Page
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm
- Fetched: 2026-09-05 02:18 CDT

# Using the Authenticate API to Develop a Custom Sign-in Page

This use case provides a step-by-step example of using the identity domains REST API to develop a custom sign-in page for an identity domain.

Note  
  
Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
Note  
  
This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.

The Authenticate API is based on the concept of a state machine. Request responses inform an application client what has to be done next rather than requiring users to have third-party cookies enabled in their browsers. Third-party cookies enabled in browsers can pose problems, especially for B2C applications where controls on end-user behavior can't be enforced. The`requestState`provided in each request response is used in the next request, providing the client with the information that it needs to process the request, and then provide the next set of operations allowed.
The Authenticate API can:
- Help you verify username and password credentials for a user as the primary authentication.
- Support user enrollment with MFA factors enabled by the administrator
- Strengthen the security of password-based authentication using Multifactor Authentication (MFA) by requiring additional verification, such as using a time-based one-time passcode or an SMS passcode.
- Allow your users to select an external SAML or Social Identity Provider for authentication.
Note  
  
See the identity domains Authentication API Postman collection for extensive authentication use case examples. Download the collection and the global variables file from the idcs-authn-api-rest-clients folder within[GitHub](https://github.com/oracle/idm-samples/tree/master/idcs-authn-api-rest-clients)and then import them into Postman.
The following example sets are included in this use case:
- [Authenticating an External SAML Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidp)
- [Authenticating a Social SAML Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextsocialidp)
- [Authenticating with an External SAML Identity Provider and MFA](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidpmfa)
- [Authenticating with User Name and Password](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authusernamepassword)
- [Authenticating User Name and Password with TOU Consent](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#Authusernameandpwtou)
- [Generating Access Token Using Authentication API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken)
- [Authenticating User Name and Password and Enrolling in Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fvv_3f1_lgb)
- [Authenticating User Name and Password and Enrolling in Account Recovery and MFA](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa)
- [Authenticating with User Name and Password and Enrolling in MFA](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaenroll)
- [Authenticating with User Name and Password and MFA](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaauth)

Authenticate and On-Demand MFA API Status Codes
- [Authentication and On-Demand MFA API HTTP Status Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIStatusCodes.htm)
- [Authentication and On-Demand MFA API Error Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIErrorCodes.htm)

## Authenticating with an External SAML Identity Provider

This use case discusses the steps to use identity domains to authenticate using an external SAML Identity Provider (IdP).
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples::
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidp__Step1-D020A9D2)
- [Step 2: Select an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidp__Step2-D020B472)

### Step 1: Begin the Authentication Flow

A user opens a browser window to access a protected page.
In the background, the request to authenticate is intercepted by identity domains and redirected to the`/authorize`endpoint. This begins the authentication process. Instead of presenting the default sign-in page, identity domains responds by creating and submitting an HTML form that contains the`loginCtx`and`signature`parameters to the browser.
Note  
  
You must expose an endpoint to receive the form post and read the two parameter values.

Example HTML Form POST

The following is an example HTML Form POST that identity domains returns to invoke the custom sign-in page:
```

```

The browser receives the HTML code, which contains JavaScript to automatically submit the form to the custom sign-in page. Since the`loginCtx`parameter is based64 encrypted, the custom sign-in app must decrypt the`loginCtx`by doing the following:
- Decode using a base64 decoder to get the encrypted binary data
- Use the tenant name and generate a key for decryption
- Decrypt the data using the key and binary data

Example Decryption Logic for Encrypted loginCtx in Java

The following is example decryption logic:
```

```

Response Example

The response should be similar to the following example:
```

```

The`loginCtx`parameter contains some important attributes:
- requestState: The state of the authentication process. It needs to be used in future POSTs and GETs to identity domains Authentication API endpoints.
- nextOp : The next operation the custom sign-in application must perform.
- nextAuthFactors : The possible authentication factors the sign-in page must present.

The values of these attributes define which authentication factor, identity providers, and social providers are presented on the sign-in page. The sign-in page appears containing the decrypted values of the`loginCtx`parameter along with the access token. The sign-in page includes JavaScript that's used to perform AJAX calls to identity domains.

### Step 2: Select a SAML Identity Provider
The user selects the external SAML IdP that they want to use to authentication from the custom sign-in page that appears. The custom sign-in page must construct and then submit the required information for the selected IdP as an HTML FORM POST to the`/sso/v1/sdk/idp`endpoint. For this step, the following attributes must be included:
- `requestState:`received in the Step 1 response
- `idpName:`name of the IdP received in the Step 1 response
- `idpType:`type of IdP received in the Step 1 response (in this example, it's SAML)
- `idpId:`id of the IdP received in the Step 1 response
- `appName:`name of the app that the client wants access to
- `clientID:`client ID of the application the browser is attempting to access
- `authorization:`parameter required for secure Idp

Example HTML Form POST Code to Select a SAML IdP
The following JavaScript example shows how to select the SAML IdP:
```

```

Request Example

The following is an example of the contents of the FORM POST to the`/sso/v1/sdk/secure/idp`endpoint:
```

```

Response Example

The following example shows the contents of the response in standard HTTP format:
```

```

Identity domains processes the request and redirects the browser to the selected external IdP for authentication and authorization. When the external IdP is finished, the browser is redirected to identity domains. Identity domains validates the assertion response and checks if additional authentication such as MFA is required.

If additional authentication isn't required, then identity domains creates the session and redirects the browser to the target URL. Or, identity domains creates an HTML auto submit FORM POST to the custom sign-in page that contains the`authnToken`. The custom sign-in page then creates the session. See[Creating a Session](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#createsession).

## Authenticating with a Social Identity Provider

This use case discusses the steps to use identity domains to authenticate using a Social Identity Provider (IdP) such as Facebook or Google.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples::
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextsocialidp__Step1-D020A9D3)
- [Step 2: Select a Social Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextsocialidp__Step2-D020B473)

### Step 1: Begin the Authentication Flow

A user opens a browser window to access a protected page.
In the background, the request to authenticate is intercepted by identity domains and redirected to the`/authorize`endpoint. This begins the authentication process. Instead of presenting the default sign-in page, identity domains responds by creating and submitting an HTML form that contains the`loginCtx`and`signature`parameters to the browser.
Note  
  
You must expose an endpoint to receive the form post and read the two parameter values.

Example HTML Form POST

The following is an example HTML Form POST that identity domains returns to invoke the custom sign-in page:
```

```

The browser receives the HTML code, which contains JavaScript to automatically submit the form to the custom sign-in page. Since the`loginCtx`parameter is based64 encrypted, the custom sign-in app must decrypt the`loginCtx`by doing the following:
- Decode using a base64 decoder to get the encrypted binary data
- Use the tenant name and generate a key for decryption
- Decrypt the data using the key and binary data

Example Decryption Logic for Encrypted loginCtx in Java

The following is example decryption logic:
```

```

Response Example

The response should be similar to the following example:
```

```

The`loginCtx`parameter contains some important attributes:
- requestState: The state of the authentication process. It needs to be used in future POSTs and GETs to identity domains Authentication API endpoints.
- nextOp : The next operation the custom sign-in application must perform.
- nextAuthFactors : The possible authentication factors the sign-in page must present.

The values of these attributes define which authentication factor, identity providers, and social providers are presented on the sign-in page. The sign-in page appears containing the decrypted values of the`loginCtx`parameter along with the access token. The sign-in page includes JavaScript that's used to perform AJAX calls to identity domains.

### Step 2: Select a Social Identity Provider
The user selects the social IdP that they want to use to authentication from the custom sign-in page that appears. The custom sign-in page must construct and then submit the required information for the selected IdP as an HTML FORM POST to the`/sso/v1/sdk/idp`endpoint. For this step, the following attributes must be included:
- `requestState:`received in the Step 1 response
- `idpName:`name of the IdP received in the Step 1 response
- `idpType:`type of IdP received in the Step 1 response (in this example, it's Social)
- `idpId:`id of the IdP received in the Step 1 response
- `appName:`name of the app that the client wants access to
- `clientID:`client ID of the application the browser is attempting to access
- `authorization:`parameter required for secure Idp

Example HTML Form POST Code to Select a Social IdP
The following JavaScript example shows how to select the social IdP:
```

```

Request Example

The following is an example of the contents of the FORM POST to the`/sso/v1/sdk/secure/idp`endpoint:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

Identity domains processes the request and redirects the browser to the selected social IdP for authentication and authorization. When the social IdP is finished, the browser is redirected to identity domains. Identity domains validates the assertion response and checks if additional authentication such as MFA is required.

If additional authentication isn't required, then identity domains creates the session and redirects the browser to the target URL. Or, identity domains creates an HTML auto submit FORM POST to the custom sign-in page that contains the`authnToken`. The custom sign-in page then creates the session. See[Creating a Session](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#createsession).

## Authenticating with an External SAML Identity Provider and MFA

This use case discusses the steps to use identity domains to authenticate using an external SAML Identity Provider (IdP) and Multifactor Authentication (MFA).
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidpmfa__Step1-D020A9D4)
- [Step 2: Select an External Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidpmfa__Step2-D020B474)
- [Step 3: Authenticate Using the Preferred Factor (SMS)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authextSAMLidpmfa__Step3-103018)

### Step 1: Begin the Authentication Flow

A user opens a browser window to access a protected page.
In the background, the request to authenticate is intercepted by identity domains and redirected to the`/authorize`endpoint. This begins the authentication process. Instead of presenting the default sign-in page, identity domains responds by creating and submitting an HTML form that contains the`loginCtx`and`signature`parameters to the browser.
Note  
  
You must expose an endpoint to receive the form post and read the two parameter values.

Example HTML Form POST

The following is an example HTML Form POST that identity domains returns to invoke the custom sign-in page:
```

```

The browser receives the HTML code, which contains JavaScript to automatically submit the form to the custom sign-in page. Since the`loginCtx`parameter is based64 encrypted, the custom sign-in app must decrypt the`loginCtx`by doing the following:
- Decode using a base64 decoder to get the encrypted binary data
- Use the tenant name and generate a key for decryption
- Decrypt the data using the key and binary data

Example Decryption Logic for Encrypted loginCtx in Java

The following is example decryption logic:
```

```

Response Example

The response should be similar to the following example:
```

```

The`loginCtx`parameter contains some important attributes:
- requestState: The state of the authentication process. It needs to be used in future POSTs and GETs to identity domains Authentication API endpoints.
- nextOp : The next operation the custom sign-in application must perform.
- nextAuthFactors : The possible authentication factors the sign-in page must present.

The values of these attributes define which authentication factor, identity providers, and social providers are presented on the sign-in page. The sign-in page appears containing the decrypted values of the`loginCtx`parameter along with the access token. The sign-in page includes JavaScript that's used to perform AJAX calls to identity domains.

### Step 2: Select an External Identity Provider
The user selects the external IdP that they want to use to authentication from the custom sign-in page that appears. The custom sign-in page must construct and then submit the required information for the selected IdP as an HTML FORM POST to the`/sso/v1/sdk/idp`endpoint. For this step, the following attributes must be included:
- `requestState:`received in the Step 1 response
- `idpName:`name of the IdP received in the Step 1 response
- `idpType:`type of IdP received in the Step 1 response (in this example, it's SAML)
- `idpId:`id of the IdP received in the Step 1 response
- `appName:`name of the app that the client wants access to
- `clientID:`client ID of the application the browser is attempting to access
- `authorization:`parameter required for secure Idp

Example HTML Form POST Code to Select an External IdP
The following JavaScript example shows how to select an external IdP:
```

```

Request Example

The following is an example of the contents of the FORM POST to the`/sso/v1/sdk/secure/idp`endpoint:
```

```

Response Example

The following example shows the contents of the response in standard HTTP format:
```

```

Identity domains processes the request and redirects the browser to the selected external IdP for authentication and authorization. When the external IdP is finished, it redirects the browser to identity domains, which then redirects the browser to begin 2-Step Verification.

### Step 3: Authenticate Using the Preferred Factor (SMS)

The initial steps to begin 2-Step Verification are similar to Step 1. Identity domains creates and submits an HTML form that contains the encrypted`loginCtx`and`signature`parameters. See Step 1 for detailed information on the form POST and how to decrypt.

After the`loginCtx`parameter is decrypted, the response should be similar to the following example:
```

```

The`loginCtx`parameter contains some important attributes:
- requestState: The state of the authentication process. It needs to be used in future POSTs and GETs to identity domains Authentication API endpoints.
- nextOp : The next operation the custom sign-in application must perform.
- nextAuthFactors : The possible authentication factors the sign-in page must present.

The values of these attributes define which authentication factor (in this example it is SMS) to present on the sign-in page. The user enters the one-time passcode that they receive on their device.
The following attributes should be sent in the request:
- `op:`tells the server what kind of operation the client wants
- `otpCode:`the code sent to the user's device
- `requestState:`received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format to complete authentication using the preferred method:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

A session must then be created. After the session is created, the browser is redirected to the originally requested URL. See[Creating a Session](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#createsession).

## Creating a Session

This use case provides an example of using identity domains to create a session after authentication, such as after authenticating using MFA.
Note  
  
Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
Note  
  
This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Note  
  
See the other use cases in[Using the Authenticate API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm)for information on using the Authenticate API.

Submit the`authnToken`and the`requestState`as a FORM POST when the client is done with authentication and MFA, and needs to create a session. For this step,`createSession`must be listed as a`nextOp`attribute value in the last response received, and the FORM POST must include one of the following attributes.
For`/sso/v1/sdk/secure/session`endpoint:
- `requestState:`received in the last response

OR
- `authnToken:`received in the last response

AND
- `authorization:`parameter required for secure session

Request Example

The following is an example of the contents of the FORM POST to the`/sso/v1/sdk/secure/session`endpoint:
```

```

OR
```

```

Response Example

The following example shows the contents of the response in standard HTTP format:
```

```

If`createSession`isn't listed as a value for the`nextOp`parameter in the last received response, you may need to create a token before creating a session. If`createSession`is listed as a value for`nextOp`, the`sdk/session`endpoint can be called directly using only the`requestState`.

Request Example

The following example shows the token request to the`/sso/v1/sdk/authenticate`endpoint in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

The server checks that no other factor evaluation is needed. If no other evaluation is required, the token is sent in the response.

## Authenticating with User Name and Password

This use case provides a step-by-step example of using the identity domains Authenticate API to authenticate with a user's credentials.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

Use the following steps for the use case.
- 

[Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authusernamepassword__sec_begin-authn-flow)
- 

[Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authusernamepassword__Step2-D020B471)

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

Error Response Example

The following example shows the contents of the response in JSON format when the user name or password provided is invalid:
```

```

## Authenticating User Name and Password with TOU Consent

This use case provides a step-by-step example of using the identity domains Authenticate API to authenticate with a user's credentials with TOU consent. When the user accepts the consent, then the user is redirected to that application page.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case.
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#Authusernameandpwtou__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials Without MFA)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#Authusernameandpwtou__Step2-D020B471)
- [Step 3: Provide the TOU Consent](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#Authusernameandpwtou__section_iyp_tj2_kgb)

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials Without MFA)
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

If the username and passwords are valid, the server responds with the TOU statement in the locale specified in the user's profile. The server also prompts the user to provide their consent credential in the next request. If the TOU statement isn't present in the user's locale`fr`, then 401 response with the error message AUTH-3036 : Terms of Use Statement for locale fr isn't added is displayed.

Request Example

The following example shows the contents of the POST request in JSON format to the`/sso/v1/sdk/authenticate`endpoint:
```

```

Response Example

The following example shows the contents of the response in JSON format when the user's locale is added:
```

```

Error Response Example

The following example shows the contents of the response in JSON format when the TOU for user's locale isn't added:
```

```

### Step 3: Provide the TOU Consent

In this scenario, the user either accepts or rejects the Terms of Use for the application. If user agrees to Terms of Use, then the user is redirected to the application page.

If user rejects the Terms of Use, then 401 response with error message, AUTH-3035 : You must accept the Terms of Use to access this application , is displayed.

Request Example

The following example shows the contents of the request in JSON format when the user agrees to TOU.

```

```

Request Example

The following example shows the contents of the request in JSON format when the user rejects the TOU.

```

```

Response Example

The following example shows the content of the response in JSON format when the user agrees to TOU statement.

```

```

Error Response Example

The following shows the contents of the response in JSON format when the TOU is rejected by the user.

```

```

## Authenticating with User Name and Password and MFA and Return an OTP

This use case provides a step-by-step example of using the identity domains REST API to authenticate with a user's credentials and Multifactor Authentication (MFA) and to return an encrypted OTP in the response.

Note  
  

Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains. This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.

Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

Identity domains can be configured to send a time-based one-time passcode (OTP) to directly to a user for authentication or have the passcode encrypted and sent to the consuming client who can then send it to the user for authentication.

For example, administrators can configure identity domains to send time-based one-time passcodes (OTP) to the Oracle Mobile Authenticator (OMA) app or email the OTPs to the user's primary email address. In both cases, identity domains generate the OTP, sends it directly to the user and the user enters the code for authentication. To understand how to set these options using REST, see[Authentication Factor Enrollment With Factor Verification-SMS](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_rt5_rxf_ngb)and[Authentication Factor Enrollment With Factor Verification-Email](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm#concept_gqj_v5g_ngb).
Alternatively, administrators can configure identity domains to return an encrypted OTP in the API response to the consuming client so that the consuming client can initiate or send the OTP to the user. Two advantages to this approach are that it allows the consuming client to customize the authentication message and to also change the sender details to suit their business needs. To configure identity domains to return the encrypted OTP in the response, the consuming client must complete the following steps.
- 

Step 1: Create a CustomUI Application
- 

Step 2: Generate a Key Pair for a Self-Signed Certificate
- 

Step 3: Configure the Application to Return the OTP in the Response
- 

Step 4: Request the OTP
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configuring Multifactor Authentication Settings.](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm)

### Encryption and Decryption

This implementation uses the following specification to encrypt and decrypt the OTP code received. See[PKCS #1: RSA Cryptography Specifications, Version 2.0, section 7.1 RSAES-OAEP](https://tools.ietf.org/html/rfc2437#section-7.1).

OTP Decryption Code
Use the following Java code to decrypt the OTP.
```

```

### Step 1: Create a CustomUI Application

See[Add Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../applications/add-applications.htm)for more information about custom applications.

### Step 2: Generate a Key Pair for a Self-Signed Certificate
In order to receive the OTP in the response, the consuming client must generate a private/public key pair, then generate a self-signed certificate, and import that certificate into the CustomUI application.
- Ensure that the`otp-client.conf`configuration file contains the following information. Then, generate a private/public key pair.

```

```

- 
Use the following command to generate a self-signed certificate.
```

```

### Step 3: Configure the Application to Return the OTP in the Response
After the self-signed certificate is generated, you need to import it into the CustomUI application.
- In the Identity Cloud Service console, expand the Navigation Drawer , select Applications , CustomUI application , Configuration , and then Client Configuration .
- Import the self-signed certificate in the Trusted Client Certificate and Save the configuration.

### Step 4: Request the OTP
Request Payload

Attribute Supported Values / Sample Values Multi-Valued Usage Details
`userFlowControlledByExternalClient`true / false false

Set this option to`true`and the OTP will be returned in the response in the encrypted format specified.

Note : The certificate used for encryption is uploaded to the application in advance and is referred using the`x5t`attribute in the request example as mentioned below.
x5t String / X509 SHA-1 Certificate Thumbprint

When specified, the service uses this uploaded certificate to encrypt the OTP data.

Note : The "x5t" attribute should match the uploaded certificate.
Request Example
```

```

Response Payload

Attribute Supported Values / Sample Values Multi-Valued Usage Details
`otp`

Map

```

```
false

When present in the response, the attribute contains the encrypted OTP with following details.
- value : Encrypted value.
- alg : Algorithm used for encryption.
- x5t : SHA-1 X509 Thumbprint of the certificate used for encryption.

Response Example

```

```

## Generating Access Token Using Authentication API

This use case provides a step-by-step example of using the identity domains to generate access token using authentication API. The user gets user information through Me Access Token using Authentication API.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

When the user tries to access an application that's associated with TOU, the identity domains server uses the application name to fetch the policy that's assigned to this application. Based on the tenant settings, the server gets the IDP and authentication policy and then guides the user to the next step.
Use the following steps for the use case.
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken__Step2-D020B471)
- [Step 3:Generate Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken__section_dwy_gl2_kgb)
- [Step 4: Obtain User Information](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken__section_gwy_gl2_kgb)

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials
In this scenario, the user posts the user credentials and retrieves the`authnToken`. The following must be included in the request:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

`AuthnToken`is the id_token in JWT format that represents the current user information, session, and request data. This is used to create an SSO session cookie and redirect to the target URL. If the username and password are valid, the`AuthnToken`is retrieved.

Request Example

The following example shows the contents of the POST request in JSON format to the`/sso/v1/sdk/authenticate`endpoint:
```

```

Response Example

The following example shows the contents of the response in JSON format where the`AuthnToken`is retrieved:
```

```

### Step 3:Generate Access Token

After you retrieve an`AuthnToken`, it's used to get access token from OAuth server.

Request Example

The following example shows the contents of the request in JSON format:

```

```

Response Example

The following example shows the contents of the response in JSON format:

```

```

### Step 4: Obtain User Information

The user submits the access token to obtain their information such as username, display name, email id, and so on.

Request Example

The following example shows the contents of the request in JSON format.

```

```

Response Example

The following example shows the contents of the response in JSON format with user information.

```

```

## Authenticating with User Name and Password and MFA

This use case provides a step-by-step example of using the identity domains REST API to authenticate with a user's credentials and Multifactor Authentication (MFA).
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

Complete the following steps for this use case:
- 

[Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaauth__sec_begin-authn-flow)
- 

[Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaauth__Step2SubmitTheUsersCredentials-D0373F20)
- 

[Step 3: Authenticate Using the Preferred Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaauth__Step3AuthenticateUsingThePreferredF-D0374285)
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configuring Multifactor Authentication Settings.](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm)

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format since PUSH Notifications is the preferred factor:
```

```

Note  
  

If the Trusted Device setting is disabled at tenant level, then the`{{trustedDeviceSettings}}`attribute isn't returned in the response.
If the Trusted Device setting is enabled at tenant level, and if the Sign-On Rule rule that is matched has MFA Frequency = Every time, then the`{{trustedDeviceSettings}}`field is returned but the`{{trustDurationInDays}}`value is returned as`0`.
```

```

In the response, the status is`pending`since the user is required to Allow or Deny the PUSH Notification on their device. The`nextOp`values in the response indicate what can be sent as the`op`value in the next request. In this use case example,`credSubmit`is sent in the next step.

### Step 3: Authenticate Using the Preferred Factor

Authenticate using the preferred factor, which in this use case example is PUSH Notifications. The client must include the following attributes in this request:
- 

`op:`tells the server what kind of operation the client wants
- 

`requestState:`received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format to complete authentication using the preferred method:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

## Authenticating with User Name and Password and Enrolling in MFA

This use case provides a step-by-step example of using the identity domains Authentication API to authenticate with a user's credentials and then enroll in Multifactor Authentication (MFA).
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- 

[Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaenroll__sec_begin-authn-flow)
- 

[Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaenroll__Step2SubmitTheUsersCredentials-D03E2204)
- 

[Step 3: Initiate Second Factor Authentication Enrollment](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaenroll__Step3InitiateSecondFactorAuthentica-D03E247B)
- 

[Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaenroll__Step4SubmitFactorCredentials-D03E275C)
- 

[Step 5: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authupmfaenroll__Step5CreateTheAuthenticationToken-D03E2A58)
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In this use case example, since MFA is set as optional in the Sign-on Policy (indicated by a value of`false`for the`enrollmentRequired`attribute), the user is given a choice to either enroll or skip enrollment. If MFA is required, the only`nextOp`value would be`enrollment.`

In this use case example,`enrollment`is sent in the next step to initiate MFA factor enrollment for the user. Note that BYPASSCODE is missing as a`nextAuthFactors`value since the user can't enroll using a Bypass Code. The Bypass Code should be generated by the user using My Profile or by requesting that an administrator generate one for them.

### Step 3: Initiate Second Factor Authentication Enrollment
This step initiates the Online Time-Based One-Time Passcode (TOTP) enrollment. The client must include the following attributes:
- 

`op:`tells the server what kind of operation the client wants
- 

`authFactor:`defines which authentication factor that the user wants to enroll in
- 

`requestState:`received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`values indicate what can be sent as the`op`value in the next request. In this use case example,`credSubmit`is sent in the next step.
Note  
  
The value for`content`always begins with`oraclemobileauthenticator//.`

### Step 4: Submit Factor Credentials
This step submits the factor credentials in the`requestState`that were received in the Step 3 response. Note that the request payload doesn't contain the`authFactor`attribute because the`requestState`contains it. The client must include the following attributes:
- 

`op:`tells the server what kind of operation the client wants
- 

`requestState:`received in the Step 3 response

Request Example

The following example shows the contents of the POST request in JSON format to submit the factor credentials:
```

```

Response Example

The`success`status appears in the response when the OMA app to server back-channel communication is completed and the`optCode`verification is successful. The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`values indicate what can be sent as the`op`value in the next request. In this use case example,`createToken`is sent in the next step.

Pending Response Example

The`pending`status appears when the OMA app to server back-channel communication isn't completed. The client keeps polling every 10 seconds and continues to poll for two minutes. After two minutes, the server sends the failed status if the`otpCode`verification isn't successful.
```

```

### Step 5: Create the Authentication Token

This step indicates that the client is done with all`authnFactors`and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or denies access. The client must include the following attributes:
- 

`op:`tells the server what kind of operation the client wants
- 

`requestState:`received in the Step 4 response

Request Example
The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

## Authenticating User Name and Password and Enrolling in Account Recovery

This use case provides a step-by-step example of using the identity domains Authentication API to authenticate with a user's credentials and then enroll for Account Recovery.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#Authusernameandpwtou__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fvv_3f1_lgb__Step2-D020B471)
- [Step 3: Initiate Account Recovery Enrollment](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fvv_3f1_lgb__section_iyp_tj2_kgb)
- [Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fvv_3f1_lgb__section_zmd_pft_kgb)
- [Step 5: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fvv_3f1_lgb__section_ufg_lgt_kgb)
Note  
  
These steps assume multiple factors are enabled for Account Recovery, but MFA enrollment isn't configured. See[Configure Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../accountrecovery/configuring-account-recovery.htm)and[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In this use case example, the user must enroll in account recovery (indicated by a value of`true`for the`accRecEnrollmentRequired:true`attribute). The`nextAuthFactors`indicates the factors in which the user can enroll for Account Recovery.

In this use case example, enrollment is sent in the next step to initiate account recovery enrollment for the user.

### Step 3: Initiate Account Recovery Enrollment

This step initiates SMS enrollment. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `authFactor`: defines which authentication factor that the user wants to enroll in
- `phoneNumber`: defines the phone number where the SMS text will be sent
- `countryCode`: defines the country code of the phone number where the SMS text will be sent
- `requestState`: received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the request in JSON format:

```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step. The`otpCode`is sent using SMS to the user's device.

### Step 4: Submit Factor Credentials
This step submits the factor credentials in the requestState that were received in the Step 3 response. Note that the request payload doesn't contain the authFactor attribute because the requestState contains it. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 3 response

Request Example

The following example shows the contents of the POST request in JSON format to submit the factor credentials:

```

```

Response Example

The success status appears in the response when the optCode verification is successful. The following example shows the contents of the response in JSON format:
```

```

In the response, the`accRecEnrollmentRequired`value is set to`false`as account enrollment is successful. The`nextOp`values indicate what can be sent as the`op`value in the next request. The`nextOp`value "enrollment" allows the user to switch to another factor to enroll in account recovery. In this use case example,`createToken`is sent in the next step.

### Step 5: Create the Authentication Token
This step indicates that the client is done and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or denies access. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants requestState: received in the Step 4 response
- `requestState`: received in the Step 4 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the response in JSON format:

```

```

## Authenticating User Name and Password and Enrolling in Account Recovery and MFA

This use case provides a step-by-step example of using the identity domains Authentication API to authenticate with a user's credentials and then enroll for Account Recovery and Multifactor Authentication (MFA).
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__Step2-D020B471)
- [Step 3: Initiate Account Recovery Enrollment](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__section_iyp_tj2_kgb)
- [Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__section_zmd_pft_kgb)
- [Step 5: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__section_ufg_lgt_kgb)
- [Step 6: Set SMS as Default MFA Factor in Overlap](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__section_rhn_xkt_kgb)
- [Step 7: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#authnusernamepwaccrecmfa__section_ywx_wlt_kgb)
Note  
  
These steps assume that Account Recovery and MFA is enabled and a sign-on policy is created for MFA. See[Configure Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../accountrecovery/configuring-account-recovery.htm)and[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In this use case example, the user must enroll in account recovery (indicated by a value of`true`for the`accRecEnrollmentRequired:true`attribute). The`nextAuthFactors`indicates the factors in which the user can enroll for Account Recovery.

In this use case example, enrollment is sent in the next step to initiate account recovery enrollment for the user.

### Step 3: Initiate Account Recovery Enrollment

This step initiates SMS enrollment. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `authFactor`: defines which authentication factor that the user wants to enroll in
- `phoneNumber`: defines the phone number where the SMS text will be sent
- `countryCode`: defines the country code of the phone number where the SMS text will be sent
- `requestState`: received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the request in JSON format:

```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step. The`otpCode`is sent using SMS to the user's device. Credentials tell the user what input is needed to pass in the next request.

### Step 4: Submit Factor Credentials
This step submits the factor credentials along with the`requestState`that were received in the Step 3 response. Note that the request payload doesn't contain the`authFactor`attribute because the`requestState`contains it. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 3 response

Request Example

The following example shows the contents of the POST request in JSON format to submit the factor credentials:

```

```

Response Example

The success status appears in the response when the`optCode`verification is successful. The following example shows the contents of the response in JSON format:
```

```

In the response, the`accRecEnrollmentRequired`value is set to`false`as account enrollment is successful. The`nextOp`values indicate what can be sent as the`op`value in the next request. The`nextOp`value "enrollment" allows the user to switch to another factor to enroll in account recovery. In this use case example,`createToken`is sent in the next step.

### Step 5: Create the Authentication Token
This step indicates that the client is done with account recovery enrollment and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or responds accordingly. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants requestState received in the Step 4 response
- `requestState`: received in the Step 4 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the response in JSON format:

```

```

In the response, as MFA is required,`enrollmentRequired`has a value of`true`under`mfaSettings`. As a result, no token is issued. The`EnrolledAccountRecoveryFactorsDetails`shows the account recovery factors the user has enrolled in. The`nextOp`values indicate what can be sent as the`op`value in the next request. In this example, the`nextOp`value "enrollment" indicates that the user is to enroll in MFA.

### Step 6: Set SMS as Default MFA Factor in Overlap

This step indicates that the client should enroll in MFA.

The client must include the following attributes:
- `authFactor`: indicates which factor to enroll in for MFA
- `accountRecoveryFactor`: when set to true, indicates that the user want to reuse already enrolled account recovery factor for MFA.

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

```

```

In the response the`nextOp`values indicate what can be sent as the op value in the next request. The`nextOp`value "enrollment" allows the user to enroll additional factor for MFA. In this use case example,`createToken`is sent in the next step.

### Step 7: Create the Authentication Token
This step indicates that the client is done with all the`authnFactors`and needs a session created. Depending on what is defined for the policy, the server validates that no other factor evaluation is needed and responds with the token or denies access. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 6 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example
The following example shows the contents of the response in JSON format:
```

```

## Authenticating with Username and Password and Keep Me Signed In

Enable and configure Keep me signed in (KMSI) so that users can access an identity domain without having to sign in repeatedly.

Use the following steps to set up KMSI using programmatic application interfaces.
- [Step 1: Enable KMSI for an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__enable-KMSI-identity-domain)
- [Step 2: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__begin-authn-flow)
- [Step 3: Submit the User's Credentials with KMSI](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__submit-user-cred)
- [Step 4: Reissue authnToken After Session Expiry](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__access-apps-kmsiToken)
- [Step 5: Submit User's Credentials with KMSI and MFA Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__submit-user-cred-kmsi-mfa-flow)
- [Step 6: Reissue authnToken After Session Expiry When an MFA Factor Is Set](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__access-apps-kmsitoken-mfa-factor-set)

This topic also contains the following sections:
- [kmsiToken Flow with requestState](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__kmsitoken-flow-with-requeststate)
- [Changes to /sso/v1/sdk/secure/session](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__changes-sso-secure-session)
- [Payload Signature for /authorize Initiated Calls](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__payload-sig-auth-init-calls)

### Before You Begin

- Ensure that KMSI has been enabled for your Cloud account. You must raise a service request (SR) with Oracle Support to enable KMSI. Specify the following feature name in the SR:`access.kmsi.support`. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Review the following sections in this topic:
- [kmsiToken Flow with requestState](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__kmsitoken-flow-with-requeststate)
- [Changes to /sso/v1/sdk/secure/session](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__changes-sso-secure-session)
- [Payload Signature for /authorize Initiated Calls](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__payload-sig-auth-init-calls)

### Step 1: Enable KMSI for an Identity Domain
After KMSI has been enabled for your Cloud account, complete the following steps to enable KMSI for an IAM identity domain.
Note  
  
If you want top use the user interface to enable KMSI, see[Changing Session Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../sessionsettings/change-session-settings.htm)and[Creating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../signonpolicies/add-sign-policy.htm).
- Get the identity domain admin access token for your account.
- Run`GET`on the`/admin/v1/KmsiSettings/KmsiSettings`endpoint. The system returns the`KmsiSettings`.
- Update the necessary attributes and run`PUT`on the`/admin/v1/KmsiSettings/KmsiSettings`endpoint.`tokenValidityInDays`Enter how many days users can stay signed in before they're automatically signed out.`kmsiEnabled`Indicates whether KMSI is enabled for the identity domain.`maxAllowedSessions`Enter the maximum number of signed-in sessions that a user can have.

Example Request

```

```

### Step 2: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

```

```

Note the new`keepMeSignedInEnabled`attribute included in the response. This indicates that this identity domain and application supports KMSI. If you have a custom interface, use this attribute to show the Keep me signed in option in the sign-in page.

### Step 3: Submit the User's Credentials with KMSI
Request
- Operation:`POST`
- 

Endpoint:`/sso/v1/sdk/authenticate`
Request Example
Note  
  
Note the new`keepMeSignedIn`attribute included in the request. This attribute indicates that the user wants to use KMSI.

```

```

If you have a custom interface, use this attribute to show the KMSI option, check the status of the checkbox (on or off) and send this parameter to create the KMSI session.

Response Example

```

```

In the response example, note the`kmsiToken`attribute. This token can be used to access any applications in the future without requiring a user to sign in again.

### Step 4: Reissue authnToken After Session Expiry
Request
- 

Operation:`POST`
- 

Endpoint:`/sso/v1/sdk/authenticate`

Request Example

```

```

Response Example

```

```

Note the operation`credSubmit`with a new`authFactor`,`appName`and`kmsiToken`being sent in the request. SSO evaluates the request and returns`authnToken`and latest updated`kmsiToken`in the response. This is a refreshed`kmsiToken`and replaces the existing token. You must include this refreshed`kmsiToken`in the next request.

### Step 5: Submit User's Credentials with KMSI and MFA Flow

Initiate`GET`on`/sso/v1/sdk/authenticate`from[Step 2: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__begin-authn-flow).
Request
- 

Operation:`POST`
- 

Endpoint:`/sso/v1/sdk/authenticate`

Response Example

```

```

Response Example

```

```

After you get the one-time passcode (OTP) on the device, add the OTP in the request.

Request Example

```

```

The response includes`authToken`and`kmsiToken`. This is a refreshed`kmsiToken`.

Response Example

```

```

### Step 6: Reissue authnToken After Session Expiry When an MFA Factor Is Set

When a user tries to sign in using`kmsiToken`and there's a second factor configured, then the user is always prompted for authentication of the second factor. Only after successful authentication, will`authnToken`and`kmsiToken`be sent in the response.
Request
- 

Operation:`POST`
- 

Endpoint:`/sso/v1/sdk/authenticate`

Request Example

```

```

The response contains a refreshed KMSI token and an MFA challenge.

Response Example

```

```

Repeat the same process where you will again prompted for the OTP on the device. Provide the below payload with the OTP. The response should include the`authnToken`.

Request Example

```

```

Response Example

```

```

### kmsiToken Flow with requestState

Use this flow to support browser context when you possess the KMSI token but not the KMSI cookie. After session expiry, the application makes an authorization call to the identity system with the`redirectUrl`,`state`,`nonce`, and so on. In the response, the identity system returns the`requestState`inside`loginCtx`. This requestState along with KMSI token is passed to redirect the required application after extending the session.
Request
- 

Operation:`POST`
- 

Endpoint:`/sso/v1/sdk/authenticate`
The API supports KMSI as an`authFactor`and authenticating KMSI with the`requestState`parameter. This allows`kmsiToken`with`requestState`to be retrieved from`loginCtx`.
Note  
  
If`requestState`and`kmsiToken`aren't from the same App, then the request is declined.

Request Example

```

```

Response Example

```

```

### Changes to`/sso/v1/sdk/secure/session`

KMSI requires a new attribute be added to the`/sso/v1/sdk/secure/session`endpoint.`kmsiToken`must be sent to the endpoint from the custom login application.

Request Example Response Example

`authnToken`or`requestState`

`authorization``kmsiToken`The new form post variable`kmsiToken`along with`authnToken`or`requestState`will redirect to the application along with SSO session cookie and KMSI cookie.

### Payload Signature for`/authorize`Initiated Calls
- When a user accesses any web application protected by identity domains, they enter their application URL, for example,`https://example.com/home/pages/profile`.
- The system redirects to the identity domain`/authorize`call.
- The identity domain redirects the user to customer deployed custom sign-in page.
- The customer hosted sign-in application collects the input parameters and decodes`loginCtx`input.
- The decrypted input parameter matches with the`GET``/sso/v1/sdk/authenticate`call.
- The payload contains`keepMeSignedInEnabled`to identify whether KMSI is enabled.
- The custom login application collects the credentials and submits it to the identity domain.
- The identity domain validates the credentials and issues`kmsiToken`and`authnToken`.
- The custom login application makes use of the`authnToken`and`kmsiToken`while making call to`/sso/v1/sdk/secure/session`endpoint. The new syntax of the secure endpoint is described in[Changes to /sso/v1/sdk/secure/session](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#concept_fnt_dw5_25b__changes-sso-secure-session).
- The identity domain validates the`authnToken`,`kmsiToken`and then the identity system issues the SSO session cookie and the KMSI cookie.
-
