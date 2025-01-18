# Get number of remaining towers
execute store result score max uhc_math run data get storage uhc:uhc towers
# Select random one
function uhc:rng/range
# Move to the end of shuffled array
scoreboard players operation tower_index uhc_utils = out uhc_math
function uhc:rng/move_tower_to_shuffled_at_index
# Loop until no towers left
execute unless score max uhc_math matches ..1 run function uhc:spawning/shuffle_towers