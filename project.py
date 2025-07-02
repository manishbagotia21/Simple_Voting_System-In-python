voters = {}
candidates={}

def add_candidate(name):
    if name not in candidates:
        candidates[name]=0
        print(f"candidate '{name}' added.")
    else:
        print(f"candidate '{name}' already exists.")

def vote(voter_id, candidate_name):
    if voter_id in voters:
        print("You have already voted.")
        return
    if candidate_name not in candidates:
        print("Candidate does not exist.")
        return
    candidates[candidate_name]+=1
    voters[voter_id]=candidate_name
    print(f"Vote casted for {candidate_name}.")

def show_results():
    print("\n--Voting Results ---")
    for name, votes in candidates.items():
        print(f"{name}: {votes}")

def show_winner():
    if not candidates:
        print("No Candidates available.")
        return
    winner=max(candidates, key=candidates.get)
    print(f"\n Winner: {winner} with {candidates[winner]} votes!")
def menu():
    while True:
        print("\n--Voting System---")
        print("1. Add Candidate")
        print("2. Vote")
        print("3. Show Results")
        print("4. Show Winner")
        print("5. Exit")
        choice= input("Enter choice:")

        if choice == '1':
            name=input("Enter Candidate Name:")
            add_candidate(name)
        elif choice =='2':
            voter_id=input("Enter Voter ID:")
            name=input("Enter candidate name to vote for:")
            vote(voter_id, name)
        elif choice =='3':
            show_results()
        elif choice == '4':
            show_winner()
        elif choice =='5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()


