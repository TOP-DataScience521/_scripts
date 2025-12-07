from graphviz import Source
from numpy import arange
from sklearn.tree import DecisionTreeClassifier, export_graphviz

from pathlib import Path
from sys import path


x = arange(20).reshape(-1, 1)
y = ['о', 'с', 'с', 'с', 'с', 'о', 'о', 'о', 'о', 'с', 'с', 'с', 'с', 'о', 'о', 'о', 'о', 'о', 'о', 'с']


model = DecisionTreeClassifier(criterion='entropy')
model.fit(x, y)

Source(export_graphviz(model)).render(
    format='png', 
    outfile=Path(path[0]) / 'dec_tree output/simple.png'
)


model = DecisionTreeClassifier(criterion='entropy', min_samples_split=6)
model.fit(x, y)

Source(export_graphviz(model)).render(
    format='png', 
    outfile=Path(path[0]) / 'dec_tree output/simple_2.png'
)

