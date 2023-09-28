#!/bin/bash
# takes and sends a request to URL, displays the size of response
curl -s "$1" | wc -c
