print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fred_vanvleet_3pts_made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
james_harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_vanvleet_3pts_made} 3 point shots")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")


print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jamal_murray_3pt_attempts = 93
print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_3pt_attempts} 3 point shots")
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fred_vanvleet_3pt_attempts = 110
print(f"In the 2020 NBA playoffs, Fred Vanvleet attempted {fred_vanvleet_3pt_attempts} 3 point shots")
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
james_harden_3pt_attempts = 109
print(f"In the 2020 NBA playoffs, James Harden attempted {james_harden_3pt_attempts} 3 point shots")


print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pt_attempts} 3 point attempts.")
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_vanvleet_3pts_made} 3 point shots and {fred_vanvleet_3pt_attempts} 3 point attempts.")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and {james_harden_3pt_attempts} 3 point attempts.")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
jm_3pts_made = 46.0
jm_3pts_attempted = 93.0
jm_3pt_pct = (jm_3pts_made/ jm_3pts_attempted * 100)
print(f"Jamal Murray has a {jm_3pt_pct} % 3 pt shooting percentage.")

# TODO: Calculate and print the 3 point percentage for Fred VanVleet
fv_3pts_made = 43.0
fv_3pts_attempted = 110.0
fv_3pt_pct = (fv_3pts_made/ fv_3pts_attempted * 100)
print(f"Fred VanVleet has a {fv_3pt_pct} % 3 pt shooting percentage.")

# # TODO: Calculate and print the 3 point percentage for James Harden
jh_3pts_made = 37.0
jh_3pts_attempted = 109.0
jh_3pt_pct = (jh_3pts_made/ jh_3pts_attempted * 100)
print(f"James Harden has a {jh_3pt_pct} % 3 pt shooting percentage.")

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.")

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
laker_2020_season = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(laker_2020_season.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = True
print(f"The Lakers are the best basketball team in the NBA: {lakers_are_best}.")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
lakers_are_best = int(True)
print({lakers_are_best})
# It's because boolean values are seen as either 1 (true) or 0 (false) when converted to an integer.

# TODO: Convert your `lakers_are best` variable to a float, and print it out
lakers_are_best = float(True)
print({lakers_are_best})

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
jm_3pt_pct = str(jm_3pts_made/ jm_3pts_attempted * 100)
print(jm_3pt_pct)
fv_3pt_pct = str(fv_3pts_made/ fv_3pts_attempted * 100)
print(fv_3pt_pct)
jh_3pt_pct = str(jh_3pts_made/ jh_3pts_attempted * 100)
print(jh_3pt_pct) 
# I did not have to multiply 100. The decimal moved two places on its own.

jm_3pt_pct = int(jm_3pts_made/ jm_3pts_attempted * 100)
print(jm_3pt_pct)
fv_3pt_pct = int(fv_3pts_made/ fv_3pts_attempted * 100)
print(fv_3pt_pct)
jh_3pt_pct = int(jh_3pts_made/ jh_3pts_attempted * 100)
print(jh_3pt_pct) 
# The decimal point was dropped and the statement returned a whole number.

