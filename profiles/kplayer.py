from core.engine import hplayer

# PLAYER
player = hplayer.addplayer('mpv', 'kplayer')

# Interfaces
player.addInterface('kmsg')

# RUN
hplayer.setBasePath("/mnt/usb")
hplayer.run()
