# About Select AI Agent
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-select-ai-agents.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-select-ai-agents.html#dcoc-content-body)

# About Select AI Agent

Select AI Agent (autonomous agent framework) is a program for creating and managing interactive and autonomous agents inside Autonomous AI Database. Agents reason about requests, call tools, reflect on results, and maintain context with short and long-term memory powered by an AI profile specified LLM with the ReAct (Reasoning and Acting) agentic pattern.

Select AI Agent enables the use of built-in tools such as RAG and Natural Language to SQL (NL2SQL), custom PL/SQL procedures, and external REST APIs to complete tasks. The framework preserves multi-turn memory, maintaining context across conversations. Together, these capabilities support scalable, context-aware generative AI that integrates with enterprise data and workflows.

The`DBMS_CLOUD_AI_AGENT`package encapsulates management, orchestration, and security boundaries. See[DBMS_CLOUD_AI_AGENT Package](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-agent-package.html#GUID-39C4A94B-C07A-4A76-8412-BEEA667C259B)for details.

Note  
  
See Also:[Select AI and Select AI Agent Capability Matrix](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database/serverless/adbsb&id=SAICM-GUID-163B5E15-03DE-437B-9570-03689ED7E1A8)to learn about Select AI capabilities available across Autonomous AI Database and Oracle AI Database releases.

## Features of Select AI Agents

The key features include integrated intelligence, flexible tooling, context-aware conversations, and faster deployment.
- 

Integrated Intelligence:

Combines planning, tool use, and reflection so agents can reason about tasks, choose and run tools, observe outcomes, adjust plans, and improve responses throughout conversation. Agents plan steps, run tools, evaluate observations, and update their approach when outcomes miss expectations. This loop strengthens accuracy, reduces rework, and keeps conversations on track.
- 

Flexible Tooling:

Support and use built-in RAG and NL2SQL, custom PL/SQL procedures, and external REST services, without orchestration components or separate infrastructure, so you can keep core logic in the database while integrating external capabilities as needed.
- 

Context-Aware Conversations:

Maintain short-term and long-term memory to keep context across turns, personalize responses, store preferences, and support human-in-the-loop control for corrections and confirmations during multi-turn sessions. Short-term memory keeps the current dialogue coherent. Long-term memory records preferences and prior outcomes, supporting follow-up interactions and oversight by human reviewers.
- 

Scalable and Secure:

Run inside Autonomous AI Database, inherit its security controls, auditing, and performance, reduce data movement, and standardize governance for enterprise deployments and regulated environments at scale. Agents benefit from database security, auditing, and performance characteristics. Keeping processing close to data reduces movement and aligns with governance practices.
- 

Faster Development:

Define agents, tasks, and tools with familiar SQL and PL/SQL, reuse existing procedures, and ship features faster while keeping logic close to operational data and teams without building separate infrastructure.

## ReAct Agentic Pattern

Select AI Agent uses ReAct (Reasoning and Acting) agentic pattern where the agent reasons about the request, chooses tools, performs actions, and evaluates results to accomplish a goal.

ReAct combines reasoning and action in a loop. The agent thinks, chooses a tool, observes results, and repeats until it can present a confident answer. The user’s AI profile specified LLM alternates between reasoning and actions through the tools. The database processes those actions and returns the observations.

The following is the pattern for each iteration:
- 

Query: The user asks a question or states a request. The agent reads it, extracts key details, and prepares to plan the next steps.
- 

Thought and Action: The agent reasons about options, picks a tool, and runs it to gather data or change state as needed for the task.
- 

Observation: Observations include tool or query results, confirmation messages, and errors. These become inputs to the agent’s next round of reasoning. The agent records observations and checks whether the results support the next step or the final response.
- 

Final Response: After enough successful thought-action and observations, the agent composes a clear answer, explains important decisions, and shares any next steps or follow-up actions.

## Select AI Agent Architecture

Select AI Agent organizes work into four layers: Planning, Tool Use, Reflection, and Memory Management. These layers coordinate reasoning, tool runs, evaluation, and context multi-turn interactions.

Planning : Planning interprets the user request, breaks it into ordered actions, selects candidate tools, and drafts a plan using session context, prior outcomes, and relevant knowledge. The agent analyzes the request, identifies missing details, and proposes an ordered sequence of actions. It chooses tools that fit policy, data scope, and expected outcomes.

Tool Use : Tool Use selects and runs the tool for each action. Supported types include RAG, NL2SQL, custom PL/SQL procedures that can be added when you create a[tool](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/select-ai-agents-concepts.html#GUID-22B125D4-6C87-4B79-BC05-099FB9391016), and external REST services such as web search and email. Each step calls a tool with parameters. Built-in tools handle retrieval and SQL generation. Custom PL/SQL encapsulates domain logic. REST tools connect to external services.

Reflection : Reflection evaluates tool results against expectations and proceeds to final response. The agent compares observations to the goal. If results look wrong or if there are tool call errors or user disapproved results, the agent revises reasoning, chooses another tool, or updates the plan before trying again. When results do not fit, it adjusts the plan, selects different tools, or may ask clarifying questions before proceeding. Select AI Agent thoughts can be queried using`USER_CLOUD_AI_CONVERSATION_PROMPTS`. See[DBMS_CLOUD_AI Views](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-views.html#GUID-5C826A3E-E60B-4D1C-AD0B-E385F6ECEBA5)for more information.

Memory Management : Memory Management stores session context and knowledge per agent team. Short-term memory holds recent messages and intermediate results per agent team. Long-term memory records preferences, history, and strategies, improving continuity, personalization, and planning. Long-term memory persists useful knowledge across sessions, improving guidance and response quality over time across agent teams.

- [About Select AI Agent](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-select-ai-agents.html#GUID-7B8A5B96-6B9C-4745-9EAA-1D6F86A3E8FF)
- [Features of Select AI Agents](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-select-ai-agents.html#GUID-5D7F84EC-7B16-4B9E-A284-AAAE439922B1)
- [ReAct Agentic Pattern](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-select-ai-agents.html#GUID-42EE0D39-FB7A-45C1-990D-50E4EB5FE1EC)
- [Select AI Agent Architecture](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-select-ai-agents.html#GUID-8FF38DC4-97B9-4BA3-9805-31771FE38BD0)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
