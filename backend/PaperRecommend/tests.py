from django.test import TestCase
from CollaborativeFiltering import proceed_data
import pandas as pd
import os
# Create your tests here.

df = pd.read_csv(os.path.join('arxiv_data', 'papers.csv'), index_col=0)
rec = proceed_data(0, [2], df)
print(rec)
