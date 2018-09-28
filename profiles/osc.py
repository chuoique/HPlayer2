from core.engine import hplayer

# PLAYER
player = hplayer.addplayer('mpv', 'simple-osc')

# Interfaces
player.addInterface('osc', 4000, 4001)

# RUN
hplayer.setBasePath("/mnt/usb")
hplayer.run()
