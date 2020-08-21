#!/bin/bash

set -uex

ls -1 *.jpg |
  while read file; do
    sed -e "s|\$URL|/images/sunshine-plaza/${file}|;s|\$TEXT|Slunecni namesti in Prague|" figure.md;
  done > figures.md