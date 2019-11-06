#!/bin/bash
apt-get update
wait
echo 'Update Check Complete'
apt-get upgrade
wait
echo 'Update Install Complete. Please read above for any install errors'