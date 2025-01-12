scoreboard players add hours uhc_timer 1

execute if score hours uhc_timer matches 1 run title @a title {"text":"1 hour remaining!","color":"yellow"}

execute unless score hours uhc_timer >= #hours_end uhc_timer run schedule function uhc:time/hour 3600s