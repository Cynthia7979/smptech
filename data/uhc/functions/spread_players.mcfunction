function uhc:reset_comp_tower_string
execute if entity @p[gamemode=survival,distance=..50] run function uhc:comp_tower_string
execute if entity @p[gamemode=survival,distance=..50] run data remove storage uhc:uhc towers_shuffled[0]
execute if entity @p[gamemode=survival,distance=..50] as @r[gamemode=survival,distance=..50] run function uhc:spawn_player_at_tower

execute if entity @p[gamemode=survival,distance=..50] run function uhc:spread_players