# Touchline Tracker — Team Editing & Statistics Filters Fix

This update fixes a regression in the team editing workflow. It restores the missing team-change tracking and confirmation helpers used by adding players, adding/editing kits, saving teams, and switching teams. Team edits can be saved before switching or explicitly discarded. The team/statistics filtering improvements are retained.

## Install
1. Export a full backup from the current app before replacing files.
2. Extract this ZIP and upload its contents to the existing GitHub Pages repository, preserving the file structure.
3. Refresh/reopen the PWA so the updated service worker can install the fix.

Saved data remains in the browser's local storage. Do not clear site storage as part of installation.
