# OTOT_Task_B2


## Setup Environment
1. Install `Anaconda`.
2. Install `python3.9` environment.
3. Install packages
    ```
    pip install networkx
    pip install pandas
    pip install matplotlib
    conda install spacy
    pip install pytextrank
    ```
4. Install the corpus
    ```
    python -m spacy download en_core_web_sm
    ```
## Graph visualization
If you cannot see this screenshot clearly, please click on it or download it.
![avatar](/marvel.png)
graph.py is the code to implement the graph visualization.
marvel.png is the screenshot of the graph visualization.

### In order to view statistical visualization and text visualization, please check the following link
[Statistical visualization and Text visualization](https://public.tableau.com/app/profile/zhang.junzhe/viz/OTOT_Task_B2/Radarchart)

## Statistical visualization
radar.py is the code to preprocess the data for the statistical visualization.

## Text visualization
textrank.py is the code for extracting a keyword from a line.  
test_textrank.py is the code for testing textrank algorithm. (i.e. main function)