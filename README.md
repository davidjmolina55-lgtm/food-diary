
# Food Diary

## Overview

Food Diary is a lightweight Django application for tracking meals and food entries. It provides a simple, user-focused interface where each authenticated user can create, view, update, and delete their own food records. The project emphasizes accessibility and consistent visual design using Bootstrap plus a curated site stylesheet.

## Table of Contents

- Overview
- Getting Started
	- Prerequisites
	- Local Setup & Migrations
- UX Design
- Key Features
- Future Enhancements
- Contributing

## UX Design

Design goals
- Clean, accessible layout with a focus on readability and clear forms.
- Consistent, minimal visual language using Bootstrap and a small site stylesheet (`static/css/style.css`).
- Accessible keyboard focus states and a "skip to main content" link.

Layout
- The site uses a `base.html` template with a Bootstrap navbar and a sticky footer. Main content sits inside a centered container limited to ~980px width.
- Auth pages (login/register) use an `.auth-card` visual pattern — a centered card with a slightly elevated surface (`.card-lite`) and rounded corners.

Forms and feedback
- Forms use accessible labels and inline errors. Flash messages are displayed at the top of the content area and auto-dismiss after 10 seconds.
- The navbar shows login/register links when anonymous and a logout button for authenticated users.

Mobile / responsive
- The design is responsive; auth card and main container adapt down to small screens with padding adjustments and stacked controls.

## Key Features

- Per-user food tracking: each `Food` record belongs to a user; list views show only the current user's entries.
- Full CRUD: create, read, update, delete food entries with server-side ownership checks.
- Authentication: django-allauth is wired for sign up, login, logout, and account management.
- Accessible UI: clear focus states, skip link, and readable forms.
- Flash messages: actions (create/update/delete) show success messages; messages auto-dismiss after 10 seconds.
- Admin integration: `Food` model registered in Django admin for quick inspection and management.

## Future Enhancements

- Add user preferences (time zone, date format, default meal type).
- Export / import CSV of food history.
- Add filtering and search on the food list (by date range, meal type, keyword).
- Provide an API (Django REST Framework) for mobile or third-party integrations.
- Unit and integration tests to cover views, forms, and permissions.
- Improve form UX: password strength indicator on signup, show/hide password toggles, inline help text.
- Optional social authentication flows via allauth.socialaccount.

## Contributing

Contributions are welcome. Please open issues for bugs or feature requests and submit PRs with focused changes.

---

If you want, I can add a short Developer Notes section describing model fields and key templates. Would you like that added?

## Developer Notes

This section lists the most important code locations and a short description to help future development.

- Models
	- `food_diary/models.py` — `Food` model
		- `name` (CharField): the food item name
		- `date` (DateField, `auto_now_add=True`): set automatically when the record is created
		- `meal_type` (CharField): choice field (breakfast, lunch, dinner, snack)
		- `user` (ForeignKey to `AUTH_USER_MODEL`): owner of the record

- Forms
	- `food_diary/forms.py` — `FoodForm` (ModelForm)
		- Exposes `name` and `meal_type` (the `date` is auto-populated by the model)
		- Widgets configured for consistent `.form-control` / `.form-select` styling

- Views
	- `food_diary/views.py`
		- `food_diary_view`: home/login landing; redirects authenticated users to the food list
		- `food_list`: shows current user's foods (`Food.objects.filter(user=request.user)`)
		- `food_create`: creates a `Food` instance and attaches `request.user`; shows a success message
		- `food_update`: edits a `Food` instance; raises `Http404` if the current user is not the owner
		- `food_delete`: asks for confirmation and deletes the instance on POST; raises `Http404` for unauthorized access

- Templates
	- `templates/base.html` — site base, navbar, message rendering, and alert auto-dismiss script
	- `food_diary/templates/food_diary.html` — login/landing page (uses allauth login view)
	- `food_diary/templates/food_list.html` — user's food list with actions to edit/delete
	- `food_diary/templates/food_form.html` — create/edit form (does not show `date` field)
	- `food_diary/templates/food_delete_confirm.html` / `food_diary/templates/food_delete_confirm.html` — delete confirmation (a clean template is used)
	- `templates/account/signup.html` — customized signup page that extends the project `base.html` and uses the `.auth-card` pattern

- Admin
	- `food_diary/admin.py` — registers the `Food` model for the Django admin

Notes
- Flash messages use Django's `messages` framework and are rendered in `base.html`; they auto-dismiss via a small JS snippet.
- Ownership checks are performed server-side in views to prevent unauthorized edits/deletes.
- The project uses `django-allauth` for authentication; account templates are under `templates/account/` and the signup template has been adapted to match the site's styling.

If you want, I can also add example API endpoints, unit tests for the views, or a short sequence of curated git commits describing the recent changes. Which of those would you prefer next?



