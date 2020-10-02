# Metis_Project2_NBA
## Developing an Algorithm to Win Daily Fantasy Sports Competitions

### Description

There are two main daily fantasy sports platforms, DraftKings and FanDuel.  Both allow users to participate in various daily competitions in which users are allocated a "salary cap" and can draft players whose "salary costs" sum to equal or less than that salary cap amount.  Various statistics that a player can generate contribute to their "score".  The goal is to draft players to your team who will score the highest number of fantasy points during the given time period (typically daily). This project aims to predict the number of fantasy points each player will score on a given day, and use that to win the competition (and money).

### Features and Target Variables

- Points, rebounds, assists, steals, blocks, free throws, three points per game along 
	- with home/away splits and per-opponent splits
- Opponent
- Days Rest
- Home/away
- Marquee Matchup (using domain knowledge)
- Rivalry (using domain knowledge)

### Data Used

- game log statistics from basketball-reference.com
- historical game times and broadcast channels if I can find that info

### Tools Used

- Numpy
- Pandas
- Matplotlib
- Seaborn
- BeautifulSoup
- Scikit-Lean
- Tableau

### Possible Impacts

If this project and resulting algorithm is successful, I will be able to compete in daily fantasy competitions and likely make money.  The platforms are currently dominated by algorithms, and so not using an analytics approach is generally not a good idea.
