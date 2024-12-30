import typing
import os
from collections.abc import Iterable
from typing import Literal

NAMESPACE = 'fireworks'

class Note:
    _INSTRUMENTS = (
        'bass',
        'snare',
        'hat',
        'basedrum',
        'bell',
        'flute',
        'chime',
        'guitar',
        'xylophone',
        'iron_xylophone',
        'cow_bell',
        'didgeridoo',
        'bit',
        'banjo',
        'pling',
        'harp'
    )

    _PITCHES = {
        'fs0': 0.5,
        'gf0': 0.5,
        'g0' : 2**(-11/12),
        'gs0': 2**(-10/12),
        'af0': 2**(-10/12),
        'a0' : 2**(-9/12),
        'as0': 2**(-8/12),
        'bf0': 2**(-8/12),
        'b0' : 2**(-7/12),
        'c1' : 2**(-6/12),
        'cs1': 2**(-5/12),
        'df1': 2**(-5/12),
        'd1' : 2**(-4/12),
        'ds1': 2**(-3/12),
        'ef1': 2**(-3/12),
        'e1' : 2**(-2/12),
        'f1' : 2**(-1/12),
        'fs1': 1,
        'gf1': 1,
        'g1' : 2**(1/12),
        'gs1': 2**(2/12),
        'af1': 2**(2/12),
        'a1' : 2**(3/12),
        'as1': 2**(4/12),
        'bf1': 2**(4/12),
        'b1' : 2**(5/12),
        'c2' : 2**(6/12),
        'cs2': 2**(7/12),
        'df2': 2**(7/12),
        'd2' : 2**(8/12),
        'ds2': 2**(9/12),
        'ef2': 2**(9/12),
        'e2' : 2**(10/12),
        'f2' : 2**(11/12),
        'fs2': 2,
        'gf2': 2
    }
    def __init__(self, inst: str, note: str, volume: float=1):
        assert inst in Note._INSTRUMENTS, f'Invalid instrument "{inst}".'
        assert note in Note._PITCHES.keys(), f'Invalid note: {note}'
        self.instrument = inst
        self.note = note
        self.pitch = Note._PITCHES[note]
        self.volume = volume
    
    def make_mcfunction(self, x: float, y: float, z: float, path: str):
        command = f'playsound block.note_block.{self.instrument} master @a {x} {y} {z} {self.volume} {self.pitch}'
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, self.filename), 'w') as f:
            f.write(command)

    @property
    def filename(self):
        return f'{self.funcname}.mcfunction'

    @property
    def funcname(self):
        return f'{self.instrument}_{self.note}'

class PlayNote:
    def __init__(self, time: float, note: Note):
        # Time is in seconds because music
        if time < 0:
            raise ValueError('Why the heck is your time a negative number')
        self.note = note
        self.time = time
        self.mcfunc_path = None
    
    def setup_note_func(self, play_at_x: float, play_at_y: float, play_at_z: float, path: str):
        self.mcfunc_path = os.path.basename(path)
        self.note.make_mcfunction(play_at_x, play_at_y, play_at_z, path)

    def __repr__(self):
        if not self.mcfunc_path:
            raise FileNotFoundError('Notes have not been initialized. Call setup_note_func')
        if self.time < 0.05:  # Current tick
            return f'function {NAMESPACE}:{self.mcfunc_path}/{self.note.funcname}'
        return f'schedule function {NAMESPACE}:{self.mcfunc_path}/{self.note.funcname} {self.time}s append'

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
    def __init__(self, x, y, z, lifetime: int, explosions: Iterable[Explosion], glowing: bool=False):
        # LifeTime is in game ticks (1s = 20t)
        self.x, self.y, self.z = x, y, z
        assert lifetime >= 0, f'Undefined lifetime {lifetime}.'
        self.lifetime = lifetime
        self.explosions = explosions
        self.glowing = glowing
    
    def __repr__(self):
        command = 'summon minecraft:firework_rocket'
        command += f' {self.x} {self.y} {self.z}'
        command += ' {'
        command += f'LifeTime:{self.lifetime}'
        if self.glowing:
            command += ',Glowing:1b'
        if self.explosions:
            command += ',FireworksItem:{id:"firework_rocket",Count:1,tag:{Fireworks:{Explosions:['
            command += ','.join([repr(e) for e in self.explosions])
            command += ']}}}'
        command += '}'
        return command

def hex_to_mcdec(hex_: str) -> int:
    assert len(hex_) <= 6 and 'x' not in hex_, 'Invalid hex string. Hex must be formatted RRGGBB and without any prefixes.'
    return int(hex_, 16)

def rgb_to_mcdec(r: int, g: int, b: int) -> int:
    return int(hex(r)[2:].zfill(2)+hex(g)[2:].zfill(2)+hex(b)[2:].zfill(2), 16)

def generate_fireworks(sequence: Iterable[Iterable[Firework]], mcfunctions_path: str, mcfunc_name: str, delays: Iterable[int], delay_unit: Literal['d', 's', 't'], offsets: Iterable[float, float, float]=(0,0,0)):
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
            if next_delay == 0:
                frame_commands.append(f'function {NAMESPACE}:{mcfunc_name}_{ind+1}')
            else:
                frame_commands.append(f'schedule function {NAMESPACE}:{mcfunc_name}_{ind+1} {next_delay}{delay_unit}')
        with open(os.path.join(mcfunctions_path, function_name), 'w') as f:
            f.write('\n'.join(frame_commands))
            if ind == 0:
                f.write(f'\nfunction {NAMESPACE}:bgm_test')

def generate_music(sequence: Iterable[PlayNote], mcfunctions_path: str, mcfunc_name: str, notes_path: str, play_at_x: float, play_at_y: float, play_at_z: float):
    notes_commands = []
    for sound in sequence:
        sound.setup_note_func(play_at_x, play_at_y, play_at_z, notes_path)
        notes_commands.append(repr(sound))
    with open(os.path.join(mcfunctions_path, f'{mcfunc_name}.mcfunction'), 'w') as f:
        f.write('\n'.join(notes_commands))

def main():
    test_explosion = Explosion('large_ball', trail=1, colors=[255], fade_colors=[hex_to_mcdec('ff0000')])

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
    generate_fireworks(ytaj_positioning, 'data/fireworks/functions/', 'ytaj', [2], 's')

    drabyel_pos = (
        (
            Firework(507, 69, 1850, 20, [test_explosion]),  # Drehmal Statue
            Firework(507, 68, 1866, 20, [test_explosion]),  # Farm 1
            Firework(497, 67, 1873, 20, [test_explosion]),  # Farm 2
            Firework(510, 68, 1878, 20, [test_explosion]),  # Farm 3
            Firework(491, 64, 1889, 20, [test_explosion]),  # Farm 4
            Firework(486, 86, 1879, 20, [test_explosion]),  # Farm tree 1
            Firework(520, 83, 1896, 20, [test_explosion]),  # Farm/church tree
            Firework(530, 79, 1858, 20, [test_explosion]),  # Church of the Split Deities
            Firework(530, 89, 1880, 20, [test_explosion]),  # Bell tower
            Firework(496, 66, 1853, 20, [test_explosion]),  # Shore
            Firework(516, 72, 1859, 20, [test_explosion]),  # Adventuring Merchant
            Firework(519, 72, 1836, 20, [test_explosion]),  # Campfire
            Firework(530, 70, 1848, 20, [test_explosion]),  # Well
            Firework(522, 68, 1855, 20, [test_explosion]),  # Map
            Firework(547, 76, 1843, 20, [test_explosion]),  # Inn
            Firework(539, 72, 1844, 20, [test_explosion]),  # Inn lower
            Firework(537, 70, 1838, 20, [test_explosion]),  # Marketplace 1
            Firework(527, 70, 1828, 20, [test_explosion]),  # Marketplace 2
            Firework(544, 70, 1834, 20, [test_explosion]),  # Marketplace 3
            Firework(535, 67, 1831, 20, [test_explosion]),  # Marketplace center
            Firework(551, 65, 1869, 20, [test_explosion]),  # Outside cemetary
            Firework(562, 70, 1860, 20, [test_explosion]),  # Flowerpot hut
            Firework(568, 74, 1844, 20, [test_explosion]),  # Library
            Firework(512, 73, 1817, 20, [test_explosion]),  # Gate tower 1
            Firework(500, 73, 1818, 20, [test_explosion]),  # Gate tower 2
            Firework(502, 72, 1843, 20, [test_explosion]),  # Stable
        ),
    )
    generate_fireworks(drabyel_pos, 'data/fireworks/functions/', 'drabyel', [2], 's')
    
    d1 = (
        (
            Firework(0, 0, 0, 0, []),  # Initial delay
        ),
        (
            Firework(526, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])], True),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])], True),
        ),
        (
            Firework(530, 79, 1858, 20, [Explosion('small_ball', flicker=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('f2a838')])], True),  # d
        ),
        (
            Firework(528, 77, 1858, 15, [Explosion('small_ball', colors=[hex_to_mcdec('1069de')], fade_colors=[hex_to_mcdec('f2a838')])], True),  # v
            Firework(532, 77, 1858, 15, [Explosion('small_ball', colors=[hex_to_mcdec('c41c02')], fade_colors=[hex_to_mcdec('f2a838')])], True),  # m
        ),
        (
            Firework(516, 72, 1859, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Adventuring Merchant
            Firework(516, 72, 1859, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Adventuring Merchant
        ),
        (
            Firework(519, 72, 1836, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Campfire
            Firework(519, 72, 1836, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Campfire
        ),
        (
            Firework(507, 68, 1866, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 1
            Firework(497, 67, 1873, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 2
            Firework(510, 68, 1878, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 3
            Firework(491, 64, 1889, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 4
            Firework(512, 73, 1817, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 2
            Firework(502, 72, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Stable
            Firework(496, 66, 1853, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Shore
            Firework(496, 66, 1853, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Shore
        ),
        (
            Firework(526, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
        ),
        (
            Firework(547, 76, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Outside cemetary
            Firework(539, 72, 1844, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn lower
            Firework(539, 72, 1844, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Inn lower
            Firework(537, 70, 1838, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 3
            Firework(535, 67, 1831, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace Center
            Firework(535, 67, 1831, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Marketplace Center
        ),
        (
            Firework(526, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
        ),
        (
            Firework(526, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(507, 68, 1866, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 1
            Firework(497, 67, 1873, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 2
            Firework(510, 68, 1878, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 3
            Firework(491, 64, 1889, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 4
            Firework(512, 73, 1817, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 2
            Firework(502, 72, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Stable
            Firework(539, 72, 1844, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn lower
            Firework(539, 72, 1844, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Inn lower
            Firework(547, 76, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Outside cemetary
            Firework(537, 70, 1838, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 3
            Firework(535, 67, 1831, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace Center
            Firework(535, 67, 1831, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Marketplace Center
            Firework(496, 66, 1853, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Shore
            Firework(496, 66, 1853, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Shore
        ),
        (
            Firework(526, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(507, 68, 1866, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 1
            Firework(497, 67, 1873, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 2
            Firework(510, 68, 1878, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 3
            Firework(491, 64, 1889, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 4
            Firework(512, 73, 1817, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 2
            Firework(502, 72, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Stable
            Firework(539, 72, 1844, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn lower
            Firework(539, 72, 1844, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Inn lower
            Firework(547, 76, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Outside cemetary
            Firework(537, 70, 1838, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 3
            Firework(535, 67, 1831, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace Center
            Firework(535, 67, 1831, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Marketplace Center
            Firework(496, 66, 1853, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Shore
            Firework(496, 66, 1853, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de')])]),  # Shore
        ),
        (
            Firework(526, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),
            Firework(507, 68, 1866, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 1
            Firework(497, 67, 1873, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 2
            Firework(510, 68, 1878, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 3
            Firework(491, 64, 1889, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 4
            Firework(512, 73, 1817, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 2
            Firework(502, 72, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Stable
            Firework(547, 76, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Outside cemetary
            Firework(537, 70, 1838, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 3
            Firework(535, 67, 1831, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace center
            Firework(522, 68, 1855, 20, [Explosion('creeper', trail=True, colors=[hex_to_mcdec('166934')]), Explosion('creeper', flicker=True, colors=[hex_to_mcdec('f2a838')]), Explosion('creeper', trail=True, colors=[hex_to_mcdec('ffffff')])]),  # Map
            Firework(530, 70, 1848, 20, [Explosion('creeper', trail=True, colors=[hex_to_mcdec('166934')]), Explosion('creeper', flicker=True, colors=[hex_to_mcdec('f2a838')]), Explosion('creeper', trail=True, colors=[hex_to_mcdec('ffffff')])]),  # Well
            Firework(507, 69, 1850, 30, [Explosion('creeper', trail=True, colors=[hex_to_mcdec('166934')]), Explosion('creeper', flicker=True, colors=[hex_to_mcdec('f2a838')]), Explosion('creeper', trail=True, colors=[hex_to_mcdec('ffffff')])]),  # Drehmal Statue
        ),
    )
    generate_fireworks(d1, 'data/fireworks/functions/', 'test', [30, 10, 5, 65, 75, 80, 40, 30, 10, 30, 10, 20, 20, 20, 20, 20], 't')
    
    bgm = (
        PlayNote(0, Note('chime', 'c1')),
        PlayNote(0.5, Note('chime', 'ef1')),
        PlayNote(4, Note('chime', 'bf0')),
        PlayNote(4.5, Note('chime', 'f1')),
        PlayNote(8, Note('chime', 'g1')),
        PlayNote(8.5, Note('chime', 'c1')),
        PlayNote(12, Note('chime', 'af1')),
        PlayNote(12.5, Note('chime', 'c1')),
        PlayNote(13, Note('chime', 'bf0')),
        PlayNote(13.25, Note('bass', 'g0')),
        PlayNote(13.5, Note('bass', 'af0')),
        PlayNote(13.75, Note('bass', 'bf0')),
        PlayNote(14, Note('chime', 'c1')),
        PlayNote(14.5, Note('chime', 'ef1')),
        PlayNote(15, Note('bass', 'c1', 0.25)),
        # PlayNote(15, Note('pling', 'c1', 0.25)),
        PlayNote(15.5, Note('bass', 'ef1', 0.25)),
        # PlayNote(15.5, Note('pling', 'ef1', 0.25)),
        PlayNote(16, Note('chime', 'bf0')),
        PlayNote(16.5, Note('chime', 'f1')),
        PlayNote(17, Note('bass', 'bf0', 0.5)),
        # PlayNote(17, Note('pling', 'bf0', 0.5)),
        PlayNote(17.5, Note('bass', 'f1', 0.5)),
        # PlayNote(17.5, Note('pling', 'f1', 0.5)),
        PlayNote(18, Note('chime', 'g1')),
        PlayNote(18, Note('bell', 'g1')),
        PlayNote(18.5, Note('chime', 'c2')),
        PlayNote(18.5, Note('bell', 'c2')),
        PlayNote(19, Note('bass', 'g1', 0.5)),
        PlayNote(19, Note('pling', 'g0', 0.2)),
        PlayNote(19.5, Note('bass', 'c2', 0.5)),
        PlayNote(19.5, Note('pling', 'c1', 0.2)),
        PlayNote(20, Note('chime', 'af0')),
        PlayNote(20, Note('chime', 'af1')),
        PlayNote(20.5, Note('bass', 'c1')),
        PlayNote(20.5, Note('bass', 'af1')),
        PlayNote(21, Note('chime', 'bf0')),
        PlayNote(21, Note('chime', 'bf1')),
        PlayNote(21.5, Note('bass', 'd1')),
        PlayNote(21.5, Note('bass', 'bf1')),
        PlayNote(21.5, Note('bell', 'af1')),
        PlayNote(21.75, Note('bell', 'bf1')),
        PlayNote(21.5, Note('snare', 'gf0', 0.25)),
        # PlayNote(21.625, Note('snare', 'gf0', 0.25)),
        PlayNote(21.75, Note('snare', 'gf0', 0.25)),
        # PlayNote(21.825, Note('snare', 'gf0', 0.25)),
        PlayNote(22, Note('chime', 'c1')),
        PlayNote(22, Note('chime', 'c2')),
        PlayNote(22, Note('bell', 'c2')),
        PlayNote(22, Note('bell', 'c1')),
        PlayNote(22, Note('pling', 'c2')),
        PlayNote(22, Note('pling', 'c1')),
    )
    generate_music(bgm, 'data/fireworks/functions', 'bgm_test', 'data/fireworks/functions/notes', 530, 68, 1848)

if __name__ == '__main__':
    main()