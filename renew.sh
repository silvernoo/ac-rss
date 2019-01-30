#!/usr/bin/env bash

python ./generator/rss_feed.py

git add .xml
git push -a ""