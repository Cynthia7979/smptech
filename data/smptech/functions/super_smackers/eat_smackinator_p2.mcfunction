tellraw @a[tag=smptech.super_smackers.awaiting_eat_p2] {"text":"Well, at least you stopped before it's too late. Take good care of the half that remains. It won't grow that back now.","color":"yellow"}
clear @a[tag=smptech.super_smackers.awaiting_eat_p2] minecraft:warped_fungus_on_a_stick{CustomModelData:1283}
execute as @a[tag=smptech.super_smackers.awaiting_eat_p2] run function smptech:super_smackers/give_half_smackinator
tag @a[tag=smptech.super_smackers.awaiting_eat_p2] remove smptech.super_smackers.awaiting_eat_p2