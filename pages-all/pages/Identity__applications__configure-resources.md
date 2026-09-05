# Configuring SSO Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/configure-resources.htm
- Fetched: 2026-09-05 02:19 CDT

# Configuring SSO Resources

Create resources individually by adding one resource for each of your application's URLs, or use regular expression to create a resource which represents a collection of URLs for your application.
A resource represents a URL or URL Pattern for which you want to restrict access or intend to give anyone to access. You need the list of resources of your application. See[Enterprise Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enterprise-applications.htm)

Policy mapping is hierarchical in App Gateway. So, order of the resources defined is important. See the following example:
If the user is accessing a resource`/myapp/logout.html`, and we have authentication policy in below order:
- `/.*`(public)
- `/.*/logout.html`(Form+logout) Then policy match stops at step #1 (`/.*`) and the same policy is applied which is "public" in this case.
Similarly, if user is accessing a resource`/myapp/logout.html`and we have authentication policy in below order.
- `/.*/logout.html`(Form+logout)
- `/.*`(public) In this case, policy match stops at point 1 (`/.*/logout.html`) and same policy is applied which is "Form+logout".

Something else to be aware of is that applications which do their own login integrations can run into problems when their integrations accessed static resources during login, but the resources weren't made public. This causes the login process to fail. To avoid this happening, you should use the`public`authentication method for your public static resources such as CSS, JavaScript, image files as follows:
- Group all public static resources together, for example under`/myapp/public/resources`.
- 

State that these directories should use the`public`authentication method using a regex such as`/myapp/public/.*`.

To configure resources:

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the enterprise application to change.
- On the Application details page, select SSO configuration , and then select Edit SSO configuration . In the Resources section, select Add resource to add a resource.
- In Add resource , provide a name and description for the resource and the resource URL. Optionally, add a URL query string . If you want to use a regular expression, then select Regex , so that App Gateway evaluates the Resource URL value as a pattern.

For example, if you want to protect the application endpoint`http://myapp.internal.example.com:3266/private/home`, you can enter`/private/home`as the value for Resource URL . If you want to protect any page under the`/private`context, then enter`/private/.*`as value for Resource URL , and select Regex .

See[Using Regular Expressions](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/use-regular-expressions.htm).
- Select Add resource .
-
