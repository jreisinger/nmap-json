#!/bin/sh

source venv/bin/activate

exec ./nmap-json.py "$@"
