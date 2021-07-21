# Digital photo frame with RPi3
Required hardware: RPi3 and and LCD3.5 inch display.

## Configuring the LCD 3.5 inch display: 
```
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD35-show 180
```

## how to run the frame
Populate directory /home/pi/Pictures/ with pictures
run fbi_start.sh script
```
fbi_start.sh
```

## making the digital photo frame run on startup
```
cp -f fbi_start.sh /home/pi
echo "/home/pi/fbi_start.sh" >> /etc/xdg/lxsession/LXDE-pi/autostart
```
