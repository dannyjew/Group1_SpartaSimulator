from ContainerClasses import *

centre_list = [Centre()]

# # print(centre_list)
# for i in range(5):
#     centre_list.append(Centre())
#
# centre_list[0].add(2)
# centre_list[1].add(10)
# centre_list[2].add_trainees()
# centre_list[3].add(15)
#
# for i in range(5):
#     print(centre_list[i].members, centre_list[i].remainder)

# list[0].add_trainees()
# list[2].add_trainees(list[1].add_trainees(list[0].add_trainees(83)))


# centre_list[0].add(95)
# centre_list[1].add(95)
# centre_list[2].add(95)

# print(centre_list[0].members, centre_list[0].remainder)
# print("")

remainder = centre_list[0].add_trainees(65)
counter = 1

while remainder > 0:
    if len(centre_list) <= counter:
        centre_list.append(Centre())
    remainder = centre_list[counter].add_trainees(remainder)
    counter += 1

for i in range(len(centre_list)):
    print(centre_list[i].members, centre_list[i].remainder)
