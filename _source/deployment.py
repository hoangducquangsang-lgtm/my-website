"""Generate a deployment plan; this does not modify live DNS, redirects or hosting."""
import csv
import json
from pathlib import Path

def write_redirect_plan(root, pages):
    destination = Path(root) / "_source/hosting"
    destination.mkdir(exist_ok=True)
    routes = sorted(pages)
    with (destination / "redirect-map.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["source_url", "target_url", "status_code", "preserve_query_string"])
        for route in routes:
            for origin in ("https://vietpaw.com", "https://www.vietpaw.com", "http://vietpaw.com", "http://www.vietpaw.com"):
                writer.writerow([origin + route + "index.html", "https://vietpaw.com" + route, 301, True])
    plan = {"deployment_status": "prepared_not_applied", "current_host": "GitHub Pages",
            "canonical_origin": "https://vietpaw.com", "routes": routes,
            "index_redirects": len(routes) * 4, "preserve_query_string": True,
            "notes": ["GitHub Pages does not execute this CSV or Cloudflare rules.",
                      "Enable a compatible redirect layer before claiming HTTP 301 is live.",
                      "Do not add noindex to index.html: it is also the document served at the clean URL."]}
    (destination / "redirect-plan.json").write_text(json.dumps(plan, indent=2)+"\n", encoding="utf-8")
