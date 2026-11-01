# Newo Platform Documentation

Nov 1, 2026 · @Inna Mezhlumyan

## Overview

The Newo platform runs AI receptionists and customer-service agents that answer calls, texts and chats for appointment-driven businesses such as restaurants, dental and medical practices, and home services. This guide explains how voice calls work, how billing works, how Newo keeps the platform reliable and secure, and how agents are built, connected to business systems and resold by partners.

Newo sells the platform directly and through a white-label partner program. Everything here describes the Newo platform as of November 2026, and details may change.

### What's in this guide

| Chapter | Read it if you want to know |
| --- | --- |
| Getting started | How to go from a new account to a live agent |
| Voice and telephony | How calls reach your agent, which numbers and countries are supported, and how to get good call quality |
| Billing | How units, plans, free units, invoices and failed payments work |
| Reliability, support and security | How to get help, how Newo handles incidents, and how your data is protected |
| Agents, integrations and partners | How agents are built, which business systems they connect to, and how the white-label program works |
| Frequently asked questions and glossary | Short answers and the terms used across the Newo platform |

## Getting started

Most businesses go from a new account to a live agent in under an hour: create the agent, check its setup, test it, then point your calls at it.

### Step by step

1. **Create your agent in Agent Creator.** Pick your business type and answer a few questions about your business. Newo builds an agent from SuperAgent, its standard agent, with your details filled in.
2. **Get a phone number.** In the United States, United Kingdom, Netherlands and Australia, a local number is assigned automatically when the agent is created. Elsewhere, request a number or connect your own phone system (see Voice and telephony).
3. **Work through the setup checklist.** The Speed Dial checklist walks you through the settings that matter most, such as hours, services, transfer numbers and the information the agent should collect.
4. **Connect your business systems.** If you take bookings or orders in another system, connect it so the agent can check availability and book for you (see Integrations).
5. **Test the agent.** Call your Newo number or start a web call, and try the conversations your customers usually have. Adjust the agent in the Customer Portal or by chatting with Vibe Mode.
6. **Go live.** Forward your business line to your Newo number, or publish the Newo number. Your agent now answers calls.
7. **Choose a plan.** New accounts start on Pay as you go with 50 free units. Pick a monthly plan if you expect steady call volume (see Billing).

### Before you go live

- [ ] Business hours, services and prices are correct
- [ ] The transfer number reaches a person who can help
- [ ] Booking or ordering system is connected and tested
- [ ] Report email and any webhooks are set
- [ ] A payment method is on file
- [ ] Call forwarding from your main number is turned on

### Your first week

Check your call history and reports in the Customer Portal every day for the first week. Look for calls where the agent transferred, could not answer, or did not finish a booking. Each one shows a setting or an instruction to improve. Small changes, such as adding a common question or clarifying a service name, usually make the biggest difference.

## Voice and telephony

Every voice call reaches a Newo agent through a carrier or web connection and is handled by Newo's Voice Service, which listens to the caller, runs the agent's reasoning and speaks the reply in real time.

&#91;embedded content: voice call path · carriers, provider services, Voice Service\]

Each kind of connection has its own provider service, and all of them stream audio to Voice Service. Voice Service then works with AI speech models and the agent's logic on the Newo platform.

### How a call is handled

- **Listening and replying.** Voice Service turns the caller's speech into text, runs the agent's turn, and turns the reply into speech. It also supports speech-to-speech models, which hear and answer in one step.
- **Turn-taking.** Noise cancellation and turn detection help the agent tell when the caller has finished speaking, so it neither interrupts nor waits too long.
- **Voice settings.** Each agent has a voice connector that holds its speech recognition, voice and speech-to-speech settings.
- **Backup providers.** If an AI speech provider has an outage, Newo can switch affected agents to a backup provider.

### Ways callers connect

| Connection | What it is for |
| --- | --- |
| Newo phone numbers | Local numbers that Newo provides and connects to your agent |
| Bring your own SIP | Connect an existing carrier or phone system to your agent over SIP, using UDP or TCP |
| Web calls | Callers talk to the agent from a browser, with no phone needed |
| WebSocket audio | Contact-center and voice platforms stream call audio to a Newo agent |

### Call features

- **Inbound calls** are answered by the agent on any connected number.
- **Outbound calls** let the agent place calls, within limits on how often, how many at once and how long. Outbound calling is turned on after a qualifying prepaid purchase.
- **Call transfer** hands the caller to a person or another number when the agent escalates.
- **SMS** lets the agent send texts such as booking confirmations, alongside voice.

### Phone numbers by country

| Region | How numbers are provided |
| --- | --- |
| United States, United Kingdom, Netherlands, Australia | Assigned automatically when you create an agent |
| Other countries in Europe, the Middle East and Africa | On request; local regulations require documents |
| Asia-Pacific and the Middle East | Limited; some countries require a local business presence |

Moving an existing number to Newo (porting) is available case by case. Many businesses instead keep their number and forward calls to their Newo number.

### Data privacy for calls

Where a speech provider supports it, Newo instructs the provider not to use customer call audio to train its models.

### Two ways the agent can speak

Voice Service can run an agent in one of two modes, set in the agent's voice connector.

|  | Classic pipeline | Speech-to-speech |
| --- | --- | --- |
| How it works | Speech is turned into text, the agent replies in text, and the reply is turned into speech | One model hears the caller and answers in speech directly |
| Strengths | Predictable behavior, wide choice of voices, precise control of wording | Natural, expressive conversation |
| Good fit | Bookings, orders and conversations where exact details matter | Open conversations where tone matters most |

Both modes use the same agent logic, integrations and reports, so you can change mode without rebuilding the agent.

### Languages

Agents can talk with callers in more than one language and can switch when a caller changes language. Fixed phrases, such as confirmations and transfer messages, are translated into the caller's language. To get the best results, enable only the languages your callers actually use, and test each one before going live.

### Outbound calls

Agents can place calls as well as answer them, for example to confirm appointments, follow up on missed calls or run a call campaign. To protect callers and phone numbers, each agent has limits on how often it calls, how many calls it makes at once and how long each call can last. Outbound calling is turned on after a qualifying prepaid purchase. Contact Newo if your use case needs different limits.

### Transferring callers

You decide when the agent hands a caller to a person, for example when the caller asks for one, has an emergency, or needs something the agent cannot do. Set a transfer number that is staffed during the hours the agent may transfer. If no one is available, have the agent take a message instead so the caller is not left waiting.

### Bring your own SIP

If you already have a carrier or a phone system, you can connect it to your Newo agent over SIP instead of using a Newo number. Newo supports both UDP and TCP transport. TCP is the safer choice when your carrier sends large SIP messages, which UDP can split in transit. Your carrier or phone-system administrator will need your agent's SIP connection details from Newo.

### Getting the best call quality

- **Expect a difference between phone and web.** Phone networks carry less audio detail than web calls, so speech recognition is usually more accurate on web calls. Test on a real phone line before going live.
- **Reduce background noise.** Busy kitchens, traffic and speakerphones make it harder for any speech system to hear the caller. Noise cancellation helps, but a quieter line always helps more.
- **Keep prompts short.** Short agent replies leave natural gaps for the caller to speak and make interruptions less likely.
- **Watch for long pauses.** If callers often wait in silence, check the agent's voice settings and any slow business-system connections, and tell Newo support.

## Billing

Newo bills by usage, measured in units. Every conversation your agent handles uses units, and your plan sets how many units are included and how extra usage is charged. Card payments are processed by Stripe.

### Plans

Every new account has a plan. If you do not choose one or add a payment method, your account starts on Pay as you go.

| Plan | How it works |
| --- | --- |
| Pay as you go (PAYG) | No included units. Usage is charged to your card in blocks of 50 units, and any remainder is charged at the end of the billing cycle. |
| AI Receptionist | A monthly plan with a set number of included units. Unused units expire at renewal. Usage beyond the included units is charged at the end of the cycle. |
| Enterprise | Custom terms agreed with Newo. |
| Partner plans | Customers of a white-label partner are billed under that partner's plans, either by Newo or by the partner. |

### Free units

Each new Pay as you go account gets 50 free units, once:

1. You get a notice when you have used 25 free units.
2. Your card is first charged when you reach unit 51.
3. If that first charge fails, the agent pauses straight away. Newo retries the card for 7 days, then archives the agent and releases its phone number.

Accounts moving from an older pricing model do not get free units.

### Invoices and renewals

Every charge creates an invoice, which is emailed to you. Monthly plans renew on the same day each month and are paid in advance. On those plans, the renewal invoice combines the new month's fee with any extra usage from the month before.

### If a payment fails

After a failed plan or usage payment, your agent keeps working on a limited basis while Newo retries the card:

1. **Days 1–3:** the agent is limited to 10 units a day. Newo retries the payment daily and emails you.
2. **Day 4:** the agent is paused.
3. **Day 7:** the agent is deleted.

Service comes back automatically once unpaid invoices are paid and a valid payment method is on file.

### Managing billing

The Billing page in the Customer Portal shows your status, a unit-usage chart, plan checkout, payment history and payment details. From there you can also add or change payment methods.

Newo sends billing notices by email and as banners in the Portal. These include:

- Card expiring or payment method invalid
- Extra usage started
- Payment failed
- Agent paused, and agent restored

### Billing for partners

White-label partners choose whether Newo bills their customers or they bill customers themselves. Partners can also set quotas for each customer: hard limits that stop usage, soft limits that warn, and limits per agent.

### Choosing a plan

- **Pay as you go** suits new agents, seasonal businesses and low call volume. You pay only for the units the agent uses.
- **AI Receptionist** suits businesses with steady call volume. Included units come with each renewal, which makes monthly costs predictable. Choose an allowance close to your usual month, since unused units do not carry over.
- **Enterprise** suits multi-location businesses and custom needs, such as special terms or integrations. Contact Newo sales.

You can see how many units your agent uses each day on the Billing page, which helps you pick the right plan after your first few weeks.

### Agent status and billing

Your agent's status reflects your billing state. The Customer Portal shows the current status.

| Status | What it means | What the agent does |
| --- | --- | --- |
| Active | Billing is up to date | Answers calls and messages as normal |
| Limited | A payment failed in the last 3 days | Works, but only up to 10 units a day |
| Paused | A payment is still unpaid after 3 days, or a first Pay as you go charge failed | Stops answering until payment is made |
| Deleted or archived | Payment was not made within the grace period | Removed; its phone number may be released |

Paying the overdue invoice and keeping a valid card on file returns a Limited or Paused agent to Active automatically. Once an agent is deleted or archived, contact Newo support.

### Avoiding billing interruptions

- Keep a valid card on file and update it before it expires. Newo emails you when a card is about to expire.
- Add a billing email that someone checks, so payment notices are not missed.
- Watch the extra-usage notice: it tells you when the agent has used up its included units.
- If you expect a busy period, such as a holiday season, consider a larger plan for those months.

## Reliability, support and security

Newo watches agents in production around the clock, runs a 24/7 on-call rotation for incidents, and operates an ISO/IEC 27001 information security program.

### Getting help with an agent

Report a problem with your agent to Newo support or to your partner. Newo's customer quality and engineering teams review each report, confirm the problem and rank it by severity before it is fixed. A report is resolved fastest when it includes:

- What the agent did, and what you expected it to do
- The session ID or call time, so the team can find the conversation
- How often it happens, and an example if you have one

Newo tracks each agent's health in four areas: conversation quality, business results, reliability, and operational signals such as errors.

### Common problems and what to check

| Problem | What to check first |
| --- | --- |
| Bookings fail or show the wrong times | The connection to your booking or calendar system, and the hours and services set up there |
| Reports or webhooks do not arrive | The report email address and the webhook URL in your agent's settings |
| The agent answers in the wrong language | The languages enabled for the agent, and whether callers switch language mid-call |
| Calls are not transferred | The transfer number and the rules for when the agent should escalate |
| Texts are not delivered | That SMS is enabled on the number, and that the recipient's country is supported |
| Long pauses or the agent talks over callers | Background noise on the line, and the agent's voice settings |

### Incident response

When something goes wrong on the platform, Newo follows a defined incident process:

1. Automated monitoring and alerting watch the platform and agents' calls.
2. A 24/7 on-call rotation, with primary and secondary responders, takes the alert.
3. An incident manager leads a response team drawn from platform, infrastructure and agent engineering.
4. If a third-party provider has an outage, Newo can move traffic to a backup provider.
5. After serious incidents, the team holds a blameless review and follows up on the fixes.

If an incident involves personal data, Newo notifies affected customers within the time limits set by GDPR and HIPAA.

### Infrastructure

The Newo platform runs on Google Cloud, with regions in the United States and the European Union. Services scale automatically with call volume. Newo regularly load-tests the platform to raise how many calls it can handle at once.

### Security and compliance

- **ISO/IEC 27001.** Newo runs an information security program based on ISO/IEC 27001, with recurring controls and regular audits.
- **Access control.** Access to production systems follows least privilege and is reviewed every quarter.
- **Vulnerability management.** Code and dependencies are scanned automatically, and findings are tracked until they are fixed.
- **Security monitoring.** Security and audit events are monitored centrally.
- **Reporting a vulnerability.** If you think you have found a security issue in the Newo platform, report it to Newo support. Reports are handled under a defined disclosure process.

### How your data is protected

- **Where data lives.** You can run on the platform's US or EU region. Partners can host their branded platform in either region.
- **Speech data.** Where a speech provider supports it, Newo tells the provider not to use your call audio to train its models.
- **Payment data.** Card details are entered and stored with Stripe, Newo's payment processor.
- **Access.** Newo staff access production systems only as their role requires, and that access is reviewed every quarter.

### Your part in keeping agents safe

Security is shared between Newo and the businesses that use the platform:

- **Manage who has access.** Give Customer Portal and Builder access only to people who need it, and remove it when they leave.
- **Protect integration credentials.** Keys and passwords for connected systems are entered in your agent's settings. Never share them in email, chat or support tickets.
- **Check transfer and outbound numbers.** Make sure transfer and outbound numbers belong to you or people you trust.
- **Tell callers they are speaking with AI.** Many places require callers to be told they are talking to an AI system. Check the rules where your callers are, and include a clear statement in the agent's greeting.
- **Review conversations.** Check call history regularly and report anything unexpected to Newo support.

### Writing a good problem report

A clear report is the fastest way to a fix. A useful report looks like this:

| Field | Example |
| --- | --- |
| Summary | Agent offers appointment times on the wrong day |
| Expected | Agent offers times for the day the caller asked for |
| Actual | Agent offered times for the next day |
| When | Session ID, or the call's date, time and caller number |
| How often | 3 of 20 booking calls since Monday |
| Evidence | Call recording or transcript excerpt |

Newo ranks each report by severity, from critical (the agent cannot take calls) to low (a small wording issue), and handles the most severe first.

## Agents, integrations and partners

Agents on the Newo platform are built from flows and skills, set up through Newo's builder tools or by chatting with Vibe Mode, and connected to booking, ordering and CRM systems through integrations. White-label partners can resell the whole platform under their own brand.

### How agents are built

Each agent belongs to a project. A project holds the agent's flows, skills, event triggers, stored information and settings. Most businesses start from SuperAgent, Newo's standard agent, which comes ready for common jobs such as answering questions, booking appointments and taking orders.

| Tool | Who uses it | What it does |
| --- | --- | --- |
| Agent Creator | Business owners and partners | Creates a new agent in a few steps |
| Customer Portal | Business owners | Settings, billing, call history and reports |
| Vibe Mode | Business owners | Set up and change your agent by chatting with it in the Portal |
| Builder | Technical teams | Full control over flows, skills and settings |
| Partner Portal | White-label partners | Manage customers, products and quotas |

**Vibe Mode** lets you change your agent's settings and instructions by describing what you want in plain language. It can also set up an integration: it installs the integration, fills in what it can work out, and asks you for the rest.

### Building blocks

| Term | What it is |
| --- | --- |
| Project | The container for an agent and everything it needs |
| Agent | The AI receptionist or assistant that talks with your customers |
| Flow | A conversation path, such as booking an appointment or taking an order |
| Skill | A single action the agent can take, such as checking availability or sending a text |
| Attributes | Your business details the agent uses, such as hours, services and transfer numbers |
| Event triggers | Rules that start a flow when something happens, such as a call ending |
| Integration module | A packaged connection to a business system, installed into a project |

### Changing your agent with Vibe Mode

In Vibe Mode you describe a change in plain words, and the agent updates its own settings. For example:

- "We're closed on public holidays. Tell callers to call back the next working day."
- "If someone asks about emergency appointments, transfer them to the front desk."
- "Connect our booking system." Vibe Mode then asks for the details it needs.

Check each change with a test call before relying on it.

### Testing and activation

After you create an agent, a setup checklist (Speed Dial) walks you through refining it, testing it and going live, typically in under an hour. Newo also scores agent conversations automatically to catch problems before and after launch.

### Call history, reports and analysis

After every conversation, the Newo platform analyzes the call and records the outcome. You can use that information in three ways:

- **Call history** in the Customer Portal shows each conversation with its transcript and outcome.
- **Reports** are sent by email after conversations, so your team knows about bookings, messages and requests without logging in.
- **Webhooks** send conversation results to your own systems, such as a CRM or a spreadsheet tool, as soon as a conversation ends.

Large accounts can export account reports for analysis. For very large date ranges, export in smaller periods.

### Integrations

Integrations connect your agent to the systems your business already uses, so it can check availability, book, take orders and update records during a call. Some integrations turn on automatically. Others are installed into your agent's project from Builder or through Vibe Mode.

| Business type | Systems with Newo integrations |
| --- | --- |
| Restaurants | Deliverect; Toast, Square and Clover through POSHub; Tableo table booking |
| Dental practices | Cloud9 (Planet DDS); Denticon |
| CRM and marketing | GoHighLevel (GHL) Marketplace; Kommo |

Customers also connect calendars, scheduling tools and CRMs through webhooks and automation platforms. Ask Newo or your partner about a system that is not listed.

### What each integration does

| Integration | What the agent can do |
| --- | --- |
| Deliverect | Create orders in your ordering setup |
| POSHub (Toast, Square, Clover and others) | Sync your menu, create and cancel orders, and track order status |
| Tableo | Book tables and send the caller a booking link by text |
| Cloud9 (Planet DDS) | Check availability, book and cancel dental appointments |
| Denticon | Work with appointments in your dental practice system |
| GoHighLevel (GHL) | Connect the agent to GHL from the GHL Marketplace |
| Kommo | Connect the agent to your Kommo CRM |

### Setting up an integration

1. Make sure you have an administrator login for the business system you want to connect.
2. In Vibe Mode, ask the agent to connect the system, or install the integration from Builder.
3. Enter the connection details the integration asks for, such as an account ID or an access key.
4. Check that the agent's services and locations match the ones in your business system.
5. Make a test call and complete a real booking or order, then cancel it in the business system.

If availability in the agent does not match your business system, first check opening hours, staff schedules and service lengths in that system.

### White-label partner program

A white-label partner gets its own branded Agent Creator and Customer Portal on its own domains, with no visible Newo branding. The partner manages its customers from the Partner Portal, sets its own products and quotas, and chooses whether Newo or the partner bills customers.

Onboarding a new partner follows these steps:

1. The partner signs an agreement with Newo.
2. The partner completes an onboarding survey with its domains, brand assets and support contact.
3. Newo sets up the branded platform, including the partner's domains and email.
4. Newo creates a test agent and hands the platform to the partner for testing.
5. The platform is marked as launched about one week after testing begins, and Newo follows up with the partner over the first weeks.

Newo can host partner platforms in either the United States or the European Union.

### What partners control

| Area | What the partner can do |
| --- | --- |
| Branding | Own domains, logo, colors and support email on the customer-facing apps |
| Customers | Create and manage customer accounts from the Partner Portal |
| Products | Define their own products and what each includes |
| Quotas | Set hard limits, soft limits with warnings, and per-agent limits for each customer |
| Billing | Choose whether Newo or the partner bills customers |
| Hosting region | Run the branded platform in the US or the EU |

Newo runs automated tests across partner platforms to catch problems before they reach partners' customers. Partners have a dedicated account manager at Newo for onboarding and ongoing support.

## Frequently asked questions

### Getting started

**How long does it take to set up an agent?** Most businesses create, test and launch an agent in under an hour using Agent Creator and the setup checklist.

**Do I need a new phone number?** No. You can keep your existing number and forward calls to your Newo number, or connect your own phone system over SIP.

**Can the agent answer texts and chats as well as calls?** Yes. The Newo platform handles phone calls, SMS, web chat and messaging.

### Calls

**What happens if the agent can't help a caller?** It transfers the caller to the number you set, or takes a message if no one is available.

**Can the agent speak more than one language?** Yes. Agents can talk in more than one language and switch when the caller does. Test each language you enable.

**Why does the agent sound clearer on web calls than on phone calls?** Phone networks carry less audio detail than web calls. Test your agent on a real phone line, and reduce background noise where you can.

**Can the agent make outbound calls?** Yes, within limits per agent. Outbound calling is turned on after a qualifying prepaid purchase.

### Billing

**What is a unit?** Units measure how much your agent is used. Each conversation uses units, and the Billing page shows your daily usage.

**Do I get free units?** New Pay as you go accounts get 50 free units, once.

**Do unused units roll over?** No. Included units on monthly plans expire at each renewal.

**What happens if my card fails?** The agent is limited to 10 units a day for 3 days while Newo retries the card, paused on day 4, and deleted on day 7. Paying the invoice restores the agent automatically while it is limited or paused.

### Data and security

**Where is my data stored?** On Google Cloud, in the US or the EU region.

**Is my call audio used to train AI models?** Where a speech provider supports it, Newo tells the provider not to use customer audio for model training.

**How do I report a security issue?** Contact Newo support. Security reports are handled under a defined disclosure process.

## Glossary

| Term | Meaning |
| --- | --- |
| Agent | An AI receptionist or assistant that talks with your customers on the Newo platform |
| Agent Creator | The tool for creating a new agent in a few steps |
| Builder | Newo's full editor for flows, skills and settings |
| Customer Portal | Where businesses manage agent settings, billing, call history and reports |
| DTMF | Touch-tone keypad input during a call |
| Flow | A conversation path the agent follows |
| Integration | A connection between the agent and a business system |
| PAYG | Pay as you go: a plan billed only for usage |
| Partner Portal | Where white-label partners manage customers, products and quotas |
| Quota | A usage limit a partner sets for a customer or agent |
| SIP | The standard protocol phone systems use to connect calls over the internet |
| Skill | A single action an agent can take |
| Speech-to-speech | A model that hears the caller and answers in speech directly |
| Speed Dial | The setup checklist that takes a new agent to launch |
| SuperAgent | Newo's standard, ready-made agent |
| Unit | The measure of agent usage that billing is based on |
| Vibe Mode | Setting up and changing an agent by chatting with it |
| Voice connector | An agent's voice settings: speech recognition, voice and mode |
| Webhook | An automatic message the Newo platform sends to your system when something happens |
| White-label | Reselling the Newo platform under a partner's own brand |

## About this guide

This guide describes the Newo platform as of 1 November 2026. Plans, limits, supported countries and integrations change over time. Contact Newo or your partner before relying on a detail for a contract or a launch date.
