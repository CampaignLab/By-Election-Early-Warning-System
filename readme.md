# ⭐ By-Election Early Warning System

View the dashboard here: https://campaignlab.github.io/By-Election-Early-Warning-System/

## Project Status Update
We have made some progress on the initial implementation. So far, we have:
- Created a web interface that pulls data from opencouncildata.co.uk/byelections.php
- Implemented an interactive map showing all upcoming by-elections with color-coding based on timeline
- Added integration with NewsData.io API for local news searching

The current implementation can be found in the `index.html` file which includes both the interface and the core functionality. 

### Next steps:
- Integrate a better news API (something with better local news coverage)
- Add councillor monitoring (attendance, personal websites, social media) to view per by-election
- Add a historical trend of council seats

## Original Project Plan

### Background
By-elections present crucial opportunities for targeted campaigning and community engagement. Having advanced knowledge and data about upcoming by-elections allows for better resource allocation and strategic planning. Can we make a system that draws from this site and highlights areas which are vulnerable to reform? https://opencouncildata.co.uk/byelections.php 

### Challenge
Create an automated monitoring system that tracks and alerts on upcoming by-elections across the UK. The system should collect and organize data about dates, locations, and relevant demographic information.

### Project Details
* Project Lead: *Not specified*
* Team Members:
  * Simon Wisdom
  * Lewis Colwill
  * Mel Tranfield
* Link to chat: https://chat.whatsapp.com/Lia9aoFUhKR6x2SJEaVYgO
* Link to GitHub: https://github.com/CampaignLab/By-Election-Early-Warning-System
* Skills Needed: Python, Web Scraping, Database Management

### Questions
* Is the idea to monitor that single data source, or also scrape from other sources?

### Strategy
* Collect demographic data and past election history for upcoming councils
* Identify councils that have a strong presence vs those that have a mix (stronghold vs marginal)
* Filter out strongholds (in theory they are not easily influenced, not worth time)
* Output a list of upcoming by-elections that are in marginal councils

### Key Questions
* How do we define 'marginal' vs 'stronghold'?
* What kind of demographic data do we care about?

### Useful Insights from HNH
* https://hopenothate.org.uk/reform-party-2024/
* https://hopenothate.org.uk/fear-and-hope-2024/
* What kind of 'warning signs' do we need to pay attention to?

## Notes: Boundary Areas of Interest

### England's Administrative Structure
In England, there are 2 broad ways of dividing up the country. There used to be a 2 tier system, in that every location was part of a district AND a county (county being larger). However, over time this has dissolved and now **some** places are only part of either a county or a district.

#### County Council
* County Electoral Divisions

#### District Council
* Ward

#### Unitary Authority (city)
* Some have an 'all out election' - all wards are elected at the same time. Each ward has 2-3 councillors
* Others do it by thirds - i.e., each year for the next 3 years, one of the three councillors are elected
* If boundaries get changed, sometimes councillors have to re-run much sooner than they had planned. Often they stand down in that case. This could be a warning sign

In most city regions (London, Manchester, Liverpool, etc), Scotland, Northern Ireland, and Wales, there is just 1 tier! This is called a council.

Another division is a "parish" - sometimes you have parishes in wards, and wards in parishes.

## Areas of Concern
* North East
  * Sunderland
* East of England
* Wales

## Warning Signs
* Big local issue that's attracting lots of attention
  * Eg. In Southampton 2 party members defected and swapped parties over a local issue
  * Local protest movements bubble up around immigration as a result of an unannounced asylum seeker shelter is set up
  * Stabbing/murder in a local area - Far right will jump on it, so that becomes a red alert
* Attendance of a councillor - below a threshold they cannot vote
* Marginality
* Councillors likely to resign - eg another by-election sooner than later (eg because a boundary redrawing)
* Look for local far right protests - they will often target areas they think might be influenced
  * Patriotic Alternative, Britain First, Homeland

## Resources
* Protest hotspots 2023: Copy of Demo and Visit data 2023.xlsx (shared from Hope Not Hate)
* Local Election Archive Project (andrewteale.me.uk/leap/)

## Planned Features
* Local news scraper
* Councillor monitoring (attendance, personal websites, social media)
* Historical trend of council seats 
* First from https://opencouncildata.co.uk 
* Zoom in by looking at actual council websites
* Look at protest hotspots - see if any map to upcoming by-election areas
* Map all of the above to upcoming by-elections

## Sprint 1 Assignments
* Lewis will work on: 
  * Historical trend of council seats 
  * First from https://opencouncildata.co.uk 
  * Zoom in by looking at actual council websites

* Simon will work on:
  * Local news scraper

* Mel will work on:
  * Councillor monitoring (attendance, personal websites, social media)