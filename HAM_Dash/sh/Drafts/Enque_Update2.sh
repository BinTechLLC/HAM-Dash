lxterminal --command="/bin/bash -c '/home/pi/Projects/HAM_Dash/sh/sudoUpdate.sh; read'"
wait
echo 'Step 1 Done'
./home/pi/Projects/HAM_Dash/sh/sudoUpgrade.sh; read
wait
echo 'Step 2 Done'
