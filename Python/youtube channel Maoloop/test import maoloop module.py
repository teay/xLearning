######################################################################
# การimport module แบบที่1    ที่นิยมใช้กัน
# 1.1 โดยพิมพ์ importตามด้วยชื่อmodule
import maoloop
maoloop.loop1()

# 1.2 โดยพิมพ์ importตามด้วยชื่อmodule โดยย่อชื่อ module ให้สั้นลงเป็น ml
import maoloop as ml
ml.loop1()
######################################################################
# การimport module แบบที่2 
# โดยพิมพ์ fromตามด้วยชื่อmodule importตามด้วยชื่อFunction

# 2.1เรียกใช้เฉพาะFunction    loopname
from maoloop import loopname
loopname()

# 2.2เรียกใช้ทั้งFunction       loopname และ loop1
from maoloop import loopname ,loop1
loopname()
loop1()
######################################################################
# การimport module แบบที่3
# โดยพิมพ์ fromตามด้วยชื่อmodule importตามด้วยเครื่องหมาย* คือเรียกใช้ทุกFuntionที่อยู่ในmoduleนี้
from maoloop import *
loopname()
loop1()