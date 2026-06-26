# SmartLoan Version 1.0 — Scoring Rules

## Purpose

This document explains how the SmartLoan Version 1.0 prototype calculates risk and makes an automatic loan decision.

The current system uses rule-based checks. It does not use a machine-learning model or human loan officer.

---

## Risk Scoring Table

| Risk factor           | Risk condition                                                   | Points added | Reason returned                                   |
| --------------------- | ---------------------------------------------------------------- | -----------: | ------------------------------------------------- |
| Existing monthly debt | Debt-to-income ratio is greater than 40%                         |            2 | Existing debt is high compared to income.         |
| Monthly expenses      | Expense-to-income ratio is greater than 60%                      |            2 | Monthly expenses are high compared to income.     |
| Credit score          | Credit score is below 600                                        |            2 | Credit score is low.                              |
| Missed payments       | Missed payments are greater than 0                               |            2 | Missed payments are present.                      |
| Requested loan amount | Requested loan amount is greater than three times monthly income |            2 | Requested loan amount is high compared to income. |

The maximum possible risk score is 10.

---

## Risk-Level Thresholds

| Risk score | Risk level |
| ---------: | ---------- |
|          0 | Low        |
|        1–3 | Medium     |
|       4–10 | High       |

Because every current risk condition adds 2 points, the scores that can currently occur are:

• 0
• 2
• 4
• 6
• 8
• 10

Therefore:

• Score 0 means no risk conditions were identified.
• Score 2 means one risk condition was identified.
• Score 4 or more means multiple risk conditions were identified.

---

## Automated Decision Policy

| Application result                                         | Final decision   |
| ---------------------------------------------------------- | ---------------- |
| Valid application with a risk score of 0                   | Approved         |
| Valid application with one or more identified risk factors | Rejected         |
| Missing or invalid application data                        | Validation Error |

SmartLoan Version 1.0 approves an application only when no current risk conditions are identified.

The current system does not use:

• manual review
• human loan officer approval
• Review Required
• More Information Required

All current decisions are made automatically using validation rules and rule-based risk checks.

---

## Ratio Calculations

### Debt-to-Income Ratio

Existing monthly debt payment is divided by monthly income.

A ratio greater than 40% adds 2 risk points.

### Expense-to-Income Ratio

Monthly expenses are divided by monthly income.

A ratio greater than 60% adds 2 risk points.

### Loan-to-Income Check

The requested loan amount is compared with three times the applicant's monthly income.

A requested amount above this limit adds 2 risk points.

---

## Current Fields Not Used in Risk Scoring

The following fields are currently required but do not add or remove risk points:

• existing loan amount
• employment status
• employment duration
• bank balance
• requested loan duration

These fields may be used in future iterations after their rules and thresholds are formally designed.
---

## Current Status

The current scoring rules match the SmartLoan Version 1.0 decision policy:

• no identified risk factors → Approved
• one or more identified risk factors → Rejected
• missing or invalid data → Validation Error

Any future scoring change must also be updated in:

• loan logic
• README
• testing notes
• Postman tests
• Loop project document
