
# ACM CCS 2023 Supporting Files

This is about formal models and code accompanying an ACM CCS 2023 
submission:

# ProVerif

Our ProVerif file models the  key-derivation chains for the 
PCS model in the CCS-submitted paper, written in ProVerif 2.04. 

Our ProVerif model is in the latest  version of ProVerif 2.04, 
as found on ProVerif's git repository (not packaged installers).

When we constructed our ProVerif model, we found a bug in ProVerif 2.04. 
This resulted in several iterations of fixes
with  the ProVerif team, and the final fix was integrated and 
merged into the main branch of the git-repository 
branch of the tool in late 2022. 
However, the 'opam' or other packaged, released installer
of ProVerif2.04 is NOT entirely up-to-date with the git-repo versions; 
i.e., they are not the latest 2.04 version of 
ProVerif, so they do contain our fix, at the time of this writing 
(04/2023).

So, it is paramount to download the latest main-branch 
version of ProVerif2.04 from 
[ProVerif's git repo](https://gitlab.inria.fr/bblanche/proverif.git), 
build it, and check our models with that built of ProVerif 2.04.
Our model was checked with the ProVerif version corresponding to git 
commit "2b7d52ede6598bf62b5dd59243297c8b9415b763" (25 April 2023)

E.g.,

`git clone https://gitlab.inria.fr/bblanche/proverif.git`

`cd proverif`

`./build`

To run any ProVerif file, in the local installation of the latest ProVerif 
2.04, in the  'proverif'  folder containing the build as per the above, 
do:
./proverif filename

E.g., 

`./proverif PCS_AKMA.pv`


To run our model, we recommend a machine with at least 32GB of RAM.

# Tamarin

For our models, we used the latest release Tamarin, 1.6.1.  See, 
[Tamarin](http://tamarin-prover.github.io/)

We provide the following Tamarin-relevant files:
 
 -- `PCS_AKMA.spthy`:  this is our Tamarin model that includes a reference 
to an Tamarin oracle we built, to automate  our proofs
 
 This  file contains the  key-derivation chains for the  PCS model in the 
CCS-submitted paper, written in Tamarin. 
 
 -- `PCS_AKMA_manual_proof.spthy`: this is a saved, manual proof  of the 
lemma "leaks_can_happen" in the model above, without the oracle.
 
 -- `oracle_pcs.py`: this is the Tamarin oracle file, to support the 
proofs in the Tamarin model aforementioned. Ensure that the oracle is 
executable, i,e., if necessary execute `chmod +x oracle_pcs.py`


### Running the Tamarin Models


To prove all lemmas  automatically, using the above oracle (which is 
referenced from within the `PCS_AKMA.spthy` file), type the below 
in a terminal:

`tamarin-prover PCS_AKMA.spthy --proof`


To either load the manual  proof of the lemma "leaks_can_happen" 
provided in our PCS_tamarin_manual.spthy 
file or do the proof yourself in the PCS_AKMA.spthy file, interactively, 
do this. In a terminal, go to the folder where you saved our files, 
and  type:

`tamarin-prover interactive . -Dmanual`

# reOpen5GCore

There are two files within the folder we submitted with this name. They 
contain the code for the 
experimentation that was carried out on the Fraunhofer 
[Open5GCore](https://www.open5gcore.org/), via our additions to the NEF 
containing the AKMA code. 

Unfortunately, due to copyright we cannot share 
the code for the Open5GCore. But, for these files to run, one 
would need an instance of the Open5GCore.

### 1) akma_experiments.py

This file was used to create the baseline timings for a number of AKMA 
calls made to the NEF.  To 
run this file, you can execute the following command in a terminal.

```python code
python akma_experiments.py
```

### 2) akmareg_experiment.py

Inside of this file contains experiments w.r.t. our new, so-called 
AKMAReg, where we  make an extra registration call for each AKMA call.  To 
run this file, you can execute the following command in a 
terminal.

```python code
python akmareg_experiment.py
```

