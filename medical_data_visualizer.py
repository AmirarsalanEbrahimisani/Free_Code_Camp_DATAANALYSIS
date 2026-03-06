import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars = ['overweight', 'active', 'alco', 'smoke', 'gluc', 'cholesterol'])


    # 6
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))
    

    # 7 & 8
    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar"
    ).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

    # 12 - drop BMI helper column before computing correlations
    corr = df_heat.drop(columns=['BMI']).corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True,
                linewidths=.5, center=0, vmin=-0.1, vmax=0.25, ax=ax,
                cbar_kws={'shrink': .5})


    # 16
    fig.savefig('heatmap.png')
    return fig
