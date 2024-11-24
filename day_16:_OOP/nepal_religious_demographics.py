from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Religion", "Percentage"]
table.add_row(["Hinduism",81.3])
table.add_row(["Buddhism",9])
table.add_row(["Islam",4.4])
table.add_row(["Kirant",3.1])
table.add_row(["Christianity",1.4])
table.add_row(["Prakriti (nature worship)",.5])

table.add_column("ethnic breakdown", ["majority of all Nepali ethnic groups", "Sherpa, Dolpa, Lopa and other ethnic groups of the mountain regions","Madhesh Muslims (of Middle Eastern descent)","Kirati","n/a","unknown"])

table.align = "l"
print(table)