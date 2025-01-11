execute as @a[gamemode=!spectator] run function uhc:triggers/teleport_player
# It's a one-off solution okay
function uhc:triggers/enable_all

execute store result score CurrentBorderSize: uhc_kills run worldborder get