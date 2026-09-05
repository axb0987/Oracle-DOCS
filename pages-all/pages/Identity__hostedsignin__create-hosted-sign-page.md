# Creating a Hosted Sign-In Page
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/create-hosted-sign-page.htm
- Fetched: 2026-09-05 02:22 CDT

# Creating a Hosted Sign-In Page

Create a Hosted Sign In page in IAM to customize the look and feel of the identity domain sign-in experience by using style classes, custom HTML, and translation support.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Settings .
- On the Settings page, select Hosted sign in .
- Select Enable hosted sign in .
- Edit the Custom HTML .

A limited set of HTML tags is available.
- div
- img
- label
- input
- h1
- h2
- h3
- span
A limited set of style properties is available.
- align-items:
- background-color:
- background:
- border-radius:
- border:
- box-shadow:
- content:
- display:
- height:
- justify-content:
- left:
- margin-top:
- margin:
- max-height:
- max-width:
- min-height:
- padding-left:
- padding-right:
- padding:
- position:
- text-align:
- top:
- width:

Properties can be applied inline. In the following example, the sign-in page background has been customized by setting the style property to`style="background-color:lightblue"`
```

```

Tip  
  
Need to start over? You can revert to the default HTML values by selecting Restore default HTML .
- Specify translations.

The following existing elements can be customized in the sign-in page. To customize the existing elements, the following reserve IDs must be used.
- Element:`username label`
- Reserve ID:`idcs-username-label`
- Element:`username placeholder`(help text inside the username field)
- Reserve ID:`idcs-username-placeholder`
- Element:`password label`
- Reserve ID:`idcs-password-label`
- Element:`password placeholder`(help text inside the username field)
- Reserve ID:`idcs-password-placeholder`
Tip  
  
Need to start over? You can clear the translations pane by selecting Restore default translations .
- Select Preview sign in to view changes without saving them.
-
