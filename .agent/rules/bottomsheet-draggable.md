---
trigger: always_on
---

# Bottom Sheet & UI Guidelines

1. **All Bottom Sheets Must Be Draggable**: Every bottom sheet in the Cashleap Prototype — including persistent screen bottom sheets (`#recentTransactionsSheet`, `#statsCategoriesSheet`, `#financeBottomSheet`, `#othersBottomSheet`) and all modal bottom sheets (`#transferSheet`, `#exchangeSheet`, `#addCardSheet`, `#userProfileSheet`, `#selectCardSheet`, `#cardDetailsSheet`, `#txDetailSheet`, `#notificationsSheet`, etc.) — must support smooth pointer/touch/mouse drag-to-expand, drag-to-collapse, and drag-to-dismiss gestures.
2. **Card Visibility Above Bottom Sheets**: Collapsed bottom sheets must never overlap or clip the bottom border or axis labels of the card above them (e.g., `STATS_SHEET_COLLAPSED_Y = 338` on `#statsCategoriesSheet` so the Current Balance chart card's bottom border and X-axis day/year labels are 100% visible).
3. **No Emoticons / Emojis**: Never use emoticons or emojis in UI buttons, badges, or modals; always use crisp monochrome vector SVGs matching the Home and Statistics aesthetic.
