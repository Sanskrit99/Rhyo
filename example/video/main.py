from pathlib import Path
from ffmpy3 import FFmpeg


class Main:
    def __init__(self, path: str):
        self.path = Path(path)
        if self.path.exists():
            pass
        else:
            raise Exception()
        m3u8 = Path('./base/m3u8')
        if m3u8.exists():
            pass
        else:
            raise Exception()
        self.name = self.path.stem
        self.p0 = m3u8.joinpath(self.name)
        if self.p0.exists():
            pass
        else:
            self.p0.mkdir()

    def f0(self, o: str):
        FFmpeg(inputs={self.path.__str__(): None}, outputs={None: o}).run()

    def d0(self, segment_time: int, segment_list_entry_prefix: str):
        path = self.p0.__str__().replace('\\', '/')
        o = f'-c:v libx264 -c:a aac -strict -2 -f segment -segment_time {segment_time} -segment_list_entry_prefix {segment_list_entry_prefix}/ -segment_list ./{path}/{self.name}.m3u8 ./{path}/{self.name}-%4d.ts'
        self.f0( o)

    def d1(self, segment_time: int, segment_list_entry_prefix: str):
        o =  r'-c:v libx264 -c:a copy  -f hls -hls_time 10 -hls_key_info_file D:/Aoc/BigProject/Kafk/Python/Server/data/base/enc.keyinfo -hls_playlist_type vod -hls_segment_filename ./huahai/huahai-%4d.ts ./huahai/huahai.m3u8'



if __name__ == '__main__':
    M = Main(r'./base/source/video.mp4')
    M.d0(10, 'snad')
