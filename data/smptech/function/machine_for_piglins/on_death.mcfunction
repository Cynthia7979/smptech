# Reset death listener
scoreboard players set @s smptech.machine_for_piglins.recent_death 0

# Check if player is on the evil side AND dropped item on death
execute if entity @e[type=item,nbt={Item:{components:{"minecraft:custom_data":{smptech.machine_for_piglins.is_evil_item:1}}}}] as @s[tag=smptech.machine_for_piglins.evil] run function smptech:machine_for_piglins/give_evil_item
# Delete any matching item entity in the world
execute as @e[type=item,nbt={Item:{components:{"minecraft:custom_data":{smptech.machine_for_piglins.is_evil_item:1}}}},limit=1] run kill

# Same thing but for the good side
execute if entity @e[type=item,nbt={Item:{components:{"minecraft:custom_data":{smptech.machine_for_piglins.is_good_item:1}}}}] as @s[tag=smptech.machine_for_piglins.good] run function smptech:machine_for_piglins/give_good_item
execute as @e[type=item,nbt={Item:{components:{"minecraft:custom_data":{smptech.machine_for_piglins.is_good_item:1}}}},limit=1] run kill