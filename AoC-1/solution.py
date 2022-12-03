## Task 1

def task2(calorieList):
    sortedCalorieList = sorted(calorieList, reverse=True)
    print(sortedCalorieList)
    calorieTotal = sortedCalorieList[0]+sortedCalorieList[1]+sortedCalorieList[2]
    print(calorieTotal)
    return

def task1():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
        elf = 0
        calorieList = []
        ## Initialise first array item
        calorieList.append(0)
        print(calorieList)

        # Start parsing
        for line in lines:
            if line != '\n':
                line = line.strip()
            # If new elf
            if line == '\n':
                elf += 1
                calorieList.append(0)
                # Add new elf line, but skip the calculation for this cycle
                continue
            # Continue with calorie calculation
            #print(calorieList)
            calorieList[elf] += int(line)
        #print(calorieList)
        max_value = max(calorieList)
        max_location = [index for index, item in enumerate(calorieList) if item == max_value]
        #print(max_value)
        #print(max_location)
        #print(max_location[0]+1)
        ## Solution to 1
        print("The largest calorie count is: " + str(max_value)+ " and held by elf nr " + str(max_location[0]+1))
        task2(calorieList)
if __name__ == '__main__':
    task1()
