execute as @a[x=533,y=74,z=1836,distance=..100] at @s run playsound block.end_portal_frame.fill master @s ~ ~ ~ 1 0.5
execute as @a[x=533,y=74,z=1836,distance=..100] at @s run playsound block.amethyst_block.chime master @s ~ ~ ~ 1 0.83
tellraw @a[x=533,y=74,z=1836,distance=..100] {"text":"-the beginning of something new, manifesting from what always has been:","color":"gold","italic":true}
schedule function fireworks:prod/run_4 6s