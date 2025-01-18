execute as @a[tag=deathpoint_waiting_for_tp] run tp @s 5000 210 5000
tag @a[tag=deathpoint_waiting_for_tp] remove deathpoint_waiting_for_tp
schedule function uhc:deathpoint/remove_end_gateway 100t