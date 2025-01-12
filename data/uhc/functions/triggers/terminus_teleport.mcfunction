execute if score @s uhc_tp_akhlo_rohma matches 1.. unless score @s uhc_allow_tp_countdown matches -1 unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/akhlo_rohma_teleport
execute if score @s uhc_tp_anyr_nogur matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/anyr_nogur_teleport
execute if score @s uhc_tp_av_sal matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/av_sal_teleport
execute if score @s uhc_tp_black_jungle matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/black_jungle_teleport
execute if score @s uhc_tp_capital_valley matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/capital_valley_teleport
execute if score @s uhc_tp_carmine matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/carmine_teleport
execute if score @s uhc_tp_casai matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/casai_teleport
execute if score @s uhc_tp_dawn_island matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/dawn_island_teleport
execute if score @s uhc_tp_dusk_island matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/dusk_island_teleport
execute if score @s uhc_tp_ebonfire matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/ebonfire_teleport
execute if score @s uhc_tp_ebony_veldt matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/ebony_veldt_teleport
execute if score @s uhc_tp_faehrcyle matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/faehrcyle_teleport
execute if score @s uhc_tp_frozen_bite matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/frozen_bite_teleport
execute if score @s uhc_tp_grand_pike_canyon matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/grand_pike_canyon_teleport
execute if score @s uhc_tp_gulf_of_drehmal matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/gulf_of_drehmal_teleport
execute if score @s uhc_tp_heartwood matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/heartwood_teleport
execute if score @s uhc_tp_hellcrags matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/hellcrags_teleport
execute if score @s uhc_tp_highfall_tundra matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/highfall_tundra_teleport
execute if score @s uhc_tp_lorahn_kahl matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/lorahn_kahl_teleport
execute if score @s uhc_tp_maels_desolation matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/maels_desolation_teleport
execute if score @s uhc_tp_merijool matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/merijool_teleport
execute if score @s uhc_tp_nimahj_swamp matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/nimahj_swamp_teleport
execute if score @s uhc_tp_north_tharxax matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/north_tharxax_teleport
execute if score @s uhc_tp_palisades_heath matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/palisades_heath_teleport
execute if score @s uhc_tp_purity_peaks matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/purity_peaks_teleport
execute if score @s uhc_tp_sahd matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/sahd_teleport
execute if score @s uhc_tp_south_tharxax matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/south_tharxax_teleport
execute if score @s uhc_tp_spearhead_forest matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/spearhead_forest_teleport
execute if score @s uhc_tp_veruhkt_plateau matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/veruhkt_plateau_teleport
# execute if score @s uhc_tp_yavhlix matches 1.. unless score @s uhc_allow_tp_countdown matches -1 as @s run function terminus:teleport_to_tower/yavhlix_teleport

# Reset trigger
execute if score @s uhc_tp_akhlo_rohma matches 1.. run scoreboard players reset @s uhc_tp_akhlo_rohma
execute if score @s uhc_tp_anyr_nogur matches 1.. run scoreboard players reset @s uhc_tp_anyr_nogur
execute if score @s uhc_tp_av_sal matches 1.. run scoreboard players reset @s uhc_tp_av_sal
execute if score @s uhc_tp_black_jungle matches 1.. run scoreboard players reset @s uhc_tp_black_jungle
execute if score @s uhc_tp_capital_valley matches 1.. run scoreboard players reset @s uhc_tp_capital_valley
execute if score @s uhc_tp_carmine matches 1.. run scoreboard players reset @s uhc_tp_carmine
execute if score @s uhc_tp_casai matches 1.. run scoreboard players reset @s uhc_tp_casai
execute if score @s uhc_tp_dawn_island matches 1.. run scoreboard players reset @s uhc_tp_dawn_island
execute if score @s uhc_tp_dusk_island matches 1.. run scoreboard players reset @s uhc_tp_dusk_island
execute if score @s uhc_tp_ebonfire matches 1.. run scoreboard players reset @s uhc_tp_ebonfire
execute if score @s uhc_tp_ebony_veldt matches 1.. run scoreboard players reset @s uhc_tp_ebony_veldt
execute if score @s uhc_tp_faehrcyle matches 1.. run scoreboard players reset @s uhc_tp_faehrcyle
execute if score @s uhc_tp_frozen_bite matches 1.. run scoreboard players reset @s uhc_tp_frozen_bite
execute if score @s uhc_tp_grand_pike_canyon matches 1.. run scoreboard players reset @s uhc_tp_grand_pike_canyon
execute if score @s uhc_tp_gulf_of_drehmal matches 1.. run scoreboard players reset @s uhc_tp_gulf_of_drehmal
execute if score @s uhc_tp_heartwood matches 1.. run scoreboard players reset @s uhc_tp_heartwood
execute if score @s uhc_tp_hellcrags matches 1.. run scoreboard players reset @s uhc_tp_hellcrags
execute if score @s uhc_tp_highfall_tundra matches 1.. run scoreboard players reset @s uhc_tp_highfall_tundra
execute if score @s uhc_tp_lorahn_kahl matches 1.. run scoreboard players reset @s uhc_tp_lorahn_kahl
execute if score @s uhc_tp_maels_desolation matches 1.. run scoreboard players reset @s uhc_tp_maels_desolation
execute if score @s uhc_tp_merijool matches 1.. run scoreboard players reset @s uhc_tp_merijool
execute if score @s uhc_tp_nimahj_swamp matches 1.. run scoreboard players reset @s uhc_tp_nimahj_swamp
execute if score @s uhc_tp_north_tharxax matches 1.. run scoreboard players reset @s uhc_tp_north_tharxax
execute if score @s uhc_tp_palisades_heath matches 1.. run scoreboard players reset @s uhc_tp_palisades_heath
execute if score @s uhc_tp_purity_peaks matches 1.. run scoreboard players reset @s uhc_tp_purity_peaks
execute if score @s uhc_tp_sahd matches 1.. run scoreboard players reset @s uhc_tp_sahd
execute if score @s uhc_tp_south_tharxax matches 1.. run scoreboard players reset @s uhc_tp_south_tharxax
execute if score @s uhc_tp_spearhead_forest matches 1.. run scoreboard players reset @s uhc_tp_spearhead_forest
execute if score @s uhc_tp_veruhkt_plateau matches 1.. run scoreboard players reset @s uhc_tp_veruhkt_plateau
# execute if score @s uhc_tp_yavhlix matches 1.. run scoreboard players reset @s uhc_tp_yavhlix
