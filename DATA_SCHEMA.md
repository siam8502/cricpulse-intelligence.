# CricPulse data schema

- `data/fixtures.json`: sourced fixture records. Include teams, competition, format, status, schedule date/time label, timezone, venue, pitch, ground, tactical plan, assessment, source URLs and last verified timestamp. Unknown fields remain null or `Data unavailable`.
- `data/historical.json`: Cricsheet-derived historical match count, venue aggregates and player aggregates. Include source coverage and generation timestamp.
- `data/reports.json`: sourced editorial reports with summary, source URLs and verification timestamp.

Never fabricate scores, fixtures, pitch reports, player availability, statistics or predictions. Scenario Lab is hypothetical and separate from real data.