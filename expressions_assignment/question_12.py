# Name: Nick Jeong
# Date: Oct 28th, 2023
# Program name: election
# Description: prints out who has higher votes with percentage

print("Election Results for New York:")
awbrey=int(input("Awbrey: "))
martinez=int(input("Martinez: "))

print("Election Results for New Jersey:")
awbrey+=int(input("Awbrey: "))
martinez+=int(input("Martinez: "))

print("Election Results for Connecticut:")
awbrey+=int(input("Awbrey: "))
martinez+=int(input("Martinez: "))

total=awbrey+martinez

print("{:<15}".format("Candidate"), "{:^10s}".format("Votes"), "{:>10}".format("Percentage"))
print("{:<15}".format("Awbrey"), "{:^10d}".format(awbrey), "{:>10}".format(f"{(awbrey/total*100):.2f}%"))
print("{:<15}".format("Martinez"), "{:^10d}".format(martinez), "{:>10}".format(f"{(martinez/total*100):.2f}%"))
print("{:<15}".format("TOTAL VOTES:"), "{:^10d}".format(total))