name: "♻️ Refactor"
description: "Suggest refactoring of code for readability, performance, or structure"
title: "[REFACTOR] "
labels: ["refactor"]
body:
  - type: input
    id: refactor_description
    attributes:
      label: "Refactor Description"
      description: "Which part of the code should be refactored?"
      placeholder: "Refactor risk_engine.py for modularity and testing"
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
