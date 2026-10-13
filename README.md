# Touchline Tracker PWA

Offline-first football match tracker. Upload the contents of this folder to the root of a GitHub Pages repository, enable Pages over HTTPS, open the published URL in Chrome on Android, and use the browser menu to install/add to home screen.

This update adds team-first statistics filtering, season/tournament filtering within a team, combined all-team statistics grouped by team, green active-period and red ended-period buttons, and an Import backup button beside Export backup on History / stats.

Data is stored locally in the browser. Export backups regularly. Importing a backup replaces data currently stored on the device.


Latest update: the live screen includes a Penalties button for a separate penalty shootout tracker with first-kicker selection, player takers, scored/missed/saved outcomes and side-by-side shootout scores. The main clock button now toggles between Start match, Pause match and Continue.


Latest update: penalty shootout data is retained in saved match records and refreshed when the archived match changes; match summaries/reports and exports include penalty scores. Player time played now includes a percentage of total match duration. The Team tab supports creating and loading named teams. Each saved team stores its player list, kit colours and per-player shirt numbers together. Loading a team on the live match screen loads its players and kit colours. Full and selective team backups include saved team kits and player shirt numbers. Match reports list each recorded penalty taker and whether the kick was scored, saved or missed.


## Latest fixes (October 2026)
- The live-match “Your kit colour” selector now contains only colours configured for the currently loaded team's kits. Generic and other-team colours are no longer added to this selector.
- The Statistics team filter also filters the Saved matches list, and includes saved teams even when they have no recorded matches yet.
- Current-match statistics indicate when the open match belongs to a different team than the selected filter.
- Changing Home/Away venue selects that team's matching Home/Away kit colour when available.
- Service-worker cache version bumped so the updated app files can be refreshed.
