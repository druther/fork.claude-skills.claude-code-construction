#!/usr/bin/env python3
"""Run a skill's extraction pipeline for eval.

Dispatches to per-skill runner modules in evals/runners/skills/.
Each module handles one skill's extraction, output, and scoring.

Usage:
  python evals/runners/run_skill.py --case evals/cases/schedule-extractor/case_01_door_schedule.json
  python evals/runners/run_skill.py --case evals/cases/project-onboarding/case_01.json
  python evals/runners/run_skill.py --list
"""

import argparse
import json
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from evals.runners.helpers import create_run_dir
from evals.runners.skills.schedule_extractor import run_schedule_extractor
from evals.runners.skills.project_onboarding import run_project_onboarding
from evals.runners.skills.submittal_log import run_submittal_log_generator
from evals.runners.skills.sheet_index import run_sheet_index_builder
from evals.runners.skills.spec_parser import run_spec_parser
from evals.runners.skills.bid_tabulator import run_bid_tabulator
from evals.runners.skills.subcontract_writer import run_subcontract_writer
from evals.runners.skills.code_researcher import run_code_researcher

SKILL_RUNNERS = {
    "schedule-extractor": run_schedule_extractor,
    "project-onboarding": run_project_onboarding,
    "submittal-log-generator": run_submittal_log_generator,
    "sheet-index-builder": run_sheet_index_builder,
    "spec-parser": run_spec_parser,
    "bid-tabulator": run_bid_tabulator,
    "subcontract-writer": run_subcontract_writer,
    "code-researcher": run_code_researcher,
}


def run(case_path, run_dir_override=None):
    """Load a case JSON and dispatch to the appropriate skill runner."""
    with open(case_path) as f:
        case = json.load(f)

    skill = case["skill"]
    case_id = case["id"]

    runner = SKILL_RUNNERS.get(skill)
    if not runner:
        print(f"No runner for skill '{skill}'.")
        print(f"Available: {', '.join(sorted(SKILL_RUNNERS.keys()))}")
        return None

    run_dir = Path(run_dir_override) if run_dir_override else create_run_dir(case_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    result = runner(case, run_dir)

    print(f"\n{'='*60}")
    print(f"COMPLETE: {case_id}")
    print(f"Artifacts: {run_dir}")
    print(f"{'='*60}")

    return result


def list_runners():
    """List all available skill runners."""
    print(f"\nAvailable skill runners ({len(SKILL_RUNNERS)}):\n")
    for name in sorted(SKILL_RUNNERS.keys()):
        print(f"  {name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a skill for eval")
    parser.add_argument("--case", help="Path to case JSON file")
    parser.add_argument("--run-dir", help="Use existing run directory (for pre-extracted data)")
    parser.add_argument("--list", action="store_true", help="List available runners")
    args = parser.parse_args()

    if args.list:
        list_runners()
    elif args.case:
        run(args.case, run_dir_override=args.run_dir)
    else:
        parser.print_help()
