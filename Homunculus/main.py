from homunculus import world as hmc
# ----------------------------------------------------------------

def find_current_location(world, pid):
  if "passages" in world:
    for passage in world["passages"]:
      if pid == passage["pid"]:
        return passage
  return {}

# ----------------------------------------------------------------

def render(world, current_location, visited):
  if "name" in current_location and "cleanText" in current_location and "links" in current_location:
    print(current_location["cleanText"])
    print()
    for link in current_location["links"]:
      if ("requires" not in link or link["requires"] in visited) and ("excludes" not in link or link["excludes"] not in visited):
        print("({}) {}".format(link["selection"], link["label"]))
    print("\n")
        
def get_input():
  response = input("What do you want to do? (type quit to quit)? ")
  return response.upper().strip()

def update(world, current_location, current_pid, response, visited):
  if response == "":
    return current_pid
  if "links" in current_location:
    for link in current_location["links"]:
      if response == link["selection"]:
        if ("requires" not in link or link["requires"] in visited) and ("excludes" not in link or link["excludes"] not in visited):
          return link["pid"]
      if response == link["label"].upper().strip():
        if ("requires" not in link or link["requires"] in visited) and ("excludes" not in link or link["excludes"] not in visited):
          return link["pid"]
  print("I don't know what you are trying to do.")
  return current_pid

def count_moves(count):
  if "tags" not in current_location or current_location["tags"] == "" or not current_location["tags"].isnumeric():
    return count 
  if int(current_location["tags"]) > 0:
    count += int(current_location["tags"])
  return count

# ----------------------------------------------------------------

pid = 0
if "startnode" in hmc:
  pid = hmc["startnode"]
current_location = {}
visited = []
response = ""
gl_count = 0


while True:
  if response == "QUIT":
    break
  if gl_count >= 25:
    break
  pid = update(hmc, current_location, pid, response, visited)
  if pid != "" and pid not in visited:
    visited.append(pid)
  current_location = find_current_location(hmc, pid)
  render(hmc, current_location, visited)
  gl_count = count_moves(gl_count)
 

  if "41" in visited:
    break 
  
  response = get_input()

if "41" in visited and "10" in visited:
    print("Through the secrets of Alchemy, we have created a new human. Something stronger faster and smarter than anyone before us. By using the greatest of humanity we created our future as a species. While our work has been long and painful, while we have done many things others would see as unforgivable, in the end, what we have done will lead humanity to a bright future. I look forward to a future with the homo-homunculus. -Michael Clark’s speech")
    
print("Thanks for playing!")
print("Your total action count was: {}".format(str(gl_count)))