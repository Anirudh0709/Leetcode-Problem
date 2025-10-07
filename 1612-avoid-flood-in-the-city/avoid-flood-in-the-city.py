from sortedcontainers import SortedSet
class Solution:
  def avoidFlood(self, rains: list[int]) -> list[int]:
    ans = [-1] * len(rains)
    lakeIdToFullDay = {}
    emptyDays = SortedSet()  
    for i, lakeId in enumerate(rains):
      if lakeId == 0:
        emptyDays.add(i)
        continue
      if lakeId in lakeIdToFullDay:
        fullDay = lakeIdToFullDay[lakeId]
        emptyDayIndex = emptyDays.bisect_right(fullDay)
        if emptyDayIndex == len(emptyDays):  # Not found.
          return []
        emptyDay = emptyDays[emptyDayIndex]
        ans[emptyDay] = lakeId
        emptyDays.discard(emptyDay)
      lakeIdToFullDay[lakeId] = i
    for emptyDay in emptyDays:
      ans[emptyDay] = 1
    return ans