# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

import seaborn as sns

sns.regplot(x="difference_pts", y="share_household", data=games_tv)
