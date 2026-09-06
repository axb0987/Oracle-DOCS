# Access Backends Using Custom Components
- Source: https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-custom-components.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/digital-assistant/doc/access-backends-using-custom-components.html#dcoc-content-body)

# Access Backends Using Custom Components

Oracle Digital Assistant has many built-in components to support basic actions like setting variables and prompting for user input. In cases where your bot design calls for actions outside of the provided components, such as calling REST APIs, implementing complex business logic, and customizing messages, you can write custom components.

Tip: If the logic or processing is needed in the context of a composite bag entity, consider using entity event handlers, which you can create directly from the composite bag's configuration page. See[Entity Event Handlers](https://docs.oracle.com/iaas/digital-assistant/doc/configure-composite-bag-entities.html#GUID-A6DECB5B-8A13-4002-AD1E-74A38A4A3B6D).

To use a custom component, complete these tasks:
- 

Implement: Using JavaScript and the Oracle Digital Assistant Node.js SDK, implement a custom component that transfers data to and from the skill using the SDK's metadata and conversation objects. See[Implement Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/implement-custom-components.html#GUID-268C35B3-57B3-4E52-BEEC-1DEE7CA0ACFB).
- 

Deploy: If you are hosting the components on Oracle Mobile Hub backend, Oracle Cloud Infrastructure Functions, or a Node.js server, deploy the component package. See[Deploy the Component Package to a Service](https://docs.oracle.com/iaas/digital-assistant/doc/deploy-component-package-service.html#GUID-E4642681-DBE5-4876-8523-EB8934F67D74).
- 

Add to Skill: Make the components available to a skill by adding a component service for it. See[Add Component Package to a Skill](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-A93D7DAB-DCCE-42CD-8E6B-A06FB9BEE90D).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
