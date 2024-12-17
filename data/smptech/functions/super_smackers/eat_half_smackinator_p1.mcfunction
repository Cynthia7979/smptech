playsound entity.generic.eat master @a ~ ~ ~
playsound entity.generic.eat master @a ~ ~ ~
playsound entity.generic.eat master @a ~ ~ ~
playsound entity.player.burp master @a ~ ~ ~
effect give @s minecraft:nausea 100 1 true
effect give @s minecraft:saturation 20
clear @s minecraft:warped_fungus_on_a_stick{CustomModelData:1789}
tellraw @s {"text":"You ate the rest of the Smackinator!","color":"yellow","italic":true}
tag @s add smptech.super_smackers.awaiting_eat_half_p2
schedule function smptech:super_smackers/eat_half_smackinator_p2 2s