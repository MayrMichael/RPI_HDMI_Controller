# RPI_HDMI_Controller
Repository for controlling the HDMI interface on a Raspberry PI

# Installation
1) Save the files in a folder
2) Make the the scripts with chmod +x script name executable.
3) If the script is to be executed with every restart, you can add the following line to the crontab and replace the braces with the actual path to the file:
'''crontab -e
  @reboot python {path to the file}/monitor_controller.py &'''
Then the script will automatic activated after restart.

