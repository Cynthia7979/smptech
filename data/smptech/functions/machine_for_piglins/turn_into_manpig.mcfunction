tag @s add smptech.machine_for_piglins.manpig
# Make sure to preserve player's current head gear. 103b is headgear slot
execute if data entity @s Inventory[{Slot:103b}] run summon minecraft:item ~ ~ ~ {Item:{id:"minecraft:barrier",Count:1b},Tags:["smptech.dropped_dummy_item"]}
data modify entity @e[type=item,tag=smptech.dropped_dummy_item,limit=1] Item set from entity @s Inventory[{Slot:103b}]
tag @e[type=item] remove smptech.dropped_dummy_item
# Manpig head item
item replace entity @s armor.head with piglin_head[item_name='[{"bold":true,"color":"dark_red","obfuscated":true,"text":"///","underlined":true},{"obfuscated":false,"text":"MANPIG"},"///"]',hide_additional_tooltip={},enchantments={levels:{"minecraft:binding_curse":1,"minecraft:vanishing_curse":1},show_in_tooltip:true},enchantment_glint_override=false,attribute_modifiers=[{id:"max_health",type:"generic.max_health",amount:10,operation:"add_value",slot:"head"},{id:"burning_time",type:"generic.burning_time",amount:-0.5,operation:"add_multiplied_base",slot:"head"},{id:"armor",type:"generic.armor",amount:-10,operation:"add_value",slot:"head"}]] 1# Give initial status effects
function smptech:machine_for_piglins/apply_manpig_effects
effect give @s minecraft:nausea 30 1
effect give @s minecraft:wither 28