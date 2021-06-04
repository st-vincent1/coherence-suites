# Dialogue Coherence Test Suites

## File Structure
```
root
|-data
| |-pol : Polish test suites
| |-spa : Spanish test suites
|-src
| |- interpret_scores.py : script for interpreting model outputs (as list of scores for test cases)
| |- scoring_pseudocode.md : a pseudocode of a scoring function which needs to be implemented for the model
```
## Usage
### Marking within the SLT Challenge
This information is compiled to help student markers when reading this assignment.
1. What challenge is this?
The challenge we had decided to participate in is the News Translation task, but instead of submitting a system we decided to submit a test suite which is something the challenge authors also call for (http://www.statmt.org/wmt21/translation-task.html).

Although we originally planned to submit this work to that challenge (it was live), we decided against it because the challenge this year (announced after the SLT Challenge started) does not support most of our language pairs. Instead we will be submitting this work to WMT on its own in due course.

2. How do I know how good your test suite is w.r.t. other test suites?
Since every test suite evaluates a different phenomenon, there's no easy way to or purpose in comparing them. The test suites are supposed to evaluate other models instead. In our report we provided a description of a short experiment we did, to show that a contextual model of our own scores ~91% accuracy on a test suite; if we had more models, we could then perform comparative evaluation.


### Label semantics
The following are the semantics for labels in `*.label` files:
1. Polish
    - speaker's gender: 0 - feminine, 1 - masculine;
    - interlocutor's gender and number: 0 - singular feminine, 1 - singular masculine, 2 - plural feminine, 3 - plural mixed;
    - formality relations: 0 - formal, 1 - informal.
    
2. Spanish
    - speaker's gender: 0 - feminine, 1 - masculine;
    - interlocutor's number: 0 - singular, 1 - plural;
    - formality relations: 0 - formal, 1 - informal.
    

### Evaluating your own methods
In order to evaluate your own model's bias or accuracy:
1. Write a scoring function for your model (see `src/scoring_pseudocode.md` for ideas)
2. Produce a `scores` file for the given test suite
3. Compute accuracy or bias using the following: `to be established`
## Support
For any queries or errors, please either raise an Issue or DM the authors.

## Contributing
Currently no contributions are accepted.

## Authors and acknowledgement
This project has been built as part of the SLT Challenge within the Centre for Doctoral Training (CDT) at the University of Sheffield.
The main researchers: Sebastian T. Vincent, Thomas AF Green and Danae Sanchez-Villegas are PhD students within the CDT.

We would like to thank our advisors Dr Carolina Scarton and Dr Loic Barrault for assisting us in this project,
as well as the admins of opensubtitles.org for distributing the data to us.

## License

## Project status
As of 4 June 2021, this project is shipped as a deliverable to the SLT Challenge, but will be developed further in due course,
as part of the head researcher's (Sebastian's) PhD.
