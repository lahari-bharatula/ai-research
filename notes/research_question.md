# Research Question

## Main Question

How effective are tool-level permission boundaries at preventing prompt injection attacks in LLM agents while preserving legitimate task completion?

## Initial Hypothesis

Tool-level permission boundaries will reduce the success rate of prompt injection attacks that attempt to trigger unauthorized actions, while preserving most legitimate task performance.

## Metrics

### Security

- Attack success rate
- Unauthorized tool-call rate

### Utility

- Legitimate task completion rate

## Important Limitations

The experiment will use a small, controlled environment and therefore cannot establish that permission boundaries prevent prompt injection in real-world agents.

## What Would Falsify Our Hypothesis?

If permission boundaries do not meaningfully reduce unauthorized actions, or if they prevent legitimate tasks from being completed, then the proposed defense may have limited practical value.
