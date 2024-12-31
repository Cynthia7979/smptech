import typing
import os
from collections.abc import Iterable
from abc import ABC, abstractmethod
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
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, f'{self.funcname}.mcfunction'), 'w') as f:
            f.write(f'playsound block.note_block.{self.instrument} master @a {x} {y} {z} {self.volume} {self.pitch}')

    @property
    def funcname(self):
        return f'{self.instrument}_{self.note}'

class PlayABC(ABC):
    @abstractmethod
    def setup_func(self, play_at_x: float, play_at_y: float, play_at_z: float, path: str):
        raise NotImplementedError('Cannot call setup_func on an abstract class.')

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError('Cannot call __repr__ on an abstract class.')

class PlaySound(PlayABC):
    def __init__(self, time: float, sound: str, pitch: float, volume: float=1):
        assert '.' in sound, f'"{sound}" doesn\'t seem like a valid Minecraft sound.'
        if time < 0:
            raise ValueError('Again, your time is negative')
        self.time = time
        self.sound = sound
        self.pitch = pitch
        self.volume = volume
        self.mcfunc_path = None
    
    def setup_func(self, play_at_x: float, play_at_y: float, play_at_z: float, path: str):
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, f'{self.funcname}.mcfunction'), 'w') as f:
            f.write(f'playsound {self.sound} master @a {play_at_x} {play_at_y} {play_at_z} {self.volume} {self.pitch}')
        self.mcfunc_path = os.path.basename(path)
    
    @property
    def funcname(self):
        return f'{self.sound}_{str(self.pitch).strip("+-")}'

    def __repr__(self):
        if not self.mcfunc_path:
            raise FileNotFoundError('Notes have not been initialized. Call setup_note_func')
        if self.time < 0.05:  # Current tick
            return f'function {NAMESPACE}:{self.mcfunc_path}/{self.funcname}'
        return f'schedule function {NAMESPACE}:{self.mcfunc_path}/{self.funcname} {self.time}s append'

class PlayNote(PlayABC):  # I really want to integrate Note with this but I just can't be bothered
    def __init__(self, time: float, note: Note):
        # Time is in seconds because music
        if time < 0:
            raise ValueError('Why the heck is your time a negative number')
        self.note = note
        self.time = time
        self.mcfunc_path = None
    
    def setup_func(self, play_at_x: float, play_at_y: float, play_at_z: float, path: str):
        self.note.make_mcfunction(play_at_x, play_at_y, play_at_z, path)
        self.mcfunc_path = os.path.basename(path)

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

def generate_fireworks(sequence: Iterable[Iterable[Firework]], mcfunctions_path: str, mcfunc_name: str, delays: Iterable[int], delay_unit: Literal['d', 's', 't'], offsets: Iterable[float, float, float]=(0,0,0), music_function_full_id: str=None):
    offset_x, offset_y, offset_z = offsets
    for ind, frame in enumerate(sequence):
        frame_commands = ['# [Generated with cynthia7979/smptech -b datapack/nye-fireworks generate_sequence.py]']
        if ind == 0 and music_function_full_id:
            frame_commands.append(f'function {music_function_full_id}')
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

def generate_music(sequence: Iterable[PlayNote], mcfunctions_path: str, mcfunc_name: str, notes_path: str, play_at_x: float, play_at_y: float, play_at_z: float):
    notes_commands = []
    for sound in sequence:
        sound.setup_func(play_at_x, play_at_y, play_at_z, notes_path)
        notes_commands.append(repr(sound))
    os.makedirs(mcfunctions_path, exist_ok=True)
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
            Firework(526, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),
            Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),
        ),
        (
            Firework(530, 79, 1858, 30, [Explosion('large_ball', flicker=True, colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('f2a838')])], True),  # d
        ),
        (
            Firework(528, 77, 1858, 20, [Explosion('small_ball', colors=[hex_to_mcdec('1069de'), hex_to_mcdec('36bcf5'), hex_to_mcdec('173ba6')], fade_colors=[hex_to_mcdec('f2a838')])]),  # v
            Firework(532, 77, 1858, 20, [Explosion('small_ball', colors=[hex_to_mcdec('c41c02'), hex_to_mcdec('a61111'), hex_to_mcdec('c70e24')], fade_colors=[hex_to_mcdec('f2a838')])]),  # m
        ),
        (
            Firework(496, 66, 1853, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Shore
            Firework(497, 67, 1873, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Farm 2
            Firework(516, 72, 1859, 30, [Explosion('star', trail=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('bd6904')])], True),  # Adventuring Merchant
            Firework(516, 72, 1859, 15, [Explosion('burst', flicker=True, colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Adventuring Merchant
        ),
        (
            Firework(512, 73, 1817, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Gate tower 2
            Firework(519, 72, 1836, 30, [Explosion('star', trail=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('bd6904')])], True),  # Campfire
            Firework(519, 72, 1836, 15, [Explosion('burst', flicker=True, colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Campfire
        ),
        (
            Firework(502, 72, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Stable
            Firework(507, 68, 1866, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Farm 1
            Firework(496, 66, 1853, 30, [Explosion('star', trail=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('bd6904')])]),  # Shore
            Firework(496, 66, 1853, 15, [Explosion('burst', flicker=True, colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Shore
        ),
        (
            Firework(526, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('ffffff')])]),
            Firework(533, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('ffffff')])]),
        ),
        (
            Firework(547, 76, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Outside cemetary
            Firework(539, 72, 1844, 30, [Explosion('large_ball', colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('bd6904')])]),  # Inn lower
            Firework(539, 72, 1844, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Inn lower
            Firework(537, 70, 1838, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('5c9aff')])]),  # Marketplace 3
            Firework(535, 67, 1831, 30, [Explosion('star', colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('bd6904')])]),  # Marketplace Center
            Firework(535, 67, 1831, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Marketplace Center
        ),
        (
            Firework(526, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('ffffff')])]),
            Firework(533, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('ffffff')])]),
        ),
        (
            Firework(526, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('ffffff')])]),
            Firework(533, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934'), hex_to_mcdec('42e352')], fade_colors=[hex_to_mcdec('ffffff')])]),
            Firework(507, 68, 1866, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 1
            Firework(497, 67, 1873, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 2
            Firework(510, 68, 1878, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 3
            Firework(491, 64, 1889, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Farm 4
            Firework(512, 73, 1817, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Gate tower 2
            Firework(502, 72, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Stable
            Firework(539, 72, 1844, 30, [Explosion('large_ball', colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn lower
            Firework(539, 72, 1844, 15, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e'), hex_to_mcdec('173ba6')])]),  # Inn lower
            Firework(547, 76, 1843, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Outside cemetary
            Firework(537, 70, 1838, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('burst', trail=True, colors=[hex_to_mcdec('fae76e')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace 3
            Firework(535, 67, 1831, 30, [Explosion('large_ball', trail=True, colors=[hex_to_mcdec('6f46b3'), hex_to_mcdec('f2248b')], fade_colors=[hex_to_mcdec('c15adb')])]),  # Marketplace Center
            Firework(535, 67, 1831, 15, [Explosion('burst', colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Marketplace Center
            Firework(496, 66, 1853, 30, [Explosion('large_ball', trail=True, colors=[hex_to_mcdec('118a29')], fade_colors=[hex_to_mcdec('c1f5cb'), hex_to_mcdec('daf5df')])]),  # Shore
            Firework(496, 66, 1853, 15, [Explosion('burst', colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Shore
            Firework(519, 72, 1836, 50, [Explosion('small_ball', colors=[hex_to_mcdec('8a0899')])]),  # Campfire
        ),
        (
            # Firework(526, 78, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),
            # Firework(533, 76, 1859, 0, [Explosion('burst', colors=[hex_to_mcdec('166934')], fade_colors=[hex_to_mcdec('ffffff')])]),
            Firework(507, 68, 1866, 30, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),  # Farm 1
            Firework(497, 67, 1873, 30, [Explosion('burst', colors=[hex_to_mcdec('781106')])]),  # Farm 2
            Firework(510, 68, 1878, 30, [Explosion('burst', colors=[hex_to_mcdec('fae76e')])]),  # Farm 3
            Firework(491, 64, 1889, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('166934')])]),  # Farm 4
            Firework(512, 73, 1817, 30, [Explosion('burst', colors=[hex_to_mcdec('fae76e')])]),  # Gate tower 1
            Firework(500, 73, 1818, 30, [Explosion('burst', colors=[hex_to_mcdec('fae76e')])]),  # Gate tower 2
            Firework(502, 72, 1843, 30, [Explosion('burst', colors=[hex_to_mcdec('781106')])]),  # Stable
            # Firework(539, 72, 1844, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Inn lower
            Firework(539, 72, 1844, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6'), hex_to_mcdec('fae76e')])]),  # Inn lower
            Firework(547, 76, 1843, 30, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),  # Inn
            Firework(562, 70, 1860, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('781106')])]),  # Flowerpot hut
            Firework(568, 74, 1844, 30, [Explosion('burst', colors=[hex_to_mcdec('781106')])]),  # Library
            Firework(551, 65, 1869, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('fae76e')])]),  # Outside cemetary
            Firework(537, 70, 1838, 30, [Explosion('burst', colors=[hex_to_mcdec('fae76e')])]),  # Marketplace 1
            Firework(527, 70, 1828, 30, [Explosion('burst', colors=[hex_to_mcdec('166934')])]),  # Marketplace 2
            Firework(544, 70, 1834, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('166934')])]),  # Marketplace 3
            # Firework(535, 67, 1831, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Marketplace Center
            Firework(535, 67, 1831, 30, [Explosion('burst', colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Marketplace Center
            # Firework(496, 66, 1853, 30, [Explosion('star', flicker=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('a16100')], fade_colors=[hex_to_mcdec('ffffff')])]),  # Shore
            Firework(496, 66, 1853, 30, [Explosion('burst', colors=[hex_to_mcdec('1069de'), hex_to_mcdec('173ba6')])]),  # Shore
            Firework(519, 72, 1836, 45, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('fae76e')])]),  # Campfire
            Firework(486, 86, 1879, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('166934')])]),  # Farm tree 1
            Firework(520, 83, 1896, 30, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('166934')])]),  # Farm/church tree
            # Firework(522, 68, 1855, 15, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('8a0899')]), Explosion('creeper', colors=[hex_to_mcdec('8a0899')]), Explosion('creeper', colors=[hex_to_mcdec('4624bf')]), Explosion('creeper', colors=[hex_to_mcdec('9c0852')], fade_colors=[hex_to_mcdec('c15adb')])]),  # Map
            # Firework(530, 70, 1848, 15, [Explosion('small_ball', trail=True, colors=[hex_to_mcdec('bd6904')]), Explosion('creeper', colors=[hex_to_mcdec('f2a838')]), Explosion('creeper', colors=[hex_to_mcdec('ffc400')]), Explosion('creeper', colors=[hex_to_mcdec('bd6904')], fade_colors=[hex_to_mcdec('fcf49a')])]),  # Well
            Firework(522, 68, 1855, 45, [Explosion('large_ball', trail=True, colors=[hex_to_mcdec('8a0899'), hex_to_mcdec('9c0852')], fade_colors=[hex_to_mcdec('c15adb')]), Explosion('creeper', colors=[hex_to_mcdec('9c0852')], fade_colors=[hex_to_mcdec('c15adb')])]),  # Map
            Firework(522, 68, 1855, 30, [Explosion('burst', flicker=True, colors=[hex_to_mcdec('4624bf')])]),  # Map
            Firework(530, 70, 1848, 45, [Explosion('large_ball', trail=True, colors=[hex_to_mcdec('f2a838'), hex_to_mcdec('bd6904')], fade_colors=[hex_to_mcdec('ffc400')]), Explosion('creeper', colors=[hex_to_mcdec('bd6904')], fade_colors=[hex_to_mcdec('fcf49a')])]),  # Well
            Firework(530, 70, 1848, 30, [Explosion('burst', flicker=True, colors=[hex_to_mcdec('bd6904')])]),  # Well
            Firework(507, 69, 1850, 45, [Explosion('creeper', trail=True, colors=[hex_to_mcdec('166934')]), Explosion('creeper', colors=[hex_to_mcdec('40ffb6'), hex_to_mcdec('c1f5cb'), hex_to_mcdec('daf5df')]), Explosion('large_ball', colors=[hex_to_mcdec('118a29')], fade_colors=[hex_to_mcdec('c1f5cb'), hex_to_mcdec('daf5df')])], True),  # Drehmal Statue
            Firework(511, 68, 1850, 30, [Explosion('burst', flicker=True, colors=[hex_to_mcdec('166934'), hex_to_mcdec('c1f5cb'), hex_to_mcdec('daf5df')])]),  # Drehmal Statue lower
        ),
        (
            Firework(497, 67, 1873, 55, [Explosion('large_ball', colors=[hex_to_mcdec('166934')])]),
            Firework(500, 73, 1818, 50, [Explosion('star', colors=[hex_to_mcdec('fae76e')])]),
            Firework(562, 70, 1860, 50, [Explosion('large_ball', colors=[hex_to_mcdec('781106')])]),
            Firework(551, 65, 1869, 60, [Explosion('small_ball', colors=[hex_to_mcdec('fae76e')])]),
            Firework(544, 70, 1834, 55, [Explosion('small_ball', colors=[hex_to_mcdec('166934')])]),
            Firework(496, 66, 1853, 65, [Explosion('small_ball', colors=[hex_to_mcdec('fae76e')])]),
            Firework(537, 70, 1838, 65, [Explosion('small_ball', colors=[hex_to_mcdec('166934')])]),
            Firework(507, 68, 1866, 60, [Explosion('large_ball', colors=[hex_to_mcdec('166934')])]),
            Firework(544, 70, 1834, 65, [Explosion('small_ball', colors=[hex_to_mcdec('166934')])]),
            Firework(496, 66, 1853, 55, [Explosion('large_ball', colors=[hex_to_mcdec('fae76e')])]),
            Firework(537, 70, 1838, 60, [Explosion('small_ball', colors=[hex_to_mcdec('166934')])]),
            Firework(507, 68, 1866, 70, [Explosion('creeper', flicker=True, colors=[hex_to_mcdec('166934')])]),
        ),
    )
    generate_fireworks(d1, 'data/fireworks/functions/', 'drabyel', [35, 10, 10, 50, 80, 85, 40, 30, 10, 30, 30, 5], 't', music_function_full_id='fireworks:bgm/drehmal_theme')
    
    theme = [
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
        PlaySound(22.35, 'block.amethyst_block.step', 1),
        PlaySound(22.5, 'block.amethyst_block.chime', 0.9),
        PlaySound(22.35, 'block.amethyst_block.chime', 0.9),
        PlaySound(22.6, 'block.amethyst_block.chime', 1.5),
        PlaySound(22.75, 'block.amethyst_block.chime', 1.5),
        PlaySound(22.75, 'block.amethyst_block.step', 1),
        PlaySound(23, 'block.amethyst_block.chime', 2),
        PlaySound(23.25, 'block.amethyst_block.chime', 2),
        PlaySound(23, 'block.amethyst_block.step', 1),
    ]
    generate_music(theme, 'data/fireworks/functions/bgm', 'drehmal_theme', 'data/fireworks/functions/notes', 530, 68, 1848)

if __name__ == '__main__':
    main()