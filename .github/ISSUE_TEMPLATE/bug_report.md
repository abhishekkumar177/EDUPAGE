name: "🐛 Bug Report"
description: "Report a bug in the Student Risk Analyzer system"
title: "[BUG] "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Please provide detailed information about the bug so we can reproduce it and fix it.

  - type: input
    id: steps
    attributes:
      label: "Steps to Reproduce"
      description: "Step by step instructions to reproduce the bug"
      placeholder: "1. Run app_student.py\n2. Log in as student\n3. Observe error"
      required: true

  - type: input
    id: expected
    attributes:
      label: "Expected Behavior"
      description: "What you expected to happen"
      placeholder: "Student dashboard should load"
      required: true

  - type: input
    id: actual
    attributes:
      label: "Actual Behavior"
      description: "What actually happened"
      placeholder: "Application crashes with FileNotFoundError"
      required: true

  - type: dropdown
    id: component
    attributes:
      label: "Affected Component"
      description: "Which part of the repo is affected?"
      options:
        - "Data Generator"
        - "Student Dashboard"
        - "Mentor Dashboard"
        - "Risk Engine"
        - "App Manager"
        - "Other"
      required: true
