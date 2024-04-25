def star_wars_recursive(num_enemy_ships):

    # Base case: if there are no ships, return an empty string
    if num_enemy_ships == 0:
        return ""
    else:
        # Recursive case: append different patterns based on whether the count of ships is odd or even
        if num_enemy_ships % 2 == 1:
            return star_wars_recursive(num_enemy_ships - 1) + "*-"
        else:
            return star_wars_recursive(num_enemy_ships - 1) + "*--"
