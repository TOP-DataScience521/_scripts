from pprint import pp


# публичные (public) атрибуты — доступные для чтения, записи
# частные (private) атрибуты — доступные для чтения, недоступные для записи
# защищённые (protected) атрибуты — недоступные для чтения и записи


class AudioPlayer:
    # "публичный" атрибут класса
    default_path = '.'
    # "частный" атрибут класса
    _formats = 'WAV', 'MP3', 'OGG'
    # "защищённый" атрибут класса
    __codecs = 'LLAM', 'PTF', 'Vorbis'
    
    def __init__(self):
        # "публичный" атрибут экземпляра
        self.volume = ...
        # "частный" атрибут экземпляра
        self._track_info = ...
        # "защищённый" атрибут экземпляра
        self.__codec = ...
    
    def show_codecs(self):
        print(self.__codecs, self.__codec, sep='\n')
    
    def _set_track_info(self, new_info):
        self._track_info = new_info
    
    def __set_codec(self, new_codec):
        if new_codec in self.__codecs:
            self.__codec = new_codec
        else:
            raise ValueError


# >>> pp(AudioPlayer.__dict__)
# mappingproxy({'__module__': '__main__',
#               'default_path': '.',
#               '_formats': ('WAV', 'MP3', 'OGG'),
#               '_AudioPlayer__codecs': ('LLAM', 'PTF', 'Vorbis'),
#               '__init__': <function AudioPlayer.__init__ at 0x0000024D2D8339C0>,
#               'show_codecs': <function AudioPlayer.show_codecs at 0x0000024D2D87C0E0>,
#               '_set_track_info': <function AudioPlayer._set_track_info at 0x0000024D2D87C180>,
#               '_AudioPlayer__set_codec': <function AudioPlayer.__set_codec at 0x0000024D2D87C220>,
#               '__dict__': <attribute '__dict__' of 'AudioPlayer' objects>,
#               '__weakref__': <attribute '__weakref__' of 'AudioPlayer' objects>,
#               '__doc__': None})


# >>> AudioPlayer.default_path
# '.'
# >>> AudioPlayer.default_path = r'.\folder'
# >>> AudioPlayer.default_path
# '.\\folder'


# >>> AudioPlayer._formats
# ('WAV', 'MP3', 'OGG')
# >>>
# >>> AudioPlayer._formats = ('WAV', 'MP3', 'OGG', 'FLAC')
# >>> AudioPlayer._formats
# ('WAV', 'MP3', 'OGG', 'FLAC')


# включается механизм подмены имён (name mangling)
# >>> AudioPlayer.__codecs
# AttributeError: type object 'AudioPlayer' has no attribute '__codecs'
# >>>
# >>> AudioPlayer._AudioPlayer__codecs
# ('LLAM', 'PTF', 'Vorbis')
# >>>
# >>> AudioPlayer._AudioPlayer__codecs = ('LLAM', 'PTF', 'Vorbis', 'ffmpeg')
# >>> AudioPlayer._AudioPlayer__codecs
# ('LLAM', 'PTF', 'Vorbis', 'ffmpeg')


# >>> inst1 = AudioPlayer()
# >>> inst1.__dict__
# {'volume': Ellipsis, '_track_info': Ellipsis, '_AudioPlayer__codec': Ellipsis}
# >>>
# >>> inst1.__codec
# AttributeError: 'AudioPlayer' object has no attribute '__codec'
# >>>
# >>> inst1._AudioPlayer__codec
# Ellipsis

