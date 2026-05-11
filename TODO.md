# TODO - SnapClass UI/UX styling refactor

- [ ] Step 1: Create unified theme (CSS variables + utilities) in `src/ui/base_layout.py`
- [ ] Step 2: Remove conflicting global CSS from `app.py`
- [ ] Step 3: Remove per-render “Per-file fix” CSS blocks from `src/screens/student_screen.py` and `src/screens/teacher_screen.py`
- [ ] Step 4: Update `src/components/subject_card.py` to use theme utilities (cards/typography/button readability)
- [ ] Step 5: Update `src/components/header.py` and `src/components/footer.py` to remove hardcoded colors and align with theme
- [ ] Step 6: Verify button text contrast + hover states + dialog/toast readability via quick app run
- [ ] Step 7: Produce before/after summary and list modified files

