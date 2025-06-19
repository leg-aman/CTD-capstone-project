import os
import database.db_handler as db_handler

def cli_menu():

    while True:
        conn, cursor = db_handler.create_db_connection()
        print("\n=====================================")
        print("  Leaders for Games Pitched")
        print("=====================================")
        print("\nChoose service you want to use : ")
        print("""
        1 : Top 5 players with most games pitched in the AL
        2 : Top 5 players with most games pitched in the NL
        3 : Player with AVG above a threshold
        4 : Top 5 years with most games pitched
        5 : Players from a team
        0 : Exit"""
              )
        choice = input("\nEnter your choice : ")

        if choice == '1':
            db_handler.top_players_by_league('AL',conn, cursor)
        elif choice == '2':
            db_handler.top_players_by_league('NL',conn, cursor)
        elif choice == '3':
            threshold = input("Enter the average threshold: ")
            try:
                threshold = float(threshold)
                db_handler.players_above_avg(threshold, conn, cursor)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            db_handler.top_years_by_games_pitched(conn, cursor)
        elif choice == '5':
            team = input("Enter the team name: ")
            if not team:
                print("Team name cannot be empty.")
                continue
            else:
                db_handler.players_from_team(team, conn, cursor)
            
        elif choice == '0':
            exit()
        else:
            print("Invalid choice. Please try again.")  


