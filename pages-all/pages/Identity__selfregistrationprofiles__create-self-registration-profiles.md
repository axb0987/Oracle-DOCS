# Creating a Self-Registration Profile
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/create-self-registration-profiles.htm
- Fetched: 2026-09-05 02:28 CDT

# Creating a Self-Registration Profile

Create self-registration profiles in IAM to manage self-registration for different sets of users, approval policies, and applications.

- On the Self registration list page, select Add profile . If you need help finding the list page, see[Listing Self-Registration Profiles](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/list-self-registration-profiles.htm).
- Enter details about the self-registration profile.
- Enter a unique name for the profile.
- To require a user to accept the terms of use during self-registration, select User consent required . To hide the terms of use from the user during self-registration, clear the option.
- To add groups to the profile, select Assign in the Assign to group section.
- Add the user's email domains allowed during the self-registration process in the Allowed email domains field. Enter all or leave this field blank to allow all email domains.
- Add design elements to the profile. Upload footer and header logos or keep the default logos.
- Complete the Self-registration content section.
- Enter the registration page name that you want to appear as a link on your customized sign in page.
- Add header, footer, and success text, or keep the default values.
- If you have selected User consent required , enter the text in User consent text .

Tip  
  
To discard your changes and return to the Manage self-registration profiles page, select Cancel .
- Select Add profile .
The profile ID that you need for the self-registration link is created.
- On the Self registration page, activate the profile. From the Actions menu (three dots) , select Activate .
Next,[construct a self-registration URL](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/construct-self-registration-url.htm)
