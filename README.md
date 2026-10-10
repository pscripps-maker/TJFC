# Touchline Tracker — Core update

## Included in this build
- Squad player positions: Goalkeeper, Defence, Midfield and Attack.
- Home/Away/Neutral match selection, team colours, location, kick-off time and formation field.
- Main per-player event buttons for Goal, Assist, Shot and Save, plus a `+` menu for additional events.
- Custom event labels, shared main-button ordering and custom event types in Settings.
- Starting-lineup selection, player on-pitch/substitute/non-playing colour states, and substitution events.
- Match event totals, goal/assist stats, season stats and timeline.
- Delete current match data and delete saved matches (with confirmation).
- Visual button feedback, JSON backup/restore, PWA install and offline app-shell cache.

## Current limitations / next stage
- The goal and shot outcomes currently use a quick-choice sheet; clickable goalmouth and shot-location maps are the planned next stage.
- The minutes-tracking toggle and lineup/formation tools are foundations for the next iteration; per-player minute totals and saved reusable lineup templates still need completing.
- Button labels and shared button order are configurable. Per-player bespoke button ordering is planned for the next iteration.

## Install on Android
1. Upload all files in this folder to the root of a GitHub repository.
2. In **Settings → Pages**, publish from `main` and `/ (root)`.
3. Open the published HTTPS URL in Chrome on Android.
4. Choose Chrome menu → **Install app** or **Add to Home screen**.
5. Load the app once online, then test offline.

The app stores data locally in the browser on this device; it does not automatically sync to the cloud. Export a JSON backup regularly. When updating an installed app, refresh the hosted files and reopen the app online so the new service-worker cache can install.


## Update notes (October 2026)
- Live player cards now stack the player name above large event buttons for better phone readability.
- Main event buttons give a visible pressed/flash response.
- Penalty and free-kick buttons open the same outcome chooser as Shot; successful attempts also record a goal.
- New matches default to 7-a-side and 2-3-1. Player count can be changed in match setup.
- Player position is an optional dropdown, with custom positions addable in Settings.
- Live match screen shows only active starting/on-pitch players, with a Sub button on each player to choose a replacement.
