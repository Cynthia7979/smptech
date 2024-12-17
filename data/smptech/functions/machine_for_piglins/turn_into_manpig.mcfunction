# Sound effect
playsound minecraft:entity.blaze.death master @s ~ ~ ~ 0.32 0.5
playsound minecraft:entity.piglin_brute.angry master @s ~ ~ ~ 0.53 0.86
playsound minecraft:entity.piglin_brute.converted_to_zombified master @s ~ ~ ~ 0.9 1.53
# Label player as a manpig
tag @s add smptech.machine_for_piglins.manpig
# Make sure to preserve player's current head gear. 103b is headgear slot
execute if data entity @s Inventory[{Slot:103b}] run summon minecraft:item ~ ~ ~ {Item:{id:"minecraft:barrier",Count:1b},Tags:["smptech.dropped_dummy_item"]}
data modify entity @e[type=item,tag=smptech.dropped_dummy_item,limit=1] Item set from entity @s Inventory[{Slot:103b}]
tag @e[type=item] remove smptech.dropped_dummy_item
# Manpig head item
item replace entity @s armor.head with carved_pumpkin{display:{Name:'[{"bold":true,"color":"dark_red","obfuscated":true,"text":"///","underlined":true},{"obfuscated":false,"text":"MANPIG"},"///"]'},HideFlags:54,Unbreakable:1b,CustomModelData:1006,Enchantments:[{id:"minecraft:fire_protection",lvl:5s},{id:"minecraft:binding_curse",lvl:1s},{id:"minecraft:vanishing_curse",lvl:1s}],AttributeModifiers:[{AttributeName:"generic.max_health",Name:"generic.max_health",Amount:15,Operation:0,UUID:[I;-772815909,-246853716,-1205404181,-423073313],Slot:"head"},{AttributeName:"generic.armor",Name:"generic.armor",Amount:-10,Operation:0,UUID:[I;47136997,-1103016581,-1710480442,44351058],Slot:"head"}]} 1
# Give initial status effects
function smptech:machine_for_piglins/apply_manpig_effects
effect give @s minecraft:nausea 30 1
effect give @s minecraft:wither 28