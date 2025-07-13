# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **discrete mathematics study repository** focused on learning mathematical concepts through programming applications and LeetCode problem solving. The repository bridges theoretical discrete math with practical programming skills, emphasizing algorithm design, complexity analysis, and mathematical reasoning in software development.

## Repository Structure

The codebase follows a chapter-based learning structure:

- `chapters/` - Chapter-specific content organized by discrete math topics
  - Each chapter contains: notes, programming applications, and LeetCode practice
  - `chapter-01-logic-proofs/` - Currently the only implemented chapter
- `templates/` - Structured templates for consistent note-taking and documentation
- `progress-tracker.md` - Learning progress and goal tracking
- `leetcode-connections.md` - Maps discrete math concepts to relevant coding problems

## Key Components

### Programming Applications (`programming-applications/`)
- **boolean-logic.py** - Core implementation demonstrating propositional logic, truth tables, proof techniques, and logical validation
- Follows object-oriented design with classes like `PropositionalLogic`, `TruthTableGenerator`, `LogicalValidation`, and `ProofTechniques`
- Includes comprehensive examples and demonstrations

### Learning Framework
- **Chapter-based progression**: Read → Notes → Exercises → Programming → LeetCode
- **Template-driven documentation**: Consistent structure across all chapters
- **Progress tracking**: Systematic monitoring of learning objectives and completed work

## Development Workflow

Since this is a learning repository rather than a traditional software project, there are no build commands, test suites, or deployment processes. Instead, the workflow focuses on:

1. **Chapter Study**: Taking notes in structured markdown files
2. **Programming Implementation**: Creating Python scripts that demonstrate mathematical concepts
3. **Problem Solving**: Connecting theory to LeetCode problems
4. **Progress Tracking**: Updating learning milestones

## Code Conventions

- **Python files**: Follow clean, documented code with type hints
- **Educational focus**: Code prioritizes clarity and concept demonstration over performance
- **Comprehensive documentation**: Each implementation includes detailed docstrings explaining the mathematical concepts
- **Practical examples**: All code includes runnable demonstrations with sample inputs/outputs

## Running Code

Execute individual Python files directly:
```bash
python chapters/chapter-01-logic-proofs/programming-applications/boolean-logic.py
```

Each programming application is designed as a standalone demonstration that can be run independently.

## File Organization Patterns

- **notes.md**: Chapter concepts and theory
- **programming-applications/**: Implementation of mathematical concepts in code
- **leetcode-practice/**: Problem lists and solutions organized by chapter
- **templates/**: Reusable structures for consistent documentation

This repository is designed for self-paced learning where mathematical theory is immediately applied through programming, making discrete mathematics concepts tangible and practical for software development.