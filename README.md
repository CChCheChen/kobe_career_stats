# kobe_career_stats
A Dash App to display Kobe Bryant's career stats

[Hosted on Render](https://kobe-career-stats.onrender.com/)

- Author: Chen Lin

Kobe fans!!!!!!!! Lakers fans!!!!!!!! 

This is the application you can view Kobe Bryant's career stats over his regular seasons and playoffs.

More details can be found in the proposal [here](https://github.com/UBC-MDS/nba_player_stat/blob/main/PROPOSAL.md).

This document provides the basic information about this Kobe Bryant Careet Stats APP project. Please feel free to navigate each section by the list below: 

* [Description of App](#description)
* [Usage and Installation](#usage-and-installation)
* [Contribution](#Contribution)
* [Contact](#contact)
* [License](#license)
* [Data Reference](#data-reference)

## Description

The visualization app contains a landing page that shows Kobe Bryant's Careet performance stats. The visualization comprises the data of NBA superstar Kobe Bryant's 20 year career. This app aims to help enthusiastic Kobe fans to understand better and assess Kobe's performances.

The visualization is designed to display multiple statistics about Kobe Bryant. The app allows users to display Kobe's career stats by filtering from regular-season and playoffs, selecting the years Kobe played (from 1996 to 2016) and choosing the options of stats as shown below:

- Games played
- Field goal made per game
- Field goal attampts per game
- Points per game
- Rebounds per game
- Assists per game
- Steals per game
- Blocks per game
- Field goal percentage

### Interaction components:

- Top-left 'Regular Season/Playoff' dropdown: select between `Regular Season` and `Playoff`

- Top-right 'Stats Type' dropdown: to select options which are shown above

- Slidebar 'Season Range' to select the years which Kobe played in NBA

### Plots

- Fist line chart: display the selected stats over the selected play year, based on the data for `Regular Season` or `Playoff` 

- Second line chart: display the total game Kobe played in the season over the selected play year, based on the data for `Regular Season` or `Playoff` 

## Usage and Installation

To install `kobe_career_stat` locally, you can:

1. Clone this repository with:

```
https://github.com/CChCheChen/kobe_career_stats.git
```

2. Run the following command to install required libraries locally:

```{r}
pip install dash pandas
```

3. Finally, run the app locally by: 

- Open `VSCode`, navigate to the `root` folder of the project folder, open `app.py` and run it by clicking `Run Python file` button on the top-right corner.

- Open a command line, navigate to the `root` folder of the project folder, run the following command to run the app locally:

```
python app.py
```

## Contribution

I welcome anyone interested in contributing to the app for Kobe's career stats. The project is open-source, which means that anyone can view and contribute to the code on this GitHub repository.

If you are interested in getting involved, check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## Contact

If you have any new ideas and suggestions for improvement about this app, please feel free to contact me. The main contact email is chen.lin.0404@gmail.com

## License

Licensed under the terms of the [MIT license](LICENSE).

## Data Reference

The data used to visualize is extracted from [Kobe Bryant's Stats](https://www.basketball-reference.com/players/b/bryanko01.html) from Basketball Reference. There are 20 years playing stats in this data set for `Regular Season` and `Playoff`. The useful data columns used for the application are listed below:

- 'G': 'Games played',
- 'FG': 'Field goal made per game',
- 'FGA': 'Field goal attampts per game',
- 'PTS': 'Points per game',
- 'TRB': 'Rebounds per game',
- 'AST': 'Assists per game',
- 'STL': 'Steals per game',
- 'BLK': 'Blocks per game',
- 'FG%': 'Field goal percentage'