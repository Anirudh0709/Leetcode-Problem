import collections

class Solution:
  def minimumTeachings(
      self,
      n: int,
      languages: list[list[int]],
      friendships: list[list[int]],
  ) -> int:
    languageSets = [set(languages) for languages in languages]
    needTeach = set()
    languageCount = collections.Counter()

    for u, v in friendships:
      if not languageSets[u - 1] & languageSets[v - 1]:
        needTeach.add(u - 1)
        needTeach.add(v - 1)

    for u in needTeach:
      for language in languageSets[u]:
        languageCount[language] += 1

    return len(needTeach) - max(languageCount.values(), default=0)
