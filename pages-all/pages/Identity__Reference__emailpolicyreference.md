# Details for the Email Delivery Service
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm
- Fetched: 2026-09-05 02:14 CDT

# Details for the Email Delivery Service

This topic covers details for writing policies to control access to the Email Delivery service.

## Resource-Types

`email-domains`

`email-work-requests`

`email-family`

`approved-senders`

`suppressions`

## Supported Variables

The Email Delivery Service supports all the general variables (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus the ones listed here.

Variable Variable Type Comments
`target.approved-sender.email-domain`String The value matches the domain portion (right-hand-side) of the email address and the name of the associated`email-domain`object if one exists. Policies should use the[U-label](https://tools.ietf.org/html/rfc5890)form of the domain. Matching is case-insensitive. This is not available for`ListSenders`.
`target.email-domain.name`String Scopes permission to domains that match the specified domain name. Policies should use the[U-label](https://tools.ietf.org/html/rfc5890)form of the domain. Matching is case-insensitive. This variable can be used with pattern matching syntax to grant sub-domain access. This is not available for`ListEmailDomains`.
`target.email-domain.id`Entity (OCID) Not available for`ListEmailDomains`or`CreateEmailDomain`.
`target.email-work-request.id`Entity (OCID) Not available for`ListWorkRequests`.
`target.approved-sender.id`Entity (OCID) Not available for ListSenders and CreateSenders.
`target.approved-sender.emailaddress`String Not available for ListSenders.
`target.dkim.email-domain`String Scopes permission to DKIMs for a specific email domain. Policies should use the[U-label](https://tools.ietf.org/html/rfc5890)form of the domain and matching is case-insensitive. Not for ListDkims.

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[email-domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

EMAIL_DOMAIN_INSPECT`ListEmailDomains`

None
read

INSPECT +

EMAIL_DOMAIN_READ`GetEmailDomain`None
use

READ +

EMAIL_DOMAIN_UPDATE`UpdateEmailDomain`None
manage

USE +

EMAIL_DOMAIN_CREATE

EMAIL_DOMAIN_DELETE

EMAIL_DOMAIN_MOVE

`CreateEmailDomain`

`DeleteEmailDomain`

`ChangeEmailDomainCompartment`None

[dkims](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

DKIM_INSPECT`ListDkims`

None
read

INSPECT +

DKIM_READ`GetDkim`None
use READ +

DKIM_UPDATE

`UpdateDkim`None
manage

USE +

DKIM_CREATE

DKIM_DELETE

`CreateDkim`

`DeleteDkim`None

[email-work-requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

EMAIL_WORK_REQUEST_INSPECT`ListWorkRequests`

None
read

INSPECT +

EMAIL_WORK_REQUEST_READ`GetWorkRequest`

`ListWorkRequestErrors``ListWorkRequestLogs`None

[email-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

APPROVED_SENDER_INSPECT

EMAIL_DOMAIN_INSPECT

EMAIL_WORK_REQUEST_INSPECT

SUPPRESSION_INSPECT

EMAIL_RETURN_PATH_INSPECT`ListSenders`

`ListEmailDomains`

`ListWorkRequestErrors``ListSuppression``ListEmailReturnPaths`None
read

INSPECT +

APPROVED_SENDER_READ

EMAIL_CONFIGURATION_READ

EMAIL_DOMAIN_READ

EMAIL_WORK_REQUEST_READ

SUPPRESSION_READ

EMAIL_RETURN_PATH_READ

`GetSender`

`GetEmailDomain``GetEmailConfiguration`

`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs``GetSuppression``GetEmailReturnPath`None
use

READ +

APPROVED_SENDER_USE

APPROVED_SENDER_UPDATE

EMAIL_DOMAIN_UPDATE

EMAIL_RETURN_PATH_UPDATE

`SmtpSend`

`UpdateSender`

`UpdateEmailDomain``UpdateEmailReturnPath`None
manage

USE +

APPROVED_SENDER_CREATE

APPROVED_SENDER_DELETE

APPROVED_SENDER_MOVE

EMAIL_DOMAIN_CREATE

EMAIL_DOMAIN_DELETE

EMAIL_DOMAIN_MOVE

SUPPRESSION_CREATE

SUPPRESSION_DELETE

EMAIL_RETURN_PATH_CREATE

EMAIL_RETURN_PATH_DELETE

`CreateSender`

`DeleteSender`

`MoveSender`

`CreateEmailDomain`

`DeleteEmailDomain`

`ChangeEmailDomainCompartment`

`CreateSuppression`

`DeleteSuppression`

`CreateEmailReturnPath`

`DeleteEmailReturnPath`

None

[approved-senders](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

APPROVED_SENDER_INSPECT`ListSenders`

None
read

INSPECT +

APPROVED_SENDER_READ`GetSender`None
use

READ +

APPROVED_SENDER_USE`SmtpSend`None
manage

USE +

APPROVED_SENDER_CREATE

APPROVED_SENDER_DELETE

APPROVED_SENDER_UPDATE

APPROVED_SENDER_MOVE

`CreateSender`

`DeleteSender`

`UpdateSender`

`MoveSender`

None

[suppressions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

SUPPRESSION_INSPECT

`ListSuppression`

None
read

INSPECT +

SUPPRESSION_READ`GetSuppression`None
use

No extra

None None
manage

USE +

SUPPRESSION_CREATE

SUPPRESSION_DELETE

`CreateSuppression`

`DeleteSuppression`

None

[custom-return-path](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/emailpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

EMAIL_RETURN_PATH_INSPECT`ListEmailReturnPaths`None
read

INSPECT +

EMAIL_RETURN_PATH_READ`GetEmailReturnPath`None
use

READ +

EMAIL_RETURN_PATH_UPDATE`UpdateEmailReturnPath`None
manage

USE +

EMAIL_RETURN_PATH_CREATE

EMAIL_RETURN_PATH_DELETE

`CreateEmailReturnPath`

`DeleteEmailReturnPath`

None

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
`GetEmailConfiguration`EMAIL_CONFIGURATION_READ
`ListEmailDomains`EMAIL_DOMAIN_INSPECT
`GetEmailDomain`EMAIL_DOMAIN_READ
`CreateEmailDomain`EMAIL_DOMAIN_CREATE
`UpdateEmailDomain`EMAIL_DOMAIN_UPDATE
`DeleteEmailDomain`EMAIL_DOMAIN_DELETE
`ChangeEmailDomainCompartment`EMAIL_DOMAIN_MOVE
`ListSenders`APPROVED_SENDER_INSPECT
`GetSender`APPROVED_SENDER_READ
`CreateSender`APPROVED_SENDER_CREATE
`UpdateSender`APPROVED_SENDER_UPDATE
`DeleteSender`APPROVED_SENDER_DELETE
`MoveSender`APPROVED_SENDER_MOVE
`SmtpSend`APPROVED_SENDER_USE
`ListSuppression`SUPPRESSION_INSPECT
`GetSuppression`SUPPRESSION_READ
`CreateSuppression`SUPPRESSION_CREATE
`DeleteSuppression`SUPPRESSION_DELETE
`ListWorkRequests`EMAIL_WORK_REQUEST_INSPECT
`GetWorkRequest`EMAIL_WORK_REQUEST_READ
`ListWorkRequestErrors`EMAIL_WORK_REQUEST_INSPECT
`ListWorkRequestLogs`EMAIL_WORK_REQUEST_INSPECT
`CreateEmailReturnPath`EMAIL_RETURN_PATH_CREATE
`DeleteEmailReturnPath`EMAIL_RETURN_PATH_DELETE
`GetEmailReturnPath`EMAIL_RETURN_PATH_READ
`ListEmailReturnPath`EMAIL_RETURN_PATH_INSPECT
`UpdateEmailReturnPath`
