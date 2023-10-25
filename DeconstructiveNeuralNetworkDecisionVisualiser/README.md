# About
This is the Deconstructive Neural Network Decision Visualiser tool
*   This tool seeks to highlight the influence of subsections of the input on the Neural Networks classification

# How to use
- First consult the main.py
- To analyse a paragraph's prediction load the dataset in with pandas
- Then choose the appropriate index and depth that you would like to use to view the prediction
    - Here, depth indicates the number of subsections. For instance, a depth of 3 will recurrently divide the input into halves 3 times (i.e creating 2^3 divisions on the lowest layer)
    - The index indicates the index of the paragraph in the dataset that you would like to be analysed
- Then let the work be done

- TO analyse a sentence's prediction load the sentence dataset in with pandas
- Then repeat the steps but with TreeVisualiser_sentences() instead of TreeVisualiser_paragraphs