#!/bin/sh

set -e

locust --headless --host http://dashboard:9000 --users "${USERS:-1}" 2>&1

