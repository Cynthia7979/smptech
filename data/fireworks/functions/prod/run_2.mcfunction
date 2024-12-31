execute as @a[x=533,y=74,z=1836,distance=..100] at @s run playsound block.end_portal_frame.fill master @s ~ ~ ~ 1 0.5
tellraw @a[x=533,y=74,z=1836,distance=..100] {"text":"Let kingdoms fall and Avihms shift, this day is always remembered-","color":"gold","italic":true}
schedule function fireworks:prod/run_3 6s