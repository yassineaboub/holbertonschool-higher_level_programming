#!/bin/bash
curl -o /dev/null --silent --write-out '%{http_code}' $1
