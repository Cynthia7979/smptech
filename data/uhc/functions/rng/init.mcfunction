scoreboard objectives add uhc_math dummy
scoreboard players set #constant uhc_math 104718471
execute unless score #lcg uhc_math matches ..0 unless score #lcg uhc_math matches 1.. run function uhc:rng/get_new_uuid_seed

scoreboard objectives add uhc_utils dummy

data modify storage uhc:uhc towers set value ["akhlo'rohma","anyr'nogur","av'sal","black jungle","capital valley","carmine","casai","dusk","dawn","ebonfire","ebony veldt","faehrcyle","frozen bite","grand pike","gulf","heartwood","hell","highfall","lorahn'kahl","mael's","merijool","nimahj","north tharxax","palisades","purity peaks","sahd","south tharxax","spearhead","veruhkt"]
# data modify storage uhc:uhc towers set value ["akhlo'rohma","anyr'nogur","av'sal","capital valley","carmine","casai","ebonfire","ebony veldt","grand pike","gulf","heartwood","highfall","lorahn'kahl","mael's","merijool","nimahj","north tharxax","palisades","purity peaks","south tharxax","spearhead","veruhkt"]
data modify storage uhc:uhc towers_shuffled set value []

scoreboard objectives add uhc_comp dummy
data modify storage uhc:uhc akhlo set value "akhlo'rohma"
data modify storage uhc:uhc anyr set value "anyr'nogur"
data modify storage uhc:uhc avsal set value "av'sal"
data modify storage uhc:uhc bjungle set value "black jungle"
data modify storage uhc:uhc capital set value "capital valley"
data modify storage uhc:uhc carmine set value "carmine"
data modify storage uhc:uhc casai set value "casai"
data modify storage uhc:uhc dusk set value "dusk"
data modify storage uhc:uhc dawn set value "dawn"
data modify storage uhc:uhc ebonfire set value "ebonfire"
data modify storage uhc:uhc ebony set value "ebony veldt"
data modify storage uhc:uhc faehrcyle set value "faehrcyle"
data modify storage uhc:uhc bite set value "frozen bite"
data modify storage uhc:uhc pike set value "grand pike"
data modify storage uhc:uhc gulf set value "gulf"
data modify storage uhc:uhc heartwood set value "heartwood"
data modify storage uhc:uhc hell set value "hell"
data modify storage uhc:uhc highfall set value "highfall"
data modify storage uhc:uhc lorahn set value "lorahn'kahl"
data modify storage uhc:uhc mael set value "mael's"
data modify storage uhc:uhc merijool set value "merijool"
data modify storage uhc:uhc nimahj set value "nimahj"
data modify storage uhc:uhc ntharxax set value "north tharxax"
data modify storage uhc:uhc palisades set value "palisades"
data modify storage uhc:uhc purity set value "purity peaks"
data modify storage uhc:uhc sahd set value "sahd"
data modify storage uhc:uhc stharxax set value "south tharxax"
data modify storage uhc:uhc spearhead set value "spearhead"
data modify storage uhc:uhc veruhkt set value "veruhkt"