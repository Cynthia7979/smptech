### Cloud Notes ###
# Newton-Raphson, 4 iterations approach
#
# min = lower range
# max = upper range
# out = random number between range


scoreboard players add max uhc_math 1
scoreboard players operation #range uhc_math = max uhc_math
scoreboard players operation #range uhc_math -= min uhc_math

scoreboard players operation #m1 uhc_math = #range uhc_math
scoreboard players remove #m1 uhc_math 1
function uhc:rng/next_int
scoreboard players operation out uhc_math += min uhc_math

scoreboard players reset #m1 uhc_math
scoreboard players remove max uhc_math 1