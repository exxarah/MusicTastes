# MusicTastes TODO

## Minimum Required

- [X] Set up Flask project
- [X] Design appearance of visualisation
  - [X] General Idea/Concept (ie, graph, pie chart)
  - [X] Mockup Visualisation
  - [X] General Website Design
- [X] Get Access to Data
  - [X] Spotify OAuth
  - [X] Get User's listened to tracks
    - [X] Last 50          https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-the-users-currently-playing-track
    - [X] Saved Songs      https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-users-saved-tracks
    - [X] User metadata?   https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-current-users-profile
- [ ] ~~Organise Data~~
  - [ ] ~~Group songs by common points (artists/metadata features/genre)~~
  - [ ] ~~Maybe make a new "struct" to represent the song by their relation to the common points being used~~
- [X] Present Data
  - [X] Actual data visualisation stuff
  - [X] ~~Click~~ Mouseover on the song entry to get song metadata
    - [X] Drawer that opens on the side of the page with song information
- [X] Website Housekeeping
  - [X] Home Page
  - [X] ~~Login~~ User Page
    - [X] Instead of an actual page, make it a drop down from the user icon in the header
    - [X] Login is handled separately (for the most part)
    - [X] User Profile dropdown
    - [ ] ~~Make OAuth login with popup rather than actual full redirect~~
    - [X] Different dropdown when not logged in
    - [X] Logout
  - [X] DataVis Page
    - [X] Is designed to disguise itself as the home page, for the appearance of a clean single page app

## Stretch Goals
- [ ] Remember previous logins, so that we can try and get historical data despite the limit of 50 recent songs for the public API
  - [ ] Can also try to do this by getting currently playing and adding it to the list on the fly
- [ ] Give recommendations of similar songs
- [ ] Responsive design
