#!/bin/bash

# list of popular websites to ping
websites=("google.com" "facebook.com" "youtube.com" "amazon.com" "wikipedia.org")

# ping each website and display the results
for website in "${websites[@]}"; do
    echo "Pinging $website..."
    ping -c 4 $website   # ping 4 times
    echo ""
done