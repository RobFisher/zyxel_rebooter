# Zyxel modem/router rebooter

## Setup:

You probably need Firefox installed.

    python3 -m pip install selenium

## Usage:

In Bash:

    export ROUTER_ADDRESS=192.168.1.1
    set +o history
    export ROUTER_PASSWORD=mypassword
    set -o history
    python3 zyxel_rebooter.py

## Notes:
Logging in to the web interface of these routers seems to require that the password
be encrypted with an RSA key. The Javascript to do this is obfuscated so I have not
yet managed to work out how to do it without running the Javascript. Therefore this
method uses a headless browser.

The limitation is that changes to the web UI are likely to break this script.

This has been tested on a Zyxel LTE5388-M804 with firmware V1.00(ABSQ.4)C0.

For fun, here is the discussion I had with ChatGPT about this. Mainly it helped me
by writing the Selenium boilerplate and getting me started with example code:
https://sharegpt.com/c/LOnOGuU

