# Wifi_Connector
Python script use in polybar to create a Network Manager

## Demo:

### On bar:
![on bar](https://media.discordapp.net/attachments/886507265450991617/1049976744070893598/image.png)

### On click:

![on bar](https://media.discordapp.net/attachments/886507265450991617/1049976839717797970/filename_12_02_191414.png?width=873&height=491)

## Usage:

First, open your polybar config file (default directory should be /etc/polybar/config.ini) and add this:

```ini
[module/wifi]
type = custom/script
; Update the module status every 60 seconds, just remember the smaller value is, the more cpu usage it will takes to update your module.
interval = 60
; You can change format-prefix to whatever icon you want it to display. I'm using Nerd Font on the polybar so I just use Nerd Icons as well.
format-prefix = "直 "
format-prefix-foreground = <the icon's color>
exec = python <path to wifi.py>
; Display the network manager and wifi connector. In this case I'm using Alacritty.
click-left = Alacritty -o font.size = 8 -v --hold -e python wificonnector.py
```
**Important**

- Don't set the *interval* value too small otherwise the code won't works correctly. The reason is due to slow response by using *speedtest* python module.

- I'm using i3-gaps, and as you can see in the second images the Alacritty use to open wifi connector window is floating. Just do it by making specified Alacritty class or make all Alacritty window become floating by adding this line into your i3 config:

```conf
for_window [class="^Alacritty$" instance="^Alacritty$"] floating enable
```

