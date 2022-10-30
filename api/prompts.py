SUMMARY_PROMPT = '''
Summarize this software developer interview and get name, and work experience :
Interview: Jose Arvelo
What is your reason for change?
-. He wants to be able to develop in more and better projects and the company is not generating those opportunities, that is why he is exploring the market and looking for a salary increase.
Currently at Genoma-work as Product Owner of an AI company. At this moment he manages 3 departments: BigData Science, UX, product development, currently with a UXUI and research team. Determination of the project.
Do you have experience in startups, do you know how they work? In what areas have you worked?
-. Yes, currently in IT Consulting Services.
Do you have experience managing teams?
-. Yes, manage 13 people, 04 science assessment, investigation data scientist, 04 UX, 05 development
Do you create the indicators, objectives to be met, goals, initiatives?
-. Create the OKRs with the CEO, you can also generate initiatives.
Project management, software development?
-. SI manages projects has participated in other software developments, web
What tools do you use? Jira, Slack, cloud, automations, saas
-.Notion, figma, miro, slack, discord, saas, power bi, jira, asana, monday, trello, Salesforce, haven't seen cloud tools or automations
What methodology do you work with, certificate or course as PO?
-.kanban, scrum, inbest, lean, agility and innovation courses.
How long are the Sprints? sprints planning, review and retrospective validate the sprint
 -. The development team is the one who does the planning sprints, they participate to validate that everything is based on the methodology.
How do you manage the Backlog? Estimate epic tasks, delivery route,
-. He prioritizes the Backlog, 01 week
Creation of user stories?
-. He creates User Stories from scratch
How do you manage the technical debt, what do you do to avoid it?
 -.He visualizes the technical debt
Comment on a project you worked on and how you did it? (Preferably linked to an ecomercer within a StartUp)
Company: Genomawork
Project: ATS Evaluations and Assessments
Project Goal: Redesign of all views.
Tasks and responsibilities: Manage the creation process, ideation until launch, database remodeling, managing the team, validating the sprint planning, managing and prioritizing the Backlog, as well as creating User Stories and visualizing the technical debt for its correction.
Technologies used: javascript, react, Figma, Jupiter.
Positively impact the churn reduction and NPS increase indicators of the product.
If you know about Churn and NPS, it is used by the commercial area.

Summary: Industrial engineer specialized in innovation, digital transformation and business and product development, with knowledge in business intelligence, web development, e-commerce and digital marketing, management of tools such as Notion, Figma, Miro, Slack, SAAS, Power Bi, Jira, Salesforce and management of kanban, scrum, inbest, lean methodologies.
In the past he has worked in StartUps, he has experience with the fields of IT Services and Consulting, Technology, Information and Internet, Pharmaceutical, Food and Beverage Services.
He has managed a team and has been responsible on occasions for creating OKRs and generating initiatives, currently as Product Owner at Genomawork, being responsible for leading the product area, working with UX/UI and development teams, prioritizing the product backlog, defining the scope of the projects and creating the user stories.

--

'''

EXTRACTION_PROMPT = '''
Extract from the text the tools used by the person

Interview: Jose Arvelo
What is your reason for change?
-. He wants to be able to develop in more and better projects and the company is not generating those opportunities, that is why he is exploring the market and looking for a salary increase.
Currently at Genoma-work as Product Owner of an AI company. At this moment he manages 3 departments: BigData Science, UX, product development, currently with a UXUI and research team. Determination of the project.
Do you have experience in startups, do you know how they work? In what areas have you worked?
-. Yes, currently in IT Consulting Services.
Do you have experience managing teams?
-. Yes, manage 13 people, 04 science assessment, investigation data scientist, 04 UX, 05 development
Do you create the indicators, objectives to be met, goals, initiatives?
-. Create the OKRs with the CEO, you can also generate initiatives.
Project management, software development?
-. SI manages projects has participated in other software developments, web
What tools do you use? Jira, Slack, cloud, automations, saas
-.Notion, figma, miro, slack, discord, saas, power bi, jira, asana, monday, trello, Salesforce, haven't seen cloud tools or automations
What methodology do you work with, certificate or course as PO?
-.kanban, scrum, inbest, lean, agility and innovation courses.
How long are the Sprints? sprints planning, review and retrospective validate the sprint
 -. The development team is the one who does the planning sprints, they participate to validate that everything is based on the methodology.
How do you manage the Backlog? Estimate epic tasks, delivery route,
-. He prioritizes the Backlog, 01 week
Creation of user stories?
-. He creates User Stories from scratch
How do you manage the technical debt, what do you do to avoid it?
 -.He visualizes the technical debt
Comment on a project you worked on and how you did it? (Preferably linked to an ecomercer within a StartUp)
Company: Genomawork
Project: ATS Evaluations and Assessments
Project Goal: Redesign of all views.
Tasks and responsibilities: Manage the creation process, ideation until launch, database remodeling, managing the team, validating the sprint planning, managing and prioritizing the Backlog, as well as creating User Stories and visualizing the technical debt for its correction.
Technologies used: javascript, react, Figma, Jupiter.
Positively impact the churn reduction and NPS increase indicators of the product.
If you know about Churn and NPS, it is used by the commercial area.

The tools used by the candidate are: JIRA, Notion, Trello, Confluence, BaseCamp

--

'''