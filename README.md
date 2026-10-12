# Touchline Tracker PWA

## Update notes — Team editing and statistics filters
- Team creation and editing are managed from the Team page. Settings now points users to that page instead of duplicating team load/edit/duplicate controls.
- The Team page shows an Unsaved changes notice when the team name, players, positions, shirt numbers or kit definitions are edited. Switching teams prompts to save or discard changes.
- History / stats includes team, season/tournament and date-range filters, a Clear filters action, and a summary of the active selection.
- Saved matches can optionally follow all selected team, season/tournament and date filters. This option is enabled by default.
- Live-match own-kit colour options are restricted to colours configured for the currently loaded team's kits.
- The existing local data structure and backup/import formats are retained. Export a full backup before replacing hosted files.

## Install
1. Export a full backup from the current app.
2. Extract the ZIP and upload its contents to the existing GitHub Pages repository, preserving the folder structure.
3. Reopen the PWA and refresh. If an older cached version remains, close and reopen it after the service worker updates.

The app stores data locally in the browser; it does not provide cloud sync. Keep a separate backup of important records.
