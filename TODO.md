# MusicTastes TODO

## Minimum Required

- [X] Set up Flask project
- [ ] Design appearance of visualisation
  - [ ] General Idea/Concept (ie, graph, pie chart)
  - [ ] Mockup Visualisation
  - [ ] General Website Design
- [X] Get Access to Data
  - [X] Spotify OAuth
  - [X] Get User's listened to tracks
    - [X] Last 50          https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-the-users-currently-playing-track
    - [X] Saved Songs      https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-users-saved-tracks
    - [X] User metadata?   https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-current-users-profile
- [ ] Organise Data
  - [ ] Group songs by common points (artists/metadata features/genre)
  - [ ] Maybe make a new "struct" to represent the song by their relation to the common points being used
- [ ] Present Data
  - [ ] Actual data visualisation stuff
  - [ ] Click on the song entry to get song metadata
- [ ] Website Housekeeping
  - [ ] Home Page
  - [ ] Login Page
    - [ ] Instead of an actual page, make it a drop down from the user icon in the header
  - [ ] DataVis Page
    - [ ] Is designed to disguise itself as the home page, for the appearance of a clean single page app

## Stretch Goals
- [ ] Remember previous logins, so that we can try and get historical data despite the limit of 50 recent songs for the public API
  - [ ] Can also try to do this by getting currently playing and adding it to the list on the fly
- [ ] Give recommendations of similar songs
- [ ] Responsive design