#!/usr/bin/env bash

python ./generator/rss_feed.py

git add .
git commit -am "renew"
git push
