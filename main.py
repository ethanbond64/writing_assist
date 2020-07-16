print('blah')
from tokenize import textToParagraphs
from cluster import paragraphsToClusters

stopwords = [
'me',
'my',
'myself',
'we',
'our',
'ours',
'ourselves',
'you',
'your',
'yours',
'yourself',
'yourselves',
'he',
'him',
'his',
'himself',
'she',
'her',
'hers',
'herself',
'it',
'its',
'itself',
'they',
'them',
'their',
'theirs',
'themselves',
'what',
'which',
'who',
'whom',
'this',
'that',
'these',
'those',
'am',
'is',
'are',
'was',
'were',
'be',
'been',
'being',
'have',
'has',
'had',
'having',
'do',
'does',
'did',
'doing',
'a',
'an',
'the',
'and',
'but',
'if',
'or',
'because',
'as',
'until',
'while',
'of',
'at',
'by',
'for',
'with',
'about',
'against',
'between',
'into',
'through',
'during',
'before',
'after',
'above',
'below',
'to',
'from',
'up',
'down',
'in',
'out',
'on',
'off',
'over',
'under',
'again',
'further',
'then',
'once',
'here',
'there',
'when',
'where',
'why',
'how',
'all',
'any',
'both',
'each',
'few',
'more',
'most',
'other',
'some',
'such',
'no',
'nor',
'not',
'only'
'own',
'same',
'so',
'than',
'too',
'very',
'can',
'will',
'just',
'dont',
'should',
'now'
]
text = """
The 7-0 vote came the night of July 14.

Hundreds of years of Black blood spilled that basically fills the cup we drink from today, said Councilman Keith Young, one of two African American members of the body and the measure's chief proponent.

It is simply not enough to remove statutes. Black people in this country are dealing with issues that are systemic in nature.

The unanimously passed resolution does not mandate direct payments. Instead, it will make investments in areas where Black residents face disparities.

Wednesday session on signs of progress in developing a vaccine for the coronavirus. Twitter Inc. fell in after-hours trading after accounts of some of America’s most prominent political and business leaders were hacked. Crude oil declined, while Treasuries were little changed. The Thai baht retreated.

While the Chinese economy returned to growth in the second quarter, retail sales in June missed estimates as they continued to contract, highlighting how confidence remains fragile.

Asian stocks were lower Thursday along with European and U.S. equity futures as investors parsed a slew of economic data in China that showed the path of economic recovery from the pandemic remains bumpy. The dollar edged higher.
"""

text2 = """
This is one of the most important charts.

It shows in orange bars the daily official number of cases in the Hubei province: How many people were diagnosed that day.

The grey bars show the true daily coronavirus cases. The Chinese CDC found these by asking patients during the diagnostic when their symptoms started.

Crucially, these true cases weren’t known at the time. We can only figure them out looking backwards: The authorities don’t know that somebody just started having symptoms. They know when somebody goes to the doctor and gets diagnosed.

What this means is that the orange bars show you what authorities knew, and the grey ones what was really happening.

On January 21st, the number of new diagnosed cases (orange) is exploding: there are around 100 new cases. In reality, there were 1,500 new cases that day, growing exponentially. But the authorities didn’t know that. What they knew was that suddenly there were 100 new cases of this new illness.

Two days later, authorities shut down Wuhan. At that point, the number of diagnosed daily new cases was ~400. Note that number: they made a decision to close the city with just 400 new cases in a day. In reality, there were 2,500 new cases that day, but they didn’t know that.

The day after, another 15 cities in Hubei shut down.

Up until Jan 23rd, when Wuhan closes, you can look at the grey graph: it’s growing exponentially. True cases were exploding. As soon as Wuhan shuts down, cases slow down. On Jan 24th, when another 15 cities shut down, the number of true cases (again, grey) grinds to a halt. Two days later, the maximum number of true cases was reached, and it has gone down ever since.

Note that the orange (official) cases were still growing exponentially: For 12 more days, it looked like this thing was still exploding. But it wasn’t. It’s just that the cases were getting stronger symptoms and going to the doctor more, and the system to identify them was stronger.

This concept of official and true cases is important. Let’s keep it in mind for later.

The rest of regions in China were well coordinated by the central government, so they took immediate and drastic measures. This is the result:
Image for post
Image for post

Every flat line is a Chinese region with coronavirus cases. Each one had the potential to become exponential, but thanks to the measures happening just at the end of January, all of them stopped the virus before it could spread.

Meanwhile, South Korea, Italy and Iran had a full month to learn, but didn’t. They started the same exponential growth of Hubei and passed every other Chinese region before the end of February.
"""
# print(text)
ps = textToParagraphs(text2)
print(paragraphsToClusters(ps,stop_words=stopwords))