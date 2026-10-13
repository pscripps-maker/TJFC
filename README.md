# Touchline Tracker — Custom Formations Update

This update adds reusable custom formations and improves the visual formation editor.

## New functionality
- Create, save, edit and delete custom formations for 5-a-side through 11-a-side.
- Formation options are filtered to the selected players-per-side count. The goalkeeper is added automatically; outfield row counts must total one fewer than the number of players per side.
- Examples for 7-a-side include `1-2-3`, `1-2-2-1`, and `2-1-2-1`.
- In the visual pitch, drag a player to an empty position to move them without swapping another player. On touch screens, tap a player then tap an empty slot.
- Drag a substitute onto an occupied shirt to make a substitution.
- The visual formation button now uses a pitch icon.
- Custom formations are stored in app settings and included in regular app backups.

## Install
1. Export a full backup from the current app before replacing files.
2. Extract this ZIP and upload its contents to the existing GitHub Pages repository, preserving the file structure.
3. Refresh/reopen the PWA so the updated service worker can install the update.

Saved data remains in browser local storage. Do not clear site storage as part of installation.


Latest update: restored touch-based player swapping in the visual pitch; added per-match unavailable player controls in the starting-lineup dialog; added an Injured / Fit again event with a red plus indicator; and added editable age-group player-count defaults in Settings with a Team-page age group selector that applies the matching players-per-side format when loading a team. Age-group counts are editable defaults and should be checked against current competition rules.
