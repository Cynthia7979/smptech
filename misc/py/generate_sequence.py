import typing
import os
from collections.abc import Iterable
from typing import Literal

class Explosion:
    _TYPES = {
        'small_ball': 0,
        'large_ball': 1,
        'star': 2,
        'creeper': 3,
        'burst': 4
    }
    def __init__(self, type: Literal['small_ball', 'large_ball', 'star', 'creeper', 'burst'], flicker: bool=False, trail: bool=False, colors: Iterable[int]=None, fade_colors: Iterable[int]=None):
        self.type = Explosion._TYPES[type]
        self.flicker = flicker
        self.trail = trail
        self.colors = colors
        self.fade_colors = fade_colors
    
    def __repr__(self):
        tag = '{'
        tag += f'Type:{self.type}'
        if self.flicker:
            tag += ',Flicker:1b'
        if self.trail:
            tag += ',Trail:1b'
        if self.colors:
            tag += ',Colors:[I;'
            tag += ','.join([str(c) for c in self.colors])
            tag += ']'
        if self.fade_colors:
            tag += ',FadeColors:[I;'
            tag += ','.join([str(fc) for fc in self.fade_colors])
            tag += ']'
        tag += '}'
        return tag

class Firework:
    def __init__(self, x, y, z, lifetime: int, explosions: Iterable[Explosion]):
        # LifeTime is in ticks (1s = 20t)
        self.x, self.y, self.z = x, y, z
        assert lifetime > 0, f'Undefined lifetime {lifetime}.'
        self.lifetime = lifetime
        self.explosions = explosions
    
    def __repr__(self):
        command = 'summon minecraft:firework_rocket'
        command += f' {self.x} {self.y} {self.z}'
        command += ' {'
        command += f'LifeTime:{self.lifetime}'
        if self.explosions:
            command += ',FireworksItem:{id:"firework_rocket",Count:1,tag:{Fireworks:{Explosions:['
            command += ','.join([repr(e) for e in self.explosions])
            command += ']}}}'
        command += '}'
        return command

def hex_to_mcdec(hex: str):
    assert len(hex) <= 6 and 'x' not in hex, 'Invalid hex string. Hex must be formatted RRGGBB and without any prefixes.'
    return int(hex, 16)

def rgb_to_mcdec(r: int, g: int, b: int):
    return int(hex(r)[2:].zfill(2)+hex(g)[2:].zfill(2)+hex(b)[2:].zfill(2), 16)

def generate_mcfunctions(sequence: Iterable[Iterable[Firework]], mcfunctions_path: str, mcfunc_name: str, delays: Iterable[int], delay_unit: Literal['d', 's', 't'], offsets: Iterable[float, float, float]=(0,0,0)):
    offset_x, offset_y, offset_z = offsets
    for ind, frame in enumerate(sequence):
        frame_commands = []
        for firework in frame:
            firework.x -= offset_x
            firework.y -= offset_y
            firework.z -= offset_z
            frame_commands.append(repr(firework))
        if ind > 0:
            function_name = f'{mcfunc_name}_{ind}.mcfunction'
        else:
            function_name = f'{mcfunc_name}.mcfunction'
        if ind < len(sequence) - 1:
            next_delay = delays[ind % len(delays)]
            frame_commands.append(f'schedule function fireworks:{mcfunc_name}_{ind+1} {next_delay}{delay_unit}')
        with open(os.path.join(mcfunctions_path, function_name), 'w') as f:
            f.write('\n'.join(frame_commands))

def main():
    test_explosion = Explosion('large_ball', trail=1, colors=[hex_to_mcdec('ff00ff')], fade_colors=[hex_to_mcdec('ffffff')])

    ytaj_positioning = (
        (
            Firework(-99952, 105, -99978, 40, [test_explosion]),  # Maelihs tower
            Firework(-99972, 78, -99887, 30, [test_explosion]),   # Khive tower
            Firework(-99964, 54, -99822, 20, [test_explosion]),   # Loeleyhn tower
            Firework(-99759, 106, -99973, 30, [test_explosion]),  # Virtuo tower
            Firework(-99856, 32, -99921, 30, [test_explosion]),  # Big lotus center
        ),
        (   # Drehmal towers
            Firework(-99912, 93, -99996, 30, [test_explosion]),
            Firework(-99898, 96, -100036, 30, [test_explosion]),
            Firework(-99856, 114, -100055, 30, [test_explosion]),
            Firework(-99814, 105, -100034, 30, [test_explosion]),
            Firework(-99800, 78, -99999, 30, [test_explosion]),
            Firework(-99912, 93, -99996, 30, [test_explosion]),
            Firework(-99855, 169, -100030, 60, [test_explosion]),   # Main tower
        )
    )

    generate_mcfunctions(ytaj_positioning, '../../data/fireworks/functions/', 'ytaj', [2], 's')

if __name__ == '__main__':
    main()