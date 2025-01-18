scoreboard players add hours uhc_timer 1

scoreboard players operation #hour_remaining uhc_timer = #hours_end uhc_timer
scoreboard players operation #hour_remaining uhc_timer -= hours uhc_timer

execute if score #hour_remaining uhc_timer matches 1 run title @a title {"text":"1 hour remaining!","color":"yellow"}

execute unless score hours uhc_timer >= #hours_end uhc_timer run schedule function uhc:time/hour 3600s