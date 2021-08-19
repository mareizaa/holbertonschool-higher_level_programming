#!/bin/bash
# A header variable X-HolbertonSchool-User-Id must be sent with the value 98
curl -s $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
