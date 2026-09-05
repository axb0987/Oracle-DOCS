# Branding the Interface
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/brand/brand_customizing-the-interface.htm
- Fetched: 2026-09-05 02:20 CDT

# Branding the Interface

Add company branding to the domain interface in IAM.

You can add a logo to the following interfaces to customize them with your company branding:
- Sign-in page
- Console pages: including: My Apps page, Catalog page
- Notification templates

You can also add a background image on the sign-in page, customize the text that users see on the sign-in page and choose the language it's displayed in.

## Required Policy or Role

To manage identity domain settings, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/brand/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/brand/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/brand/../policieshow/Policy_Basics.htm).

## Image Requirements for Logos and Background Images

The files that you upload for logos or background images must be in one of these allowed file types: GIF, JPEG, JPG or PNG.

The images must also meet the size requirements shown in the following table. All measurements are in pixels.

Image or Icon Max Width and Height Allowed

Recommended Dimensions

Width X Height Maximum File Size Ratio Notes
Sign-in page logo 250W X 50H 250W X 50H 300 KB 5:1 If you use larger images, be aware that larger images will be resized to maintain a 5:1 ratio.
Sign-in page background image None None 300 KB Not applicable If the image is too small, the image is repeated horizontally and vertically.
My Apps and Catalog page logos 64H No restriction in width. 250W x 50H 300 KB 5:1 If you use an image that is 250 pixels wide or larger, the text on My Console might be displaced.
