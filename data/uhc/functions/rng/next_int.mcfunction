function uhc:rng/lcg

scoreboard players operation #temp uhc_math = out uhc_math
scoreboard players operation out uhc_math %= #range uhc_math
scoreboard players operation #temp uhc_math -= out uhc_math
scoreboard players operation #temp uhc_math += #m1 uhc_math
execute if score #temp uhc_math matches ..-1 run function uhc:rng/next_int