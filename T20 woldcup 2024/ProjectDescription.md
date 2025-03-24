# T20 World Cup 2024 - Top 11 Players Dashboard

### Dashboard Link: (https://app.powerbi.com/reportEmbed?reportId=b2e4af6b-8628-47f3-b5f5-c96809147246&autoAuth=true&ctid=0d8f96a4-62c2-4e68-9449-66de88e46f86)

## Problem Statement
 
This dashboard aims to analyze and identify the top 11 players of the T20 World Cup 2024 based on key performance metrics such as batting average, strike rate, wickets taken, economy rate, and fielding efficiency. By leveraging statistical analysis and visualization, the project provides an objective ranking, offering valuable insights for cricket enthusiasts, analysts, and decision-makers.

Since selecting the best players is crucial for understanding team performances, this dashboard categorizes players based on their roles—openers, middle-order batsmen, finishers, all-rounders, and specialist bowlers. The interactive features allow users to explore detailed player stats, compare performances, and make data-driven selections.

## Steps Followed

- **Step 1:** Loaded five datasets (**Best Batting, Best Bowling, List of Players, T20 2024 Summary, and Total Runs**) into Power BI.
- **Step 2:** Cleaned and preprocessed data to ensure accuracy and consistency.
- **Step 3:** Categorized players based on their roles (**Openers, Middle Order, Finishers, All-rounders, Specialist Bowlers**).
- **Step 4:** Used various charts to analyze each category (**Tables, Area Charts, and Scatter Charts**).
- **Step 5:** Designed a **"Final Team"** tab using **slicers and tables** to allow users to filter and select the best 11 players.
- **Step 6:** Created **hidden tooltip pages** with detailed player stats (**Player Details by Match, Openers, Finishers, and Bowlers**) that appear when clicking on a player.
- **Step 7:** Implemented **DAX calculations** to create key performance measures.
- **Step 8:** Designed an **interactive dashboard layout**, adding team-wise insights and filters.
- **Step 9:** **Published the report** to Power BI Service for easy access and sharing.

## Key DAX Measures Used

```DAX
// Average Balls Faced
Average Balls Faced = AVERAGE('total run of the players'[Balls faced])

// Balls Bowled
Balls Bowled = SUM('best bowling (2)'[Balls Bowled])

// Boundary Percentage
Boundary % = DIVIDE(SUM('best batting'[Boundaries]),[Total Runs],0)

// Display Text for Player Selection
Display Text = IF([Player Selection] = "1", " ", "Select Player(s) by clicking the player’s name to see their individual or combined strength.")

// Total Innings Batted
Total Innings Batted = COUNT('total run of the players'[Innings])

// Total Runs
Total Runs = SUM('total run of the players'[Runs])
```

## Visualizations Used

- **For Openers, Middle Order, Finishers, All-Rounders, and Specialist Bowlers:**
  - Tables
  - 4 Area Charts
  - 1 Scatter Chart (for performance comparison)
- **For Final Team Selection:**
  - Slicer (for filtering players)
  - Table (displaying selected players)
- **Hidden Tooltip Pages:**
  - Player Details by Match
  - Details of Openers
  - Details of Finishers
  - Details of Bowlers

## Insights from the Dashboard

- **Top Performers by Role:**
  - Openers with the highest strike rates and runs scored.
  - Middle-order batsmen known for their stability and finishing ability.
  - All-rounders who contributed significantly with both bat and ball.
  - Bowlers with the best economy rates and wicket-taking abilities.
- **Key Performance Trends:**
  - Players with the highest boundary percentages.
  - Economy rates of bowlers in powerplay and death overs.
  - Player contributions across different match stages (**Qualifiers, Super 8, Finals**).
- **Final 11 Team Selection:**
  - Interactive feature allowing users to select players and view their combined performance.

## Filters & Interactive Elements

- **Team-wise player selection**
- **Role-based filtering** (Openers, Middle Order, Finishers, All-rounders, Specialist Bowlers)
- **Interactive tooltips** displaying detailed player stats
- **Player selection slicers** for final team analysis

## Screenshots

![Dashboard Screenshot]
![Image](https://github.com/user-attachments/assets/ab022a30-b70b-40a5-baa2-4f54a6c60e2d)
![Image](https://github.com/user-attachments/assets/06c31901-3a93-4b62-b0e3-dbce5179f973)
![Image](https://github.com/user-attachments/assets/3051b74f-0efe-441d-838b-21247b1bb258)

## Publishing & Final Report

- The **dashboard was published on Power BI Service**.
- Users can interact with the report by selecting players, filtering by team, and exploring insights.

## Conclusion

This **T20 World Cup 2024 Top 11 Players Dashboard** provides a **data-driven approach** to evaluating the best performers. It allows users to explore player statistics, compare performances, and make informed decisions. By combining **statistical analysis with interactive visualizations**, this dashboard offers a **comprehensive overview of the tournament's standout players**.

---

### Author: **Akanksha Bisht**  
### Date: **July 18, 2024**  
### Institution: **Shivalik College of Engineering (SCE)**  

---
