execute as @a[x=533,y=74,z=1836,distance=..100] at @s run playsound block.beacon.ambient master @s ~ ~ ~ 1 0.9
title @a[x=533,y=74,z=1836,distance=..100] times 7t 2.5s 7t
title @a[x=533,y=74,z=1836,distance=..100] actionbar {"text":"You notice a strange sense of refreshment...","color":"white","italic":true}
function fireworks:prod/countdown_60
schedule function fireworks:prod/run_1 13s