function uhc:spawning/reset_comp_tower_string
execute if entity @p[gamemode=!spectator,distance=..50] run function uhc:spawning/comp_tower_string
execute if entity @p[gamemode=!spectator,distance=..50] run data remove storage uhc:uhc towers_shuffled[0]
execute if entity @p[gamemode=!spectator,distance=..50] as @r[gamemode=!spectator,distance=..50] run function uhc:spawning/spawn_player_at_tower

execute if entity @p[gamemode=!spectator,distance=..50] run function uhc:spawning/spread_players