#!/bin/sh

if [ ! -d ac-rss ]; then
  git clone https://${GITHUB_USER}:${GITHUB_PW}@github.com/silvernoo/ac-rss.git
  cd ac-rss
  git config user.email ${GIT_MAIL}
  git config user.name ${GIT_NAME}
fi

/usr/sbin/crond -f -l 8