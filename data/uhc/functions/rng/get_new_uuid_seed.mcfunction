summon minecraft:area_effect_cloud ~ ~ ~ {Tags:["seed"]}
execute store result score #lcg uhc_math run data get entity @e[tag=uuid,limit=1] UUID[0]
execute store result score #temp uhc_math run data get entity @e[tag=uuid,limit=1] UUID[1]
execute store result score #temp1 uhc_math run data get entity @e[tag=uuid,limit=1] UUID[2]
execute store result score #temp2 uhc_math run data get entity @e[tag=uuid,limit=1] UUID[3]
scoreboard players operation #lcg uhc_math += #temp uhc_math
scoreboard players operation #lcg uhc_math += #temp1 uhc_math
scoreboard players operation #lcg uhc_math += #temp2 uhc_math
kill @e[tag=seed]