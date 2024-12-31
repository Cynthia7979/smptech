execute as @a[x=533,y=74,z=1836,distance=..100] at @s run playsound block.end_portal_frame.fill master @s ~ ~ ~ 1 0.5
execute as @a[x=533,y=74,z=1836,distance=..100] at @s run playsound block.beacon.activate master @s ~ ~ ~ 1 0.5
tellraw @a[x=533,y=74,z=1836,distance=..100] {"text":"All beings of creation are gathering under the moons.","color":"gold","italic":true}
#FIXME: REMOVE THIS LINE
# schedule function fireworks:prod/countdown_5 42s
schedule function fireworks:prod/run_2 6s