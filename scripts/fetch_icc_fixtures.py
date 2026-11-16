#!/usr/bin/env python3
"""Best-effort ICC structured-data fixture importer. Preserves last-known-good data on failure."""
import json, re, urllib.request
from pathlib import Path
URL="https://www.icc-cricket.com/fixtures-results?appview=true"
OUT=Path("data/fixtures.json")
def main():
    req=urllib.request.Request(URL,headers={"User-Agent":"CricPulse/1.0 (personal research)"})
    with urllib.request.urlopen(req,timeout=25) as response: html=response.read().decode("utf-8","replace")
    found=[]
    for raw in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',html,re.I|re.S):
        try: obj=json.loads(raw)
        except Exception: continue
        nodes=obj if isinstance(obj,list) else obj.get("@graph",[obj]) if isinstance(obj,dict) else []
        for e in nodes:
            if isinstance(e,dict) and e.get("@type") in ("SportsEvent","Event"):
                teams=[x.get("name") if isinstance(x,dict) else str(x) for x in [e.get("homeTeam"),e.get("awayTeam")] if x]
                if teams: found.append({"teams":teams,"competition":e.get("superEvent",{}).get("name") if isinstance(e.get("superEvent"),dict) else None,"schedule_date":e.get("startDate"),"venue":(e.get("location") or {}).get("name") if isinstance(e.get("location"),dict) else None,"status":"scheduled","source_urls":[e.get("url") or URL],"last_verified":None})
    if not found: raise SystemExit("No supported structured fixture records found; existing file preserved.")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"updated_at":None,"source":URL,"fixtures":found},indent=2),encoding="utf-8")
if __name__=="__main__": main()
