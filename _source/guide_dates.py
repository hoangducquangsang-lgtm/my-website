"""Owner-requested displayed editorial dates; not reconstructed edit history.

Dates stay fixed across builds. Assign a deliberate date when adding a guide;
never derive existing dates from the build clock or shift them with list order.
"""
from datetime import date

GUIDE_UPDATED_DATES = {
    "natural-dog-chew-toys-guide": "2026-08-30",
    "are-coffee-wood-chews-safe-for-dogs": "2026-08-27",
    "coffee-wood-vs-antler-nylon-rawhide": "2026-08-23",
    "best-natural-chews-for-aggressive-chewers": "2026-08-20",
    "how-long-do-coffee-wood-chews-last": "2026-08-16",
    "coffee-wood-chew-size-guide": "2026-08-13",
    "plastic-free-biodegradable-pet-toys-guide": "2026-08-09",
    "are-dog-toys-biodegradable": "2026-08-06",
    "what-is-coconut-fiber-pet-toys": "2026-08-02",
    "non-toxic-cat-toys-wholesale-buying-guide": "2026-07-30",
    "sustainable-pet-toy-materials-compared": "2026-07-26",
    "sourcing-eco-pet-toys-vietnam": "2026-07-23",
    "natural-dog-toy-manufacturer-vietnam": "2026-07-19",
    "wholesale-coconut-fiber-cat-toys-supplier": "2026-07-16",
    "private-label-oem-eco-pet-toys-explained": "2026-07-12",
    "pet-toy-moq-fob-pricing-lead-times": "2026-07-09",
    "sourcing-pet-toys-vietnam-vs-china": "2026-07-05",
    "pet-toy-safety-compliance-cpsia-reach": "2026-07-02",
    "pet-toy-safety-testing-requirements": "2026-06-28",
    "how-to-vet-an-eco-pet-toy-supplier": "2026-06-25",
}
MONTHS = "January February March April May June July August September October November December".split()


def updated_time(slug):
    iso = GUIDE_UPDATED_DATES[slug]
    value = date.fromisoformat(iso)
    label = f"{value.day} {MONTHS[value.month - 1]} {value.year}"
    return f'<time datetime="{iso}">{label}</time>'
