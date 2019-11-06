sleep 0.5s
echo -e '\e[92m'	# Set Text Coolor To Green
echo ' '
echo '****************************************************************************'
echo 'Raspbian (Debian) System Software Update Module'
echo 'for HAM Dash by Binford Integrated Technology, LLC.'
echo 'Written and Debugged by Koltin Binford.'
echo '****************************************************************************'
echo ' '
echo -e '\e[5m\e[91m****************************************************************************'
echo -e '\e[0m\e[91mDO NOT CLOSE THIS WINDOW UNLESS YOU WANT TO CANCEL'
echo ' '
echo 'HAM Dash will re-open after updates are complete or canceled'
echo -e '\e[5m****************************************************************************'
echo -e '\e[0m\e[92m'	# Stop Flashing and Change to Green
echo -e '\e[95m****************************************************************************'
echo 'Running updates in 30 seconds.'
echo -e '****************************************************************************\e[92m'
sleep 30s
echo ' '
echo ' '
echo ' '
echo ' '
echo '****************************************************************************'
echo 'Checking repository list. Please wait...'
echo '****************************************************************************'
sleep 3s
echo ' '
echo ' '
sudo apt-get update &
wait
sleep 1s
echo ' '
echo ' '
echo '****************************************************************************'
echo 'Repository list updated. Continuing in 3 seconds...'
echo '****************************************************************************'
sleep 5s
echo ' '
echo '****************************************************************************'
echo 'Performing core updates.'
echo '****************************************************************************'
sleep 3s
echo ' '
echo ' '
sudo apt-get -y upgrade &
wait
sleep 1s
echo ' '
echo ' '
echo '****************************************************************************'
echo 'Core updates complete. Continuing in 3 seconds...'
echo '****************************************************************************'
sleep 3s
echo ' '
echo '****************************************************************************'
echo 'Performing distribution updates.'
echo '****************************************************************************'
sleep 3s
echo ' '
echo ' '
sudo apt-get -y dist-upgrade &
wait
sleep 1s
echo ' '
echo ' '
echo '****************************************************************************'
echo 'Distribution updates complete. Continuing in 3 seconds...'
echo '****************************************************************************'
sleep 3s
echo ' '
echo '****************************************************************************'
echo 'Cleaning up. Please wait...'
echo '****************************************************************************'
sleep 3s
echo ' '
echo ' '
sudo apt-get -y auto-remove &
wait
sleep 1s
echo ' '
echo ' '
echo '****************************************************************************'
echo 'Cleanup complete.'
echo '****************************************************************************'
sleep 1s
echo ' '
echo -e '\e[95m****************************************************************************'
echo 'Updates done. You may now close this window.'
echo -e '****************************************************************************\e[92m'
echo ' '
echo '****************************************************************************'
echo 'Raspbian (Debian) System Software Update Module'
echo 'for HAM Dash by Binford Integrated Technology, LLC.'
echo 'Written and Debugged by Koltin Binford.'
echo '****************************************************************************'
