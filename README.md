# Touchline Tracker — Complete website package

This ZIP contains the files needed to host Touchline Tracker as a static website / Progressive Web App (PWA):

- `index.html` — the app and its interface (includes the app JavaScript)
- `manifest.webmanifest` — PWA name, launch settings and icons
- `sw.js` — service worker for offline caching and updates
- `icon-192.png`, `icon-512.png`, `icon.svg` — app icons
- `app.js` and `inline-check.js` — supporting copies of the app script for reference/validation; the current `index.html` runs its embedded script

## Publish on GitHub Pages

1. Back up your Touchline Tracker data from inside the app before updating.
2. Extract this ZIP.
3. Upload **all the files in this ZIP** to the root of your existing GitHub Pages repository, keeping the filenames unchanged. `index.html` should be at the published root, not buried inside another folder.
4. Commit the changes and wait for GitHub Pages to publish.
5. Open the site using its HTTPS GitHub Pages URL, then refresh/reopen the app. HTTPS is required for service-worker/PWA installation; opening `index.html` directly as a local file will not enable offline PWA features.

## Visual formation controls

- Tap a player, then tap another player to swap positions.
- Tap a substitute and then the player to replace, or tap the player first and then the substitute.
- Save formation and Save starting lineup save the changes and close their popups.

## Data safety

The app stores team and match data in the browser's local storage on each device. Updating the website should not require clearing browser storage. **Do not clear site data/storage** as part of the update. Export a backup regularly, and especially before replacing the hosted files.
