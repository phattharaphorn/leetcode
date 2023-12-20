import pprint

text = "It's the first of April. It's still cold in the UK. But I'm going to the museum so it should be a wonderful day"

counts = {}
for word in text.split():
    counts.setdefault(word, 0)
    counts[word] += 1

pprint.pprint(counts)

