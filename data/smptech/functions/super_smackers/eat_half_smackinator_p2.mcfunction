tellraw @a[tag=smptech.super_smackers.awaiting_eat_half_p2] [{"text":"You just ate your ","color":"yellow"},{"text":"entire, limited edition ","italic":true},{"text":"souvenir for playing in an event. ","italic":false},{"text":"How diabolical.","italic":true}]
tag @a[tag=smptech.super_smackers.awaiting_eat_half_p2] add smptech.super_smackers.awaiting_eat_half_p3
tag @a[tag=smptech.super_smackers.awaiting_eat_half_p2] remove smptech.super_smackers.awaiting_eat_half_p2
schedule function smptech:super_smackers/eat_half_smackinator_p3 4s