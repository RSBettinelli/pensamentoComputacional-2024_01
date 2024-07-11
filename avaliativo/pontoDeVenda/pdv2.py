#python 3.10.12

from functions import secundary_functions as secundary
# you will need this file to others functions

# i am using the OS import to see how many collumns
# is yout terminal using
# import os	# the default line size will be based on the terminal collumns.

import datetime
import time


# when start a new sale
def sale(bag: list, sales_list: list | None, start_time: float, expensivest_sale: float, longest_sale: float):
	if bag == None:
		sale_list = []
	
	else:
		sale_list = bag
		
	default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"		      # default line for each terminal
	print(default_line)
	print("     |   Please press a valid product number, \"0\" or \"E\"" + " " * int(secundary.window_size()[0] - 61), "|")
	number = input("     |   ")
	
	if (number == "i") or (number == "I") or (number == "0"):	# -------------------------	return to start
		starting(sales_list, [0, None], [0, None], expensivest_sale, longest_sale)
		exit()
		
	elif (number == "e") or (number == "E"):		# ---------------------------------	finish this sale
		finish_sale(bag, sales_list, start_time, expensivest_sale, longest_sale)
		exit()
	
	valid_number = secundary.is_valid_number(number)	# ---------------------------------	if it is valid, will get the item
								# ---------------------------------	else will return None
	
	while valid_number is None:			
		default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"	      # default line for each terminal
		print(default_line)
		print("     |   Please press a valid product number, \"0\" or \"E\"" + " " * int(secundary.window_size()[0] - 61), "|")
		number = input("     |   ")
		valid_number = secundary.is_valid_number(number)	# ---------------------------------	if it is valid, will get the item
									# ---------------------------------	else will return None
		
		if (number == "i") or (number == "I") or (number == "0"):	# -------------------------	return to start
			starting(sales_list, [0, None], [0, None], expensivest_sale, longest_sale)
			exit()
			
		elif (number == "e") or (number == "E"):		# ---------------------------------	finish this sale
			finish_sale(bag, sales_list, start_time, expensivest_sale, longest_sale)
			exit()
		
	if valid_number != None:	# -----------------------------------------------------------------	it means the product is valid
		item_amount(valid_number, sale_list, sales_list, start_time, expensivest_sale, longest_sale)# -----------	choose the amount
		

# the user will chose the amount of each product
def item_amount(item: list, sale_list: list, sales: list | None, start_time: float, expensivest_sale: float, longest_sale: float):
	sale_list_amount = sale_list
	invalid_amount = True
	while invalid_amount:
		invalid_amount = False
		default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"		# ---- default line for each terminal
		print(default_line)
		print(
			"     |   Please press how many " + item['nome'] + " " + item['tipo'] + " do you want" + 
			" " * int(secundary.window_size()[0] - len(item['nome']) - 50) + "|"
		)
		
		number = input("     |   ")
		
		if number == "0":		# ------------------------------------------------------------	cancel this product
			sale(sale_list_amount, start_time)
			exit()
			
		elif number == "i" or number == "I":
			starting(sales, [0, None], [0, None], expensivest_sale, longest_sale)
			exit()
					
		elif (number == ""):		# ------------------------------------------------------------ it will add 1 unity
			if item['tipo'] == "un":
				number = "1"
				
			else:
				number = "N"
		
		points_in_char = 0
		for char in number:		# ------------------------------------------------------------- compare each char
			if item["tipo"] == "kg":
				if "." == char:	# ----------------------------------------- if the user try to put more than one point in a fractionary number
					points_in_char += 1
					
				if ((not char.isnumeric()) and (char != ".")) or (points_in_char > 1):	# ----- it can be fractioned
					invalid_amount = True
					
			else:
				if (not char.isnumeric()):				# --------------------	it can not be fractioned
					invalid_amount = True
					
					
	for itens_list in sale_list_amount:			# --------------------  if the product already is in the sale list amount
		if item == itens_list[0]:
			itens_list[1] = str(float(itens_list[1]) + float(number))    #  it will just add the new amount
			sale(sale_list_amount, sales, start_time, expensivest_sale, longest_sale)
			exit()
	
	sale_list_amount.append([item, number])				# --------------------	add the item description and quantity to another list 
	sale(sale_list_amount, sales, start_time, expensivest_sale, longest_sale)	# ----  return to sale
	exit()


# when finish a sale will show the subtotal price, the amount of each product and the total price from the sale
def finish_sale(sale_list: list | None, sales: list | None, start_time: float, expensivest_sale: float, longest_sale):
	finish_time = time.time()
	finish_time_epoch = datetime.datetime.now()
	total_time = finish_time - start_time
	
	final_bag = sale_list
	sales_list = sales
	
	default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"			# default line for each terminal
	total_price = 0
	
	sizes = secundary.size_table_price()		# _______________________ how many spaces you will need to put for each terminal
	
	print(
		default_line +				# ----------------------- default line
		"\n     |Code | Name" + " " * int(sizes[0] - 12)  + "| " + # ----- "code...name" + spaces sizes[0] less the words lenght times
		"Price" + " " * int(sizes[1] + sizes[2] - 16)  + "| " + # ----------- spaces sizes[1] + sizes [2] less the words lenght times
		"Amount | " +	# ----------------------------------------------- just print "amount"
		"Subtotal" + " " * int(sizes[3] - 9) + "|" # -------------------- "subtotal" + spaces size[3] less words lenght times
	)
	if not (final_bag is None):	# if the bag is not empty
		for item in final_bag:	# for each item in the bag
			item.append(float(item[0]["preco"]) * float(item[1]))
			total_price += item[2]
			print(
				"     |" + item[0]['codigo'].rjust(4, "0") + " | " + 
				item[0]['nome'] + " " * int(sizes[0] - len(item[0]['nome']) - 8) + "|" + # "name" + spaces sizes[0] less the words lenght times
				" " * int(sizes[1] + sizes[2] - len(str(item[0]['preco'])) - 11) + str(item[0]['preco']) + " | " + # spaces sizes[1] + sizes [2] 
																   #   less the words lenght times
				str(item[1]).rjust(6, " ") + " |" + # print de amount
				" " * int(sizes[3] - len(str(item[2]))) + str(item[2]) + "|"	# space sizes[3] less words lenght times
			)
			#print(item[2] + "\n")
			
		print(
			default_line +			# ------------ FINAL SALE TIME ------------- #
			"\n     | How long the Sale was: "  + " " * int(secundary.window_size()[0] -
			len(str(datetime.datetime.utcfromtimestamp(total_time).time().replace(microsecond = 0))) - 34) +
			str(datetime.datetime.utcfromtimestamp(total_time).time().replace(microsecond = 0)) + "|\n" + 
			default_line +			# ------------ FINAL SALE PRICE ------------ #
			"\n     |   Total:" + " " * int(secundary.window_size()[0] - len(str(total_price)) - 20) + str(total_price) + " |\n" +
			default_line
		)
		
	else:						# ------------ EMPTY SALE ------------ #
		print("     |   Empty sale" + " " * int(secundary.window_size()[0] - 23) + "|\n" +
			default_line
		)
		
	sales_list.append(final_bag)

	starting(sales_list, [total_time, final_bag], [total_price, final_bag], expensivest_sale, longest_sale)  
	# -------------------------------- this sale has been finished, so will return to start
	exit()



# when finish the apliation will show the resume
def resume(sales: list | None, longest_time: float, expensivest_sale: float):
	resume_list = []
	default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"	# ------- default line for each terminal
	sizes = secundary.size_table_price()		# _______________________ how many spaces you will need to put for each terminal
	total_price = 0
	
	print(default_line)
	
	print(
		default_line +				# ----------------------- default line
		"\n     |Code | Name" + " " * int(sizes[0] - 12)  + "| " + # ----- "code...name" + spaces sizes[0] less the words lenght times
		"Price" + " " * int(sizes[1] + sizes[2] - 16)  + "| " + # ----------- spaces sizes[1] + sizes [2] less the words lenght times
		"Amount | " +	# ----------------------------------------------- just print "amount"
		"Subtotal" + " " * int(sizes[3] - 9) + "|" # -------------------- "subtotal" + spaces size[3] less words lenght times
	)
	
	if sales != None:
		for sale in sales:	# ----------------------------------------------------  for each sale
			if sale != None and sale != []:	# --------------------------------------------  if the client bought something
				for itens_list in sale:		# ----------------------------  compare each item in sale
					already = False		# ----------------------------  i will use it to jump some lines later
				
					if resume_list == []:		# --------------------  if the resume_list is empty (happens the first time)
						resume_list.append(itens_list)		# ----  add the first item
						already = True
					
					else:		# ------------------------------------  the list is not empty
						for past_item in resume_list:	# ------------  for each item in the list
							if itens_list[0] == past_item[0]: # --  if the item in sale already is in resume_list
								past_item[1] = str(float(past_item[1]) + float(itens_list[1]))    #  it will just add the new amount
								past_item[2] = str(float(past_item[2]) + float(itens_list[2]))    #  it will just add the new price
								already = True
					
					if already == False:	# ----------------------------  the next line will be skiped if already
								# ----------------------------   added the item or increase the amount	
					
						resume_list.append(itens_list)	# ------------  add the item to the resume list
	
	for finish_list in resume_list:	# --------------------------------------------  for each item
		print(
			"     |" + finish_list[0]['codigo'].rjust(4, "0") + " | " + 
			finish_list[0]['nome'] + " " * int(sizes[0] - len(finish_list[0]['nome']) - 8) + "|" + # "name" + spaces sizes[0] less the words lenght times
			" " * int(sizes[1] + sizes[2] - len(str(finish_list[0]['preco'])) - 11) + str(finish_list[0]['preco']) + " | " + # spaces sizes[1] + sizes [2] 
															   #   less the words lenght times
			str(finish_list[1]).rjust(6, " ") + " |" + # print de amount
			" " * int(sizes[3] - len(str(finish_list[2]))) + str(finish_list[2]) + "|"	# space sizes[3] less words lenght times
		)

	if sales != None:
		for sale in sales:
			for item in sale:
				total_price += float(item[2])
			
		print(
			default_line +			# ------------ FINAL PRICE ------------ #
			"\n     |   Total:" + " " * int(secundary.window_size()[0] - len(str(total_price)) - 20) + str(total_price) + " |\n" +
			default_line +
			"\n     | Expensivest Sale: " + # print the most expensive sale price
			" " * int( secundary.window_size()[0] - len(str(expensivest_sale)) - 29 ) + str(expensivest_sale) + "|" + 
			
			"\n     | Longest Sale: " + 
			" " * int(secundary.window_size()[0] - len(str(datetime.datetime.utcfromtimestamp(longest_time).time().replace(microsecond = 0))) - 25) + 
			str(datetime.datetime.utcfromtimestamp(longest_time).time().replace(microsecond = 0)) + "|\n"+
					# print how many hours/minutes/seconds			
			default_line
		)
	
	

# when start a new operation
def starting(sales: list  | None, total_time: list | None, expensive: list | None, past_expensivest: float | None, longest_sale: float | None):
	if sales == None:		# ------------ if it is starting
		sales_list = []		# ------------ create an empty list for all sales
		print("\n" * int(secundary.window_size()[1]))
	
	else:
		sales_list = sales	# ------------ set sales_list to sales
	
	if expensive == None:				# ------ if it is the first sale
		expensivest_sale = 0			# ------ the most expensive sale cost 0
		
	elif expensive[0] > past_expensivest:		# ------ if the last sale was the most expensive one 
		expensivest_sale = expensive[0]		# ------ expensivest_sale becomes the last sale
		
	else:						
		expensivest_sale = past_expensivest	# ------ the expensivest_sale continue being the past sale
	
	if total_time == None:			# ------- if it is the first time
		longest_sale = 0		# ------- the longest sale will be 0
		
	elif total_time[0] > longest_sale:	# ------- the
		longest_sale = total_time[0]
	
	default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"			# default line for each terminal
	print(
		"     _" + "_" * int(secundary.window_size()[0] - 10) + "_" +
		"\n     |   Continue new sale?", " " * int(secundary.window_size()[0] - 33), "|\n" +	# new sale or finish
		default_line
	)
	answer = "None"

	while (answer != "a") and (answer != "A") and (answer != "r") and (answer != "R"):		# if the user do not press A or R
		default_line = "     |" + "_" * int(secundary.window_size()[0] - 10) + "|"		# default line for each terminal
		print("     |   Press A to confirm or R" + " " * int(secundary.window_size()[0] - 37), "|")	# press A to a new sale or R 
														# to see the day resume
	
		answer = input("     |   ")
		
	if answer == "a" or answer == "A":
		start_time = time.time()
		sale(None, sales_list, start_time, expensivest_sale, longest_sale)
		exit()
		
	elif answer == "r" or answer == "R":
		resume(sales_list, longest_sale, expensivest_sale)
		exit()


final_list = []

starting(None, None, None, 0, 0)