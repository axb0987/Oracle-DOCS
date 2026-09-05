# Configuring DKIM
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configure-dkim-using-the-console.htm
- Fetched: 2026-09-05 02:01 CDT

# Configuring DKIM

Learn how to configure Domain Keys Identified Mail (DKIM) to verify that an email is sent and authorized by the owner of the sender's domain.

DKIM is set up within DNS records to verify digital signing of emails.
Note  
  
This procedure doesn't apply to OCI Classic services such as Fusion Apps, Cloud Notification Services, and classic IDCS. As these services don't use OCI Email Delivery, DKIM support for these services requires opening a support ticket to the service that generates the email. Note that if you set up a DKIM key for an OCI Classic service and a DKIM key for OCI Email Delivery in the same email domain, each of these keys must have a different selector. When opening a support ticket, mention the service that's generating the email so the support team can route your ticket correctly.
Note  
  

This procedure also doesn't apply to Oracle Integration Cloud Generation 2 (OIC) or Oracle Transportation and Global Trade Management (OTMGTM) services. Each of these services requires its own service-specific DKIM key that must have a different selector from other DKIM keys in your email domain. For the procedure for OIC, see[Configure Email Authentication Settings for SPF and DKIM](https://docs.oracle.com/en/cloud/paas/integration-cloud/oracle-integration-oci/configure-email-authentication-settings-spf-and-dkim.html). For the procedure for OTMGTM, see[Configure DKIM](https://docs.oracle.com/en/cloud/saas/transportation/24a/otmol/configuration/configure_dkim.htm?rhhlterm=otmgtm).

When opening a support ticket, mention the specific service (OIC or OTMGTM) so the support team can route your ticket correctly.

## Using the Console

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Email Domains .
- Select the name of the email domain where you want to configure DKIM.
- In the details page, select DKIM .
- In the DKIM section, select Add DKIM .
- Select Add new DKIM and select Next .
(Optional) Add tags to organize your resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask the administrator.
- In the DKIM selector field:

- Enter the prefix to be used in generating the DKIM selector for this particular DKIM key. Replacement keys each have their own unique selector and include a date component to easily identify when the key is rotated. The DKIM selector can contain only up to 63 lowercase alphanumeric characters (a-z, 0-9) with dashes.
- Select Next .
- Select Generate DKIM Record to generate the DKIM record. The system generates a CNAME record and value that can be used in your DNS setup for your email domain.

Note  
  
For non-commercial realms, add the DKIM Text Record Value to your DNS setup.
- Copy the CNAME and CNAME Record Value and add it to your DNS setup.

Note  
  
To add DNS records, the domain must be registered and available on the public Internet. DNS records must be added using the domain's registered DNS provider, which is the DNS system that the domain's name servers point to.
- Select Add DKIM .

Email Delivery supports a maximum of two DKIM keys per email domain. However, only one DKIM record can be active for your domain at a time. We recommend that you rotate your keys every six months.
- To verify SPF and DKIM are configured, go to the Email Domain Details page and use the SPF and DKIM verification feature to confirm your DNS is configured correctly. For more information, see[Configuration of DKIM within OCI Email Delivery](https://blogs.oracle.com/cloud-infrastructure/post/configuration-of-dkim-within-oci-email-delivery-is-now-simple)
