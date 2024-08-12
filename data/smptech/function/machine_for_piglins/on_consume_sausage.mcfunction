# Reset scoreboard
scoreboard players set @s smptech.machine_for_piglins.jigsaw_used 0
# Give player another sausage
function smptech:machine_for_piglins/give_evil_item
# Roll RNG for turning into manpig
# Fun fact; the chance in predicate RNG is dynamic, meaning if I want I can make it dependant on number of times sausage's been eaten >:)
execute if predicate smptech:machine_for_piglins/sausage_roll run say triggered!
# TODO here
# alright good night