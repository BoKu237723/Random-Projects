import random
import json
    
class Game:
    def __init__(self):
        self.players = []
        self.rankings = ["1st","2nd","3rd","4th","5th"]
        self.total_rounds = {}

    def json_modify(self):
        with open("index.json", "w") as file:
            json.dump(self.players, file, indent = 4)

    def round_start_point(self):
        for i in self.players:
            self.total_rounds[i["id"]] = 0

    def individual_data(self, total_players):
        for i in range(total_players):
            name = input(f"Enter '{i}' username: ")
            data = {
                "id": i, 
                "name": name, 
                "game_data": {
                    "total_amount":0, 
                    "savings":0, 
                    "history": {}
                    }
                }
            
            self.players.append(data)
            self.json_modify()

    def final_sorting(self):
        unsorted = {}
        for i in self.players:
            unsorted[i["name"]] = i["game_data"]["total_amount"]

        sorted_items = dict(sorted(unsorted.items(), key=lambda item: item[1], reverse = True)) 
        return sorted_items

    def add_round_to_json(self,i,j):
        print(self.total_rounds) # this is a dictionary
        round_rank = self.total_rounds.get(i)
        name = "round" + str(round_rank)
        j["game_data"]["history"].update({name : {}})

    def add_small_round_to_json(self, current_user, current_small_round, usr_generated_number):
        current_user_id = current_user
        round_name = str(current_small_round) + ". round"
        points = usr_generated_number
        round_rank = "round" + str(self.total_rounds.get(current_user_id))
        self.players[current_user_id]["game_data"]["history"][round_rank].update({round_name : points})

    def start_game(self):
        self.round_start_point()
        while True: 
            for i in self.players: # big_round
                self.total_rounds[i["id"]] += 1
                self.add_round_to_json(i["id"], i)
                small_rounds = 0

                while True: # small round
                    usr_number = random.randint(1,10)
                    print(f"\nThis is {i['name']} turn")
                    print(f"Your generated Number = {usr_number}")
                    small_rounds += 1
                    self.add_small_round_to_json(i["id"],small_rounds, usr_number)
                    if usr_number != 1:
                        print(f"Added amount to your savings = {usr_number}")
                        i["game_data"]["savings"] += usr_number
                        self.json_modify()
                        usr_input = input("Enter 'continue' to continue playing or 'break' to take a break!\nYour Input: ")
                        
                        if usr_input == 'continue':
                            continue

                        elif usr_input == 'break':
                            i["game_data"]["total_amount"] += i["game_data"]["savings"]
                            i["game_data"]["savings"] = 0
                            self.json_modify()

                            if i["game_data"]["total_amount"] >= 50:
                                print("====================")
                                print(f"\n{i["name"]} is the winner!\n\nTotal Amount: {i["game_data"]["total_amount"]}")
                                sorted_items = self.final_sorting()
                                j = 0
                                for keys, values in sorted_items.items(): # keys = name # values = points 
                                    print(f"{self.rankings[j]}: {keys}")
                                    print(f"Total Amount: {values}\n")
                                    j+=1
                                quit()
                            else:
                                break

                        else:
                            print("Invalid Input!")

                    else:
                        i["game_data"]["savings"] = 0
                        self.json_modify()
                        print(f"Wiped your savings. Savings: {i["game_data"]["savings"]}")
                        print(f"Turn of {i['name']} finished.")
                        break

def main():
    g = Game()

    print("Welcome to the Game!\n")
    print("Game Rules!")
    print("- The numbers will be generated randomly from 1 - 10")
    print("- All numbers (except 1) you generate will be added to your 'score'")
    print("- When your generated number is '1', all your scores will be 0 and wiped out")
    print("- You can quit anytime you want or keep gambling")
    print("- If you quit, your score will be added to your total")
    print("- The player whose total is 100 or more than 50 will win!")
    print("- 3-5 players can participate")
    print("HAVE FUN!\n")

    while True:
        try:
            total_players = int(input("Enter total players who will participate: "))
            if total_players <3 or total_players >5:
                print("Only 3-5 players can participate in a game!")
                continue
            else:
                g.individual_data(total_players)
                break

        except ValueError as ve:
            print("Enter an integer (number)!")
            continue
    g.start_game()
            
if __name__ == "__main__":
    main()