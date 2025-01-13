execute as @a at @s run playsound block.note_block.bit master @s ~ ~ ~ 1 2
title @a title {"text":"The border is now shrinking!","color":"dark_red"}
tellraw @a {"text":"The border is now shrinking!","color":"dark_red"}
worldborder set 50 1800