## Pseudocode for producing a score for the suite (not optimized for batch processing)

### Pseudocode (in pythonic syntax)
```python3 
def score_translation(source, hypothesis):
  score = 0
  # Start predictions from the start_of_sequence token.
  next_token = sos_token
  for k, hyp_token in enumerate(hypothesis):
    # Generate the probability distribution over the vocabulary.
    log_probs = decoder.incremental_forward(next_token, source...)
    # Log-probabilities are added together.
    score = score + log_probs[hyp_token]
    # Assume the previous token is determined by the hypothesis, rather than best prediction.
    next_token = hyp_token
    # End predicting if we find the eos_token
    if next_token == eos_token:
      break
  return score
```

To optimize for batch processing, simply parallelise this function. 
Remember that scores for each hypothesis must no longer be updated once that hypothesis reaches EOS.

### Support
For any queries or errors, please either raise an Issue or DM the authors.