#!/usr/bin/env python3
"""Cricsheet historical-data builder placeholder. See README before importing data."""
from pathlib import Path
import json
OUT=Path("data/historical.json")
def main():
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"generated_at":None,"match_count":None,"venues":[],"players":[],"coverage_note":"Import and aggregate licensed Cricsheet data before publishing statistics."},indent=2),encoding="utf-8")
if __name__=="__main__": main()
