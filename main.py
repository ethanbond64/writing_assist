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

Every flat line is a Chinese region with coronavirus cases. Each one had the potential to become exponential, but thanks to the measures happening just at the end of January, all of them stopped the virus before it could spread.

Meanwhile, South Korea, Italy and Iran had a full month to learn, but didn’t. They started the same exponential growth of Hubei and passed every other Chinese region before the end of February.
"""

text3 = """
sweden has famously followed a different coronavirus strategy than most of the rest of the Developed world: Let the virus run loose, curb it enough to make sure it doesn’t overwhelm the healthcare system like in Hubei, Italy or Spain, but don’t try to eliminate it. They think stopping it completely is impossible. The natural consequence is that most citizens get infected, and that eventually slows down the epidemic. That’s why, in short, people call that strategy “Herd Immunity”.

The other strategy is the Hammer and the Dance: Aggressively attack the coronavirus by locking down the economy. Once curbed, jump into the Dance by replacing the aggressive lockdown with cheap and intelligent measures to control the virus.

Some countries and states, such as the Netherlands and the UK, or US states like Texas and Georgia, have implemented measures in between the two strategies. So which strategy is best?

1. Sweden’s Case
What’s the Situation in Sweden?

People in Sweden haven’t been locked down the way they have been in other countries.

Swedes have been free to walk around. Elementary and middle schools have remained open, as well as businesses like bars, clubs, gyms, or restaurants.

So what has been the result?



The best way to understand Sweden is by comparing it to the countries that look the most like it. Thankfully, we have nearly perfect comparisons: other Nordic countries. They share a similar culture, weather, behavior, economy, demographics, and received coronavirus cases at approximately the same time, as we can see in the first half of March. Other countries aren’t as comparable, since they either suffered much earlier outbreaks (such as Italy, Spain, France…), have a different density (such as the UK, Germany, France, Italy, Belgium…), or have different demographics (such as large households with kids and grand-parents in the Mediterranean), etc.

Some people will complain at this comparison. They will say: “But Italy has more deaths per million inhabitants! And Spain! And Belgium!” So let’s dig slightly deeper. What other countries can we compare Sweden to?
Who Should We Compare Sweden to?


On the horizontal axis, we have how many cases there were in that country initially. I picked cases per inhabitant, although you can pick total cases to measure the initial outbreak, and the correlation is even stronger, with R2~0.5. I chose March 22nd because most developed countries only took measures after March 15th, and it took at least 2 weeks for them to have an impact on numbers, so the number of cases on March 22nd is close to the last time when cases were determined by luck and not by action. The vertical axis shows deaths per million inhabitants as of the beginning of June. This conveys the impact of the individual country strategy since March. Both axes are logarithmic.

This graph has plenty of insights. The horizontal axis shows initial cases in mid March per million inhabitants, to give a sense of how unlucky that country was to get an early outbreak. The vertical axis tells you deaths per million inhabitants. We can see that the bigger the initial outbreak, the more deaths.

This tells you, for example, that you shouldn’t compare Sweden to Spain or Italy, because these countries were unlucky enough to have many more initial cases. Same thing for countries like Canada, Lithuania or Slovakia: They had few initial cases. What we should compare here is countries in the same vertical, because that shows countries that had the same initial outbreak. Their management of that initial outbreak determined how many deaths they ended up with.

In that sense, Sweden is by far the worst of its group. It’s done worse than France, Ireland, Netherlands, Portugal, Denmark, Norway, Austria, Germany, Czechia, Australia, Estonia, Slovenia, Malta, Finland… This group includes Denmark, Finland, and Norway, other Nordic countries, which is very convenient for our analysis.

The graph also shows why defenders of Sweden’s strategy pick the UK or Belgium as comparisons: They are the only countries with more deaths per person and a similar number of initial cases per capita. However, this is not a fair comparison.



Both Belgium and the UK have had massive initial outbreaks in comparison to Sweden’s. These are much harder to control. They are also much more connected internationally, with many more incoming infections. They have a much higher population density, worse population health, and more people per household.

On top of that, the UK has been a leader of coronavirus mismanagement and bad luck: It took too long to impose a lockdown, the lockdown was not as strong as in other countries, sick patients were sent back into nursing homes…

Meanwhile, Belgium is counting approximately twice as many deaths as most other countries: Half of the country’s deaths are in care homes, but of those only 5% have been tested. 95% have simply been assumed to be caused by the coronavirus. It also suffered from a massive initial peak that has since been controlled.
Sweden vs. Other Nordic Countries

Based on all of the above, to clearly get a sense of the Herd Immunity strategy vs. the Hammer and the Dance, the best way is to compare Sweden to other Nordic countries: Denmark, Norway, and Finland. Also, for contrast, I included Austria and Czechia, as other countries East European countries with a similar size (~10 million inhabitants) and a comparable initial outbreak.



As of June 10th, Sweden had more daily cases than all of its Scandinavian neighbors combined, and this trend is only getting worse. In fact, if you add up the cases of the 21 EU countries with the least cases last week, Sweden still has more cases than all of them combined.

In the graph above, we can see that Sweden started off much better than its neighbors Denmark and Norway, as well as Austria, and similar to Czechia and Finland. However, all these other countries applied a Hammer in the second half of March. Two weeks later, at the beginning of April, we could see their cases go down together while Sweden’s kept going up.

This is despite the fact that Sweden does not exhaustively count its coronavirus cases:



This shows the percentage of tests that turn out positive. The lower that percentage, the more confident you are that you’re counting all cases. Sweden is testing 10 times less than its neighbors, because it doesn’t really care about total cases, since it’s not trying to eliminate the epidemic. As a result, they’re undercounting cases.

Even then, cases are only as good as the official records. A more reliable data point is deaths.

So what about deaths?



While coronavirus deaths have stopped growing in Scandinavian countries and other comparable ones, they’re still piling up in Sweden. To understand why, we need to understand Sweden’s strategy to fight the coronavirus.
The Swedish Strategy

Sweden never went into lockdown. Instead, the country closed its high schools and colleges, forbade gatherings above 50 people on March 27th, and encouraged its citizens to stay home and avoid unnecessary travel. Visitors were banned from nursing homes on March 30th. But beyond that, the government just asked people to work from home as much as possible and to practice social distancing. And it’s obligatory for kids to go to school. Why?

This is how Sweden’s official epidemiologists summarized their strategy:

“It’s impossible to stop the coronavirus. Only Herd Immunity will make that happen. Lockdowns won’t. So let’s flatten the curve to avoid the collapse of the healthcare system, but that’s it. If we lock down the economy, it will be costly and will only postpone the inevitable. Meanwhile, let’s protect older people, since they are the ones dying. The virus is not that bad anyways.”

Some people call this a mitigation strategy, because it reduces the cases so that they don’t overwhelm the healthcare system, but doesn’t go beyond that to completely eliminate most cases. Others label this strategy Herd Immunity, because of the side effect: The belief is that the epidemic will only stop once enough people have been infected and develop immunity against it. For the coronavirus, it is assumed that the moment arrives when around 65% of people have been infected.

Swedish officials don’t like the Herd Immunity label, but it’s useful since it’s memorable, everybody calls it that way, and it does not hide the nasty end result. So I’ll use that.

There are many statements in the description of the strategy from above. Some are true. For example, the measures it declared (banning large gatherings, asking people to work from home, closing high-schools and universities) were enough to flatten the curve. The government also increased the capacity of the healthcare system, which contributed to keeping it working despite the weight of coronavirus cases.

Here are the statements that deserve scrutiny:

    The coronavirus is unstoppable.
    The virus is not that bad.
    We can protect the elderly from it.
    It’s better for the economy to just flatten the curve while the virus spreads through the population than it is to implement the Hammer and the Dance strategy, a heavy lockdown followed by a reopening of the economy.

Let’s look at each one.
2. Is the Coronavirus Unstoppable?
Does the Hammer Work?

Anders Tegnell, Sweden’s head epidemiologist, had stated that there is not enough scientific evidence that lockdowns work, a statement that has been echoed by other Swedish government epidemiologists.

“Closedown, lockdown, closing borders — nothing has a historical scientific basis, in my view. We have looked at a number of European Union countries to see whether they have published any analysis of the effects of these measures before they were started and we saw almost none.”—Anders Tegnell, Sweden’s head epidemiologist.

If I were a Swedish politician and I heard that, I would have instantly started worrying. First, the evidence of that analysis has not been shared, as far as I could find. More importantly, this shows the scientists don’t understand what it’s like to manage in the real world.

Were the scientists waiting for a peer-reviewed scientific study unequivocally proving that lockdowns work? This is not a lab. That doesn’t exist. It was impossible to have a clean analysis with a completely new virus.


The world is messy. Data is imperfect. Are politicians supposed to wait until all evidence is perfect? No. That’s too late. They need to piece together all the data they have and take action, even if it’s not perfect. Because perfect is too late and gets you killed.


And yet… There was evidence, based on everything that had happened in Wuhan, South Korea, Taiwan, Italy…

Since then, plenty of countries have acted on that evidence, and their performance is accumulating. So what did the available evidence indicate?

"""
# print(text)
ps = textToParagraphs(text3)
paragraphsToClusters(ps,stop_words=stopwords)