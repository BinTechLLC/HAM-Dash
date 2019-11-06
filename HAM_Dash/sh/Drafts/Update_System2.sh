echo 'Raspbian / Debian System Software Update Module.'
echo 'Coded for use on the Raspberry Pi operating system.'
echo 'Written and Debugged by Koltin Binford.'
echo 'This module was intended for HAM Dash.'
echo 'The software update will begin in 15 seconds.'
echo ' '
echo ' '
sleep 4s
sudo apt-get update &
wait
sleep 2s
echo ' '
echo ' '
echo ' '
echo ' '
echo '.'
sleep 2s
echo 'Starting updates
echo ' '
echo ' '
echo ' '
echo ' '
sudo apt-get upgrade &
wait
sleep 2s
echo ' '
echo ' '
echo ' '
echo ' '
echo ' '
echo ' '
echo 'Update Complete. Any errors will be listed above.'
echo 'If no errors, you can close this window.'
sleep 2s
echo ' '
echo ' '
echo 'Raspbian / Debian System Software Update Module.'
echo 'Coded for use on the Raspberry Pi operating system.'
echo 'Written and Debugged by Koltin Binford.'
echo 'This module was intended for HAM Dash.'
echo 'Binford Integrated Technology, LLC.'