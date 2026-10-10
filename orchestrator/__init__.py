"""Workflow orchestrator for the Human-AI Collaborative Science Framework.

Runs the four-stage workflow (Planning, Modeling, Reporting, Reviewing) with
any configured agents and stops only at human nodes: Tier 1 decision
checkpoints, Tier 2 stage gates, and stuck states. See docs/orchestration.md.
"""

STAGES = ["planning", "modeling", "reporting", "reviewing"]
