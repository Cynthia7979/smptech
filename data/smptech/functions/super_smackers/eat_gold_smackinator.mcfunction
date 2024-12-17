playsound entity.generic.eat master @a ~ ~ ~
playsound entity.generic.eat master @a ~ ~ ~
playsound entity.generic.eat master @a ~ ~ ~
playsound entity.player.burp master @a ~ ~ ~
effect give @s minecraft:nausea 5 1 true
effect give @s minecraft:saturation 5
tag @s add smptech.super_smackers.gold_smackinator_eat_cooldown
clear @s minecraft:warped_fungus_on_a_stick{CustomModelData:1058}
title @s title {"text":"Golden Smackinator is on eat cooldown","color":"gray","italic":true}
schedule function smptech:super_smackers/on_gold_finish_eat_cooldown 30s