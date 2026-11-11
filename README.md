
# FinPilot AI

An open-source intelligent enterprise invoice
processing and reconciliation platform.

## Overview

FinPilot AI aims to automate accounts payable
operations through document processing,
business-rule validation, duplicate detection,
purchase order matching and approval workflows.

## Problem Statement

Businesses receive invoices in multiple formats
and often rely on manual processing.

This creates operational inefficiencies,
duplicate payments, data-entry errors and
delays in invoice approvals.

FinPilot AI aims to address these challenges
through an automated and auditable workflow.

## Current Features

- FastAPI backend
- Application health monitoring
- Interactive API documentation

## Planned Features

- Vendor management
- Invoice upload and processing
- OCR and AI-based extraction
- Invoice validation
- Duplicate detection
- Purchase order matching
- Exception management
- Approval workflows
- Audit logging
- Analytics dashboard

## Technology Stack

- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL (planned)
- React and TypeScript (planned)
- Tesseract OCR (planned)
- Local LLMs (planned)

## Getting Started

### 1. Clone the repository

git clone https://github.com/ShadyDuck36/finpilot-ai.git

### 2. Navigate to backend

cd finpilot-ai/backend

### 3. Create virtual environment

py -3.12 -m venv .venv

### 4. Install dependencies

.\.venv\Scripts\python.exe -m pip install -r ../requirements.txt

### 5. Start the application

.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload

### 6. Open API documentation

http://127.0.0.1:8000/docs

## Project Status

Early development - Milestone 1.

## License

To be determined.
