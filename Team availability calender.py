import random
from time import strptime, strftime
class TeamManager:
    def __init__(self):
        self.teams_data = []
        self.availability_slots = {
            1: '09AM-10AM',
            2: '01PM-03PM',
            3: '04PM-06PM'
        }

    def generate_team_id(self):
        return random.randint(100000, 999999)

    def generate_member_id(self):
        return random.randint(1000, 9999)

    def create_team(self):
        team_name = input("Enter the team name: ")
        team_members = []

        for i in range(4):
            member_name = input(f"Enter the name of team member {i + 1}: ")
            member_id = self.generate_member_id()

            while any(member['id'] == member_id for member in team_members):
                member_id = self.generate_member_id()

            team_members.append({'name': member_name, 'id': member_id, 'availability': []})

        team_id = self.generate_team_id()

        print("\nTeam Details:")
        print(f"Team Name: {team_name}")
        print(f"Team ID: {team_id}")

        print("\nTeam Members:")
        for member in team_members:
            print(f"Name: {member['name']}, ID: {member['id']}, Availability: {member['availability']}")

        team_data = {'team_name': team_name, 'team_id': team_id, 'team_members': team_members}
        self.teams_data.append(team_data)

    def delete_team_member(self):
        team_id_to_delete = int(input("Enter the team ID for which you want to delete a member: "))
        member_name_to_delete = input("Enter the name of the team member to delete: ")
        member_id_to_delete = int(input("Enter the ID of the team member to delete: "))

        found_team = None
        for team in self.teams_data:
            if team['team_id'] == team_id_to_delete:
                found_team = team
                break

        if found_team:
            found_member = None
            for member in found_team['team_members']:
                if member['id'] == member_id_to_delete and member['name'] == member_name_to_delete:
                    found_member = member
                    break

            if found_member:
                found_team['team_members'].remove(found_member)
                print(f"Team member {member_name_to_delete} with ID {member_id_to_delete} deleted successfully.")
            else:
                print(
                    f"Team member not found with ID {member_id_to_delete} and name {member_name_to_delete} in team {team_id_to_delete}.")
        else:
            print(f"Team not found with ID {team_id_to_delete}.")

    def update_availability(self):
        team_id_to_update = int(input("Enter the team ID for which you want to update availability: "))
        member_id_to_update = int(input("Enter the ID of the team member for whom you want to update availability: "))
        availability_slot = input("Enter the availability slot (e.g., 9am-10am): ")

        found_team = None
        for team in self.teams_data:
            if team['team_id'] == team_id_to_update:
                found_team = team
                break

        if found_team:
            found_member = None
            for member in found_team['team_members']:
                if member['id'] == member_id_to_update:
                    found_member = member
                    break

            if found_member:
                found_member['availability'].append(availability_slot)
                print(
                    f"Availability for Team member {found_member['name']} with ID {found_member['id']} updated successfully.")
            else:
                print(f"Team member not found with ID {member_id_to_update} in team {team_id_to_update}.")
        else:
            print(f"Team not found with ID {team_id_to_update}.")

    def find_common_availability(self, team_id):
        found_team = next((team for team in self.teams_data if team['team_id'] == team_id), None)
        if found_team:
            team_members = found_team['team_members']
            availability_slots = [member['availability'] for member in team_members]
            start_times, end_times = [], []
            for slots in availability_slots:
                for slot in slots:
                    start_time, end_time = slot.split('-')
                    start_times.append(start_time)
                    end_times.append(end_time)
            start_times = list(map(self.convert_to_time, start_times))
            end_times = list(map(self.convert_to_time, end_times))
            common_availability = self.find_overlapping_time_slots(start_times, end_times)
            if not common_availability:
                print(f"No common availability for Team {team_id}.")
            else:
                time = ''.join(common_availability)
                print(f"Common Availability time slot for Team {team_id} is: {time}")
                return time
        else:
            print(f"Team with ID {team_id} not found in the list of teams.")

    def find_overlapping_time_slots(self, start_times, end_times):
        # Find the overlapping time range
        overlap_start = max(start_times)
        overlap_end = min(end_times)

        # Check if there is an actual overlap
        if overlap_start < overlap_end:
            return f"{strftime('%I%p',overlap_start)}-{strftime('%I%p',overlap_end)}"
        else:
            return "No overlapping time slots"

    def convert_to_time(self, time_str):
        # Convert string time to datetime object
        return strptime(time_str, "%I%p")

    def display(self):
        for team in self.teams_data:
            print("\nTeam Details:")
            print(f"Team Name: {team['team_name']}")
            print(f"Team ID: {team['team_id']}")
            # Display the individual time availability for each team member

            for member in team['team_members']:
                print(f"Name: {member['name']}, ID: {member['id']}, Availability: {', '.join(member['availability'])}")

        if not self.teams_data:
            print("No team data available. Please create a team first.")

    def schedule_meeting(self, slot_id, team_id):
        found_team = next((team for team in self.teams_data if team['team_id'] == team_id), None)
        if found_team:
            common_availability = self.find_common_availability(team_id)
            if common_availability == self.availability_slots[slot_id]:
                print(f"Meeting scheduled for Team {team_id} at {common_availability}.")
                # You can add additional logic here for updating the meeting schedule, if needed.
            else:
                print(
                    f"Cannot schedule meeting. Common availability does not match the specified slot for Team {team_id}.")
        else:
            print(f"Team with ID {team_id} not found in the list of teams.")



t=TeamManager()
while True:
    print("********************************************************************")
    print("1. Create Team")
    print("2. Delete Team Member")
    print("3. Update Availability")
    print("4. Find Common Availability")
    print("5. Display Team Details")
    print('6.Schedule Meeting')
    print("7. Exit")

    ch=int(input("Enter your choice (1-6): "))

    if ch==1:
        t.create_team()

    elif  ch==2:
        t.delete_team_member()

    elif  ch==3:
        t.update_availability()

    elif  ch==4:
        team_id = int(input("Enter the team ID to find common availability: "))
        t.find_common_availability(team_id)

    elif  ch==5:
        t.display()

    elif  ch==6:
        team_id = int(input("Enter the team ID to schedule a meeting: "))
        slot_id = int(input("Enter the slot ID to schedule a meeting: "))
        t.schedule_meeting(slot_id, team_id)
        
    elif ch==7:
        print("TERMINATING")
        print("********************************************************************")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")