# Overview of Hosted Sign In Pages
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/what-is-hosted-sign-page.htm
- Fetched: 2026-09-05 02:22 CDT

# Overview of Hosted Sign In Pages

A Hosted Sign In page allows you to customize the look and feel of the identity domain sign-in experience by using style classes, custom HTML, and translation support.

Learn about Hosted Sign In pages:
- [Customize the Login Experience](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/what-is-hosted-sign-page.htm#what-is-hosted-sign-page__hosted-sign-in-overview)
- [Understand the Custom HTML](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/what-is-hosted-sign-page.htm#understand-default-custom-html)
- [Understand How Translations Work](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/what-is-hosted-sign-page.htm#understand-how-translations-work)
- [Use the Backup URL to Recover the Sign In Page](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/what-is-hosted-sign-page.htm#use-backup-url-recover-sign-page)

Create a Hosted Sign In page:
- [Creating a Hosted Sign-In Page](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/create-hosted-sign-page.htm)

## Customize the Login Experience
You can customize the login experience using one or both of the following methods.

Add your own Background image to the sign-in page.

Background images provided for the sign-in page in the Branding settings apply for all the sign-in flows. See[Customizing the Sign-In Page Branding](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/../brand/customizing-the-signin-page.htm).
Provide custom HTML and custom translations using Hosted Sign In.

Hosted Sign In provides custom HTML and custom translations, in order to overwrite the current sign-in page definition. This customization applies to the main sign-in page. It doesn't affect all sign-in flows, for example, it doesn't affect the reset password and MFA flows.
The Hosted Sign In page:
- Allows you to change current styles and to add new HTML elements.
- Supports translations for existing elements as well as new elements.

See[Creating a Hosted Sign-In Page](https://docs.oracle.com/en-us/iaas/Content/Identity/hostedsignin/create-hosted-sign-page.htm).

## Assumptions

- The feature is based on JET 7.2. All browsers that support JET 7.2 can use this feature.
- Administrators are familiar with existing style classes in the sign-in page.

## Limitations

- HTML Comments (`<!-- comment -->`) aren't allowed.
- 

Adding custom JavaScript isn't allowed.
- 

The`<style>`tag isn't allowed. But you can only use an inline style of elements, for example`<div style="property: value, ...">`
- 

There is no code validation. Use the Preview option to verify that your custom code is valid.
- 
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
- 
A limited set of HTML tags is available.
- div
- img
- label
- input
- h1
- h2
- h3
- span

## Understand the Custom HTML

When Hosted Sign In is enabled for the first time, default HTML code is provided. You customize this code to define your Hosted Sign In page. This new code becomes your custom HTML.

Use this default HTML code as a template for your custom HTML. The code is fully functional, which means that the Hosted Sign In page will work even if nothing is changed.

### Default HTML

```

```

### Customized HTML Example

```

```

## Understand How Translations Work

Hosted Sign In allows you to specify translations for existing elements as well as new elements for your custom HTML code.

The default translations value is`{}`, which means there are no translations provided for the custom HTML code.

### The Structure of Translations
Each attribute represents a label, the key is`data-idcs-text-translation-id`, and the value is an object containing the different languages and the translated strings. The following example has translations for existing elements (`idcs-username-label`), as well as new elements (`welcometext`).
```

```

The following existing elements can be customized in the sign-in page. To customize the existing elements, the following reserve IDs must be used.
- Element:`username label`
- Reserve ID:`idcs-username-label`
- Element:`username placeholder`(help text inside the username field)
- Reserve ID:`idcs-username-placeholder`
- Element:`password label`
- Reserve ID:`idcs-password-label`
- Element:`password placeholder`(help text inside the username field)
- Reserve ID:`idcs-password-placeholder`

### Translating New Labels

If a new label is introduced in the Hosted Sign In page, by using`<div>`,`<span>`or header tags like`<h1>`,`<h2>`,`<h3>`, and so on, a translation ID (`data-idcs-text-translation-id`) must be provided for them. For example, use`<div data-idcs-text-translation-id="instructions"></div>`where`data-idcs-text-translation-id`of the element is used to provide a translated text.

## Use the Backup URL to Recover the Sign In Page

If changes made to the Hosted Sign-in code break the sign-in flow (for example, removing core components), administrators can use this URL to sign in with the default login page and gain access to the identity domain.

Create a backup URL like the following:`<hostname:[port]>/ui/v1/signin? noBranding=true`

Note
