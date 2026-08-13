# -*- coding: utf-8 -*-
import os, shutil, sys

SRC = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SRC)
ROOT = "/tmp/site_build/site"

if os.path.exists(ROOT):
    shutil.rmtree(ROOT)
os.makedirs(ROOT)

# copy assets
os.makedirs(f"{ROOT}/assets/img", exist_ok=True)
os.makedirs(f"{ROOT}/assets/downloads", exist_ok=True)
for f in os.listdir("/tmp/site_build/assets/img"):
    shutil.copy(f"/tmp/site_build/assets/img/{f}", f"{ROOT}/assets/img/{f}")
shutil.copy(f"{SRC}/style.css", f"{ROOT}/assets/style.css")

MODULES = [
    "content_home_about",
    "content_company",
    "content_materials",
    "content_categories",
    "content_products",
    "content_solutions",
    "content_guides",
]

for m in MODULES:
    mod = __import__(m)
    print("Building", m)
    mod.build(ROOT)

print("DONE. Pages written:")
count = 0
for base, dirs, files in os.walk(ROOT):
    for f in files:
        if f == "index.html":
            count += 1
print(count, "HTML pages")
