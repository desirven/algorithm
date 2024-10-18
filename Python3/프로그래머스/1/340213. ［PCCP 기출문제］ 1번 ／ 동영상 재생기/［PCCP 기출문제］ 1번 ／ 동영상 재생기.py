def solution(video_len, pos, op_start, op_end, commands):
    vp = VideoPlayer(video_len, pos, op_start, op_end)
    for cmd in commands:
        vp.move(cmd)
    return vp.print_pos_time()

class VideoPlayer:
    def __init__(self, video_len, pos, op_start, op_end):
        self.video_len = self.str2time(video_len)
        self.pos = self.str2time(pos)
        self.op_start= self.str2time(op_start)
        self.op_end = self.str2time(op_end)
        self.skip_op()
        
    def str2time(self, strtime):
        return int(strtime[:2])*60 + int(strtime[3:])
    
    def print_pos_time(self):
        return f'{self.pos//60:02d}:{self.pos%60:02d}'
    
    def skip_op(self):
        if self.op_start <= self.pos < self.op_end:
            self.pos = self.op_end
    
    def move(self, command):
        if command == "next":
            self.pos = min(self.video_len, self.pos+10)
        elif command == "prev":
            self.pos = max(0, self.pos-10)
        self.skip_op()
    