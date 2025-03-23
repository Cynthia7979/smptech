execute as @e[type=item,tag=!scanned,predicate=players:is_asc] run function players:items/asc/give_back
item replace entity @s weapon.mainhand from block 1000000 0 1000000 container.0
scoreboard players operation #secs temp = @s asc_cool
scoreboard players add #secs temp 19
scoreboard players operation #secs temp /= #20 const
playsound minecraft:dcustom.block.anvil.land player @s ~ ~ ~ 0.5 2
tellraw @s ["",{"text":"Holy Moonlight is on cooldown for ","color":"red"},{"score":{"name":"#secs","objective":"temp"},"color":"red"},{"text":"s","color":"red"}]
