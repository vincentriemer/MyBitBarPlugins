#!/bin/bash

# internal-ip
# BitBar plugin
#
# by Mat Ryer
#
# Gets the current internal IP address, and shows more information in
# the details.

printResult() {
  interface=$1

  echo "$(ipconfig getifaddr $interface)"
  echo "---"
  echo "(Internal IP address)"
  echo "---"
  ifconfig "$interface"
}

if [[ $(ipconfig getifaddr en0) ]]; then
  printResult "en0"
elif [[ $(ipconfig getifaddr en1) ]]; then
  printResult "en1"
elif [[ $(ipconfig getifaddr en2) ]]; then
  printResult "en2"
elif [[ $(ipconfig getifaddr en3) ]]; then
  printResult "en3"
else
  echo "No Internal IP Found"
fi

