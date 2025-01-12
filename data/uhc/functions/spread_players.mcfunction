execute if entity @p[gamemode=survival,distance=..5] run function uhc:comp_tower_string
execute if entity @p[gamemode=survival,distance=..5] run data remove storage uhc:uhc towers_shuffled[0]
execute if entity @p[gamemode=survival,distance=..5] as @r[gamemode=survival,distance=..5] run function uhc:spawn_player

execute if entity @p[gamemode=survival,distance=..5] run function uhc:spread_players