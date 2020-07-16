## Goal 
To make writing easier by adding a model that iteratively helps create a paper or article


## Sections

### Size and Shape
recursivish. Length of the paper in paragraphs, length of a specific paragraph, length of a sentence within the paragraph

### Structure
classification of types of sentences


## Getting Started

1. Take an article and group paragraphs by topic
   There is now a list of topics, each one has n paragraphs with m sentences
   This might best be described with an adjacency matrix [topic #,paragraph #] where a cell stores the number of sentences
   Or it could be a simple nonlinear regression model, where the inputs are 
     (topic #,length of topic 1 before it,length of topic 2 before it,max s/p 1 before, min s/p 1 before, avg s/p 1 before,**past 3 but with 2)
   model would be good for classification and for providing insight after the user has written a draft, but thats not the goal, the goal is to generate a template to be written into based on topics.

2. Classify sentences as one of a type, this might get pretty rule based but thats ok
   


