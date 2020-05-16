#https://productmetrics.net/blog/creating-sankey-diagram-python/
#https://medium.com/kenlok/how-to-create-sankey-diagrams-from-dataframes-in-python-e221c1b4d6b0
import seaborn as sns
import pandas as pd
import ipysankeywidget

df = pd.read_csv('sampleSankey')

data = []

# Generate a colour pallet to let us colour in each line
palette = sns.color_palette('cubehelix', len(df.index) + df.Category.nunique())
colours = palette.as_hex()

level1 = df[['Category', 'UnitedKingdom']].groupby('Category').;agg('sum')

# Counter so we can iterate through the colours
c_count = 0

for i, r in level1.reset_index().iterrows():
    # Map from a top leve "Expenditure" category to the low level items
    data.append(
        {'source': 'Expenditure', 'target': r['Category'], 'value': r['UnitedKingdom'], 'color': colours[c_count]})

    # Get the item sub-totals for the category
    for item_i, item_r in df[df['Category'] == r['Category']][['Category', 'Item', 'UnitedKingdom']].groupby(
            ['Category', 'Item']).agg('sum').reset_index().iterrows():
        # Increment the colour counter
        c_count += 1

        # Record the Category --> Item breakdown
        data.append({'source': item_r['Category'], 'target': item_r['Item'], 'value': item_r['UnitedKingdom'],
                     'color': colours[c_count]})