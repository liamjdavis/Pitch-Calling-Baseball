# HMM Pitch Caller
This is a hidden markov model that suggests what baseball pitch should be thrown next. The model is trained on 2019 MLB pitch sequences.

## Running the Program
Install all dependencies. Line 27 defines the list "necessaryPitches." Add every pitch in the pitcher's arsenal into this list based on the MLB pitch types index(https://www.mlb.com/glossary/pitch-types.) The observation sequence is defined in the second code block. As the pitcher's outing continues, every pitch must be added to the end of the list. For every pitch, compile and run the program and the suggested pitch will be outputed.

## Usage
This model is meant to assist intuition. It should not be used to call every pitch. The model output is merely a suggestion. Coaches must know their pitchers and call what the pitcher is confident throwing.
