# Customizing the Sign-In Page Branding
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/brand/customizing-the-signin-page.htm
- Fetched: 2026-09-05 02:20 CDT

# Customizing the Sign-In Page Branding

Customize the sign-in page options for an identity domain in IAM.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- Select Branding .
- If Oracle branding (default) is selected, then select Custom branding .
- Under Sign in page , change the following values as needed:

- Translation : Select the language displayed on the sign-in page.
- Company name : Enter the name of the company that appears on the sign-in page.
- Hide ContinueToSignin button : Enable to prevent the Continue to Sign In button from displaying.
- Login text : Enter the text that's displayed on the sign-in page. This text can be a hint to help users sign in.

Note  
  
The Continue to Sign In button is displayed if any of the following is true:
- 

`returnUrl`is present in the reset password token sent in the reset password link.
- 

the SSO Cookie is resent. For example, ORA_OCIS_REQ_1.
- the user is a henosis user.

As the third condition is always true for a henosis user, all migrated tenancies and newly created tenancies always see that button. Hiding the button restores parity with the pre-henosis flow, ignoring the third condition for first time users while setting their password. By IDCS design, this button can't be fully hidden for every login.
- Under Company logos , in the Sign in page area, upload the following images:

- To include a logo on the sign-in page, upload the logo image file to the Logo slot.
- To include a background image on the sign in page, upload the image file to the Background image slot.
- To preview your changes, at the top of the page, select Preview Sign In . A new web page opens that displays a preview of the customizations you made to the sign-in page.
- Reduce the size of the preview web page so that the dimensions of the page resemble the dimensions of a mobile device, and verify that the logo appears properly.
- Select Save changes .
-
