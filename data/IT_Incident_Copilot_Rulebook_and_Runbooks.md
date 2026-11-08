# IT Incident Copilot — Rulebook and Runbook Corpus

> **Status:** Synthetic educational corpus. These are not verified company procedures. A qualified service owner must adapt, review, and approve every procedure before operational use.

## 1. Purpose and scope
This rulebook defines safe triage and knowledge-use rules for an IT Incident Copilot RAG portfolio project. Runbooks offer example decision paths; historical tickets (if included separately) show what happened in past cases and must not be treated as universal instructions.

## 2. Authority and evidence hierarchy
1. Current approved policy, runbook, change record, and service-owner instruction take precedence over historical tickets.
2. A ticket marked “Resolved” is not proof that its fix is safe or generally applicable.
3. If sources conflict, surface the conflict and defer to the current approved source; do not silently combine instructions.
4. Separate confirmed facts, hypotheses, and recommended checks. State unknowns explicitly.
5. Cite source IDs and section names for recommendations. Never fabricate citations or claim a source says something it does not.
6. If no approved guidance exists for a high-risk action, stop and escalate rather than inventing a procedure.

## 3. Standard incident workflow
1. Establish scope: one user/device, team/site, one service, or multiple services.
2. Capture business impact, start time with timezone, environment, exact sanitized error, and recent changes.
3. Check service health and active incident/change notices.
4. Prefer read-only, reversible diagnostics before changes.
5. Test a small number of hypotheses with checks that distinguish among them.
6. Change production only with evidence, authorization, an owner, monitoring plan, and rollback trigger.
7. Verify the original user workflow and check for side effects.
8. Record evidence, actions, approvals, result, rollback status, and follow-up owner.

## 4. Security and safety rules
- Never request or store passwords, MFA codes, recovery codes, API keys, tokens, private keys, or full connection strings.
- Never recommend disabling MFA, EDR/antivirus, logging, backups, monitoring, or firewalls as a shortcut.
- Never recommend broad permissions, broad firewall openings, guessed production changes, destructive database operations, or deleting recovery points.
- Use least privilege and approved change control; privileged actions require the responsible owner or incident commander.
- Minimize personal data. Sanitize logs, URLs, headers, request IDs, and screenshots before sharing.
- Suspected compromise, phishing, password spraying, data exposure, or malicious activity must follow security incident response.
- Stop and escalate if an action could cause data loss, downtime, privilege escalation, or weaken a security boundary.

## 5. Priority and escalation
Use the organization's official severity matrix if available; do not invent contractual SLAs. If no matrix is provided, describe impact and urgency. Illustrative categories: **Critical**—broad outage, critical workflow unavailable, material security incident, imminent data/recovery risk; **High**—multiple users or important service materially impaired; **Medium**—limited scope with workaround and no security/data risk; **Low**—minor inconvenience. Align these examples with local policy before operational use.

Escalate immediately for suspected compromise, sensitive-data exposure, risk of data loss, uncontrolled production impact, privileged-account issues, no safe rollback, or ambiguous/outdated runbook instructions.

## 6. Change, rollback, verification
- Do not change production based only on semantic similarity to a historical ticket.
- Before a change, identify target, expected effect, risk, owner, approval, monitoring, and rollback trigger.
- Temporary mitigations need an owner and expiry/review time.
- Roll back if impact worsens, unexpected access appears, or verification fails.
- Do not declare resolution until the requester/service owner or approved health check confirms recovery.

## 7. RAG ingestion rules
- Keep `source_type=ticket` and `source_type=runbook` distinct.
- Ticket metadata: ticket ID, category/subcategory, priority, resolution date if available, related runbook ID, and synthetic/real provenance.
- Runbook metadata: runbook ID, category/subcategory, section heading, version, status, approval state, and owner if known.
- Use section-aware runbook chunking; repeat runbook ID and section heading in every chunk.
- Keep cautions, prerequisites, verification, rollback, and escalation connected to the procedure they govern.
- Deduplicate near-identical documents, preserve provenance, and never ingest secrets or unapproved internal data.
- Label synthetic material as synthetic. Never present generated tickets as real production evidence.

## 8. Retrieval and answer policy
Retrieve current approved runbook guidance first, then similar tickets as historical context. Filter by environment/service/version/approval metadata when possible. Responses should include: **Assessment** (facts vs hypothesis), **Evidence** (source IDs and sections), **Safe checks**, **Recommended next step** (with authorization/risk), **Verification**, **Escalate if**, and **Unknowns**. Ask a clarifying question when scope, environment, or authorization changes the advice. Use qualitative confidence and explain missing evidence rather than inventing a numeric score.

## 9. Evaluation gates
Before claiming reliability, test held-out queries for retrieval recall@k, correct runbook/section retrieval, citation correctness, distinction between historical evidence and procedure, safety, abstention on missing/conflicting evidence, robustness to vague/misspelled reports, latency, and cost. Keep a gold set of expected source IDs and safe answer elements; do not tune and test on the same exact queries.

## 10. Runbook lifecycle
Every operational runbook should have an owner, approver, version, last-reviewed date, review cadence, environment scope, dependencies, and change history. Retire outdated versions from default retrieval while preserving audit history. These examples are explicitly marked draft.

## 11. Standard evidence checklist
- Impact/scope and affected business workflow
- Start time and timezone; first observed time
- Sanitized error, correlation/request IDs, and diagnostic results
- Relevant deployment/change/incident IDs
- Actions taken, approvals, and before/after state
- Verification results, rollback status, follow-up owner, and review date

## 12. Corpus inventory
This bundle contains 22 synthetic runbooks spanning network, identity, endpoint, messaging, application, database, security, platform, backup, storage, workplace technology, and cloud platform scenarios.


---

# RUN-NET-003: VPN Authentication Failures

Category: Network / VPN

Purpose: Restore approved remote access while separating credential, MFA, client, and service-side failures.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with vpn authentication failures.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Record exact error, timestamp, client version, network type, and scope.
2. Check VPN and identity-provider service health and known changes.
3. Review approved sign-in logs for account status, MFA outcome, policy result, and correlation ID.
4. Check device time, supported client version, and captive portal/restricted-network conditions.
5. Perform one controlled retry after correcting an evidenced client-side issue; escalate gateway or identity-policy faults.

## Verification
- VPN connects and approved internal resources are reachable.
- No repeated authentication failures remain.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Multiple users/sites affected; suspected certificate or identity-provider outage.

## Safety cautions
- Never disable MFA or collect passwords, recovery codes, or one-time codes.

## Related runbooks
- RUN-IAM-004
- RUN-IAM-008
- RUN-NET-007

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-NET-007: Internal DNS Resolution Failures

Category: Network / DNS

Purpose: Diagnose name resolution without unapproved DNS changes.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with internal dns resolution failures.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Determine scope: hostname, device, subnet, VPN users, or broad outage.
2. Query the approved resolver and record response, TTL, and timestamp.
3. Compare with a known-good internal name and a second approved resolver if authorized.
4. Check client/VPN DNS settings, DNS service health, zone history, and resolver logs.
5. Change records only through approved change control and record the previous value.

## Verification
- Name resolves to the expected approved address.
- Application works by hostname and resolver errors stop.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Core names fail broadly; suspected unauthorized DNS change; zone replication/DNSSEC issue.

## Safety cautions
- Do not publish internal DNS details or guess replacement IP addresses.

## Related runbooks
- RUN-NET-003
- RUN-NET-011

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-NET-011: Routing or Firewall Reachability

Category: Network / Connectivity

Purpose: Separate routing, filtering, endpoint, and listener causes.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with routing or firewall reachability.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Validate source, destination, port/protocol, owner, and expected path.
2. Run authorized connectivity checks and record timeout versus refusal.
3. Compare affected and unaffected network segments where possible.
4. Review route, firewall, ACL, and flow logs alongside recent change records.
5. Submit a narrowly scoped, owner-approved change with justification and expiry where appropriate.

## Verification
- Only the required path is reachable.
- Monitoring and application checks pass without broader access.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Production-wide impact, unexpected broad access, route instability, or suspected boundary bypass.

## Safety cautions
- Never disable a firewall globally or create broad any-any rules.

## Related runbooks
- RUN-NET-007
- RUN-APP-009

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-IAM-004: Repeated Account Lockouts

Category: Identity / Account lockout

Purpose: Find the source of repeated lockouts without weakening account protection.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with repeated account lockouts.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Verify identity through the approved support process.
2. Review identity audit logs for timestamps, source device/IP, application, and failure reason.
3. Determine whether attempts come from cached credentials, mobile clients, scheduled tasks, or interactive sign-ins.
4. Coordinate credential updates with service owners for dependent services.
5. Perform one controlled sign-in test and monitor for recurrence.

## Verification
- Account remains unlocked through the observation window.
- The identified failure source stops and normal sign-in works.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Multiple accounts affected, unknown source, suspicious sign-ins, or privileged/service account involved.

## Safety cautions
- Do not lower lockout thresholds or request passwords.

## Related runbooks
- RUN-IAM-008
- RUN-SEC-009

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-IAM-008: Repeated MFA Prompts

Category: Identity / MFA

Purpose: Resolve repeated MFA challenges while preserving strong authentication.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with repeated mfa prompts.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Ask whether prompts were initiated by the user; unsolicited prompts are a security signal.
2. Review sign-in logs for policy, device compliance, session expiry, and MFA results.
3. Check device clock, supported client, and approved browser/session settings.
4. Check identity service health and recent policy changes.
5. Use an approved fresh-session procedure only when appropriate; escalate unexplained prompts to security.

## Verification
- Expected session remains active and policy-compliant.
- Unexplained prompts stop.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Unsolicited prompts, suspected compromise, or multiple users affected after a policy change.

## Safety cautions
- Never disable MFA or advise approving prompts the user did not initiate.

## Related runbooks
- RUN-IAM-004
- RUN-SEC-009

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-END-005: High CPU or Slow Endpoint Performance

Category: Endpoint / Performance

Purpose: Identify resource pressure and safe remediation on a managed workstation.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with high cpu or slow endpoint performance.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Record start time, affected apps, recent changes, and user impact.
2. Use approved monitoring to inspect CPU, memory, disk, and top processes.
3. Check security alerts, update activity, disk capacity, and system events.
4. Compare processes with the approved software inventory; do not terminate unknown agents.
5. Collect approved diagnostics and route persistent pressure to endpoint engineering.

## Verification
- Resource use returns to expected range and user workflow is responsive.
- No security or management agent was disabled.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Repeated crashes, disk/memory errors, suspected malware, or fleet-wide impact.

## Safety cautions
- Do not disable EDR/antivirus or delete files/registry entries without approved procedure.

## Related runbooks
- RUN-PLT-004

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-END-014: External Monitor or Dock Not Detected

Category: Endpoint / Display and dock

Purpose: Restore display/dock operation through low-risk checks.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with external monitor or dock not detected.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Check monitor power/input, cable seating, dock power, and supported port.
2. Test one variable at a time with known-good approved cable/port if available.
3. Review OS display settings and approved driver/firmware versions.
4. Check managed update history and compatibility notices.
5. Escalate hardware faults with inventory identifiers and test results.

## Verification
- Display works at expected resolution and peripherals stay connected.
- No recurring disconnects appear.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Overheating, damaged connectors, repeated power faults, or fleet update impact.

## Safety cautions
- Do not open powered equipment or install drivers from untrusted sites.

## Related runbooks
- RUN-END-005

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-MSG-003: Outlook Authentication Prompts

Category: Messaging / Email client

Purpose: Diagnose recurring email-client authentication prompts.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with outlook authentication prompts.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Determine whether approved webmail works and capture exact error/time.
2. Review service health and identity sign-in logs.
3. Confirm client version, device compliance, account status, and license.
4. Correlate with password, policy, certificate, or client changes.
5. Use approved client repair/profile steps only after confirming mailbox data is server-synchronized.

## Verification
- Client authenticates and folders synchronize.
- Test message sends and receives without repeated prompts.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Service outage, apparent missing data, multiple users affected, or compromise indicators.

## Safety cautions
- Never request tokens/passwords or delete local data before verifying synchronization.

## Related runbooks
- RUN-IAM-008
- RUN-MSG-006

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-APP-004: HTTP 500 Application Errors

Category: Application / HTTP 500

Purpose: Triage server-side errors and identify failing dependencies.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with http 500 application errors.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Capture sanitized error, request ID, timestamp, endpoint, and scope.
2. Check error-rate dashboards, resource saturation, and dependency health.
3. Correlate onset with deployments, feature flags, configuration rotations, and infrastructure changes.
4. Inspect authorized logs/traces using request IDs; redact secrets and personal data.
5. If a recent change is implicated, follow approved rollback/feature-flag process and document findings.

## Verification
- Error rate returns to baseline and key user journeys pass.
- No continuing exception pattern is visible.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Critical outage, data integrity/security risk, no safe rollback, or errors persist after rollback.

## Safety cautions
- Do not expose stack traces/secrets to users or edit production data as a shortcut.

## Related runbooks
- RUN-APP-009
- RUN-APP-014
- RUN-DB-003

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-APP-009: HTTP 502 or 503 Gateway Errors

Category: Application / HTTP 502/503

Purpose: Determine whether gateway errors come from upstream health, routing, or capacity.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with http 502 or 503 gateway errors.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Check service health, synthetic checks, and change announcements.
2. Compare gateway errors with upstream health and request IDs.
3. Review target health, readiness, connection pools, capacity, and routing changes.
4. Check dependency outages and saturation before altering gateway settings.
5. Apply approved rollback or documented capacity mitigation and set a review time.

## Verification
- Gateway responses and upstream health recover.
- Latency/error rate return to service objectives.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- No healthy upstream, multi-region outage, cascading failure, or data risk.

## Safety cautions
- Avoid blind retry increases and never bypass gateway authorization.

## Related runbooks
- RUN-APP-004
- RUN-APP-014
- RUN-PLT-004

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-DB-003: Application Database Connection Timeouts

Category: Database / Connectivity and timeout

Purpose: Diagnose DB connectivity and saturation while protecting data integrity.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with application database connection timeouts.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Check database health, connection count, CPU, storage, and latency.
2. Correlate app errors with database and network telemetry.
3. Inspect pool saturation, long-running queries, and recent releases using approved read-only tools.
4. Verify secret/certificate rotation metadata without printing values.
5. Require DBA authorization for query cancellation, failover, restart, or parameter changes.

## Verification
- Connection errors return to baseline and representative transactions succeed.
- Database and replication indicators remain healthy.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Corruption risk, exhausted storage, replication lag, broad outage, or potential lost/duplicated transactions.

## Safety cautions
- Never run unreviewed writes, reset production DBs, or paste credentials/connection strings.

## Related runbooks
- RUN-APP-004
- RUN-APP-014
- RUN-DB-007

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-SEC-005: Suspected Phishing Email

Category: Security / Phishing

Purpose: Contain and investigate suspicious email through approved response processes.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with suspected phishing email.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Tell reporter not to click, open, reply, or forward outside approved reporting tooling.
2. Preserve original message and headers using the approved security workflow.
3. Security staff review sender authentication, links, attachment verdicts, and distribution.
4. Ask whether links were clicked, files opened, credentials submitted, or prompts approved.
5. Follow incident response for session revocation, credential reset, endpoint checks, and message containment as appropriate.

## Verification
- Message is dispositioned and affected users receive approved guidance.
- Possible exposure is contained and monitored.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Credentials submitted, malware executed, payment fraud, privileged target, or broad distribution.

## Safety cautions
- Do not test links on a normal workstation or share malicious files publicly.

## Related runbooks
- RUN-SEC-009
- RUN-IAM-008

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-PLT-004: Container Restarts and Memory Pressure

Category: Platform / Containers

Purpose: Triage restarts and memory pressure using observability and safe controls.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with container restarts and memory pressure.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Review events, restart counts, exit reasons, memory/CPU metrics, and deployment history.
2. Compare memory usage to requests/limits and assess traffic/input changes.
3. Inspect sanitized logs and check node pressure and neighboring workloads.
4. If a release is implicated, use approved rollback or documented resource adjustment.
5. Validate probes against realistic startup behavior; monitor workload and node health.

## Verification
- Restart rate stabilizes and workload serves test requests.
- Cluster/namespace capacity remains within policy.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Cluster-wide pressure, critical workload instability, or no safe capacity.

## Safety cautions
- Do not delete persistent volumes, restart all workloads indiscriminately, or expose cluster secrets.

## Related runbooks
- RUN-APP-009
- RUN-CLD-009

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-BKP-006: Slow or Failed Backup Jobs

Category: Backup and Recovery / Backup

Purpose: Investigate backup failure while preserving known-good recovery points.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with slow or failed backup jobs.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Check job status, error, duration, asset health, repository capacity, and recent changes.
2. Determine whether failures share proxy, storage, network, or credential dependencies.
3. Review throughput, snapshot/provider health, repository state, and maintenance notices.
4. Verify credential status via metadata only.
5. Retry only if policy allows and cause is understood; notify asset owner of missed recovery points.

## Verification
- Successful backup is recorded and repository/retention remain compliant.
- Restore-test evidence meets policy.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Critical asset has no valid recovery point, multiple failures, retention risk, or suspected ransomware.

## Safety cautions
- Do not delete recovery points to free space without retention-owner approval; a green job is not proof of restoreability.

## Related runbooks
- RUN-DB-007
- RUN-SEC-005

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-STO-003: Network File Share Access

Category: Storage / File share

Purpose: Resolve share access/availability while maintaining least privilege.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with network file share access.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Determine whether issue is DNS, connectivity, authentication, authorization, or server health.
2. Check whether other authorized users can access the same path.
3. Review effective permissions and group membership with approved tools.
4. Check recent ACL, group, capacity, and server changes with resource owner.
5. Request the smallest approved entitlement change and verify access.

## Verification
- User accesses only the intended files and share.
- Permissions match approved group membership.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Sensitive-data exposure, suspected unauthorized access, corruption, or widespread outage.

## Safety cautions
- Never grant Everyone-like access or copy sensitive files to personal storage.

## Related runbooks
- RUN-IAM-015
- RUN-NET-007

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-WKS-002: Printer Offline or Queue Failures

Category: Workplace Technology / Printing

Purpose: Restore managed printing with low-risk checks and controlled queue administration.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with printer offline or queue failures.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Determine scope across users and a test workstation.
2. Check power, printer status, network, consumables, and service notices.
3. Verify managed queue and supported driver.
4. Review queue/server logs for stuck jobs, driver faults, and connectivity.
5. Cancel only confirmed affected jobs; shared-queue clearing requires owner approval.

## Verification
- Harmless test page prints and queue returns to normal.
- Sensitive output is collected or disposed of securely.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Multiple departments affected, hardware fault, or confidential print exposure.

## Safety cautions
- Do not use confidential documents as tests or restart shared services without approval.

## Related runbooks
- RUN-NET-011

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-IAM-015: Missing Application Access

Category: Identity / Authorization

Purpose: Resolve application access through entitlement, licensing, and approval checks.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with missing application access.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Distinguish authentication failure from authorization failure.
2. Check application assignment, license, group membership, role mapping, and provisioning state.
3. Confirm the requested role is approved for the job function and data scope.
4. Check recent governance or app configuration changes.
5. Apply minimum approved entitlement through the source-of-truth access process.

## Verification
- Required function works and effective permissions match approval.
- Access grant is auditable.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Unapproved privileged request, sensitive-data exposure risk, or broad provisioning failure.

## Safety cautions
- Do not grant administrator rights or bypass approval/separation-of-duties controls.

## Related runbooks
- RUN-IAM-004
- RUN-STO-003

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-CLD-009: Kubernetes Pods Cannot Be Scheduled

Category: Cloud Platform / Kubernetes scheduling

Purpose: Diagnose pending pods using scheduler events and policy/capacity evidence.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with kubernetes pods cannot be scheduled.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Inspect pod events for the specific unsatisfied constraint.
2. Check allocatable capacity, requests, taints/tolerations, affinity, quota, and volume binding.
3. Compare workload spec with approved deployment configuration.
4. Check node pool/autoscaler, storage class, and admission policy health.
5. Correct evidenced constraints or restore eligible capacity only through approved change control.

## Verification
- Pods schedule and become Ready.
- No unrelated workload is displaced or left pending.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Capacity exhaustion across teams, policy conflict, unbound stateful volume, or production outage.

## Safety cautions
- Do not remove security constraints broadly or delete persistent volumes.

## Related runbooks
- RUN-PLT-004
- RUN-APP-009

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-SEC-009: Suspected Password Spraying

Category: Security / Credential attack

Purpose: Triage repeated authentication failures across accounts with security-led containment.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with suspected password spraying.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Review identity detections for patterns across users, apps, locations, and timestamps.
2. Look for successful sign-ins after failures and assess account privilege and session activity.
3. Correlate source indicators with approved threat intelligence and network telemetry.
4. Notify security response; avoid independent broad blocking without authorization.
5. Security responders apply targeted controls under incident plan and monitor recurrence.

## Verification
- Indicators are contained and affected accounts reviewed.
- Suspicious successful sessions are addressed.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Suspicious successful login, privileged target, data exposure, or persistent campaign.

## Safety cautions
- Do not weaken authentication or publish raw personal/account data outside approved channels.

## Related runbooks
- RUN-IAM-004
- RUN-IAM-008
- RUN-SEC-005

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-MSG-006: Shared Mailbox Access and Synchronization

Category: Messaging / Shared mailbox

Purpose: Resolve shared mailbox permission or synchronization issues.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with shared mailbox access and synchronization.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Check messaging service health and approved web-client access.
2. Verify Full Access, Send As, or Send on Behalf matches the approved request.
3. Check permission propagation and audit logs.
4. Separate server-side permission issues from client cache/automapping behavior.
5. Use approved client refresh/re-add procedure and test with a non-sensitive message.

## Verification
- Mailbox folders synchronize and only approved capabilities work.
- Audit trail matches intended access.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Unauthorized mailbox access, sensitive exposure, or broad messaging outage.

## Safety cautions
- Do not grant Full Access when narrower permission suffices; do not test with confidential content.

## Related runbooks
- RUN-MSG-003
- RUN-IAM-015

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-APP-014: Slow Business Application Responses

Category: Application / Latency

Purpose: Identify whether slowness originates in client, service, dependency, or capacity.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with slow business application responses.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Quantify latency against service objective and determine scope by workflow, region, and endpoint.
2. Compare frontend, application, database, network, and dependency telemetry for the same window.
3. Check releases, traffic, queue depth, and resource saturation.
4. Use traces/request IDs to locate slow segment while redacting secrets and personal data.
5. Apply only evidence-based approved mitigation and assign monitoring/follow-up owner.

## Verification
- Latency returns within objective and key transactions pass.
- Mitigation does not overload downstream services.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Critical workflow breaches objective, dependency saturation threatens other services, or impact grows.

## Safety cautions
- Do not blindly increase timeouts/retries or cache sensitive data without review.

## Related runbooks
- RUN-APP-004
- RUN-APP-009
- RUN-DB-003

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner

---

# RUN-DB-007: Database Storage Capacity Alerts

Category: Database / Storage capacity

Purpose: Respond to storage pressure before writes fail or recovery risk rises.

Status: Draft synthetic material; review before operational use.

## Symptoms
- Users or monitoring report an issue consistent with database storage capacity alerts.
- The issue may affect one user, a group, or a shared service; determine scope before acting.

## Prerequisites
- Confirm requester/service identity and business impact using approved process.
- Identify environment, owner, first-failure time, and relevant recent changes.
- Use authorized diagnostic tools and least-privilege access.

## Procedure
1. Confirm utilization, growth rate, threshold, and time-to-exhaustion.
2. Identify growing category: data, transaction logs, temp space, indexes, or backup staging.
3. Correlate growth with workload, batch jobs, retention changes, and abnormal transactions.
4. Review approved capacity expansion options, quotas, and maintenance constraints.
5. Require database-owner approval for expansion or policy-compliant cleanup; monitor writes, replication, and backups.

## Verification
- Capacity returns below agreed threshold and writes succeed.
- Backup, replication, and recovery posture remain healthy.

## Rollback and recovery
- Revert only an identified approved change using the documented change record.
- If rollback is unsafe or the cause is uncertain, stop and contact the service owner.

## Escalation
- Near-term production exhaustion, blocked replication, or cleanup conflicts with retention/recovery rules.

## Safety cautions
- Never manually delete DB files/logs/backups or purge data without reviewed recovery plan.

## Related runbooks
- RUN-DB-003
- RUN-BKP-006

## Evidence to record
- Impact and scope
- Start time and timezone
- Sanitized errors and correlation IDs
- Diagnostics and change IDs
- Actions, approver, outcome, and follow-up owner
