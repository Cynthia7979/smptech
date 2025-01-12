scoreboard players set hours uhc_timer 0
scoreboard players set minutes uhc_timer 0
scoreboard players set seconds uhc_timer 0
function uhc:time/set_duration

schedule function uhc:time/hour 3600s
schedule function uhc:time/min 60s
schedule function uhc:time/sec 1s