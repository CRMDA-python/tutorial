#Regex: Regular Expressions

Real world problem Example:
When we match short DNA sequences (query) to longer sequences (reference), we use tools called aligners or mappers. These tools provide a lot of information about how the query aligns to the reference. Many times, that information is abbreviated in short strings called CIGAR tags. Here are a few examples of a CIGAR tags:


- 75M
- 14M1D61M
- 45M1D30M
- 26M1D49M

Here is what they mean:

__75M__: all 75 nucleotides in the query match (M) the reference

__14M1D61M__: 
- 14M = the first 14 nucleotides in the query match (M) the reference, then
- 1D = there is a missing nucletide (D = deletion) in the query, and then
- 61M = the last 61 nucletides in the query match the reference

## Problem
Sometimes you need to know whether a specific nucleotide in the query matches the reference or not, so you have to split the tag to extract the necessary information. Two options:

- Splitting a CIGAR tag __without__ regular expressions: _possible but painful_
- Splitting a CIGAR tag __with__ regular expressions: _easy and somewhat painful_

Jeet's REGEX Solution:
```{python}
import re
pattern = re.compile(r'(\d+)(\w)')
matches = pattern.findall(tag)
```

#[Interactive tutorial] (https://regexone.com/)
