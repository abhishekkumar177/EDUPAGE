name: "🚀 Enhancement"
description: "Suggest an improvement to the existing functionality"
title: "[ENHANCEMENT] "
labels: ["enhancement"]
body:
  - type: input
    id: enhancement_description
    attributes:
      label: "Enhancement Description"
      description: "Describe the improvement you want to see"
      placeholder: "Add a filter for overdue fees in mentor dashboard"
      required: true

  - type: dropdown
    id: priority
    attributes:
      label: "Priority"
      options:
        - High
        - Medium
        - Low
      required: true
