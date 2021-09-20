# MySpotify TODO

## Minimum Required

- [X] Set up Flask project
- [ ] Design appearance of visualisation
  - [ ] General Idea/Concept (ie, graph, pie chart)
  - [ ] Mockup Visualisation
  - [ ] General Website Design
- [ ] Get Access to Data
  - [ ] Spotify OAuth
  - [ ] Get User's listened to tracks
    - [ ] Last 50
    - [ ] Saved Songs
    - [ ] User metadata?
- [ ] Organise Data
  - [ ] Group songs by common points (artists/metadata features/genre)
  - [ ] Maybe make a new "struct" to represent the song by their relation to the common points being used
- [ ] Present Data
  - [ ] Actual data visualisation stuff
  - [ ] Click on the song entry to get song metadata
- [ ] Website Housekeeping
  - [ ] Home Page
  - [ ] Login Page
  - [ ] DataVis Page

## Stretch Goals
- [ ] Remember previous logins, so that we can try and get historical data despite the limit of 50 recent songs for the public API
  - [ ] Can also try to do this by getting currently playing and adding it to the list on the fly
- [ ] Give recommendations of similar songs
- [ ] Responsive design