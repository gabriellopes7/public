is_rain = True

print("Today, i'm with clothes " + ('dry.', 'wets.')[is_rain])

print("Today, i'm with clothes " + ('wets.' if is_rain else 'dry.'))
