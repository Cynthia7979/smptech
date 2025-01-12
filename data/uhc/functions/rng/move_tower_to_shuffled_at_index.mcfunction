execute if score tower_index uhc_utils matches 0 run data modify storage uhc:uhc towers_shuffled append from storage uhc:uhc towers[0]
execute unless score tower_index uhc_utils matches 0 run data modify storage uhc:uhc towers append from storage uhc:uhc towers[0]
data remove storage uhc:uhc towers[0]
scoreboard players remove tower_index uhc_utils 1
execute unless score tower_index uhc_utils matches ..-1 run function uhc:rng/move_tower_to_shuffled_at_index