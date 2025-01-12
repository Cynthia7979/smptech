scoreboard players add seconds uhc_timer 1
execute unless score seconds uhc_timer >= #seconds_end uhc_timer run schedule function uhc:time/sec 1s