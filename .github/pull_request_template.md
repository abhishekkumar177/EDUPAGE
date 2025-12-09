name: "🔀 Pull Request"
description: "Template for pull requests in Student Risk Analyzer"
title: "[PR] "
labels: ["pr"]
body:
  - type: input
    id: pr_description
    attributes:
      label: "Pull Request Description"
      description: "Describe what changes you made"
      placeholder: "Fixed bug in attendance calculation or added a new feature"
      required: true

  - type: tasklist          # ✅ FIXED!
    id: checklist
    attributes:
      label: "Checklist"
      options:
        - label: "Code runs without errors"
        - label: "Tested locally"
        - label: "Updated documentation if needed"
        - label: "Followed coding standards"
        - label: "Added comments where necessary"

  - type: dropdown
    id: component
    attributes:
      label: "Affected Component"
      options:
        - "Data Generator"
        - "Student Dashboard"
        - "Mentor Dashboard"
        - "Risk Engine"
        - "App Manager"
        - "Other"
      required: true
