import collections
import Exp10_2 as module
# VAibhav Bhaliya    68   SeitB_B3
queue = collections.deque(["Mon","Tue","Wed"])
print(queue)

module.add(queue)
module.popfront(queue)
module.rotate(queue)
module.extend(queue)
