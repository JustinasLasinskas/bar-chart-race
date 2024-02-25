import bar_chart_race as bcr
import pandas as pd

# Load the data
data = pd.read_csv('data/gdp_1960_2020.csv')

# Filter the data
europe_data = data[data['state'] == 'Europe']
europe_data = europe_data[['year', 'country', 'gdp']]
# convert GDP into billions
europe_data['gdp'] = europe_data['gdp'] / 1e9

# Reformat the data to the acceptable the car chart race format
final_df = europe_data.rename(columns={'year': 'date'})
final_df = final_df.pivot(index='date', columns='country', values='gdp')
final_df.index = pd.to_datetime(final_df.index, format='%Y')
final_df = final_df.sort_index()
final_df = final_df.fillna(0)
final_df = final_df.reset_index()
final_df.columns.name = None
final_df = final_df.set_index('date')

# Visualisation
bcr.bar_chart_race(
    df=final_df,
    filename='output/Largest_European_Countries_by_GDP.mp4',
    orientation='h',
    sort='desc',
    n_bars=10,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'TOP10 Countries Average GDP (Billion $): {v.nlargest(10).mean():,.0f}',
                                      'ha': 'right', 'size': 12, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(8, 4),
    dpi=144,
    cmap='tab10',
    title='10 Largest European Countries by GDP (billion $)',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'Courier New', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .9},
    filter_column_colors=False)  