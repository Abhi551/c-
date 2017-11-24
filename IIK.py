import sys;
import time;
import getpass;
class student(object):
	
	def __init__(self,student_profile={'15MA20002':"Abhishek@1",'15MA20026':'Juggler42_1'},list_roll_no=['15MA20002','15MA20026'],student_profile_name={'15MA20002':'Abhishek','15MA20026':'Naman'}):
		
		self.list_roll_no=list_roll_no;
		roll_no=raw_input("\t Enter your Roll no. :- ");
		self.roll_no=roll_no;
		if roll_no in list_roll_no:
			pass;
		else:
			self.list_roll_no.append(roll_no);


		
		x=input("\t enter \n \t 1. for login \n \t 2. for sign up \n \t 3. for exit :-  ");

		

		while x not in [1,2,3]:
			print "Wrong choice try again";
			x=input("\t enter \n \t 1. for login \n \t 2. for sign up \n \t 3. for exit :-  ");

		while x!=2 :
			if x==3:
				sys.exit();
			elif x==1 :
				if student_profile.has_key(roll_no):
					password=getpass.getpass('\n\t enter the password for id %s  :- '%roll_no);
					if password==student_profile[str(roll_no)]:
						break;
					else :
						print '\t wrong password \n try again';
						sys.exit();
				else:
					if student_profile.has_key(roll_no):
						pass;

					else:
						password=getpass.getpass('\n\t enter the password for id %s  :- '%roll_no);
						print '\t invalid login try sign up ';
						x=input("\n\t enter 1. for login \n 2. for sign up \n 3. for exit ");
		else:
			if student_profile.has_key(roll_no):
				print "\n \n \t\t try logging in , it seems that you already signned up.";
				password=getpass.getpass('\n\t enter the password for id %s  :- '%roll_no);
				if password==student_profile[str(roll_no)]:
						pass;
				else : 
					print " \n \n \t\t WRONG PASSWORD \n \t\t TRY AGAIN";
					sys.exit();



			else:
				password=getpass.getpass('\n\t enter the password for id %s  :- '%roll_no);
				view_password=raw_input("\n\t Do you want to see your password enter 'y' for yes else 'n' ");
				if view_password=='y':
					print "\n \t password = ",password;
				student_name=raw_input("\n\t name of the student :- ");
				self.student_name=student_name;

		
		if not student_profile.has_key(roll_no):
			student_profile.update({str(roll_no):str(password)});
			student_profile_name.update({str(roll_no):str(student_name)});
		



class student_recipe():
	



		print "".rjust(144,'_')

		#list of Recipies
		list_recipies={1:"Rice",2:"Dal",3:"Chilly Chicken",4:"Aloo Paratha",5:"Methi Paratha",6:"Onion Paratha",7:"Chicken Tikka",8:
		"Bread and Jam",9:"Bread and Butter",10:"Butter Chicken",11:"Masala Dosa",12:"Chole Bhatura",13:"Curry",14:"Chicken Biryani",15:"Lemon Rice",
		16:"Egg Bhurji",17:"Paneer",18:"Mushroom Rice",19:"French Toast",20:"Fish",21:"Paneer Tikka"};

		#dictionary for ingredients of recipies
		recipies_ingredients={
				         "Rice"   : ["Rice",'Water'] ,
					 	 "Dal"	  : ["Pulses" , "Water" , "Oil" , "Onion" , "Corriandor" , "Tomato" , 'Salt' ,"Turmeric" ],
					 	 "Chilly Chicken":["Chicken" , "Chicken Masala" , "Onion" , "Tomato" , "Oil" , "Water" , "Corriandor" ,"Salt" , "Turmeric"],
					 	 "Aloo Paratha":["Potato" , "Salt" , "Onion" , "Oil" , "Wheat Flour" , "Water", "Turmeric"],
					 	 "Methi Paratha":["Salt" , "Onion" , "Oil" , "Wheat Flour" , "Water", "Methi","Turmeric"],
					 	 "Onion Paratha":["Salt" , "Onion" , "Oil" , "Wheat Flour" , "Water","Turmeric"],
					 	 "Chicken Tikka":["Chicken" , "Chicken Masala" , "Chicken Tikka Masala","Onion" , "Tomato" , "Oil" , "Water" , "Corriandor" ,"Salt" , "Turmeric"],
					 	 "Bread and Jam":["Bread", "Jam","Eggs","Onion","Oil","Salt","Turmeric"],
					 	 "Bread and Butter":["Bread","Butter","Eggs","Oil","Salt","Onion","Turmeric"],
					 	 "Butter Chicken":["Chicken","Chicken Butter Masala","Oil","Onion","Salt","Tomato","Corriandor","Butter","Chilies","Turmeric"],
					 	 "Masala Dosa":["Potato","Aloo Masala","Parboiled Rice","Tomato","Onion","Salt","Oil","Turmeric","Coconut Chutney"],
					 	 "Chole Bhatura":["Salt" , "Onion" , "Oil" , "Flour" , "Water", "Tomato","Turmeric" ,"Chole","Chole Masala"],
					 	 "Curry":["Gram Flour" , "Curry Masala" ,"Salt","Oil","Onion","Water","Curry Leaves"],
					 	 "Chicken Biryani":["Chicken","Chicken Masala" , "Rice" ,"Water","Oil","Salt","Tomato" ,"Turmeric","Biryani Masala"],
					 	 "Lemon Rice":["Rice","Lemon","Pulses","Curry Leaves","Turmeric"],
					 	 "Egg Bhurji":["Eggs","Oil","Salt","Onion","Turmeric","Tomato","Potato","Garam Masala"],
					 	 "Paneer":["Paneer" , "Turmeric" , "Paneer Masala" , "Oil" , "Water" , "Salt" , "Onion" , "Corriandor"],
					 	 "Mushroom Rice":["Rice",'Water',"Mushroom","Turmeric","Salt","Mushroom Masala","Oil","Onion"],
					 	 "French Toast":["Bread","Butter","Eggs","Oil","Salt","Onion"],
					 	 "Fish":["Fish","Fish Masala","Oil","Turmeric","Water","Salt","Curd","Tomato","Onion"],
					 	 "Paneer Tikka":["Paneer" , "Paneer Tikka Masala" ,"Turmeric" , "Oil" , "Water" , "Salt" , "Onion" ]
				
					 	 }

		def recipe(self):
			print "WELCOME TO RECIPE COUNTER ".center(146);
			choice=int(raw_input("\t\tchoose one of the following option \n \t 1.view and alter the ingredients of recipes \n \t 2. add   recipies \n \t 3.exit \n \t :- "));
		
			while choice not in [1,2,3]:
				print "Wrong Choice . TRY AGAIN!!!!";
				choice=int(raw_input("\n\n\tchoose one of the following option \n\n \t 1.view and alter the ingredients of recipes \n \t 2. add   recipies \n \t 3.exit \n \t :- "));

			if choice==3:
				sys.exit();
			choice_add_recipies='y';
			if choice ==2:
				c=0;
				while choice_add_recipies=='y':
					add_recipe=raw_input("Enter the name of recipe you want to add \t :- ");
					next='y';
					c=c+1;
					add_ingredient_list=[]
					while next=='y':
						add_recipe_ingredient=raw_input("Enter the ingredients of recipe you added \t :- ");
						add_ingredient_list.append(add_recipe_ingredient);
						next=raw_input("Enter 'y' to add more ingredients \t :- ");
					self.recipies_ingredients.update({add_recipe:add_ingredient_list});
					choice_add_recipies=raw_input("Do you want to add more recipies  \t :-"); 
					self.list_recipies.update({len(self.list_recipies)+c:add_recipe});
					for i,j in self.list_recipies.iteritems():
						print i,".\t",j;


			elif choice==1:
				for i ,j in self.list_recipies.iteritems():
					print "\t\t \n",i,'. ',j;
				x=input("\t Enter your choice \n \t Enter 1 to view ingredients of recipies \n \t Enter 2 to change ingredients of recipies \n \t Enter 3 to Exit \n \t Enter 4 to End program \t :-");
				while x not in [1,2,3,4]:
					print "Wrong Input . TRY AGAIN !!!!";
					x=input("\t Enter your choice \n \t Enter 1 to view ingredients of recipies \n \t Enter 2 to change ingredients of recipies \n \t Enter 3 to Exit \n \t Enter 4 to End program \t :-");

				while x  in [1,2,3,4]:
					if x==1:
						y=raw_input("\t Which recipe's ingredients do you want see ?? .. :- ")
						while y not in self.recipies_ingredients.keys():
							print "\n\tthere is no such recipe . TRY AGAIN!!!\n"
							y=raw_input("\t Which recipe's ingredients do you want see ?? .. :- ")
						for i,j in enumerate(self.recipies_ingredients[y]):
							print i+1,'\t',j;
					elif x==2:	
						y=raw_input("\t Which recipe's ingredients do you want change ?? .. :- ")
						while y not in self.recipies_ingredients.keys():
							print "\n\t there is no such recipe . TRY AGAIN!!!\n"
							y=raw_input("\t There is no such recipe . TRY AGAIN !!!\n")
						for i,j in enumerate(self.recipies_ingredients[y]):
							print i+1,'\t',j;
						choice_change_ingredient='y'
						while choice_change_ingredient=='y':
							del_ingredient=raw_input("do you want to delete an ingredient of a recipe \n enter 'y'  to delete else 'n'  \t :- ");
							if del_ingredient=='y'  :
								change_ingredient=raw_input("Enter the name of ingredient you want to delete \t :- ");
								self.recipies_ingredients[y].remove(change_ingredient);
							add_ingredient=raw_input("do you want to add an ingredient \n Enter 'y' or 'Y' or 'yes' for yes else 'n' or 'N' or 'no' \t :- ");
							if add_ingredient=='y' or "Y" or 'yes' :
								change_ingredient=raw_input("Enter the name of ingredient you want to add \t :- ");
								self.recipies_ingredients[y].append(change_ingredient);
							print "here is your changed ingredients of your recipe";
							for i,j in enumerate(self.recipies_ingredients[y]):
								print i+1,'\t',j;
							choice_change_ingredient=raw_input("Do you want to change again ingredients of a recipe 'y' to change else 'n'\t :- ");
					elif x==3:
						break;
					else :
						sys.exit();
					x=input("\t Enter your choice \n \t Enter 1 to view ingredients of recipies \n \t Enter 2 to change ingredients of recipies \n \t Enter 3 to Exit \n \t Enter 4 to End program \t :-")
					while x not in [1,2,3,4]:
						print "Wrong Input. TRY AGAIN!!!!";
						x=input("\t Enter your choice \n \t Enter 1 to view ingredients of recipies \n \t Enter 2 to change ingredients of recipies \n \t Enter 3 to Exit \n \t Enter 4 to End program \t :-")





class student_method(student_recipe):

	def __init__(self):
		recipies_methods={
				         "Rice"   : ["\nAdd water to rice .\ncook them on pressure cooker for 15-20 minutes "] ,
					 	 "Dal"	  : ["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix mashed pulses to the prepared mash and add some water .\nServe it hot." ],
					 	 "Chilly Chicken":["Chicken" , "Chicken Masala" , "Onion" , "Tomato" , "Oil" , "Water" , "Corriandor" ,"Salt" , "Turmeric"],
					 	 "Aloo Paratha":["\nMix Potato and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix mashed Potato and Wheat Flour to the prepared mash and add some Oil and prepare Paratha.\nServe it hot."],
					 	 "Methi Paratha":["\nMix Methi , Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix mashed Methi with onion and Wheat Flour to the prepared mash and add some Oil and prepare Paratha.\nServe it hot."],
					 	 "Onion Paratha":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix mashed Onion and Wheat Flour to the prepared mash and add some Oil and prepare Paratha.\nServe it hot."],
					 	 "Chicken Tikka":["\nMix Onion and Tomato and fry it for 5 Minutes.\nNow add Chicken Masala and Chicken and add some water and cook for 15-20 Minutes.\nServe it hot"],
					 	 "Bread and Jam":["\nToast Bread for 2-3 Minutes.\nApply Jam and Butter and have it as Sandwich. "],
					 	 "Bread and Butter":["\nToast Bread for 2-3 Minutes.\nApply Butter. \nBreak a pair of eggs.\nMix well them with chopped pieces of onion , chillies , corriandor.\nPour oil on pan and after 2 minutes pour your mixture .\nServe it hot"],
					 	 "Butter Chicken":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow add Chicken Masala, Butter and Chicken and some Water and Salt.\nCook for 10-15 Minutes.\nServe it with Roti."],
					 	 "Masala Dosa":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix mashed Poato and Alu Masala to the prepared mash and addsome Oil.\nUsing Parboiled Rice and Oil prepare dosa and add the above prepared mix to the Dosa.\nServe it hot."],
					 	 "Chole Bhatura":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow add Channa Cooking Masala and Channa and some Water and Salt.\nCook for 10-15 Minutes.\nPrepare Bhatura with Wheat Flour and Oil.\nServe it along with Channa Masala."],
					 	 "Curry":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nMix some gram Flour with water .\nMix the 2 mixtures so created .\nCook them for 15-20 minutes"],
					 	 "Chicken Biryani":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix Chicken, Chicken Masala and Briyani Masala to the prepared mash and addsome Oil.\nAdd some water and Salt and cook for 15-20 Minutes.\nServe it hot."],
					 	 "Lemon Rice":["\nAdd water to rice . \ncook them on pressure cooker for 15-20 minutes . \nTake them out and mix lemon and curry leaves with turmeric .\nServe it hot"],
					 	 "Egg Bhurji":["\nBreak a pair of eggs. \nMix well them with chopped pieces of onion , potato ,chillies and corriandor. \nCook the mixture with some oil for 12-23 minutes.\nServe it hot"],
					 	 "Paneer":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow add Cooking Masala and Paneer and some Water and Salt.\nCook for 10-15 Minutes.\nServe it with Roti."],
					 	 "Mushroom Rice":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix Mushroom, Garam Masala and Turmeric powder Masala to the prepared mash and addsome Oil.\nAdd some water and Salt and cook for 15-20 Minutes.\nServe it hot."],
					 	 "French Toast":["\nBreak a pair of eggs. \nMix well them with chopped pieces of onion , chillies , corriandor. \nApply the mixture to bread .\nBake them for 2-3 minutes.\nServe it hot"],
					 	 "Fish":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix Fish, Fish Masala and Garam Masala to the prepared mash and addsome Oil.\nAdd some water and Salt and cook for 15-20 Minutes.\nServe it hot."],
					 	 "Paneer Tikka":["\nMix Onion and Tomato and mash them.\nAdd some Oil and fry it for some time.\nNow mix Paneer and Tikka Masala to the prepared mash.\nAdd some Salt and fry it in Oil for 15-20 Minutes.\nServe it hot." ]

					 	 }
		self.recipies_methods=recipies_methods;


	def modify_steps(self):
		x=raw_input("To change the steps of a recipe enter 'y' else 'n' \t :- ");
		while x=='y':
			c=1
			for i in self.recipies_methods.iterkeys():
				print c,'.',i;
				c=c+1;
			recipe=raw_input("Enter the recipe of which you want to change the steps \t :- ");
		
			for i in self.recipies_methods[recipe]:
				print i;
			y=raw_input("Enter 'y' to change steps else 'n' \t :- ");
			steps=""
			if y=='y':
				while y=='y':
					new_steps=raw_input("Write new steps you want to add \t :- ");
					steps=steps+".\n"+new_steps;
					y=raw_input("Enter 'y' to add more steps else 'n' \t :- ");
				steps=steps[2:];
				print steps;
				steps=[steps];
				self.recipies_methods[recipe]=steps;
				print "new steps are :-"
				for i in self.recipies_methods[recipe]:
					print i;

			x=raw_input("To change the steps of another recipe enter 'y' else 'n' \t :- ")





	def view_steps(self):
		
		c=1;
		x='y'
		for i  in self.recipies_methods.iterkeys():
			print c,'.',i;
			c=c+1;
		while x=='y': 
			recipe = raw_input("Enter the name of recipe of which you want to view recipe \t :- ");
			for i,j in enumerate(self.recipies_methods[recipe]):
				print j;
			x=raw_input("do you want to see other recipe's steps \t :- ");



print "\n\n\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>INTERACTIVE INTELLIGENT KITCHEN HELPER<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<";
print "	   				______________________________________________________"
print "\n \n \n \n"; 
print "WELCOME	TO HALL MESS".center(145);
print"_____________________________________________________________________________________________________________________________________________"
print "\n\n\n";


s=student();
action=input("\n \t Choose your action \n \t\t 1.view or change ingredients \n \t\t 2. view or change method of recipe \n \t\t :- ");
while action not in [1,2]:
	print "Wrong Input . TRY AGAIN !!!!";
	action=input("\n \t Choose your action \n \t\t 1.view or change ingredients \n \t\t 2. view or change method of recipe \n \t\t :- ");
while action == 1 or 2:
	if action ==1:
		sr=student_recipe();
		sr.recipe();
		action=input("Choose your action \n \t\t 1.view or change ingredients \n \t\t 2. view or change method of recipe \n \t\t :- ");
		while action not in [1,2]:
			print "Wrong Choice . TRY AGAIN !!!!.";
			action=input("Choose your action \n \t\t 1.view or change ingredients \n \t\t 2. view or change method of recipe \n \t\t :- ");

	else :
		sm=student_method();
		modify_choose=input("\n enter 1 to modify and enter new steps to recipies \n enter 2 to just view  methods of preparation");
		if modify_choose==1:
			sm.modify_steps();
		elif modify_choose==2:
			sm.view_steps();
		else:
			print "wrong choice"
			sys.exit();
		action=input("Choose your action \n \t\t 1.view or change ingredients \n \t\t 2. view or change method of recipe \n \t\t :- ")
  		while action not in [1,2]:
 			print "Wrong Choice . TRY AGAIN !!!!.";
			action=input("Choose your action \n \t\t 1.view or change ingredients \n \t\t 2. view or change method of recipe \n \t\t :- ");